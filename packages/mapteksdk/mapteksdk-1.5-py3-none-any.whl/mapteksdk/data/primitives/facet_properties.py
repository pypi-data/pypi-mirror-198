"""Support for facet primitives.

A facet is a triangle defined by three points. In Python, a facet is
represented as a numpy array containing three integers representing the
indices of the points which make up the three corners of the triangle.
For example, the facet [0, 1, 2] indicates the triangle defined by the
0th, 1st and 2nd points. Because facets are defined based on points, all
objects which inherit from FacetProperties must also inherit from
PointProperties.

"""
###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import ctypes
import logging
import typing

import numpy as np

from .primitive_attributes import PrimitiveAttributes, PrimitiveType
from ..errors import DegenerateTopologyError
from ...capi import Modelling
from ...internal.data_property import DataProperty, DataPropertyConfiguration

if typing.TYPE_CHECKING:
  from ...common.typing import FacetArray, BooleanArray, ColourArray, IndexArray
  from ...internal.lock import ReadLock, WriteLock
  import numpy.typing as npt

log = logging.getLogger("mapteksdk.data")

# The following warning can be enabled if the <Primitive>Properties classes
# ended in Mixin as then pylint expects that the members are defined elsewhere.
# pylint: disable=no-member

class FacetProperties:
  """Mixin class which provides spatial objects support for facet primitives.

  A facet is a triangle drawn between three points. For example, the
  facet [i, j, k] is the triangle drawn between object.points[i],
  object.points[j] and object.points[k].

  Functions and properties defined on this class are available on all
  classes which support facets.
  """
  __facets: DataProperty
  __facet_colours: DataProperty
  __facet_selection: DataProperty
  __facet_attributes: PrimitiveAttributes | None

  # Properties the inheriting object is expected to provide:
  is_read_only: bool
  _lock: WriteLock | ReadLock
  _raise_if_read_only: typing.Callable[[str], None]
  _raise_if_save_in_read_only: typing.Callable[[], None]
  _reconcile_changes: typing.Callable[[], None]

  def _initialise_facet_properties(self):
    """Initialises the facet properties.

    This must be called during the __init__ function of child classes.
    """
    self.__facets = DataProperty(
      lock=self._lock,
      configuration=DataPropertyConfiguration(
        name="facets",
        dtype=ctypes.c_int32,
        default=0,
        column_count=3,
        primitive_count_function=Modelling().ReadFacetCount,
        load_function=Modelling().FacetToPointIndexBeginR,
        save_function=Modelling().FacetToPointIndexBeginRW,
        cached_primitive_count_function=None,
        set_primitive_count_function=Modelling().SetFacetCount,
        raise_on_error_code=Modelling().RaiseOnErrorCode
      )
    )

    self.__facet_colours = DataProperty(
      lock=self._lock,
      configuration=DataPropertyConfiguration(
        name="facet_colours",
        dtype=ctypes.c_uint8,
        default=np.array([0, 220, 0, 255], dtype=ctypes.c_uint8),
        column_count=4,
        primitive_count_function=Modelling().ReadFacetCount,
        cached_primitive_count_function=lambda: self.facet_count,
        load_function=Modelling().FacetColourBeginR,
        save_function=Modelling().FacetColourBeginRW,
        is_colour_property=True,
        raise_on_error_code=Modelling().RaiseOnErrorCode
      )
    )

    self.__facet_selection = DataProperty(
      lock=self._lock,
      configuration=DataPropertyConfiguration(
        name="facet_selection",
        dtype=ctypes.c_bool,
        default=False,
        column_count=1,
        primitive_count_function=Modelling().ReadFacetCount,
        cached_primitive_count_function=lambda: self.facet_count,
        load_function=Modelling().FacetSelectionBeginR,
        save_function=Modelling().FacetSelectionBeginRW,
        raise_on_error_code=Modelling().RaiseOnErrorCode
      )
    )

    self.__facet_attributes = None

  @property
  def facets(self) -> FacetArray:
    """A 2D numpy array of facets in the object.

    This is of the form: [[i0, j0, k0], [i1, j1, k1], ..., [iN, jN, kN]] where
    N is the number of facets. Each i, j and k value is the index of the point
    in Objects.points for the point used to define the facet.
    """
    return self.__facets.values

  @facets.setter
  def facets(self, facets: npt.ArrayLike):
    self.__facets.values = facets

  @property
  def facet_colours(self) -> ColourArray:
    """A 2D numpy array containing the colours of the facets."""
    return self.__facet_colours.values

  @facet_colours.setter
  def facet_colours(self, facet_colours: npt.ArrayLike):
    self.__facet_colours.values = facet_colours

  @property
  def facet_selection(self) -> BooleanArray:
    """A 1D numpy array representing which facets are selected.

    If object.facet_selection[i] = True then the ith facet
    is selected.
    """
    return self.__facet_selection.values

  @facet_selection.setter
  def facet_selection(self, facet_selection: npt.ArrayLike):
    self.__facet_selection.values = facet_selection

  @property
  def facet_count(self) -> int:
    """The number of facets in the object."""
    if not self.__facets.are_values_cached:
      return Modelling().ReadFacetCount(self._lock.lock)
    return self.facets.shape[0]

  def _invalidate_facet_properties(self):
    """Invalidates the cached facet properties.

    The next time a facet property is accessed, its values will be loaded from
    the project.
    """
    self.__facets.invalidate()
    self.__facet_colours.invalidate()
    self.__facet_selection.invalidate()
    self.__facet_attributes = None

  # If another class is added which needs this function it should be
  # converted into a FacetDeletionProperties mixin class.
  def remove_facets(self, facet_indices: npt.ArrayLike) -> bool:
    """Remove one or more facets from the object.

    Calling this function is preferable to altering the facets array because
    this function also removes the facet properties associated with the removed
    facets (e.g. facet colours, facet visibility, etc). Additionally,
    after the removal any points or edges which are not part of a facet
    will be removed from the object.

    This operation is performed directly on the Project and will not be undone
    if an error occurs.

    Parameters
    ----------
    facet_indices
      The index of the facet to remove or a list of indices of facets to
      remove.
      Indices should only contain 32-bit unsigned integer (They should be
      greater than or equal to 0 and less than 2**32).
      Any index greater than or equal to the facet count is ignored.
      Passing an index less than zero is not supported. It will not delete
      the last facet.

    Returns
    -------
    bool
      If passed a single facet index, True if the facet was removed
      and False if it was not removed.
      If passed an iterable of facet indices, True if the object supports
      removing facets and False otherwise.

    Raises
    ------
    ReadOnlyError
      If called on an object not open for editing. This error indicates an
      issue with the script and should not be caught.

    Warnings
    --------
    Any unsaved changes to the object when this function is called are
    discarded before any facets are deleted. If you wish to keep these changes,
    call save() before calling this function.
    """
    self._invalidate_facet_properties()
    if isinstance(facet_indices, int):
      result = self._remove_facet(facet_indices)
    else:
      if not isinstance(facet_indices, np.ndarray):
        facet_indices = np.array(facet_indices, dtype=np.uint32)
      result = self._remove_facets(facet_indices)
    self._reconcile_changes()
    return result

  def _save_facet_properties(self):
    """Save the facet properties.

    This must be called during save() of the inheriting object.
    This should never be called directly. To save an object, call save()
    instead.

    Raises
    ------
    CannotSaveInReadOnlyModeError
      If in read-only mode.

    Notes
    -----
    Generally this should be called after PointProperties.save_points().
    """
    self._raise_if_save_in_read_only()
    # Write all relevant properties for this primitive type
    if self.facet_count == 0:
      message = "Object must contain at least one facet"
      raise DegenerateTopologyError(message)

    self.__facets.save()
    self.__facet_colours.save()
    self.__facet_selection.save()

    if self.__facet_attributes is not None:
      self.__facet_attributes.save_attributes()

  @property
  def facet_attributes(self) -> PrimitiveAttributes:
    """Access the custom facet attributes.

    These are arrays of values of the same type, with one value for each facet.

    Use Object.facet_attributes[attribute_name] to access a facet attribute
    called attribute_name. See PrimitiveAttributes for valid operations
    on facet attributes.

    Returns
    -------
    PrimitiveAttributes
      Access to the facet attributes.

    Raises
    ------
    ValueError
      If the type of the attribute is not supported.
    """
    if self.__facet_attributes is None:
      self.__facet_attributes = PrimitiveAttributes(
        PrimitiveType.FACET,
        # FacetProperties requires that the inheriting class is Topology
        # so that self can be passed here.
        self # type: ignore
      )
    return self.__facet_attributes

  def save_facet_attribute(
      self,
      attribute_name: str,
      data: npt.ArrayLike):
    """Create new and/or edit the values of the facet attribute attribute_name.

    This is equivalent to Object.facet_attributes[attribute_name] = data.

    Parameters
    ----------
    attribute_name : str
      The name of attribute.
    data : array
      A numpy array of a base type data to store for the attribute
      per-primitive.
    """
    self.facet_attributes[attribute_name] = data

  def delete_facet_attribute(self, attribute_name: str):
    """Delete a facet attribute by name.

    This is equivalent to: facet_attributes.delete_attribute(attribute_name)

    Parameters
    ----------
    attribute_name : str
      The name of attribute.

    Raises
    ------
    Exception
      If the object is opened in read-only mode.
    """
    self.facet_attributes.delete_attribute(attribute_name)

  def _remove_facet(self, facet_index: int):
    """Remove facet at given index of facet array.

    Parameters
    ----------
    facet_index
      Index of facet to remove.

    Returns
    -------
    bool
      True if successful.

    Raises
    ------
    ReadOnlyError
      If called on an object not open for editing. This error indicates an
      issue with the script and should not be caught.

    Notes
    -----
    Changes will not be reflected until the object is saved or
    _reconcile_changes() is called.
    """
    self._raise_if_read_only("remove facet")
    return Modelling().RemoveFacet(self._lock.lock,
                                   facet_index)

  def _remove_facets(
      self, facet_indices: IndexArray):
    """Remove list of facets at given indices of facets array.

    Parameters
    ----------
    facet_indices
      1D array of uint32 indices of facets to remove.

    Returns
    -------
    bool
      True if successful.

    Raises
    ------
    ReadOnlyError
      If called on an object not open for editing. This error indicates an
      issue with the script and should not be caught.

    Notes
    -----
    Changes will not be reflected until the object is saved or
    _reconcile_changes() is called.
    """
    self._raise_if_read_only("remove facets")
    index_count = len(facet_indices)
    array = (ctypes.c_uint32 * index_count)(*facet_indices)
    return Modelling().RemoveFacets(
      self._lock.lock, array, index_count)
