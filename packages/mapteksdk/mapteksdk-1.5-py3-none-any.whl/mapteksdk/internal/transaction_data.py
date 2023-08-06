"""Transaction data structs for transactions.

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

from .comms import InlineMessage

DATA_GROUP = "mdf::serC_DataGroup"

class TransactionData(InlineMessage):
  """Abstract base class for TransactionData classes.

  Classes which implement this can be used to set the initial values
  displayed in a panel when requesting a transaction or to read the values
  which the user entered into the panel.

  Examples
  --------
  Imagine a simplified version of the panel for creating 2D text which accepts
  only a single string and a single point. The inputs are represented as
  type hinted variables on the class (A point is represented as three floats).
  Then the inheriting class needs to determine the name of the transaction.

  >>> class SimpleLabelTransactionData(TransactionData):
  ...     message: str
  ...     X: ctypes.c_float64
  ...     Y: ctypes.c_float64
  ...     Z: ctypes.c_float64
  ...     @classmethod
  ...     def transaction_name():
  ...         return "mdf::cadC_SimpleLabelTransaction"
  """
  @staticmethod
  def transaction_name() -> str:
    """The name of the transaction this data is for.

    This includes the namespace.
    """
    raise NotImplementedError("Must be implemented in child classes.")

  @staticmethod
  def data_type_name() -> str:
    """The name of the data type this transaction accepts.

    This is "mdf::serC_DataGroup" by default, which is what most montages
    use, however child classes may overwrite this if they use a different type.
    """
    return DATA_GROUP

class StringTransactionData(TransactionData):
  """Transaction data for a simple request of a string.

  This is realised as a panel with a single text box the user can type a string
  into.
  """
  data: str

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<mdf::Tstring>"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::Tstring"


class DoubleTransactionData(TransactionData):
  """Transaction data for a simple request of a 64 bit float.

  By default this is realised as a panel with a single text box the user
  can type a number into.
  """
  data: ctypes.c_double

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<double>"

  @staticmethod
  def data_type_name() -> str:
    return "::Tfloat64"


class BooleanTransactionData(TransactionData):
  """Transaction data for a simple request of a boolean.

  If this is a top-level request, it is realised as a panel with a "Yes" and
  a "No" button.
  """
  data: bool

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<bool>"

  @staticmethod
  def data_type_name() -> str:
    return "::Tbool"
