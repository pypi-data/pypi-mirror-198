"""Core functionality for connecting to a Maptek MDF-based application.

This handles connecting to the application and initialises internal
dependencies. The Project class provides methods for interacting with user
facing objects and data within the application.

"""
###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from __future__ import annotations

import atexit
from collections.abc import Generator, Iterable
from contextlib import contextmanager
import ctypes
import logging
import os
import posixpath
import typing

from .. import capi
from ..capi.types import T_ObjectHandle
from ..capi.util import (register_dll_directory, disable_dll_loading,
                         CApiDllLoadFailureError)
from ..data import (Surface, EdgeNetwork, Marker, Text2D, Text3D, Container,
                    VisualContainer, PointSet, Polygon, Polyline,
                    DenseBlockModel, Topology, NumericColourMap,
                    StringColourMap, StandardContainer, Scan,
                    GridSurface, SubblockedBlockModel, Raster, Discontinuity,
                    DataObject, RibbonChain, RibbonLoop, SparseBlockModel,
                    Ellipsoid)
from ..data.containers import ChildView
from ..data.objectid import ObjectID
from ..geologycore import Drillhole, DrillholeDatabase
from ..internal import account
from ..internal.lock import ReadLock, WriteLock, LockType
from ..internal.logger import configure_log
from ..internal.mcp import (ExistingMcpdInstance, McpdConnection,
                            find_mdf_hosts, McpdDisconnectError)
from ..internal.options import (ProjectOptions, ProjectBackendType,
                                ProjectOpenMode, McpdMode)
from ..internal.util import default_type_error_message
from ..labs.cells import SparseIrregularCellNetwork
from .errors import (DeleteRootError, ObjectDoesNotExistError,
                     ProjectConnectionFailureError, ApplicationTooOldError,
                     TypeMismatchError, NoRecycleBinError, InvalidParentError)
from .selection import Selection

# pylint: disable=too-many-public-methods
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

ObjectT = typing.TypeVar('ObjectT', bound=DataObject)
"""Type hint used for arguments which are subclasses of DataObject."""

ObjectIdT = typing.TypeVar("ObjectIdT", bound=DataObject)
"""Type hint used for ObjectID of any DataObject subclass.

Note that ObjectT and ObjectIdT may not refer to the same type for certain
functions.
"""

class Project:
  """Main class to connect to an instance of an MDF application.
  Project() establishes the communication protocol and provides base
  functionality into the application, such as object naming, locating,
  copying and deleting.

  Parameters
  ----------
  options
    Optional specification of project and connection
    settings. Used for unit testing to start a new database and
    processes without an MDF host application already running.
  existing_mcpd
    If None (default) then the latest relevant application that was launched
    will be connected to. This is equivalent to passing in
    Project.find_running_applications()[0].

    Otherwise it may be ExistingMcpdInstance which refers to the host
    application to connect to otherwise a McpdConnection which is an
    existing connection to a host application (its mcpd).

  Raises
  ------
  ProjectConnectionFailureError
    If the script fails to connect to the project. Generally this is
    because there is no application running, or the specified application
    is no longer running.

  """

  # Keep track of if the logging has been configured.
  # See configure_log for details.
  _configured_logging = False

  def __init__(
      self,
      options: ProjectOptions=None,
      existing_mcpd: ExistingMcpdInstance | McpdConnection | None=None):
    self.mcp_instance = None
    self.backend_index = None
    self._is_connected_to_existing_application = False
    self.dataengine_connection = False
    self.broker_session = None

    # The types listed here are the default types expected to be available
    # in every application the SDK can connect to.
    self.__types_for_data: list[tuple[int, ObjectT]] = [
      (7, Scan),
      (6, SubblockedBlockModel),
      (6, SparseIrregularCellNetwork),
      (6, SparseBlockModel),
      (6, GridSurface),
      (6, DenseBlockModel),
      (5, Text3D),
      (5, Text2D),
      (5, RibbonChain),
      (5, RibbonLoop),
      (4, Surface),
      (4, StandardContainer),
      (4, Polyline),
      (4, Polygon),
      (4, PointSet),
      (4, Marker),
      (4, EdgeNetwork),
      (4, Discontinuity),
      (4, Ellipsoid),
      (3, VisualContainer),
      (3, StringColourMap),
      (3, Raster),
      (3, NumericColourMap)
    ]
    """Sorted list of types openable by the Project class.

    Each element in the list is a tuple of the form (priority, type)
    where priority is the number of base classes between the type
    and deC_Object (The ultimate base class of all objects stored in
    a maptekdb).

    Derived classes have higher priority than their bases and will be checked
    before their base classes. This ensures that Project.edit() and
    Project.read() will open an object as the most derived possible type.

    Use Project.register_types() to add additional types to this list.
    """

    # :TRICKY: atexit.register to ensure project is properly unloaded at exit.
    # By implementing the standard logging library, __del__ and __exit__ are
    # no longer guaranteed to be called. During unit testing, spawned mcpd.exe
    # and backendserver.exe would remain open indefinitely after the unit tests
    # finished - preventing subsequent runs.
    # Not an issue if connecting to an existing host application.
    self._exit_function = atexit.register(self.unload_project)
    self.__dll_directory_set = False

    # Configure all the MDF loggers with defaults. This is done when the user
    # creates the Project() instance so they don't need to do it themselves and
    # so by default we can have consistent logging.
    #
    # Only configure the logging once as otherwise output will be duplicated as
    # it set-up multiple log handlers.
    if not Project._configured_logging:
      configure_log(logging.getLogger('mapteksdk'))
      Project._configured_logging = True

    self.log = logging.getLogger('mapteksdk.project')

    # If no options are provided, there are some default options we expect.
    if not options:
      options = ProjectOptions('')

      # When no options are provided we are expecting to connect to the
      # project of a running application.
      assert options.mcpd_mode == McpdMode.CONNECT_TO_EXISTING

    broker_connector_path = options.account_broker_connector_path
    connection_parameters = options.account_broker_session_parameters

    # Configure the DLL load path, (possibly by finding an mcpd to connect
    # to in the process).
    if not options.dll_path:
      # No DLL path was set, so the MDF DLLs can't be loaded yet (unless
      # there is an existing mcpd which would already have set it up, and
      # has simply not provided the where in the ProjectOptions).
      #
      # If the plan is to connect to an existing mcpd, then finding one will
      # discover the DLLs required.
      #
      # If creating a new mcpd, then the DLL path should already be set.
      # Unless a new mode is supported where an existing mcpd (application) is
      # found first then it is used to start it.
      #
      if options.mcpd_mode == McpdMode.CONNECT_TO_EXISTING:
        if not existing_mcpd:
          # If the bin path and mcp path environment variables are
          # defined, use them to determine which mcpd instance (and hence
          # which application) to connect to. This ensures scripts run
          # from workbench connect to the correct application.
          # Otherwise connect to the most recently opened application.
          try:
            dll_path = os.environ["SDK_OVERWRITE_BIN_PATH"]
            socket_path = os.environ["SDK_OVERWRITE_MCP_PATH"]
            existing_mcpd = ExistingMcpdInstance(-1, dll_path, socket_path)
          except KeyError:
            try:
              # The result of the find is used when trying to connect to ensure
              # looking for the mcpd is not performed twice. That itself could
              # lead to different mcpd being found (and thus a mismatch).
              existing_mcpd = find_mdf_hosts(self.log)[0]
            except Exception as error:
              # Suppress the stack trace from the KeyError because it is
              # not relevant. This also means the environment variables
              # (i.e. internal implementation details) are not included in the
              # user-facing error message.
              raise error from None
          options.dll_path = existing_mcpd[1]
        elif not isinstance(existing_mcpd, McpdConnection):
          # The connection hasn't been established yet so the DLL path isn't
          # configured either.
          options.dll_path = existing_mcpd[1]

    if not options.dll_path:
      raise ProjectConnectionFailureError(
          "Failed to locate folder containing required DLLs. "
          "No search paths could be determined.")

    try:
      register_dll_directory(options.dll_path)
      self.__dll_directory_set = True
    except FileNotFoundError as error:
      searched_paths = "\n".join([str(x) for x in error.searched_paths])
      raise ProjectConnectionFailureError(
        "Failed to locate folder containing required DLLs. "
        f"Searched:\n{searched_paths}") from None

    try:
      # Acquire a licence for Maptek Extend.
      #
      # First, try with an anonymous session. This allows the use of borrowed
      # licences when the user isn't logged into Maptek Account.
      #
      # Secondly, if that that fails then we try non-anonymous so the user is
      # prompted to log-in. Unless the caller has been explicit and said they
      # only want an anonymous session.
      self.log.info('Acquiring licence for Maptek Extend')
      required_parameters = {
        'AnonymousSession': True,
        'MaptekAccountUserName': '',
        'MaptekAccountAuthKey': '',
        'ApiToken': '',
      }
      if connection_parameters:
        force_parameters = connection_parameters.copy()
        force_parameters.update(required_parameters)
      else:
        force_parameters = required_parameters

      for try_parameters in [force_parameters, connection_parameters]:
        try:
          self.broker_session = account.connect_to_maptek_account_broker(
            broker_connector_path, try_parameters)

          with self.broker_session.acquire_extend_licence(
              capi.License().supported_licence_format()) as licence:
            self.log.info('Acquired licence for Maptek Extend')
            os.environ["MDF_ACTIVE_PACKAGE"] = licence.license_string
            os.environ["MDF_EXTEND_LICENCE_STRING"] = licence.license_string

          break
        except ValueError as error:
          # That failed, but we can try again this time without requiring it
          # to be anonymous to allow the user to login.
          if self.broker_session:
            self.broker_session.disconnect()

          # There are two options for how to log the message here. One is to be
          # generic to match how this code is written (which is rather generic)
          # so it would be future-proof, for example "Initial attempt to licence
          # has failed, trying again.". Two is to actually say the intent at
          # the time which was "Failed to find a borrowed licence. Trying a live
          # licence."
          self.log.info('Failed to find a borrowed licence. Trying a live '
                        'licence.')

          # However it is possible the caller has explicitly said be
          # anonymous in which case this won't make any difference.
          if connection_parameters and connection_parameters.get(
              'AnonymousSession', False):
            raise

          # Capture the error so it can throw if it was the last one.
          broker_error = error
      else:
        raise broker_error

      # Setup mcpd connection
      self.options = options
      self.allow_hidden_objects = self.options.allow_hidden_objects

      if isinstance(existing_mcpd, McpdConnection):
        self.mcp_instance = existing_mcpd
      else:
        # An existing McpdConnection instance has not been supplied but if
        # existing_mcpd isn't None then connection details have been.
        self.mcp_instance = McpdConnection(
          self.options,
          specific_mcpd=existing_mcpd,
          )

      self.__connect_to_dataengine()

      # Store easy access for project's root object.
      self.root_id = ObjectID(capi.DataEngine().RootContainer())
    except:
      # If an error occurs then unload the project. The unload function is
      # capable of dealing with the incomplete state and will handle undoing
      # what was successfully done prior to the error.
      self.unload_project()
      raise

  def __enter__(self):
    self.log.debug("__enter__ called")
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.log.debug("__exit__ called")
    self.unload_project()

  def __load_dlls_with_dataengine_types(self) -> None:
    """Loads the DLLs which contain DataEngine types.

    This must be called before connecting to the DataEngine. Once the
    script has connected, it is an error to load DLLs which contain
    DataEngine types.
    """
    capi.DataEngine()
    capi.Modelling()
    capi.Selection()
    capi.Scan()
    capi.Viewer()
    capi.Vulcan()

    # The DrillholeModel DLL is only available when connecting to Vulcan
    # GeologyCore. Failing to load it thus should not be treated as an error.
    try:
      drillhole_version = capi.DrillholeModel().version
      # Only add the Drillhole and DrillholeDatabase classes if they are
      # supported by the C API.
      if drillhole_version >= (1, 7):
        # Register the drillhole types as openable.
        self._register_types([
          (6, Drillhole),
          (4, DrillholeDatabase)
        ])
      else:
        self.log.info(
          "The drillhole types are not available. The drillhole model DLL is "
          "too old.")
    except CApiDllLoadFailureError:
      self.log.info(
        "The drillhole types are not available. The drillhole model DLL "
        "could not be loaded.")

  def __connect_to_dataengine(self) -> None:
    """Connects the current OS thread to the DataEngine.

    This ensures the DLLs containing DataEngine types are loaded and handles
    the difference between the open modes.

    This will set: root_id, backend_index and
    _is_connected_to_existing_application.

    Notes
    -----
    It is an error to connect to the DataEngine on a thread which is already
    connected to the DataEngine.
    """
    self.__load_dlls_with_dataengine_types()

    self._is_connected_to_existing_application = False

    # Check the project options to see if using a host application DataEngine,
    # or creating/opening a new or existing one.
    if self.options.open_mode is ProjectOpenMode.MEMORY_ONLY:
      # No executables or servers will be used. This means no mcpd or
      # backendServer will be launched or used.
      self.dataengine_connection = capi.DataEngine().CreateLocal()
      if self.dataengine_connection:
        self.log.info("Created memory-only dataengine")
      else:
        last_error = capi.DataEngine().ErrorMessage().decode(
          "utf-8")
        error_message = ("There was an error while creating"
          f" memory-only project ({last_error})")
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)

      # A backend index of 0 means the backend is the DataEngine itself.
      self.backend_index = 0
    elif self.options.mcpd_mode is McpdMode.CONNECT_TO_EXISTING:
      # The host is expected to have an existing backend server running.
      if not self.mcp_instance.is_connected:
        error_message = "Connection with the mcpd failed. Can't connect " + \
          "to existing application. Check the application is functioning " + \
          "and is properly licenced."
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)
    elif self.options.mcpd_mode is McpdMode.CREATE_NEW:
      # Start a backend server.
      if 'MDF_BIN' not in os.environ:
        error_message = "Failed to register backend server - environment " + \
          "variable MDF_BIN not set."
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)

      # Ideally, the absolute path would be provided to the backendServer,
      # however the underlying function doesn't handle spaces. Using an
      # environment variable allows the given string to have no spaces but
      # for the path to contain spaces when it is expanded.
      backend_registered = self.mcp_instance.register_server(
        '$MDF_BIN/backendServer')
      if not backend_registered:
        error_message = "Failed to register backend server"
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)

      # Ensure there are no stale lock files.
      if not capi.DataEngine().DeleteStaleLockFile(
          self.options.project_path.encode('utf-8')):
        last_error = capi.DataEngine().ErrorMessage().decode("utf-8")
        self.log.error(
          "There was a problem ensuring no stale lock files "
          "had been left in the project. Error message: %s", last_error)

        # Try sharing the project?
        self.options.backend_type = ProjectBackendType.SHARED
        self.log.warning('Attempting to share the project "%s"',
                         self.options.project_path)

      # Create or open project.
      self.backend_index = capi.DataEngine().OpenProject(
        self.options.project_path.encode('utf-8'),
        self.options.open_mode,
        self.options.access_mode,
        self.options.backend_type,
        self.options.proj_units)
      if self.backend_index == 0:
        last_error = capi.DataEngine().ErrorMessage().decode("utf-8")
        error_message = ("There was a problem using the requested database "
                         "load or creation settings. If running in "
                         "stand-alone mode, check that the libraries "
                         "were built with appropriate license. "
                         f"Error message: {last_error}")
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)
    else:
      raise ProjectConnectionFailureError(
        f'Unsupported McpdMode: {self.options.mcpd_mode}')

    if self.dataengine_connection:
      # Store easy access for project's root object.
      self.root_id = ObjectID(capi.DataEngine().RootContainer())
    else:
      # Connecting to an existing DataEngine session.
      create_new_session = False
      self.dataengine_connection = capi.DataEngine().Connect(
        create_new_session)
      if not self.dataengine_connection:
        last_error = capi.DataEngine().ErrorMessage().decode("utf-8")
        error_message = (
          f"There was an error connecting to the database ({last_error})")
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)

      # Store easy access for project's root object.
      self.root_id = ObjectID(capi.DataEngine().RootContainer())

      # The backend is managed by an existing application and what kind of
      # backend is not provided when connecting to it, however we can query
      # it from the root object.
      backend_index = ctypes.c_uint16()
      if not capi.DataEngine().ObjectBackEnd(self.root_id.handle,
                                             ctypes.byref(backend_index)):
        last_error = capi.DataEngine().ErrorMessage().decode("utf-8")
        error_message = (
          "Unable to determine the backend used by the application "
          f"({last_error})")
        self.log.critical(error_message)
        raise ProjectConnectionFailureError(error_message)

      self.backend_index = backend_index
      self._is_connected_to_existing_application = True
    capi.DataEngine().is_connected = self.dataengine_connection

  def __find_from(
    self,
    object_id: ObjectID[DataObject],
    names: list[str],
    create_if_not_found: bool) -> ObjectID[DataObject] | None:
    """Internal function for find_object() and
    _find_object_or_create_if_missing().

    Parameters
    ----------
    object_id
      The ID of the object to start at.
    names
      list of container paths to recursively search through
      and / or create if not found (if create_if_not_found)
      e.g. ['surfaces', 'new container', 'surfaces 2'].
    create_if_not_found
      Create specified path if it doesn't exist.

    Returns
    -------
    ObjectID
      Object ID of the object if found.
    None
      Object could not be found including if the object couldn't be
      created when it's not found.
      The path can't be created if the object is not a container or is
      a topology which shouldn't be treated as a container (unless
      allow_hidden_objects is True).

    Raises
    ------
    Exception
      Error trying to create path that didn't exist (unknown error).
    ValueError
      A new path needs to be created and will result in
      creating hidden objects (i.e. start with '.') when
      project attribute allow_hidden_objects is False.

    """
    if not names:
      return object_id

    if not object_id.is_a(Container):
      self.log.info("The path %s can not be created as the object before it "
                    "is not a container",
                    '/'.join(names))
      # names could not be found.
      return None

    if object_id.is_a(Topology) and not self.allow_hidden_objects:
      # Treat it as if the object couldn't be found (specifically the container).
      #
      # This prevents creating a container within a topology object.
      self.log.info("The path %s can not be created as the object before it "
                    "is a topology and allow_hidden_objects is False.",
                    '/'.join(names))
      return None

    with ReadLock(object_id.handle) as r_lock:
      found = ObjectID(capi.DataEngine().ContainerFind(
        r_lock.lock, names[0].encode("utf-8")))

    if not found and create_if_not_found:
      self.log.info("The path %s didn't exist so attempting to create it.",
                    '/'.join(names))

      if not self.allow_hidden_objects:
        # Check that none of the objects created would be hidden.
        if any(name.startswith('.') for name in names):
          raise ValueError("Invalid path provided. No object name may start "
                           "with '.' as that would be a hidden object.")

      # Create a new container for each part of the path (as none of them
      # exist)
      new_containers = [
        ObjectID(capi.Modelling().NewVisualContainer())
        for _ in range(len(names))
      ]

      # Add each new container to the container before it.
      new_parents = [object_id] + new_containers[:-1]
      for parent, child, name in zip(reversed(new_parents),
                                     reversed(new_containers),
                                     reversed(names)):
        with WriteLock(self.__get_obj_handle(parent)) as w_lock:
          capi.DataEngine().ContainerAppend(
            w_lock.lock,
            name.encode("utf-8"),
            self.__get_obj_handle(child),
            True)
      return new_containers[-1]

    if not found and not create_if_not_found:
      # It doesn't exist and the caller wants to know
      return None
    return self.__find_from(found, names[1:], create_if_not_found)

  def _register_types(self, new_types: list[tuple[int, type]]) -> None:
    """Register types to be openable via Project.edit() and Project.read().

    This maintains the sort order of the list of openable types.

    Parameters
    ----------
    new_types
      List of tuples of the form (priority, type) where priority is the
      priority of the new type and type is the new openable type.
      The new type must inherit from DataObject.
    """
    self.__types_for_data.extend(new_types)
    # This is using sort instead of "bisect.insort" because reversing
    # insort requires Python 3.10.
    self.__types_for_data.sort(key=lambda x: x[0], reverse=True)

  def unload_project(self) -> None:
    """Call the mcp class to unload a spawned mcp instance (i.e. when not
    using a host application like Eureka or PointStudio).
    Use this when finished operating on a project that has
    ProjectOptions that requested an mcpd_mode of CREATE_NEW.

    Also unloads dataengine created with same methods.

    Failure to call this un-loader may leave orphan mcpd.exe processes
    running on the machine.

    """
    self.log.info("unload_project() called")
    if self.backend_index is not None:
      if self._is_connected_to_existing_application:
        # The backend for the project is hosted by another application, we
        # simply need to disconnect from it. However if our connection was
        # keeping the backend alive we need to close it if we are the last
        # one.
        self.log.info("Disconnecting from a project opened by an another "
                      "application.")
        close_backends_if_last_client = True
        capi.DataEngine().Disconnect(close_backends_if_last_client)
        self._is_connected_to_existing_application = False
      elif self.backend_index == 0:
        # A DataEngine backed project aren't expected to have any other
        # clients. Its primary use is for tests and scripts which need to
        # open a DataEngine, create/import and save results then close it, i.e
        # not in multi-process situations where the lifetime of the processes
        # are unknown.
        self.log.info("Disconnecting from an in-memory project.")
        close_backends_if_last_client = False
        capi.DataEngine().Disconnect(close_backends_if_last_client)
      else:
        self.log.info("Closing project with backend index: %s",
                      self.backend_index)
        capi.DataEngine().CloseProject(self.backend_index)
      self.backend_index = None

    if self.mcp_instance:
      try:
        self.mcp_instance.unload_mcp()
      except McpdDisconnectError:
        # The exception is already logged, so it is safe to ignore it.
        pass

    if self.broker_session:
      self.broker_session.disconnect()

    if self.__dll_directory_set:
      disable_dll_loading()
      self.__dll_directory_set = False

    # The project has been unloaded so it doesn't need to be done when the
    # interpreter terminates.
    if self._exit_function:
      atexit.unregister(self._exit_function)
      self._exit_function = None

  @property
  def api_version(self) -> tuple[int, int]:
    """Returns the API version reported by the application.

    Returns
    -------
    tuple
      The API version of the application in the form: (major, minor).

    Notes
    -----
    The following table summarises the API version for officially supported
    applications:

    +---------------------------+-------------+
    | Application               | api_version |
    +===========================+=============+
    | Eureka 2020               | (1, 1)      |
    +---------------------------+-------------+
    | PointStudio 2020          | (1, 1)      |
    +---------------------------+-------------+
    | PointStudio 2021          | (1, 2)      |
    +---------------------------+-------------+
    | PointStudio 2021.1        | (1, 3)      |
    +---------------------------+-------------+
    | PointStudio 2022          | (1, 3)      |
    +---------------------------+-------------+
    | PointStudio 2022.0.1      | (1, 3)      |
    +---------------------------+-------------+
    | PointStudio 2022.1        | (1, 3)      |
    +---------------------------+-------------+
    | Vulcan GeologyCore 2021   | (1, 4)      |
    +---------------------------+-------------+
    | Vulcan GeologyCore 2021.1 | (1, 4)      |
    +---------------------------+-------------+
    | Vulcan GeologyCore 2022   | (1, 5)      |
    +---------------------------+-------------+
    | Vulcan GeologyCore 2022.1 | (1, 7)      |
    +---------------------------+-------------+

    Earlier applications will have an API version of (0, 0). It is not
    recommended to connect to applications with API versions less than (1, 1).
    """
    # Though each C API could have its own version, currently they all
    # return the same version.
    return capi.Modelling().version

  def raise_if_version_below(self, version: tuple[int, int]) -> None:
    """Raises an error if the script has connected to an application whose
    version is lower than the specified version.

    This allows for scripts to exit early when attaching to an application
    which does not support the required data types.

    Parameters
    ----------
    version
      A tuple (major, minor). If the API version is less than this tuple
      an error will be raised.

    Raises
    ------
    ApplicationTooOldError
      If the API version is lower than the specified version.

    Examples
    --------
    Exit if the application does not support GridSurface (api_version is
    less than (1, 2)).

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> project.raise_if_version_below((1, 2))

    It is also possible to catch this error and add extra information.

    >>> from mapteksdk.project import Project, ApplicationTooOldError
    >>> project = Project()
    >>> try:
    ...     project.raise_if_version_below((1, 2))
    >>> except ApplicationTooOldError as error:
    ...     raise SystemExit("The attached application does not support "
    ...                      "irregular grids") from error

    """
    if self.api_version < version:
      message = (f"API version is too old: {self.api_version}. "
                 f"This script requires an API version of at least: {version}")
      raise ApplicationTooOldError(message)

  def find_object(self, path: str) -> ObjectID[DataObject] | None:
    """Find the ObjectID of the object at the given path.

    Parameters
    ----------
    path
      Path to the object.

    Returns
    -------
    ObjectID
      The ID of the object at the given path.
    None
      If there was no object at path.

    """
    parts = path.strip("/").split("/")
    # Remove empty strings (e.g. /surfaces/ = '', surfaces, '')
    parts = list(filter(None, parts))
    return self.__find_from(self.root_id, parts, create_if_not_found=False)

  def _find_object_or_create_if_missing(self, path: str
      ) -> ObjectID[DataObject]:
    """Find object ID of the object at the given path.

    Parameters
    ----------
    path
      The path to the object to get or create.

    Returns
    -------
    ObjectID
      The ID of the object at the given path.
    None
      If the path doesn't exist.

    """
    parts = path.strip("/").split("/")
    # Remove empty strings (e.g. /surfaces/ = '', surfaces, '')
    parts = list(filter(None, parts))
    return self.__find_from(self.root_id, parts, create_if_not_found=True)

  @contextmanager
  @typing.overload
  def read(self, path_or_id: str) -> Generator[DataObject, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield DataObject(None, None)

  @contextmanager
  @typing.overload
  def read(self, path_or_id: ObjectID[ObjectIdT]
      ) -> Generator[ObjectIdT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield DataObject(None, None)

  @contextmanager
  @typing.overload
  def read(self, path_or_id: str, expected_object_type: type[ObjectT]
      ) -> Generator[ObjectT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield expected_object_type(None, None)

  @contextmanager
  @typing.overload
  def read(
      self,
      path_or_id: ObjectID[ObjectIdT],
      expected_object_type: type[ObjectT]
      ) -> Generator[ObjectT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield expected_object_type(None, None)

  @contextmanager
  def read(self,
      path_or_id: str | ObjectID[ObjectIdT],
      expected_object_type: ObjectT | None = None
      ) -> Generator[DataObject | ObjectIdT, None, None]:
    """Open an existing object in read-only mode.

    In read-only mode the values in the object can be read, but no changes can
    be saved. Use this function instead of edit() if you do not intend to make
    any changes to the object.

    If this is called using a with statement, close() is called
    automatically at the end of the with block.

    Parameters
    ----------
    path_or_id
      The path or the ID of the object to open.
    expected_object_type
      The expected type for the object. If None (default), then the type will
      be determined automatically.
      If set to a DataObject subclass, the object will be opened as that
      subclass. If the object is not of this type, a TypeMismatchError will
      be raised.

    Raises
    ------
    ObjectDoesNotExistError
      If path_or_id is not an existent object.
    TypeMismatchError
      If expected_object_type is specified and path_or_id refers to an object
      which cannot be opened as that type.
    TypeError
      If path_or_id is an unsupported object.

    Examples
    --------
    Read an object at path/to/object/to/read and then print out the
    point, edge and facet counts of the object.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> path = "path/to/object/to/read"
    >>> with project.read(path) as read_object:
    ...     if hasattr(read_object, "point_count"):
    ...         print(f"{path} contains {read_object.point_count} points")
    ...     if hasattr(read_object, "edge_count"):
    ...         print(f"{path} contains {read_object.edge_count} edges")
    ...     if hasattr(read_object, "facet_count"):
    ...         print(f"{path} contains {read_object.facet_count} facets")
    ...     if hasattr(read_object, "cell_count"):
    ...         print(f"{path} contains {read_object.cell_count} blocks")
    ...     if hasattr(read_object, "block_count"):
    ...         print(f"{path} contains {read_object.block_count} blocks")

    The optional expected_object_type parameter can be used to ensure that
    the read object is of a specified type. This will cause Project.read()
    to raise an error if the object is not of the specified type, however it
    also guarantees that within the with block the read object will be of
    the specified type. This is demonstrated by the following example:

    >>> from mapteksdk.project import Project
    >>> from mapteksdk.data import Surface
    >>> path = "path/to/object/to/read"
    >>> with Project() as project:
    ...     # Because the second argument was set to Surface, this will raise
    ...     # an error if the object is not a Surface.
    ...     with project.read(path, Surface) as surface:
    ...         # The surface variable is guaranteed to be a surface here,
    ...         # so it is not necessary to check if the object has these
    ...         # properties.
    ...         print(f"{path} contains {surface.point_count} points")
    ...         print(f"{path} contains {surface.edge_count} edges")
    ...         print(f"{path} contains {surface.facet_count} facets")
    """
    if isinstance(path_or_id, ObjectID):
      object_id = path_or_id
    else:
      object_id = self.find_object(path_or_id)

    if not object_id or not object_id.exists:
      error_msg = f"Tried to read an object that doesn't exist: {path_or_id}"
      self.log.error(error_msg)
      raise ObjectDoesNotExistError(error_msg)

    if expected_object_type:
      # If the object type was specified raise an error if the object is
      # not of that type.
      # pylint: disable=protected-access
      if object_id._is_exactly_a(expected_object_type):
        object_type = expected_object_type
      else:
        actual_object_type = self._type_for_object(object_id)
        raise TypeMismatchError(expected_object_type, actual_object_type)
    else:
      # The object type was not specified, so derive it.
      object_type = self._type_for_object(object_id)

    opened_object = object_type(object_id, LockType.READ)
    try:
      yield opened_object
    finally:
      opened_object.close()

  @contextmanager
  def new(
      self,
      object_path: str,
      object_class: type[ObjectT] | ObjectT ,
      overwrite: bool=False) -> Generator[ObjectT, None, None]:
    """Create a new object and add it to the project. Note that
    changes made to the created object will not appear in the
    view until save() or close() is called.

    If this is called using a with statement, save() and close()
    are called automatically at the end of the with block.

    Parameters
    ----------
    object_path
      Full path for new object. e.g. "surfaces/generated/new surface 1"
      If None, the new object will not be assigned a path and will
      only be available through its object ID.
    object_class
      The type of the object to create. (e.g. Surface).
    overwrite
      If overwrite=False (default) a ValueError is raised if
      there is already an object at new_name.
      If overwrite=True then any object at object_path is replaced
      by the new object. The overwritten object is orphaned rather
      than deleted and may still be accessible through its id.

    Yields
    ------
    DataObject
      The newly created object. The type of this will be object_class.

    Raises
    ------
    ValueError
      If an object already exists at new_path and overwrite = False.
    ValueError
      If object path is blank, '.' or '/'.
    TypeError
      If creating an object of the given type is not supported.
    NotImplementedError
      If creating an object of the given type is not implemented but may
      be implemented in a future version of the SDK.
    InvalidParentError
      If object_path contains an object that can't be a parent of the new
      object.

    Notes
    -----
    If an exception is raised while creating the object the object will
    not be saved.

    If you do not assign a path to an object on creation, project.add_object()
    can be used to assign a path to the object after creation.

    Examples
    --------
    Create a new surface and set it to be a square with side length
    of two and centred at the origin.

    >>> from mapteksdk.project import Project
    >>> from mapteksdk.data import Surface
    >>> project = Project()
    >>> points = [[-1, -1, 0], [1, -1, 0], [-1, 1, 0], [1, 1, 0]]
    >>> facets = [[0, 1, 2], [1, 2, 3]]
    >>> with project.new("surfaces/square", Surface) as new_surface:
    ...   new_surface.points = points
    ...   new_surface.facets = facets
    ...   # new_surface.close is called implicitly here.

    """
    # Background process:
    # Create empty object of provided type, get new handle & open write lock
    # with [yield >> user populates with data]
    # finally [done] >> Add to project
    if isinstance(object_class, type):
      # :TRICKY: Check if the user passed in a type, like Triangle,
      # or instance of that type, like Triangle().  This is
      # required to support more complicated types that require
      # constructor parameters to be useful (like DenseBlockModel(...)).
      # If not an instance, then create one:
      new_object = object_class(lock_type=LockType.READWRITE)
    else:
      new_object = object_class
    try:
      yield new_object
      new_object.save()
      if object_path is not None:
        # The new object does not yet exist as an item in the Project
        # add it now.
        self.add_object(object_path, new_object, overwrite=overwrite)
      new_object.close()
    except:
      # If there was an exception the object is an orphan,
      # so delete it then re-raise the exception.
      new_object.close()
      self.delete(new_object, True)
      raise

  @contextmanager
  @typing.overload
  def edit(self, path_or_id: str) -> Generator[DataObject, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield DataObject(None, None)

  @contextmanager
  @typing.overload
  def edit(self, path_or_id: ObjectID[ObjectIdT]
      ) -> Generator[ObjectIdT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield DataObject(None, None)

  @contextmanager
  @typing.overload
  def edit(self, path_or_id: str, expected_object_type: type[ObjectT]
      ) -> Generator[ObjectT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield expected_object_type(None, None)

  @contextmanager
  @typing.overload
  def edit(
      self,
      path_or_id: ObjectID[ObjectIdT],
      expected_object_type: type[ObjectT]
      ) -> Generator[ObjectT, None, None]:
    # :HACK: SDK-785. This is a workaround for a false positive in
    # pylint's 'not-context-manager' check:
    # https://github.com/PyCQA/pylint/issues/5273
    # The body of the overload should be:
    # ...
    yield expected_object_type(None, None)

  @contextmanager
  def edit(
      self,
      path_or_id: str | ObjectID[ObjectIdT],
      expected_object_type: ObjectT | None = None
      ) -> Generator[DataObject | ObjectIdT, None, None]:
    """Open an existing object in read/write mode.

    Unlike read, this allows changes to be made to the object. Note that
    changes made will not appear in the view until save() or close() is called.

    If this is called using a with statement, save() and close()
    are called automatically at the end of the with block.

    Parameters
    ----------
    path_or_id
      Path or ID of the object to edit.
    expected_object_type
      The expected type for the object. If None (default), then the type will
      be determined automatically.
      If set to a DataObject subclass, the object will be opened as that
      subclass. If the object is not of this type, a TypeMismatchError will
      be raised.

    Yields
    ------
    DataObject
      The object at the specified path opened for editing.

    Raises
    ------
    ObjectDoesNotExistError
      If the object to edit does not exist.
    TypeMismatchError
      If expected_object_type is specified and path_or_id refers to an object
      which cannot be opened as that type.
    TypeError
      If the object type is not supported.

    Notes
    -----
    If an exception is raised while editing an object, any changes made
    inside the with block are not saved.

    Examples
    --------
    Edit the surface created in the example for project.new to a hourglass
    shape instead of a square.

    >>> from mapteksdk.project import Project
    >>> points = [[-1, -1, 0], [1, -1, 0], [-1, 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> facets = [[0, 1, 4], [2, 3, 4]]
    >>> project = Project()
    >>> with project.edit("surfaces/square") as edit_surface:
    ...     edit_surface.points = points
    ...     edit_surface.facets = facets
    ...     # edit_surface.close is called implicitly here.

    One problem with the above example is that if the object at
    "surfaces/square" is not a Surface it will fail.
    e.g. If "surfaces/square" is a Polyline, Polygon or EdgeNetwork:

      * The assignment to "points" would succeed because these objects
        have points, just like a surface.
      * The assignment to "facets" would fail silently because Python allows
        the assignment even though the object does not have facets.
      * The script would exit with a success even though it actually failed
        to set the facets.

    This can be avoided by specifying the expected type of the object when
    opening it. This ensures that if the object is of an unexpected type, the
    script will fail before any changes have been made to the object. By failing
    quickly, the chances of unintentional changes are minimised.
    A fixed version of the above example is shown below:

    >>> from mapteksdk.project import Project
    >>> from mapteksdk.data import Surface
    >>> points = [[-1, -1, 0], [1, -1, 0], [-1, 1, 0], [1, 1, 0], [0, 0, 0]]
    >>> facets = [[0, 1, 4], [2, 3, 4]]
    >>> project = Project()
    >>> # The second argument of Surface means this will fail immediately
    >>> # with an exception if the object at "surfaces/square" is not
    >>> # a surface.
    >>> with project.edit("surfaces/square", Surface) as edit_surface:
    ...     edit_surface.points = points
    ...     edit_surface.facets = facets
    """
    if isinstance(path_or_id, ObjectID):
      object_id = path_or_id
    else:
      object_id = self.find_object(path_or_id)

    if not object_id or not object_id.exists:
      error_msg = f"Tried to edit an object that doesn't exist: {path_or_id}"
      self.log.error(error_msg)
      raise ObjectDoesNotExistError(error_msg)

    if expected_object_type:
      # If the object type was specified raise an error if the object is
      # not of that type.
      # pylint: disable=protected-access
      if object_id._is_exactly_a(expected_object_type):
        object_type = expected_object_type
      else:
        actual_object_type = self._type_for_object(object_id)
        raise TypeMismatchError(expected_object_type, actual_object_type)
    else:
      # The object type was not specified, so derive it.
      object_type = self._type_for_object(object_id)

    opened_object = object_type(object_id, LockType.READWRITE)
    try:
      yield opened_object
      opened_object.save()
    except:
      # Only some object types require cancelling the pending changes to an
      # object here, as many are written in such a way that the changes are
      # deferred until save().
      cancel = getattr(opened_object, 'cancel', None)
      if cancel:
        cancel()

      raise
    finally:
      opened_object.close()

  @contextmanager
  def new_or_edit(
      self,
      path: str,
      object_class: ObjectT | type[ObjectT],
      overwrite: bool=False) -> Generator[ObjectT, None, None]:
    """This function works as project.new if the specified object does not
    exist. Otherwise it acts as project.edit.

    Parameters
    ----------
    path
      Path to the object to create or edit.
    object_class
      Class of the object to create or edit.
    overwrite
      If False (default) and there is already an object at path
      whose type is not editable as object_class a ValueError is raised.
      If True, any object at path which is not object_class
      is orphaned to make room for the new object.

    Yields
    ------
    DataObject
      The newly created object or the object at the specified path.

    Raises
    ------
    ValueError
      If overwrite=False and there exists an object at path whose
      type is not object class.
    AttributeError
      If path is not a string.
    InvalidParentError
      If object_path contains an object that can't be a parent of the new
      object.

    """
    existing_id = self.find_object(path)

    # Edit if there is an object of the correct type at path. Otherwise
    # attempt to create a new object of the correct type at path.
    if existing_id and existing_id.is_a(object_class):
      with self.edit(path) as opened_object:
        yield opened_object
    else:
      with self.new(path, object_class, overwrite) as opened_object:
        yield opened_object

  def __get_obj_handle(
      self,
      object_or_handle: DataObject | ObjectID[DataObject] | T_ObjectHandle | str
      ) -> T_ObjectHandle:
    """Helper to retrieve T_ObjectHandle for passing to the C API.

    Parameters
    ----------
    object_or_handle
      Object with a handle, ID of an object, object handle or path to object.

    Returns
    -------
    T_ObjectHandle
      The object handle.
    None
      On exception.

    """
    if object_or_handle is None:
      return None

    if isinstance(object_or_handle, ObjectID):
      return object_or_handle.handle

    if isinstance(object_or_handle, str):
      object_or_handle = self.find_object(object_or_handle)
      return None if object_or_handle is None else object_or_handle.handle

    if isinstance(object_or_handle, T_ObjectHandle):
      return object_or_handle

    return object_or_handle.id.handle

  @typing.overload
  def add_object(
      self,
      full_path: str,
      new_object: ObjectID[ObjectIdT],
      overwrite: bool=False) -> ObjectID[ObjectIdT]:
    ...

  @typing.overload
  def add_object(
      self,
      full_path: str,
      new_object: ObjectT,
      overwrite: bool=False) -> ObjectID[ObjectT]:
    ...

  def add_object(
      self,
      full_path: str,
      new_object: ObjectT | ObjectID[ObjectIdT],
      overwrite: bool=False) -> ObjectID[ObjectT | ObjectIdT]:
    r"""Adds a new DataObject to the project. Normally this is not necessary
    because Project.new() will add the object for you. This should only need
    to be called if Project.new() was called with path = None or after a call
    to a function from the mapteksdk.io module.

    Parameters
    ----------
    full_path
      Full path to the new object (e.g. '/surfaces/new obj').
    new_object : DataObject or ObjectID
      Instance or ObjectID of the object to store at full_path.
    overwrite
      If overwrite=False (default) a ValueError will be raised if there is
      already an object at full_path. If overwrite=True and there is an
      object at full_path it will be overwritten and full_path will now point
      to the new object. The overwritten object becomes an orphan.

    Returns
    -------
    ObjectID
      ID of newly stored object. This will be the object ID of
      new_object.

    Raises
    ------
    ValueError
      If invalid object name (E.g. '/', '', or (starting with) '.' when
      project options don't allow hidden objects).
    ValueError
      If path contains back slashes (\).
    ValueError
      If overwrite=False and there is already an object at full_path.
    TypeError
      If full_path is not a string.
    TypeError
      If new_object is not a DataObject or ObjectID
    InvalidParentError
      If new_object is being added to an object that is not a container.
      Topology objects are not considered containers when the project options
      don't allow hidden objects. The fact that they're containers is a
      implementation detail and they're not portrayed as containers to end
      users in the applications.

    Notes
    -----
    Has no effect if new_object is already at full_path.

    """
    if not isinstance(full_path, str):
      raise TypeError(
        default_type_error_message("full_path", full_path, str)
      )
    container_name, object_name = self._valid_path(full_path)
    if container_name == '':
      container_object = self.root_id
    else:
      self.log.info('Adding object %s to %s', object_name, container_name)
      container_object = self._find_object_or_create_if_missing(container_name)
    handle_to_add = self.__get_obj_handle(new_object)
    if not isinstance(handle_to_add, T_ObjectHandle):
      raise TypeError(
        default_type_error_message(
          "new_object", new_object, (DataObject, ObjectID)
        )
      )

    if not container_object:
      raise InvalidParentError("new_object", full_path)

    if not container_object.is_a(Container) or (
            container_object.is_a(Topology) and not self.allow_hidden_objects):
      raise InvalidParentError("new_object", full_path)

    self.log.debug("Opening container %s to store object: %s",
                   container_name, ObjectID(handle_to_add))
    with WriteLock(self.__get_obj_handle(container_object)) as w_lock:
      existing_object = capi.DataEngine().ContainerFind(
        w_lock.lock, object_name.encode("utf-8"))
      if existing_object:
        if handle_to_add.value == existing_object.value:
          return ObjectID(existing_object)
        if overwrite:
          capi.DataEngine().ContainerRemoveObject(
            w_lock.lock, existing_object, False)
        else:
          raise ValueError(
            f"There is already an object in the container called {object_name}"
          )

      capi.DataEngine().ContainerAppend(w_lock.lock,
                                        object_name.encode("utf-8"),
                                        handle_to_add,
                                        True)
    self.log.debug("Stored new object %s into container %s",
                   object_name,
                   container_name)
    return ObjectID(handle_to_add)

  def add_objects(
      self,
      destination_container: str,
      new_objects: list[tuple[str, ObjectID[DataObject]]] |
                   dict[str, ObjectID[DataObject]],
      overwrite: bool=False) -> list[ObjectID[DataObject]]:
    r"""Adds multiple objects into the project.

    This can be used to batch the insertions. Most likely you will want to use
    this with an object that hasn't been added to the project before. You can
    avoid adding new objects to the project when calling Project.new() by
    providing a path of None.

    This is treated as an atomic operation so either all objects are added or
    none are added. This means if there is a problem with adding one of the
    objects then none of the objects will be added and the destination
    container will remain unchanged.

    Parameters
    ----------
    destination_container
      Full path to the container where the objects will be added.
    new_objects
      If new_objects is a dictionary then the keys are names and the values
      are the objects to add.
      If new_objects is a list then the list should contain (name, object)
      pairs.
      The objects can be either DataObject or ObjectID.
    overwrite
      If overwrite=False (default) a ValueError will be raised if there is
      already an object in the destination container with that name that isn't
      the object itself. If overwrite=True and there is an object in the
      destination container then it will be overwritten. The overwritten
      object becomes an orphan.

    Returns
    -------
    list
      A list of object IDs of newly added objects.
      This will be in the same order as add_objects().
      If an object was already in the container under that name it will still
      be returned even when it wasn't added.

    Raises
    ------
    ValueError
      If invalid object name (E.g. '/', '', or (starting with) '.' when
      project options don't allow hidden objects).
    ValueError
      If paths contains back slashes (\).
    ValueError
      If overwrite=False and there is already an object in the destination
      container with that name and it is not the object being added.
    InvalidParentError
      If destination_container or an object in the path is not a container.
      Topology objects are not considered containers when the project options
      don't allow hidden objects. The fact that they're containers is a
      implementation detail and they're not portrayed as containers to end
      users in the applications.

    Warnings
    --------
    For older versions of the application, if an error occurs any objects added
    prior to the object which triggered the error will still be added.

    Notes
    -----
    If any object in new_objects is already in the destination container with
    the specified name, it will be left unchanged.
    """
    parent_name, container_name = self._valid_path(destination_container)
    if parent_name == '':
      container_object = self.root_id
    else:
      container_object = self._find_object_or_create_if_missing(
        posixpath.join(parent_name, container_name))

    if isinstance(new_objects, dict):
      new_objects = new_objects.items()

    if not container_object:
      raise InvalidParentError("new_object", destination_container)

    if not container_object.is_a(Container) or (
        container_object.is_a(Topology) and not self.allow_hidden_objects):
      raise InvalidParentError("new_objects", destination_container)

    objects_added = []

    with WriteLock(self.__get_obj_handle(container_object),
                   rollback_on_error=True) as w_lock:

      for object_name, object_to_add in new_objects:
        self._check_path_component_validity(object_name)
        handle_to_add = self.__get_obj_handle(object_to_add)

        existing_object = capi.DataEngine().ContainerFind(
          w_lock.lock, object_name.encode('utf-8'))

        if existing_object:
          if handle_to_add.value == existing_object.value:
            objects_added.append(ObjectID(existing_object))
            continue

          if overwrite:
            capi.DataEngine().ContainerRemoveObject(
              w_lock.lock, existing_object, False)
          else:
            raise ValueError(
              "There is already an object in the container called "
              f"{object_name}"
            )

        capi.DataEngine().ContainerAppend(w_lock.lock,
                                          object_name.encode('utf-8'),
                                          handle_to_add,
                                          True)
        objects_added.append(ObjectID(handle_to_add))

    return objects_added

  def get_children(self, path_or_id: str | ObjectID[DataObject]=""
      ) -> ChildView:
    """Return the children of the container at path as (name, id) pairs.

    Parameters
    ----------
    path_or_id
      The path or object ID of the container to work with.

    Returns
    -------
    ChildView
      Provides a sequence that can be iterated over to provide the
      (name, id) for each child. It also provides name() and ids() functions
      for querying just the names and object IDs respectively.

    Raises
    ------
    ObjectDoesNotExistError
      If the path does not exist in the project.
    TypeError
      If the path is not a container.
    ValueError
      If the path is a container but not suitable for accessing its children.

    """

    if isinstance(path_or_id, str):
      if path_or_id and path_or_id != '/':
        container = self.find_object(path_or_id)
      else:
        container = self.root_id
    else:
      container = path_or_id
      path_or_id = '/'

    if not container:
      message_template = '"%s" is not in the project.'
      self.log.error(message_template, path_or_id)
      raise ObjectDoesNotExistError(message_template % path_or_id)

    if not container.is_a(Container):
      message_template = 'The object "%s" (%s) is not a container.'
      self.log.error(message_template, path_or_id, container)
      raise TypeError(
        default_type_error_message(
          argument_name="path_or_id",
          actual_value=path_or_id,
          required_type=(str, ObjectID[Container])
        )
      )

    # TODO: Prevent the users from querying the children of certain objects
    # that they don't see as being containers like edge chain/loops
    # (topologies). This issue is tracked by SDK-46.

    with self.read(ObjectID(self.__get_obj_handle(container))) as container:
      container.allow_hidden_objects = self.allow_hidden_objects
      return ChildView(container.items())

  def get_descendants(self, path_or_id: str | ObjectID[Container]=""
      ) -> ChildView:
    """Return all descendants of the container at path as (name, id) pairs.

    Parameters
    ----------
    path_or_id
      The path or object ID of the container to work with.

    Returns
    -------
    ChildView
      Provides a sequence that can be iterated over to provide the
      (name, id) for each child. It also provides name() and ids() functions
      for querying just the names and object IDs respectively.

    Raises
    ------
    KeyError
      If the path does not exist in the project.
    TypeError
      If the path is not a container.
    ValueError
      If the path is a container but not suitable for accessing its children.

    """
    def list_all_descendants(parent: str | ObjectID[Container]
        ) -> list[tuple[str, ObjectID[DataObject]]]:
      # Recursive function to retrieve all children of all VisualContainers
      results = []
      for child_name, child_id in self.get_children(parent):
        results.append((child_name, child_id))
        if child_id.is_a(VisualContainer):
          if isinstance(parent, str):
            # if provided, use a path to define the next level of the family,
            # avoiding any issue where an ObjectID has multiple paths.
            path = posixpath.join(parent, child_name)
            results.extend(list_all_descendants(path))
          else:
            results.extend(list_all_descendants(child_id))
      return results
    return ChildView(list_all_descendants(path_or_id))

  @typing.overload
  def copy_object(
      self,
      object_to_clone: ObjectID[ObjectIdT],
      new_path: str,
      overwrite: bool=False,
      allow_standard_containers: bool=False) -> ObjectID[ObjectIdT]:
    ...

  @typing.overload
  def copy_object(
      self,
      object_to_clone: str,
      new_path: str,
      overwrite: bool=False,
      allow_standard_containers: bool=False) -> ObjectID[DataObject]:
    ...

  @typing.overload
  def copy_object(
      self,
      object_to_clone: ObjectT,
      new_path: str,
      overwrite: bool=False,
      allow_standard_containers: bool=False) -> ObjectID[ObjectT]:
    ...

  def copy_object(
      self,
      object_to_clone: ObjectT | ObjectID[ObjectIdT] | str,
      new_path: str,
      overwrite: bool=False,
      allow_standard_containers: bool=False) -> ObjectID[
        ObjectIdT | ObjectT | DataObject] | None:
    """Deep clone DataObject to a new object (and ObjectID).

    If this is called on a container, it will also copy all of the
    container's contents.

    Parameters
    ----------
    object_to_clone
      The object to clone or the ID for the object to clone
      or a str representing the path to the object.
    new_path
      full path to place the copy (e.g. 'surfaces/new/my copy').
      Set as None for just a backend object copy.
    overwrite
      If False (default) a ValueError will be raised if
      there is already an object at new_name.
      If True and there is an object at new_path the object
      at new_path is overwritten. The overwritten object is orphaned
      instead of deleted and may still be accessible via its id.
    allow_standard_containers
      If False (default) then attempting to copy a standard container
      will create a visual container instead.
      If True (not recommended) copying a standard container will
      create a new standard container.

    Returns
    -------
    ObjectID
      Id of new object (The clone).
    None
      If the operation failed.

    Raises
    ------
    ObjectDoesNotExistError
      If object_to_clone does not exist.
    ValueError
      If an object already exists at new_path and overwrite = False.
    RuntimeError
      If object_to_clone is a DataObject subclass and it is open with
      Project.edit().

    """
    source_id = object_to_clone
    if isinstance(object_to_clone, str):
      source_id = self.find_object(object_to_clone)
    elif isinstance(object_to_clone, DataObject):
      # pylint: disable=protected-access
      # Error if the object is opened for editing. Because the changes
      # made in the SDK are cached until save() is called, copying an
      # object open for editing has surprising behaviour where it will
      # copy the object as it was before it was opened for editing.
      if (object_to_clone.lock_type is LockType.READWRITE
          and not object_to_clone.closed):
        raise RuntimeError("Cannot copy an object open for editing.")
      source_id = object_to_clone.id

    # This allows type(None) because the None case is handled by the
    # next if statement.
    if not isinstance(source_id, (ObjectID, type(None))):
      raise TypeError(default_type_error_message(
        "object_to_clone",
        object_to_clone,
        ObjectID))

    if source_id is None or not source_id.exists:
      raise ObjectDoesNotExistError(
          f"Cannot copy non-existent object: '{object_to_clone}'"
        )

    if not isinstance(new_path, (str, type(None))):
      raise TypeError(default_type_error_message("new_path", new_path, str))

    # Special handling for standard containers.
    #
    # Copying a standard container creates a visual container instead
    # of a standard container. This is what happens in the application when
    # the user user copies and pastes a standard container.
    #
    # If allow_standard_containers then this is not done and a new standard
    # container will created.
    if source_id.is_a(StandardContainer) and not allow_standard_containers:
      with self.read(source_id) as source:
        # It is hard to know why the container had hidden objects and thus if
        # they should always be copied. The behaviour to date has been to only
        # copy hidden objects if its allowed.
        source.allow_hidden_objects = self.allow_hidden_objects
        source_children = source.items()

      with self.new(new_path, VisualContainer, overwrite=False) as copy:
        # Clone each object in the standard container and add to copy.
        for child_name, child_id in source_children:
          copied_child_id = self.copy_object(child_id, new_path=None)
          copy.append((child_name, copied_child_id))

      return copy.id

    old_handle = self.__get_obj_handle(source_id)
    with ReadLock(old_handle) as r_lock:
      copyobj = ObjectID(capi.DataEngine().CloneObject(r_lock.lock, 0))
      if not copyobj:
        last_error = capi.DataEngine().ErrorMessage().decode(
          "utf-8")
        self.log.error('Failed to clone object %s because %s',
                       object_to_clone, last_error)

    self.log.debug("Deep copy %s to %s",
                   old_handle,
                   new_path if new_path is not None else "[Backend Object]")
    if new_path is not None:
      return self.add_object(new_path, copyobj, overwrite=overwrite)
    return copyobj

  def rename_object(
      self,
      object_to_rename: DataObject | ObjectID[DataObject] | str,
      new_name: str,
      overwrite: bool=False,
      allow_standard_containers: bool=False) -> bool:
    """Rename (and/or move) an object.

    Renaming an object to its own name has no effect.

    Parameters
    ----------
    object_to_rename
      The object to rename or
      the ID of the object to rename or
      full path to object in the Project.
    new_name
      new name for object.
      Standalone name (e.g. 'new tri') will keep root path.
      Full path (e.g. 'surfaces/new tri') will change location.
      Prefix with '/' (e.g. '/new tri' to move to the root
      container).
    overwrite
      If False (default) then if there is already an object at new_name
      then a ValueError is raised.
      If True and if there is already an object at new_name then
      the object at new_name is overwritten. The overwritten object is
      orphaned rather than deleted and may still be accessible via
      its ID.
    allow_standard_containers
      If False (default) then attempting to rename a standard container
      will create a new container and move everything in the standard
      container into the new container.
      If True (not recommended) standard containers can be renamed.

    Returns
    -------
    bool
      True if rename/move successful,
      False if failed (overwrite checks failed).

    Raises
    ------
    ValueError
      New object name begins with full stop when project
      attribute allow_hidden_objects is False (default).
    ValueError
      New object name can't be '.'.
    ValueError
      If there is already an object at new_name and overwrite=False.
    ObjectDoesNotExistError
      Attempting to rename an object that doesn't exist.
    DeleteRootError
      Attempting to rename root container.

    Notes
    -----
    new_name can not start with a full stop '.' when allow_hidden_objects is
    False and cannot be '/' or '' or '.'.

    """
    object_to_rename = ObjectID(self.__get_obj_handle(object_to_rename))

    # Safety checks:
    if not object_to_rename:
      error_message = "Unable to locate object for renaming"
      self.log.error(error_message)
      raise ObjectDoesNotExistError(error_message)

    if object_to_rename == self.root_id:
      error_message = "Can't rename root container"
      self.log.error(error_message)
      raise DeleteRootError(error_message)

    # Special handling for standard containers.
    # Rename creates a new visual container and moves the standard container's
    # contents into the copy.
    # If allow_standard_containers, this is bypassed.
    if object_to_rename.is_a(StandardContainer) \
        and not allow_standard_containers:

      with self.edit(object_to_rename) as standard_container:
        with self.new(new_name, VisualContainer,
                      overwrite=overwrite) as new_container:

          for child in standard_container.items():
            new_container.append(child)

        standard_container.clear()

      return True

    # Shift/rename object or container:
    old_parent = object_to_rename.parent
    if old_parent:
      old_parent_path = old_parent.path
    else:
      old_parent_path = ''  # The object is not in a container.

    new_parent_path, new_obj_name = self._valid_path(new_name)
    new_parent_is_root = new_parent_path == '' and new_name.startswith('/')

    if not new_parent_path and not new_parent_is_root:
      new_parent_path = old_parent_path

    old_path = object_to_rename.path.strip('/')
    new_path = (new_parent_path + "/" + new_obj_name).strip('/')

    if old_parent and old_path:
      # If the object is in a container then we check to ensure its in a path
      # that should be manipulated (accounting for if it is within a hidden
      # container).
      self._valid_path(old_path)

    self.add_object(
      new_path,
      object_to_rename, overwrite=overwrite)

    # If the object didn't have a parent, then it wasn't in a container so there
    # is no need to remove it from a container.
    # Additionally, if the new path and the old path are the same, then it
    # is in the same container, so don't remove it.
    if old_parent and old_path != new_path:
      try:
        self.__remove_from_container(object_to_rename, old_parent)
      except OSError:
        self.log.exception("Error while removing object %r from container %r",
                           old_parent, object_to_rename)

    return True

  def delete_container_contents(
      self,
      container: DataObject | ObjectID[DataObject] | str):
    """Deletes all the contents of a container.

    Any child objects that are not in another container will be deleted.

    Parameters
    ----------
    container
      the object to delete or
      the ID for the object to delete or
      path to container (e.g. '/surfaces/old').

    Raises
    ------
    ObjectDoesNotExistError
      If container is not an existent object.
    """
    self.log.info("Delete container contents: %s", container)
    with self.edit(container) as editable_container:
      editable_container.allow_hidden_objects = self.allow_hidden_objects
      editable_container.clear()

  def new_visual_container(
      self, parent_container: str, container_name: str
      ) -> ObjectID[VisualContainer]:
    """Creates a new visual container.

    Parameters
    ----------
    parent_container
      The path to the parent container or the parent container.
    container_name
      New container name.

    Returns
    -------
    ObjectID
      The object ID for newly created container.

    Raises
    ------
    ValueError
      When attempting to create a container name or part of path
      that would result in hidden objects (i.e. starts with '.')
      and allow_hidden_objects is False.
    ValueError
      If the container name contains "/" characters.
    ValueError
      If there is already an object called container_name in parent_container.
    InvalidParentError
      If object_path contains an object that can't be a parent of the new
      object.

    Examples
    --------
    To add a visual container to the root container, use "/" as the parent
    container name. The following example creates a container called
    "example_container" in the root container.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> project.new_visual_container("/", "example_container")

    To add a visual container to another container, use the path to
    that container as the container name. The following example
    creates a container called "sub_container" in the "example_container"
    created in the previous example.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> project.new_visual_container("example_container", "sub_container")

    This is the full path to that container if that container is in another
    container. The following example creates a container called
    "sub_sub_container" inside the "sub_container" created in the
    previous example. In particular, note that the path to "sub_container"
    includes a "/" because it is inside of another container.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> project.new_visual_container(
    ...     "example_container/sub_container",
    ...     "sub_sub_container"
    ... )
    """
    if parent_container not in ["", "/"]:
      parent_container = "/".join(self._valid_path(parent_container))
    elif parent_container == "/":
      # Always refer to the root container as a blank parent name.
      # Referring to it as a slash results in two slashes at the start
      # of the path, which is invalid.
      parent_container = ""
    self._check_path_component_validity(container_name)

    new_container = ObjectID(capi.Modelling().NewVisualContainer())

    # add_object() will create the container hierarchy up to and including
    # parent_container.
    self.add_object(f"{parent_container}/{container_name}", new_container)
    self.log.info("Created new container: [%s] under [%s]",
                  container_name,
                  parent_container)
    return new_container

  def __remove_from_container(
      self,
      object_to_remove: ObjectID[DataObject],
      container: ObjectID[Container]) -> None:
    """Removes an object from a container but doesn't delete it.

    Parameters
    ----------
    object_to_remove
      The ID of the object to remove.
    container
      The ID of the container to remove the object from.

    """
    if self.log.isEnabledFor(logging.DEBUG):
      self.log.info("Remove object %r (%s) from parent container %r (%s).",
                    object_to_remove, object_to_remove.path, container,
                    container.path)
    else:
      self.log.info("Remove object %r from parent container %r.",
                    object_to_remove, container)

    with WriteLock(container.handle) as w_lock:
      return capi.DataEngine().ContainerRemoveObject(
        w_lock.lock, object_to_remove.handle, False)

  def delete(
      self,
      mdf_object_or_name: str | DataObject | ObjectID[DataObject],
      allow_standard_containers: bool=False) -> bool:
    """Deletes the given object.

    Parameters
    ----------
    mdf_object_or_name
      Container name, instance of object as DataObject or
      ObjectID of the object.

    allow_standard_containers
      If False (default) then attempting to delete a standard
      container will result in the container contents being deleted.
      If True then standard containers will be deleted. See warnings
      for why you shouldn't do this.

    Returns
    -------
    bool
      True if deleted successfully or False if not.

    Raises
    ------
    DeleteRootError
      If the object provided is the root container.

    RuntimeError
      If the the object can't be deleted. The most common cause is something
      is writing to the object at this time.

    Warnings
    --------
    Deleting a standard container created by a Maptek application
    may cause the application to crash. The allow_standard_containers
    flag should only be used to delete standard containers you have created
    yourself (It is not recommended to create your own standard containers).

    """
    self.log.info("Delete object: %s", mdf_object_or_name)
    try:
      if isinstance(mdf_object_or_name, str):
        object_id = self.find_object(mdf_object_or_name)
        self._delete(object_id, allow_standard_containers)
      else:
        self._delete(mdf_object_or_name, allow_standard_containers)
      return True
    except RuntimeError as error:
      self.log.error("Error deleting object: %s [%s]",
                     mdf_object_or_name, error)
      raise

  def _delete(
      self,
      mdf_object: DataObject | ObjectID[DataObject],
      allow_standard_containers: bool) -> None:
    """Internal delete - by object (not string).

    Parameters
    ----------
    mdf_object
      The object to delete.
    allow_standard_containers
      If False (default) then attempting to delete a standard
      container will result in the container contents being deleted.
      If True then standard containers will be deleted.

    Raises
    ------
    DeleteRootError
      If the object provided is the root container.
    RuntimeError
      If the the object can't be deleted. The most common cause is something
      is writing to the object at this time.
    """
    object_id = ObjectID(self.__get_obj_handle(mdf_object))
    if object_id == self.root_id:
      raise DeleteRootError("You cannot delete the root container.")
    if mdf_object is None:
      return

    # Special handling for standard containers.
    # Deleting a standard container deletes its contents
    # and leaves the container untouched.
    # If allow_standard_containers, this is bypassed.
    if object_id.is_a(StandardContainer) and not allow_standard_containers:
      self.delete_container_contents(mdf_object)
      return

    # Special handling for the recycle bin. Only delete its contents.
    if object_id and object_id == self.recycle_bin_id:
      self.delete_container_contents(object_id)
      return

    mdf_object = self.__get_obj_handle(mdf_object)
    success = capi.DataEngine().DeleteObject(mdf_object)
    if not success:
      error = capi.DataEngine().ErrorMessage().decode("utf-8")
      raise RuntimeError(error)

  def _type_for_object(
      self,
      object_handle: DataObject | ObjectID[DataObject]) -> type:
    """Return the type of an object based on the object ID without needing
    to read the object.

    Parameters
    ----------
    object_handle
      The object to query the type for.

    Returns
    --------
    type
      The DataObject type e.g. Surface, Marker as type only.

    Raises
    ------
    TypeError
      If the object handle is of a type that isn't known or supported.
    ObjectDoesNotExistError
      If object_handle does not refer to a valid object.

    """
    object_handle = self.__get_obj_handle(object_handle)
    if object_handle is None:
      error_message = "Unable to locate object"
      self.log.error(error_message)
      raise ObjectDoesNotExistError(error_message)

    object_type = capi.DataEngine().ObjectDynamicType(object_handle)

    # The types for data list is sorted such that iterating over it
    # will check derived types before base types.
    for _, class_type in self.__types_for_data:
      type_index = class_type.static_type()
      if capi.DataEngine().TypeIsA(object_type, type_index):
        return class_type

    # This doesn't use an is_a() because we want to handle the case where a
    # plain container was created. Typically a Container is a base-class
    # of higher level types and treating them as such wouldn't be ideal.
    if object_type.value == Container.static_type().value:
      return Container

    raise TypeError('Unsupported object type')

  def get_selected(self) -> Selection:
    """Return the IDs of the selected objects.

    When connected to an existing application, these are the objects selected
    in that application (via the explorer, view or some other method).

    Returns
    -------
    Selection
      A list of selected ObjectIDs.

    """
    # Query how many objects are selected.
    count = capi.DataEngine().GetSelectedObjectCount()
    # Allocate to receive the selected objects.
    object_array = (T_ObjectHandle * count)()
    # Populate the array and build up a list of object IDs.
    capi.DataEngine().GetSelectedObjects(object_array)
    selected_objects = [ObjectID(buff) for buff in object_array]
    return Selection(selected_objects)

  def set_selected(
      self,
      object_ids_or_paths:
        Selection |
        list[str] |
        list[ObjectID[DataObject]] |
        str |
        ObjectID[DataObject]=None,
      include_descendants: bool=True) -> None:
    """Set active project selection to one or more objects.
    If None specified, selection will be cleared.
    If objects are provided but are not valid, they will not be selected.
    No action will be taken if entire selection specified is invalid.
    Any VisualContainer objects specified will include their descendants.

    Parameters
    ----------
    mdf_objects_or_paths
      List of object paths to select, List of ObjectID to select,
      path to object to select, ObjectID of object to select.
      Pass None or an empty list to clear the existing selection.
    include_descendants
      whether to also select descendants of any VisualContainer provided
      within the selection criteria (default=True).

    Raises
    -------
    ValueError
      If any or all objects within the selection specified is invalid.

    """
    if not object_ids_or_paths:
      # Clear selection
      self.log.info("Clearing active object selection")
      capi.DataEngine().SetSelectedObjects(None, 0)
    else:
      # List of selected visual containers.
      containers = []
      # Handles of the selected objects.
      selected_handles = []
      if not isinstance(object_ids_or_paths, Iterable) or \
          isinstance(object_ids_or_paths, str):
        object_ids_or_paths = [object_ids_or_paths]

      # Ensure all objects provided are valid and exist
      for obj in object_ids_or_paths:
        handle = self.__get_obj_handle(obj)
        if handle and capi.DataEngine().ObjectHandleExists(handle):
          oid = ObjectID(handle)
          if oid.is_a(VisualContainer):
            containers.append(oid)
          selected_handles.append(handle)
        else:
          error_msg = ("An invalid object ({}) was specified for "
                       + "selection.\nVerify objects specified in the "
                       + "selection are valid and still exist.").format(obj)
          self.log.error(error_msg)
          raise ValueError(error_msg)

      if include_descendants:
        # Include handles of descendant objects for any VisualContainer objects
        # specified and their children.
        descendants = []
        for obj in containers:
          descendants.extend(self.get_descendants(obj).ids())
        if descendants:
          self.log.info("Adding %d descendant objects to selection",
                        len(descendants))
          selected_handles.extend(child.handle for child in descendants)

      object_count = len(selected_handles)
      self.log.info("Set selection with %d objects", object_count)
      object_array = (T_ObjectHandle * object_count)(*selected_handles)
      capi.DataEngine().SetSelectedObjects(object_array, object_count)

  @property
  def recycle_bin_id(self) -> ObjectID:
    """The object ID of the recycle bin.

    Returns
    -------
    ObjectID
      The ID of the recycle bin object.

    Raises
    ------
    NoRecycleBinError
      The project has no recycle bin.

    See Also
    --------
    recycle: Move an object to the recycle bin.
    """
    if capi.DataEngine().version >= (1, 8):
      recycle_bin = ObjectID(capi.DataEngine().RecycleBin(self.backend_index))
    else:
      # For older versions of the applications that don't have the C API
      # function, use an alternative.
      recycle_bin = self.__find_from(
        self.root_id, ['.system', 'Recycle Bin'], create_if_not_found=False)

    if not recycle_bin:
      raise NoRecycleBinError()

    return recycle_bin

  def recycle(self, object_to_recycle: DataObject | ObjectID[DataObject]):
    """Move the given object to the recycle bin.

    This does not provide the ability to recycle a standard container because
    the user will be unable to move the item out of the recycle bin.

    Raises
    ------
    NoRecycleBinError
      The project has no recycle bin.
    """
    object_to_recycle = ObjectID(self.__get_obj_handle(object_to_recycle))
    object_to_recycle_name = object_to_recycle.name

    # This does not honour the user operations that can be set either per-type
    # or per-object, which would otherwise prevent the user from moving the
    # object to the recycle bin (known as deleting it in the software).

    if object_to_recycle.is_a(StandardContainer):
      # Collect up the children and remove them from the container.
      children_to_recycle = self.get_children(object_to_recycle).ids()
      for child in children_to_recycle:
        self.recycle(child)

      return

    recycle_bin = self.recycle_bin_id

    # Remove the object from its parents.
    parent = object_to_recycle.parent
    while parent:
      with WriteLock(self.__get_obj_handle(parent)) as w_lock:
        capi.DataEngine().ContainerRemoveObject(
          w_lock.lock, object_to_recycle.handle, True)
      parent = object_to_recycle.parent

    # Add the object to the recycle bin.
    with WriteLock(self.__get_obj_handle(recycle_bin)) as w_lock:
      # Compute a new name that is suitable for it to have in the recycle bin,
      # as names must be unique within a given container.
      name_in_recycle_bin = object_to_recycle_name
      suffix = 2
      while capi.DataEngine().ContainerFind(
          w_lock.lock,
          name_in_recycle_bin.encode('utf-8')):

        name_in_recycle_bin = f'{object_to_recycle_name} {suffix}'
        suffix += 1

      capi.DataEngine().ContainerAppend(
        w_lock.lock,
        name_in_recycle_bin.encode('utf-8'),
        self.__get_obj_handle(object_to_recycle),
        False)

  def is_recycled(self, mdf_object: DataObject | ObjectID[DataObject]) -> bool:
    """Check if an object is in the recycle bin.

    Parameters
    ----------
    mdf_object
      Object to check.

    Returns
    -------
    bool
      True if the object is in the recycle bin (deleted)
      and False if it is not.

    """
    mdf_object = self.__get_obj_handle(mdf_object)
    return capi.DataEngine().ObjectHandleIsInRecycleBin(mdf_object)

  def type_name(self, path_or_id: str | ObjectID[DataObject]) -> str:
    """Return the type name of an object.

    This name is for diagnostics purposes only. Do not use it to alter the
    behaviour of your code. If you wish to check if an object is of a given
    type, use ObjectID.is_a() instead.

    Parameters
    ----------
    path_or_id
      The path or the ID of the object to query its type's name.

    Returns
    -------
    str
      The name of the type of the given object.

    See Also
    --------
    mapteksdk.data.objectid.ObjectID.is_a : Check if the type of an object is
      the expected type.
    """
    mdf_object = self.__get_obj_handle(path_or_id)
    dynamic_type = capi.DataEngine().ObjectDynamicType(mdf_object)
    raw_type_name: str = capi.DataEngine().TypeName(dynamic_type).decode('utf-8')

    # Tidy up certain names for users of the Python SDK.
    raw_to_friendly_name = {
      '3DContainer': 'VisualContainer',
      '3DEdgeChain': 'Polyline',
      '3DEdgeNetwork': 'EdgeNetwork',
      '3DNonBrowseableContainer': 'NonBrowseableContainer',
      '3DPointSet': 'PointSet',
      'BlockNetworkDenseRegular': 'DenseBlockModel',
      'BlockNetworkDenseSubblocked': 'SubblockedBlockModel',
      'EdgeLoop': 'Polygon',
      'RangeImage': 'Scan',
      'StandardContainer': 'StandardContainer',
      'TangentPlane': 'Discontinuity',
    }

    # Exclude the old (and obsolete) revision number.
    raw_type_name = raw_type_name.partition('_r')[0]

    return raw_to_friendly_name.get(raw_type_name, raw_type_name)

  def _check_path_component_validity(self, path: str):
    """Raises an appropriate error if the path component is invalid.

    Parameters
    ----------
    path
      The path to check for validity.

    Raises
    ------
    ValueError
      path is empty or only whitespace.
    ValueError
      Backslash character is in the path.
    ValueError
      path starts with "." and hidden objects are disabled.
    ValueError
      If path starts or ends with whitespace.
    ValueError
      If path contains newline characters.
    ValueError
      If path contains a "/" character.

    """
    if path == "" or path.isspace():
      raise ValueError("Object name cannot be blank.")

    if path[0].isspace() or path[-1].isspace():
      raise ValueError("Names cannot start or end with whitespace.")

    if "\\" in path:
      raise ValueError("Paths cannot contain \\ characters.")

    if "\n" in path:
      raise ValueError("Paths cannot contain newline characters.")

    if "/" in path:
      raise ValueError("Names cannot contain / characters.")

    if not self.allow_hidden_objects and path.startswith("."):
      raise ValueError(
        "Names cannot start with '.' if hidden objects are disabled.")

  def _valid_path(self, full_path: str) -> tuple[str, str]:
    """Returns a tuple consisting of the container name and the object
    name for the passed full_path with any leading/trailing "/" or
    whitespace removed.

    Parameters
    ----------
    full_path
      Full path to the object. This includes all parent containers, along
      with an optional leading and trailing "/" character.

    Returns
    -------
    tuple
      Tuple containing two elements. The first is the container name and
      the second is the object name. This has leading and trailing "/"
      characters and whitespace removed.

    Raises
    ------
    ValueError
      If any path component is invalid, as specified by
      _check_path_component_validity.

    Notes
    -----
    The returned container name can be nested. For example, if full_path =
    "cad/lines/line1" then the return value would be:
    ("cad/lines", "line1")

    """
    full_path = full_path.strip()
    if full_path.startswith("/"):
      full_path = full_path[1:]

    if full_path.endswith("/"):
      full_path = full_path[:-1]
    full_path = full_path.split("/")

    for path in full_path:
      self._check_path_component_validity(path)

    if len(full_path) == 1:
      return ("", full_path[0])

    return ("/".join(full_path[:-1]), full_path[-1])

  @staticmethod
  def find_running_applications() -> list[ExistingMcpdInstance]:
    """Return a list of applications that are candidates to be connected to.

    No checking is performed on the application to determine if it is suitable
    to connect to. For example, if the product is too old to support the SDK.

    Once you select which application is suitable then pass the result as the
    existing_mcpd parameter of the Project class's constructor.

    The list is ordered based on the creation time of the mcpd process with the
    latest time appearing first in the list.

    Returns
    -------
    list of ExistingMcpdInstance
      The list of candidate applications (host) that are running.

    Examples
    --------
    Finds the running applications and chooses the oldest one.

    >>> from mapteksdk.project import Project
    >>> applications = Project.find_running_applications()
    >>> project = Project(existing_mcpd=applications[-1])

    """
    return find_mdf_hosts(logging.getLogger('mapteksdk.project'))
