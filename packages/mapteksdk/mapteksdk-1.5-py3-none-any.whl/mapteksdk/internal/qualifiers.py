"""The qualifier factory.

This is used by both RequestTransactionWithInputs and TransactionManager.

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

import enum
import typing

from .comms import InlineMessage, SubMessage, RepeatingField, SerialisedText
from .util import default_type_error_message


class InstanceTypes(enum.Enum):
  """Instance types for the InstanceType Qualifier."""
  MONTAGE = "Montage"
  IMPERATIVE = "Imperative"
  USER_MESSAGE = "UserMessage"
  APPLICATION = "Application"
  CUSTOM_TOOL_BARS = "CustomToolBars"
  GLOBAL_MANIPULATOR = "GlobalManipulator"
  MENU_BAR = "MenuBar"
  SELECTION_TYPE = "SelectionType"
  TOOL_BAR = "ToolBar"
  VIEW = "View"
  CHOICE = "Choice"
  SEQUENCE = "Sequence"
  EMBEDDED_VIEW = "EmbeddedView"
  WIZARD = "Wizard"
  MENU = "Menu"
  REDO = "Redo"
  UNDO = "Undo"
  WIDGET_INSPECTOR = "WidgetInspector"


class Qualifiers:
  """A factory of qualifiers."""

  @staticmethod
  def label(message):
    """The Label qualifier.

    This is typically used to set the label on a transaction.

    Parameters
    ----------
    message : str
      The text to put in the label.
    """
    qualifier = Qualifier()
    qualifier.key = 'Label'
    qualifier.cumulative = False

    text = SerialisedText("%s", message)
    qualifier.parameters = Qualifier.Parameters(text)
    return qualifier

  @staticmethod
  def title(message):
    """The Title qualifier.

    This is typically used to set the title of a transaction.
    Note that in older applications the label qualifier was used instead.

    Parameters
    ----------
    message : str
      The title text.
    """
    qualifier = Qualifier()
    qualifier.key = 'Title'
    qualifier.cumulative = False

    text = SerialisedText("%s", message)
    qualifier.parameters = Qualifier.Parameters(text)
    return qualifier

  @staticmethod
  def message(message):
    """The Message qualifier.

    This is typically used to set the message displayed by a transaction.

    Parameters
    ----------
    message : str
      The message text.
    """
    qualifier = Qualifier()
    qualifier.key = 'Message'
    qualifier.cumulative = True

    text = SerialisedText("%s", message)
    qualifier.parameters = Qualifier.Parameters(text)
    return qualifier

  @staticmethod
  def markup(markup_string: str):
    """The Markup qualifier.

    This is used to determine how a various types should be represented in
    the user interface.

    Parameters
    ----------
    markup_string
      Markup string to apply to the value.
    """
    qualifier = Qualifier()
    qualifier.key = 'Markup'
    qualifier.cumulative = False

    qualifier.parameters = Qualifier.Parameters(markup_string)
    return qualifier

  @staticmethod
  def toast():
    """The Toast qualifier.

    This is used to indicate to a transaction that it should display the
    message as a toast notification.
    """
    qualifier = Qualifier()
    qualifier.key = 'Toast'
    qualifier.cumulative = False
    qualifier.parameters = Qualifier.Parameters()

    return qualifier

  @staticmethod
  def instance_type(instance_type: InstanceTypes):
    """The instance type qualifier.

    This is used to find the appropriate factory for creating the UI realisation
    of a request.

    Parameters
    ----------
    instance_type
      The instance type of this qualifier.
    """
    if not isinstance(instance_type, InstanceTypes):
      raise TypeError(default_type_error_message(
        "instance_type", instance_type, InstanceTypes
      ))
    qualifier = Qualifier()
    qualifier.key = 'InstanceType'
    qualifier.cumulative = False

    qualifier.parameters = Qualifier.Parameters(instance_type.value)
    return qualifier

  @staticmethod
  def choice_values(choices: typing.Iterable[typing.Any]):
    """Restrict the values to the given choices.

    Parameters
    ----------
    choices
      The choices to restrict the operation to. These must be
      of an appropriate type (e.g. If the request is for a string,
      these must also be strings).
    """
    qualifier = Qualifier()
    qualifier.key = "ChoiceValues"
    qualifier.cumulative = True
    qualifier.parameters = Qualifier.Parameters(*choices)

    return qualifier

class Qualifier(InlineMessage):
  """A qualifier is used to attribute a quality to a transaction."""

  class Parameters(SubMessage):
    """The parameters or values of a qualifier."""

    values: RepeatingField[typing.Any]

    def __init__(self, *args):
      self.values = args

  key: str
  cumulative: bool
  parameters: Parameters


class QualifierSet(SubMessage):
  """A set of qualifiers often used with a transaction to qualify it."""
  values: RepeatingField[Qualifier]
