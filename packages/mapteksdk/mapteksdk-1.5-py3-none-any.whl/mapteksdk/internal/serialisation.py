"""Classes designed to be serialised in MCP messages.

Warnings
--------
Vendors and clients should not develop scripts or applications against
this package. The contents may change at any time without warning.
"""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import ctypes
import json
import typing

from mapteksdk.internal.comms import InlineMessage, SubMessage
from mapteksdk.internal.qualifiers import QualifierSet

class Icon:
  """This type should be used in the definition of a message where an icon is
  expected.
  """
  storage_type = str

  def __init__(self, name=''):
    self.name = name

  @classmethod
  def convert_from(cls, storage_value):
    """Convert from the underlying value to this type."""
    assert isinstance(storage_value, cls.storage_type)
    return cls(storage_value)

  @classmethod
  def convert_to(cls, value):
    """Convert the icon name to a value of the storage type (str).

    Returns
    -------
      A str which is the name of the icon.

    Raises
    ------
    TypeError
      If value is not a Icon or str, i.e the value is not an icon.
    """
    if isinstance(value, cls):
      return value.name
    if isinstance(value, str):
      return value

    raise TypeError('The value for a Icon should be either an Icon or str.')


class JsonValue:
  """This type should be used in the definition of a Message where JSON is
  expected.
  """

  storage_type = str

  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)

  @classmethod
  def convert_from(cls, storage_value):
    """Convert from the underlying value to this type."""
    assert isinstance(storage_value, cls.storage_type)
    return cls(json.loads(storage_value))

  @classmethod
  def convert_to(cls, value):
    """Convert the value to the storage type.

    Returns
    -------
      The serialised value to a JSON formatted str.

    Raises
    ------
    TypeError
      If value is not a JsonValue or not suitable for seralisation to JSON
      with Python's default JSON encoder.
    """
    if isinstance(value, cls):
      return json.dumps(value.value)

    return json.dumps(value)

class KeyBinding(InlineMessage):
  """A key binding for a transaction."""
  is_valid: bool
  is_hold_and_click: bool
  key: ctypes.c_uint32 # keyE
  modifiers: ctypes.c_uint32 # keyE_Modifier

class Context(SubMessage):
  """Transaction context object."""
  active_view_id: ctypes.c_uint64
  active_view_name: str
  associated_view_ids: typing.Set[ctypes.c_uint64]
  workspace_views: typing.Set[ctypes.c_uint64]
  finish_hint: ctypes.c_uint8 # uiC_Outcome (Enum)
  selection_contains_objects: bool
  selection_type: ctypes.c_int32 # picE_SelectionType
  # A datetime is represented as two floats - a day number and seconds
  # since midnight.
  # Converting these to/from a Python datetime is non-trivial, so just
  # pretend it is two floats.
  selection_last_change_time_day_number: ctypes.c_double
  selection_last_change_time_seconds_since_midnight: ctypes.c_double
  key_modifiers: ctypes.c_uint32 # keyE_Modifiers
  key_binding: KeyBinding
  scones: QualifierSet
  cookies: QualifierSet
