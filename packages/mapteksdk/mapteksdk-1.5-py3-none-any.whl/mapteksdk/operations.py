"""General operations which work with multiple applications."""
###############################################################################
#
# (C) Copyright 2021, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from __future__ import annotations
import csv
import ctypes
import enum
import logging
import typing

import numpy

from mapteksdk.internal.qualifiers import (
  QualifierSet, Qualifiers, InstanceTypes)
from mapteksdk.internal.transaction import (request_transaction,
                                            RequestTransactionWithInputs,
                                            TransactionRequest)
from mapteksdk.internal.serialisation import Icon
from mapteksdk.internal.util import default_type_error_message
from mapteksdk.internal.transaction_manager import (
  TransactionManager, TransactionCancelledError, TransactionFailedError)
from mapteksdk.internal.transaction_data import (
  StringTransactionData, DoubleTransactionData, BooleanTransactionData)
from mapteksdk.view import ViewController
from mapteksdk.capi import Mcpd
from mapteksdk.data import DataObject, ObjectID
from mapteksdk.workflows import WorkflowSelection

if typing.TYPE_CHECKING:
  from mapteksdk.internal.transaction_data import TransactionData

  TransactionDataT = typing.TypeVar("TransactionDataT", bound=TransactionData)

  ObjectT = typing.TypeVar('ObjectT', bound=DataObject)
  """Type hint used for arguments which are subclasses of DataObject."""

LOGGER = logging.getLogger("mapteksdk.operations")


class TooOldForOperation(Exception):
  """Error raised when the application is too old to support an operation.

  Parameters
  ----------
  minimum_version
    Minimum version required to support the operation. This is of the form
    (major, minor).
  current_version
    Current version required to support the operation. This is of the form
    (major, minor).

  Notes
  -----
  This does not check that current_version is older than new_version.
  """

  def __init__(
      self, minimum_version: tuple[int, int], current_version: tuple[int, int]):
    Exception.__init__(
      self,
      f'Application is too old ({current_version}) to support this operation.'
      f' Requires newer version ({minimum_version}).')
    self.minimum_version = minimum_version
    self.current_version = current_version


class PickFailedError(ValueError):
  """Error raised when a pick operation fails.

  This is also raised when a pick operation is cancelled.

  Parameters
  ----------
  pick_type
    The SelectablePrimitiveType for the pick which failed, or a string
    representing the type of the pick operation.

  Notes
  -----
  This inherits from ValueError instead of OperationCancelledError
  because it predates OperationCancelledError. Scripts should always
  catch this error as a PickFailedError. It may be changed to inherit
  from OperationCancelledError in a future version of the SDK.
  """
  def __init__(self, pick_type: SelectablePrimitiveType | str):
    super().__init__(f"{pick_type} pick operation was cancelled or failed.")
    self.pick_type = pick_type


class OperationCancelledError(Exception):
  """Error raised when an operation is cancelled.

  This indicates the user closed the panel associated with the operation
  or pressed "Cancel".
  """


class OperationFailedError(Exception):
  """Error raised when an operation fails.

  This error typically shouldn't be caught. It typically indicates the
  application is incompatible with the current version of the SDK.
  """


class SelectablePrimitiveType(enum.Enum):
  """Enum representing the selectable primitive types.

  Warning
  -------
  Block selections are impossible in PointStudio even when block objects
  are loaded into the view.

  """
  POINT = 1
  EDGE = 2
  FACET = 3
  # TETRA = 4
  CELL = 5
  BLOCK = 6


class Severity(enum.Enum):
  """Enum of severity of messages."""
  INFORMATION = 0
  """The message is an information message.

  The message will display with a blue circle with a white "i" icon.
  This severity indicates that though the message is important, but it
  is less severe than an error or a warning.
  """
  WARNING = 1
  """The message is a warning.

  The message will be displayed with an orange exclamation mark icon.
  This severity indicates that the message is a warning - something
  potentially bad has happened or is about to happen, but not something bad
  enough that the script will stop.
  """
  ERROR = 2
  """The message is an error.

  The message will display with a red cross icon and the Workbench
  will play a warning sound. This severity indicates that something
  bad has happened, or is about to happen, and the script cannot
  continue.
  """


class Primitive:
  """Class which can uniquely identify a selected primitive.

  Includes the object the primitive exists in, the type of the primitive
  and the index of that primitive in the object.

  Parameters
  ----------
  path
    The path to the object containing the primitive.
  primitive_type
    The type of primitive selected.
  index
    Index of the selected primitive in the object.

  """
  def __init__(
      self, path: str, primitive_type: SelectablePrimitiveType, index: int):
    if not isinstance(primitive_type, SelectablePrimitiveType):
      raise TypeError(default_type_error_message(
        argument_name="primitive_type",
        actual_value=primitive_type,
        required_type=SelectablePrimitiveType
      ))

    self.__path = path
    self.__primitive_type = primitive_type
    self.__index = index

  def __str__(self):
    return (f"Object: '{self.__path}' {self.__primitive_type.name} at "
            f"index: {self.__index}")

  @property
  def path(self) -> str:
    """Path to the object containing the selected primitive."""
    return self.__path

  @property
  def primitive_type(self) -> SelectablePrimitiveType:
    """The type of primitive which was selected."""
    return self.__primitive_type

  @property
  def index(self) -> int:
    """The index of the selected primitive in the primitive array."""
    return self.__index


def open_new_view(
    objects: list[ObjectID[DataObject]]=None, wait: bool=True
    ) -> ViewController:
  """Open a new view window in the current application.

  This is only suitable for use by the Python SDK When connecting to an
  existing Maptek application.

  Using the Python SDK to develop an application which creates an Maptek
  Viewer within it requires special handling to set-up that isn't provided
  by this function.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  objects
    The list of objects to include in the new view.
  wait
    If True then the function waits until the view has been opened and
    is considered complete before returning and will return the ObjectID of
    the newly created view. Otherwise it won't wait and it will return
    immediately with no result.

  Returns
  -------
  ViewController
    The view controller for the newly created view if wait is True.
  None
    If wait is False.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.
  """
  if Mcpd().version < (1, 2):
    raise TooOldForOperation((1, 2), Mcpd().version)

  if objects is None:
    objects = []

  if objects:
    requester_icon = 'ViewSelection'
    inputs = [
      ('selection', RequestTransactionWithInputs.format_selection(objects)),
    ]
  else:
    requester_icon = 'ViewNew'
    inputs = []

  outputs = request_transaction(
    server='uiServer',
    transaction='mdf::uiS_NewViewTransaction',
    command_name='Maptek.Core.Window.Commands.New View',
    inputs=inputs,
    requester_icon=Icon(requester_icon),
    wait=wait,
  )

  if wait:
    for output in outputs.value:
      if output['idPath'] == 'viewId':
        value = output.get('value', '')
        if value:
          return ViewController(WorkflowSelection(value).ids[0])

  return None


def opened_views() -> list[ViewController]:
  """Return the list of opened views in the current application.

  This does not include embedded views in panels.

  This is only suitable for use by the Python SDK when connecting to an
  existing Maptek application.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Returns
  -------
  list
    A list containing the ViewController for each of the opened views.
    If there are no opened views this list will be empty.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.

  Example
  -------
  Print out the list of active views.

  >>> from mapteksdk.project import Project
  >>> import mapteksdk.operations as operations
  >>> project = Project()
  >>> print('Open views:')
  >>> for view in operations.opened_views():
  >>>     print(view.server_name, view.window_title)
  """

  if Mcpd().version < (1, 2):
    raise TooOldForOperation((1, 2), Mcpd().version)

  outputs = request_transaction(
    server='uiServer',
    transaction='mdf::uiS_ListViewsTransaction',
    command_name='Maptek.Core.Window.Commands.List Views',
    inputs=[],
    requester_icon=Icon('ListViews'),
  )

  selection = _decode_selection(outputs).ids
  return [ViewController(view_id) for view_id in selection]


def active_view() -> ViewController | None:
  """Return the active view of the current application otherwise None if there
  is no active view

  This is only suitable for use by the Python SDK when connecting to an
  existing Maptek application.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Returns
  -------
  ViewController
    The view controller for the active view
  None
    If there was no active view.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.

  Example
  -------
  Query the active view

  >>> from mapteksdk.project import Project
  >>> import mapteksdk.operations as operations
  >>> project = Project()
  >>> view = operations.active_view()
  >>> if view:
  >>>    print(f"The active view is: {view}")
  >>> else:
  >>>     print("There is no active view.")
  """

  if Mcpd().version < (1, 2):
    raise TooOldForOperation((1, 2), Mcpd().version)

  outputs = request_transaction(
    server='uiServer',
    transaction='mdf::uiS_ListViewsTransaction',
    command_name='Maptek.Core.Window.Commands.List Views',
    inputs=[],
    requester_icon=Icon('ActiveView'),
  )

  for output in outputs.value:
    if output['idPath'] == 'viewId':
      value = output.get('value', 'OID(I0, C0, T0)')
      if value == 'OID(I0, C0, T0)':
        return None
      return ViewController(WorkflowSelection(value).ids[0])

  # There was no active view.
  return None


def active_view_or_new_view() -> ViewController | None:
  """Return the active view of the current application or opens a new view if
  there is none.

  This is only suitable for use by the Python SDK when connecting to an
  existing Maptek application.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Returns
  -------
  ViewController
    The view controller for the active view or new view.
  None
    If it was unable to determine the active view or create a new view.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.

  Example
  -------
  Query the active view or create a new view if there is no active view.

  >>> from mapteksdk.project import Project
  >>> import mapteksdk.operations as operations
  >>> project = Project()
  >>> view = operations.active_view_or_new_view()
  """

  if Mcpd().version < (1, 2):
    raise TooOldForOperation((1, 2), Mcpd().version)

  outputs = request_transaction(
    server='uiServer',
    transaction='mdf::uiS_GetActiveOrNewViewTransaction',
    command_name='Maptek.Core.Window.Commands.Get Active/New View',
    inputs=[],
    requester_icon=Icon('ActiveView'),
  )

  for output in outputs.value:
    if output['idPath'] == 'viewId':
      view = WorkflowSelection(output.get('value', '')).ids[0]
      return ViewController(view)

  # Unable to find the active view or create a new view.
  return None


def coordinate_pick(*,
    label: str="",
    support_label: str="",
    help_text: str="") -> numpy.ndarray:
  """Requests for the user to select a coordinate in the software.

  This will wait for the user to select a coordinate and then returns the
  point.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  label
    The label to show for the coordinate pick. This is shown in the status
    bar to the left of the X, Y and Z coordinates of the selected point.
    Default is "Select a coordinate". The default may be translated to the
    user's selected language within the application.
  support_label
    The support label to display in a yellow box at the top of the view.
    Default is "Select a coordinate". The default may be translated to the
    user's selected language within the application.
    If label is specified and this is not, this will default to label.
  help_text
    Text to display when the mouse hovers over the status bar during the
    coordinate pick option.
    Default is: "Select a coordinate for the running Python Script".
    The default may be translated to the user's selected language within the
    application.

  Returns
  -------
  ndarray
    A ndarray with shape (3,) representing the selected coordinate.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.
  PickFailedError
    If the pick operation is cancelled or fails.

  Notes
  -----
  A coordinate pick allows the user to pick any coordinate and thus the
  coordinate may not be a part of any object. If the selected coordinate
  must be a coordinate on an object, use primitive pick instead.

  Examples
  --------
  Request for the user to select two points in the running application and
  then calculates the distance between those two points. The selected points
  and the distance is displayed in the report window. When picking the first
  point, the message in the bottom corner of the screen will be:
  "Pick the first point". For the second point it will be:
  "Pick the second point".

  >>> import numpy as np
  >>> from mapteksdk.operations import (coordinate_pick, write_report)
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> start = coordinate_pick(label="Pick the first point.")
  >>> end = coordinate_pick(label="Pick the second point.")
  >>> difference = start - end
  >>> distance = np.linalg.norm(difference)
  >>> write_report(f"Distance between points",
  ...              f"The distance between {start} and {end} is {distance}")

  """
  if Mcpd().version < (1, 3):
    raise TooOldForOperation((1, 3), Mcpd().version)

  if label != "" and support_label == "":
    support_label = label

  inputs = [("source", "Python Script"), ("label", label),
            ("supportLabel", support_label), ("help", help_text),]

  print("Select a point in the running application.")
  outputs = request_transaction(
    server="cadServer",
    transaction="mtp::cadS_CoordinatePickWithLabelsTransaction",
    command_name="",
    inputs=inputs,
    wait=True,
    confirm_immediately=True)

  for output in outputs.value:
    if output["idPath"] == "coordinate":
      try:
        result = output.get("value")
      except KeyError as error:
        raise PickFailedError("Coordinate") from error

      try:
        return numpy.array(result.strip("()").split(","),
                           dtype=ctypes.c_double)
      except ValueError as error:
        raise PickFailedError("Coordinate") from error
  raise PickFailedError("Coordinate")

def object_pick(*,
    object_types: type[ObjectT] | tuple[type[ObjectT], ...] | None=None,
    label: str="",
    support_label: str="",
    help_text: str="") -> ObjectID[ObjectT | DataObject]:
  """Requests for the user to select an object in the software.

  This will wait for the user to select an object and then returns it.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  object_type
    DataObject subclass or a tuple of DataObject subclasses to restrict the
    object pick to. Only objects of the specified types will be accepted as
    valid picks by the operation.
  label
    The label to show for the object pick. This is shown in the status
    bar.
    Default is "Select a object". The default may be translated to the user's
    selected language within the application.
  support_label
    The support label to display in a yellow box at the top of the view.
    Default is "Select a object". The default may be translated to the user's
    selected language within the application.
    If label is specified and this is not, this will default to label.
  help_text
    Text to display when the mouse hovers over the status bar during the
    object pick option.
    Default is: "Select a object for the running Python Script".
    The default may be translated to the user's selected language within the
    application.

  Returns
  -------
  ObjectID
    Object ID of the selected object. This may be a null object id.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.
  PickFailedError
    If the pick operation is cancelled or fails.
  TypeError
    If object_types contains an object which is not a DataObject subclass.

  Examples
  --------
  Ask for the user to select an object in the running application. A
  report is added to the report window containing the type of the
  selected object.

  >>> from mapteksdk.operations import object_pick, write_report
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> oid = object_pick(label="Query object type",
  ...                   support_label="Select an object to query its type")
  >>> write_report("Query type", f"{oid.path} is a {oid.type_name}")

  Specifying the object type allows for restricting the operation to
  specific types. For example, setting the object type to Surface will
  cause the pick to only accept surfaces, as shown in the following
  script:

  >>> from mapteksdk.data import Surface
  >>> from mapteksdk.operations import object_pick
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> oid = object_pick(object_types=Surface
  ...                   label="Pick a surface")
  >>> with Project.edit(oid) as surface:
  ...   # The surface variable is guaranteed to be a Surface.
  ...   pass

  Alternatively, a tuple of types can be passed to specify a group of types
  to restrict the pick to. For example, the following script restricts the
  pick to Polygon and Polyline:

  >>> from mapteksdk.data import Polyline, Polygon
  >>> from mapteksdk.operations import object_pick
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> oid = object_pick(object_types=(Polyline, Polygon)
  ...                   label="Pick a polyline or polygon")
  >>> with Project.edit(oid) as line:
  ...   # The line variable is guaranteed to be a Polyline or Polygon.
  ...   pass
  """
  if Mcpd().version < (1, 3):
    raise TooOldForOperation((1, 3), Mcpd().version)

  if label != "" and support_label == "":
    support_label = label

  inputs = [
    ("source", "Python Script"),
    ("label", label),
    ("supportLabel", support_label),
    ("help", help_text),
  ]

  if object_types is not None:
    if not isinstance(object_types, typing.Iterable):
      object_types = (object_types,)
    try:
      inputs.append(("objectTypeIds", ",".join([
        str(object_type.static_type().value) for object_type in object_types])))
    except AttributeError as error:
      LOGGER.info(error)
      raise TypeError(
        "One of the object types is not a subclass of DataObject.\n"
        f"object_types: {object_types}"
      ) from None

  print("Select an object in the running application.")
  while True:
    outputs = request_transaction(
      server="cadServer",
      transaction="mtp::cadS_ObjectPickWithLabelsTransaction",
      command_name="",
      inputs=inputs,
      wait=True,
      confirm_immediately=True)

    for output in outputs.value:
      if output["idPath"] == "object":
        try:
          value = output.get("value")
          # Blank value indicates the pick operation was cancelled.
          if value == "":
            raise PickFailedError("Object")
          oid = ObjectID.from_path(value)
          # If no object types were specified, return the ObjectID.
          if not object_types:
            return oid
          # If object types were specified, only return the ObjectID
          # if the object is of the specified types.
          if oid.is_a(object_types):
            return oid
        except KeyError as error:
          raise PickFailedError("Object") from error


def primitive_pick(
    primitive_type: SelectablePrimitiveType=SelectablePrimitiveType.POINT,
    *,
    label: str="",
    support_label: str="",
    help_text: str="") -> Primitive:
  """Requests for the user to select a primitive of the specified type
  in the software.

  This will wait for the user to select a primitive and returns it.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  primitive_type
    The type of Primitive the user will be asked to select.
  label
    The label to show for the primitive pick. This is shown in the status
    bar.
    Default is "Select a primitive". The default may be translated to the user's
    selected language within the application.
  support_label
    The support label to display in a yellow box at the top of the view.
    Default is "Select a primitive". The default may be translated to the
    user's selected language within the application.
    If label is specified and this is not, this will default to label.
  help_text
    Text to display when the mouse hovers over the status bar during the
    primitive pick option.
    Default is: "Select a primitive for the running Python Script".
    The default may be translated to the user's selected language within the
    application.

  Returns
  -------
  Primitive
    Object representing the selected primitive.

  Raises
  ------
  TooOldForOperation
    If the application does not have the necessary support for this operation.
  PickFailedError
    If the pick operation is cancelled or fails.

  Examples
  --------
  Request for the user to pick a point and then displays a report
  containing the coordinate of the selected point.

  >>> from mapteksdk.operations import (primitive_pick,
  ...                                   SelectablePrimitiveType,
  ...                                   write_report)
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> primitive = primitive_pick(SelectablePrimitiveType.POINT)
  >>> with project.read(primitive.path) as read_object:
  ... write_report("Selected point", str(read_object.points[primitive.index]))

  Request for the user to pick an edge then displays a report containing the
  points the selected edge connects.

  >>> from mapteksdk.operations import (primitive_pick,
  ...                                   SelectablePrimitiveType,
  ...                                   write_report)
  >>> from mapteksdk.project import Project
  >>> project = Project()
  >>> primitive = primitive_pick(SelectablePrimitiveType.EDGE)
  >>> with project.read(primitive.path) as read_object:
  ...     edge = read_object.edges[primitive.index]
  ...     start = read_object.points[edge[0]]
  ...     end = read_object.points[edge[1]]
  ...     write_report("Selected Edge", f"{start} to {end}")

  """
  if Mcpd().version < (1, 3):
    raise TooOldForOperation((1, 3), Mcpd().version)

  if label != "" and support_label == "":
    support_label = label

  inputs = [("source", "Python Script"), ("label", label),
            ("supportLabel", support_label), ("help", help_text),
            ("primitiveType", str(primitive_type.value))]

  print(f"Select a {primitive_type.name} in the running application.")
  outputs = request_transaction(
    server="cadServer",
    transaction="mtp::cadS_PrimitivePickWithLabelsTransaction",
    command_name="",
    inputs=inputs,
    wait=True,
    confirm_immediately=True)

  for output in outputs.value:
    if output["idPath"] == "primitive":
      try:
        result = output.get("value")
      except KeyError as error:
        raise PickFailedError(primitive_type.name) from error

      try:
        # Format is: path,primitive_type_id,index.
        # Use csv reader to read as it will handle paths containing quoted
        # commas.
        result = list(csv.reader([result]))[0]
        type_id = SelectablePrimitiveType(int(result[1]))
        index = int(result[2])
        return Primitive(result[0], type_id, index)
      except IndexError as error:
        # This will occur if the pick is cancelled.
        raise PickFailedError(primitive_type.name) from error
  raise PickFailedError(primitive_type.name)


def write_report(label: str, message: str):
  """Write a report to the report window of the application.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  label
    The label to show on the report.
  message
    The message to include in the report. This is essentially the body of the
    report itself.

  Example
  -------
  Write out a simple report

  >>> from mapteksdk.project import Project
  >>> import mapteksdk.operations as operations
  >>> project = Project()
  >>> operations.write_report(
  ...     'My Script', 'Completed filtering in 1.5 seconds')
  """
  request = TransactionRequest()
  request.transaction = 'mdf::uiC_Report'
  request.qualifiers = QualifierSet()

  if Mcpd().version <= (1, 3):
    title_qualifier = Qualifiers.label(label)
  else:
    title_qualifier = Qualifiers.title(label)

  request.qualifiers.values = [
    title_qualifier,
    Qualifiers.message(message),
    ]
  request.send(destination='appServer')


def show_message(
    title: str, message: str, severity: Severity=Severity.INFORMATION):
  """Display a popup message box in the application.

  Note that message boxes can be disruptive to the user and should
  be used sparingly. Consider using write_report() or
  display_toast_notification() instead.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  title
    The title which will be displayed in the title bar of the message box.
    This should be no more than 255 characters long.
  message
    The message which will be displayed in the main area of the message box.
  severity
    The severity of the message. See the documentation on the enum for
    more information.

  Raises
  ------
  ValueError
    If title is longer than 255 characters.
  """
  __show_message(title, message, severity, toast=False)


def show_toast_notification(
    title: str, message: str, severity: Severity=Severity.INFORMATION):
  """Display a toast notification in the application.

  The toast notification will appear at the bottom of the application
  and fade away after a few seconds. This is useful for transient messages.
  If the message may need to be kept, use write_report() instead.

  Parameters
  ----------
  title
    The title which will be displayed at the top of the toast notification
    in bold text.
    This should be no more than 255 characters long.
  message
    The message which will be displayed in the main area of the toast
    notification.
  severity
    The severity of the message. See the documentation on the enum for
    more information.

  Raises
  ------
  ValueError
    If title is longer than 255 characters.

  """
  __show_message(title, message, severity, toast=True)


def __show_message(
    title: str, message: str, severity: Severity, toast: bool):
  """Show a message box or toast notification.

  Supported by PointStudio 2021.1, Vulcan GeologyCore 2021 and higher.

  Parameters
  ----------
  title
    The title which will be displayed in the title bar of the message box.
    This should be no more than 255 characters long.
  message
    The message which will be displayed in the main area of the message box.
  severity
    The severity of the message. See the documentation on the enum for
    more information.
  toast
    If false, this will display a message box. Otherwise it will display
    a toast notification.

  Raises
  ------
  ValueError
    If title is longer than 255 characters.
  """
  title_length = len(title)
  if title_length >= 255:
    raise ValueError("Title must not be more than 255 characters. "
                     f"Length: {title_length}")
  request = TransactionRequest()

  if severity is Severity.INFORMATION:
    transaction = "mdf::uiS_InformationMessage"
  elif severity is Severity.WARNING:
    transaction = "mdf::uiS_WarningMessage"
  elif severity is Severity.ERROR:
    transaction = "mdf::uiS_ErrorMessage"
  else:
    raise ValueError(f"Unrecognised severity: {severity}")

  request.transaction = transaction
  request.qualifiers = QualifierSet()

  if Mcpd().version <= (1, 3):
    title_qualifier = Qualifiers.label(title)
  else:
    title_qualifier = Qualifiers.title(title)

  qualifiers = [
    title_qualifier,
    Qualifiers.message(message),
    ]

  if toast:
    qualifiers.append(Qualifiers.toast())

  request.qualifiers.values = qualifiers
  request.send(destination='appServer')


def request_string(
    label: str,
    *,
    title: str="Python",
    initial_value: str | None=None,
    choices: typing.Iterable[str] | None=None) -> str:
  """Request a string.

  By default, this creates a window in the connected application into which
  the user can type. When they press "OK" in the application, whatever value
  the user typed in is returned by this function.

  If the choices parameter is specified, this instead creates
  a window in the connected application which contains a drop down box.
  When the user presses "OK" the selected item in the drop down box
  is returned.

  Parameters
  ----------
  label
    The label to display next to the text box.
  title
    The title of the window. This is "Python" by default.
  initial_value
    The initial value in the panel.
    If choices is not specified, this value will be in the text
    box when the panel is opened.
    If choices is specified, this must be one of the items in
    choices. This item will be selected in the drop down box when the
    panel opens.
    By default, this is the empty string or the first item in choices
    if it is specified.
  choices
    Iterable of possible choices. If this is specified, the user is
    required to choose one of these choice values. They will be presented
    in a drop down box.

  Returns
  -------
  str
    The string the user entered into the text box or selected
    in the drop down box.

  Raises
  ------
  ValueError
    If choices is specified and initial value is not in choices.
  OperationCancelledError
    If the user cancelled the operation.
  OperationFailedError
    If the operation failed to complete.
  """
  if Mcpd().version < (1, 8):
    raise TooOldForOperation(
      minimum_version=(1, 8),
      current_version=Mcpd().version
    )
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.label(label),
    Qualifiers.title(title),
    # The instance_type qualifier is used to find the factory for creating
    # the ui representation.
    Qualifiers.instance_type(InstanceTypes.IMPERATIVE),
  ]
  if choices:
    choice_list = [str(x) for x in choices]

    # The initial value must be specified if there are choice values.
    # Default it to the first item in choice values.
    if initial_value is None:
      initial_value = choice_list[0]
    if initial_value not in choice_list:
      raise ValueError(
        "Initial value must be one of the choice values."
      )
    qualifiers.values.append(
      Qualifiers.choice_values(choice_list))
  actual_value = StringTransactionData()
  actual_value.data = initial_value or ""
  return _request_transaction_and_wait_for_result(
    StringTransactionData,
    qualifiers,
    actual_value
  )


def request_float(label: str, *, initial_value: float=0.0) -> float:
  """Request a float.

  This creates a window in the connected application into which the user can
  type a number. When they press Okay, this function will return the number
  they typed in.

  Parameters
  ----------
  label
    The label to display next to the text box.
  initial_value
    The initial value to place in the text box. This is 0.0 by default.

  Returns
  -------
  float
    The float the user typed into the text box.

  Raises
  ------
  OperationCancelledError
    If the user cancelled the operation.
  OperationFailedError
    If the operation failed to complete.
  """
  if Mcpd().version < (1, 8):
    raise TooOldForOperation(
      minimum_version=(1, 8),
      current_version=Mcpd().version
    )
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.label(label),
    # The instance_type qualifier is used to find the factory for creating
    # the ui representation.
    Qualifiers.instance_type(InstanceTypes.IMPERATIVE),
  ]
  actual_value = DoubleTransactionData()
  actual_value.data = initial_value
  return _request_transaction_and_wait_for_result(
    DoubleTransactionData,
    qualifiers,
    actual_value
  )


def request_integer(label: str, *, initial_value: int=0) -> int:
  """Request an integer.

  This creates a window in the connected application into which the user can
  type an integer. When they press Okay, this function will return the number
  they typed in.

  Unlike request_float(), this only allows the user to enter a whole number.

  Parameters
  ----------
  label
    The label to display next to the text box.
  initial_value
    The initial value to place in the text box. This is 0 by default.

  Returns
  -------
  int
    The integer the user typed into the panel.

  Raises
  ------
  OperationCancelledError
    If the user cancelled the operation.
  OperationFailedError
    If the operation failed to complete.
  """
  if Mcpd().version < (1, 8):
    raise TooOldForOperation(
      minimum_version=(1, 8),
      current_version=Mcpd().version
    )
  # :HACK: Requesting an integer directly doesn't handle having a null
  # parent on the C++ side. To avoid needing to change the C++ code, this
  # emulates an integer request using a float request.
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.label(label),
    Qualifiers.instance_type(InstanceTypes.IMPERATIVE),
    # Format the field to show zero decimal places (i.e. An integer)
    Qualifiers.markup(".0f"),
  ]
  actual_value = DoubleTransactionData()
  actual_value.data = initial_value
  return int(_request_transaction_and_wait_for_result(
    DoubleTransactionData,
    qualifiers,
    actual_value
  ))


def ask_question(question: str, *, title: str="Python") -> bool:
  """Ask a yes/no question.

  This creates a window with a "Yes" and a "No" button.

  Parameters
  ----------
  question
    The content of the question. This appears above the Yes/No buttons.
  title
    The title of the window. This is "Python" by default.

  Returns
  -------
  bool
    True if the user clicked "Yes"; False if they clicked "No".

  Raises
  ------
  OperationFailedError
    If the operation failed to complete.
  """
  if Mcpd().version < (1, 8):
    raise TooOldForOperation(
      minimum_version=(1, 8),
      current_version=Mcpd().version
    )
  qualifiers = QualifierSet()
  qualifiers.values = [
    Qualifiers.label(question),
    Qualifiers.title(title),
    # The instance_type qualifier is used to find the factory for creating
    # the ui representation.
    Qualifiers.instance_type(InstanceTypes.IMPERATIVE),
  ]
  actual_value = BooleanTransactionData()
  actual_value.data = False
  try:
    return _request_transaction_and_wait_for_result(
      BooleanTransactionData,
      qualifiers,
      actual_value
    )
  except OperationCancelledError:
    # If the user clicks "No", then instead of sending a TransactionConfirm
    # message with a value of False, the server sends a TransactionCancel
    # message. The transaction converts this into an error, so catch the
    # error and return False.
    return False


def _decode_selection(outputs):
  """Function for decoding the selection from the transaction output."""
  for output in outputs.value:
    if output['idPath'] == 'selection':
      selection_string = output.get('value', '')
      break
  else:
    selection_string = ''

  return WorkflowSelection(selection_string)


def _request_transaction_and_wait_for_result(
    data_type: type[TransactionDataT],
    qualifiers: QualifierSet,
    initial_value: TransactionDataT) -> typing.Any:
  """Request a Transaction with the transaction manager and returns the result.

  Parameters
  ----------
  data_type
    Data type of the transaction to request.
  qualifiers
    Qualifiers to pass to the transaction.
  initial_value
    Initial values to place in the panel.

  Returns
  -------
  Any
    The result of the transaction request.

  Raises
  ------
  OperationCancelledError
    If the user cancelled the operation.
  OperationFailedError
    If the operation failed to complete.
  """
  with TransactionManager() as manager:
    transaction = None
    try:
      transaction = manager.request_transaction(
        data_type=data_type,
        qualifiers=qualifiers,
        initial_value=initial_value,
      )
      response = transaction.wait_for_value()
    # These except statements raise from None because the inner exception
    # is not intended to be user facing.
    except TransactionCancelledError as error:
      LOGGER.info(error)
      raise OperationCancelledError(
        "The operation was cancelled by the user.") from None
    except TransactionFailedError as error:
      LOGGER.info(error)
      raise OperationFailedError(
        "The operation failed for unknown reasons.") from None
    finally:
      if transaction:
        manager.remove_transaction(transaction)
    return response.data
