"""Request transactions without using the Workflows system.

This is an alternative to the classes defined in transactions.py.
Unlike RequestTransactionWithInputs, this requests the transaction the
same way as C++ code in the application would do it. This provides more
versatility than RequestTransactionWithInputs, however it is more difficult
to automate and read outputs.

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
import itertools
import logging
import typing

from .comms import Request, InlineMessage, Message
from .serialisation import Context
from .transaction import QualifierSet
from .transaction_data import TransactionData
from ..capi.mcp import Mcpd
from ..capi.types import T_MessageHandle

LOG = logging.getLogger("mapteksdk.internal.transaction_manager")

NEXT_OPERATION_ID = itertools.count(start=1)

T = typing.TypeVar("T", bound=TransactionData)


# :NOTE: These errors are not intended to be user facing. They should be
# caught and converted into user-friendly errors by callers.
class TransactionFailedError(Exception):
  """Error raised when a transaction fails.

  This may indicate this operation is not supported by the application.
  """


class TransactionSetUpError(TransactionFailedError):
  """Exception thrown when failing to start a transaction.

  This indicates the server returned an error response to TransactionRequest.

  Parameters
  ----------
  transaction_name
    Name of the menu command which could not be created.
  """
  def __init__(self, transaction_name: str):
    self.transaction_name = transaction_name
    super().__init__(
      f"Failed to start menu command: {transaction_name}."
    )


class TransactionCancelledError(Exception):
  """Error raised when a menu command is cancelled.

  This indicates the user pressed "Cancel" or closed the window
  without confirming it.
  """
  def __init__(self, transaction_name: str):
    self.transaction_name = transaction_name
    super().__init__(
      f"The following command was cancelled: {transaction_name}."
    )


class TransactionCreate(Request):
  """A message requesting for a transaction to be created."""
  message_name = 'TransactionCreate'

  class Response(InlineMessage):
    """The response to a TransactionCreate message."""
    success: bool
    """True if the transaction was successfully started."""
    server_address: ctypes.c_uint64
    """The address of the transaction on the server."""

  response_type = Response

  transaction_manager_address: ctypes.c_uint64
  """Address of the transaction manager associated with the transaction.

  This is primarily used for undo/redo support, however the
  Python SDK doesn't support this so this isn't used for
  anything other than equality operations.
  """

  # Currently this class doesn't include the parent transaction address
  # because the Python SDK doesn't support it.
  # parent_transaction_address: typing.Optional[ctypes.c_uint64]

  class_name: str
  """The class name of the transaction to create.

  This should include the namespace.
  """

  data_type_name: str
  """The data type name for this transaction."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction object.

  This is used, along with the transaction token, to uniquely
  identify the transaction.
  """

  transaction_token: ctypes.c_uint64
  """The transaction token.

  This is used, along with the transaction address, to uniquely
  identify the transaction. This should be different for every
  message sent within the same process.
  """

  qualifiers: QualifierSet
  """Qualifiers to apply to the transaction."""

  initial_value: InlineMessage
  """Initial values to place into the panel.

  This is typically (but not required to be) a TransactionData subclass.
  """


class TransactionDestroy(Message):
  """Destroy a transaction on the server."""
  message_name: typing.ClassVar[str] = "TransactionDestroy"

  parent_transaction_address: ctypes.c_uint64
  """The address of the parent transaction of the transaction to destroy."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction to destroy."""


class TransactionConfirm(Message):
  """A message indicating a transaction has been confirmed.

  This does not parse the entire TransactionConfirm message. Instead
  it only parses the generic part of the message. This is used to identify
  which transaction was confirmed. The transaction then parses the remainder
  of the message (typically via a TransactionData subclass).

  This can never be sent by Python, only received.
  """
  message_name: str = "TransactionConfirm"

  transaction_address: ctypes.c_uint64
  """The address of the transaction which was confirmed.

  This will be the same as in the corresponding TransactionCreate
  message.
  """

  transaction_token: ctypes.c_uint64
  """The token of the transaction which was confirmed.

  This will be the same as in the corresponding TransactionCreate
  message
  """

  def send(self, destination):
    raise TypeError(
      "This type of message is a response only. It shouldn't be sent."
    )


class TransactionCancel(Message):
  """A message indicating a transaction has been cancelled.

  This does not parse the entire TransactionCancel message. Instead it
  only parses the generic part of the message. This is used to identify which
  transaction was cancelled.

  This can never be sent by Python, only received.
  """
  message_name: str = "TransactionCancel"

  top_level_transaction_address: ctypes.c_uint64
  """The address of the top-level transaction which was cancelled."""

  transaction_token: ctypes.c_uint64
  """The token of the transaction which was cancelled."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction which was cancelled."""

  def send(self, destination):
    raise TypeError(
      "This type of message is a response only. It shouldn't be sent."
    )


class Transaction(typing.Generic[T]):
  """Class representing a Transaction managed by the TransactionManager."""
  def __init__(
      self,
      transaction_manager: "TransactionManager",
      transaction_data: typing.Type[T],
      qualifiers: QualifierSet,
      initial_value: T):
    self.__transaction_manager = transaction_manager
    self.__transaction_data = transaction_data
    self.__qualifiers = qualifiers
    self.__initial_value = initial_value
    self.__token = next(NEXT_OPERATION_ID)
    self.__value = None
    self.__is_cancelled = False
    self.__has_error = False
    self.__server_address = None
    """The address of the server-side representation of the transaction.

    This is required to destruct the server-side representation of this
    transaction.
    """

  def name(self) -> str:
    """The name of the transaction, including the namespace."""
    return self.__transaction_data.transaction_name()

  def key(self) -> typing.Tuple[ctypes.c_uint64, ctypes.c_uint64]:
    """Key which uniquely identifies this transaction (within this process).

    This is used by the transaction manager to determine which transaction
    an event is relevant to.

    Returns
    -------
    tuple
      A tuple containing the id of this Python object and the token
      assigned to this object.
    """
    return (id(self), self.__token)

  def send(self):
    """Send the transaction to the relevant server.

    Raises
    ------
    TransactionSetUpError
      If the menu command could not be created on the relevant server.
    """
    request = TransactionCreate()
    request.transaction_manager_address = id(self.__transaction_manager)
    request.class_name = self.__transaction_data.transaction_name()
    request.data_type_name = self.__transaction_data.data_type_name()
    request.transaction_address = id(self)
    request.transaction_token = self.__token
    request.qualifiers = self.__qualifiers
    request.initial_value = self.__initial_value
    response = request.send('uiServer')
    # pylint: disable=no-member
    # Pylint can't figure out that response is of ResponseType.
    if not response.success:
      raise TransactionSetUpError(self.name())
    self.__server_address = response.server_address

  def delete_server_side(self):
    """Delete the transactions server-side representation.

    This should be called immediately after receiving a response from
    the server to ensure that any UI the server created for the request
    is disposed of quickly.

    It is safe to call this function multiple times.
    """
    if not self.__server_address:
      return
    destroy_request = TransactionDestroy()
    # We don't currently support parent transactions, so the parent
    # address is the same as the transaction address.
    destroy_request.parent_transaction_address = self.__server_address
    destroy_request.transaction_address = self.__server_address
    destroy_request.send('uiServer')
    self.__server_address = None

  def wait_for_value(self) -> T:
    """Wait for the transaction to be confirmed and return a value.

    Returns
    -------
    T
      The response type for this transaction.
    """
    try:
      while True:
        Mcpd().dll.McpServicePendingEvents()
        if self.__value is not None:
          break
        if self.__is_cancelled:
          break
        if self.__has_error:
          break
    except OSError as error:
      LOG.exception(error)
      raise
    if self.__is_cancelled:
      raise TransactionCancelledError(self.name())
    if self.__has_error:
      raise TransactionFailedError(
        "Failed to read result of operation."
      )

    assert self.__value is not None
    return self.__value

  def read_transaction_data(self, message_handle: T_MessageHandle):
    """Read the transaction data from a message.

    Parameters
    ----------
    message_handle
      Message handle to read the transaction data from.
      This message handle should already have been partially
      read via TransactionConfirm.from_handle(). This reads the remaining
      data from the message and assigns it to this object so that it
      will be returned by wait_for_value().
    """
    try:
      self.__value = self.__transaction_data.from_handle(message_handle)
    except:
      self.__has_error = True
      raise

  def cancel(self):
    """Cancels the transaction."""
    self.__is_cancelled = True

class TransactionManager:
  """Manages MCP messages related to transactions.

  This class maintains a list of all of the transactions it has started.
  When an MCP event arrives which is relevant to one of these transactions,
  it parses enough of the message to identify which transaction the message
  is for. It then passes the remainder of that message to the transaction
  for handling.
  """
  def __init__(self):
    self.__callback_handles: typing.List[
      typing.Tuple[typing.Any, typing.Callable[[typing.Any], None]], str] = []
    """List of callbacks created by this object.

    Each element of the list is a tuple containing:

    * The callback handle.
    * The callback function.
    * The name of the message which will trigger the callback.

    Both the handle and the function need to be kept until this object is
    destructed to avoid undefined behaviour caused by attempting to call a
    callback which has been disposed of.

    This is also used to ensure all of the callbacks are disposed when
    this object is disposed.
    """

    self.__transactions: typing.Dict[
      typing.Tuple[ctypes.c_uint64, ctypes.c_uint64], Transaction] = {}
    """Dictionary of transactions this object is keeping track of.

    The keys are a tuple of the transaction address and transaction token,
    and the values are the actual Transaction objects.
    """

  def __enter__(self):
    def _on_transaction_confirm(message_handle):
      """Callback run when a TransactionConfirm message arrives."""
      # This reads the generic parts of the TransactionConfirm.
      # It doesn't read to the end of the message, only the
      # generic part at the beginning.
      event = TransactionConfirm.from_handle(message_handle)
      try:
        # pylint: disable=no-member
        # Pylint incorrectly deduces the type of event as Message
        # instead of TransactionConfirm.
        # See: https://github.com/PyCQA/pylint/issues/981
        transaction = self.__transactions[
            (event.transaction_address, event.transaction_token)
          ]
        # Immediately destroy the server-side representation of the
        # transaction to ensure the panel doesn't hang around.
        transaction.delete_server_side()

        # This doesn't currently use the context. Read it and discard it
        # so that the next part of the message can be read.
        _ = Context.from_handle(message_handle)

        # Read the transaction-specific data.
        transaction.read_transaction_data(message_handle)
      except KeyError:
        # pylint: disable=no-member
        # Same issue as in the try block.
        LOG.info(
          "Received TransactionConfirm for: "
          "transaction_address: %s"
          "transaction token: %s"
          "But it was not found in the transaction list",
          event.transaction_address, event.transaction_token)

    def _on_transaction_cancel(message_handle):
      """Callback run when a TransactionCancel message arrives."""
      event = TransactionCancel.from_handle(message_handle)

      try:
        # pylint: disable=no-member
        transaction = self.__transactions[
          (event.transaction_address, event.transaction_token)
        ]
        transaction.cancel()
        # Immediately destroy the server-side representation of the
        # transaction to ensure the panel doesn't hang around.
        transaction.delete_server_side()

        # :NOTE: This could read the context and transaction data,
        # but it isn't used.
      except KeyError:
        # pylint: disable=no-member
        LOG.info(
          "Received TransactionCancel for: "
          "transaction_address: %s "
          "transaction token: %s "
          "But it was not found in the transaction list",
          event.transaction_address, event.transaction_token)

    self.__register_callback(
      "TransactionConfirm",
      _on_transaction_confirm
    )
    self.__register_callback(
      "TransactionCancel",
      _on_transaction_cancel
    )
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    for transaction in list(self.__transactions.values()):
      self.remove_transaction(transaction)
    for callback_handle, _, message_name in self.__callback_handles:
      Mcpd().dll.McpRemoveCallbackOnMessage(
        message_name.encode("utf-8"), callback_handle)

  def __register_callback(self, event_name: str, callback):
    """Register a callback to be called for the given MCP event.

    This handles registering the callback to be removed when this
    object is disposed.

    Parameters
    ----------
    event_name
      The name of the event which should call the callback.
    callback
      Function which accepts a message handle and returns no value
      to be called when the event arrives.
    """
    callback_handle = Mcpd().dll.Callback(callback)
    # :TRICKY: Include the callback handle in the tuple to ensure
    # it is not garbage collected before it is called.
    self.__callback_handles.append(
      (Mcpd().dll.McpAddCallbackOnMessage(
        event_name.encode("utf-8"),
        callback_handle
      ), callback_handle, event_name)
    )

  def request_transaction(
      self,
      data_type: typing.Type[T],
      qualifiers: QualifierSet,
      initial_value: T) -> Transaction[T]:
    """Request a transaction by name.

    Parameters
    ----------
    data_type
      The data type the transaction will return.
    qualifiers
      Qualifier set to apply to the transaction.
    initial_value
      Initial values to be entered into the panel.

    Returns
    -------
    Transaction
      The newly created transaction. This is already registered with this
      object and ready to be sent to the appropriate server.

    Raises
    ------
    TransactionSetUpError
      If the transaction could not be created on the server.
    """
    transaction = Transaction(
      self, data_type, qualifiers,
      initial_value
    )
    key = transaction.key()
    self.__transactions[key] = transaction
    try:
      transaction.send()
    except TransactionSetUpError:
      # Failed to create the transaction on the server. Remove it from
      # the dictionary.
      del self.__transactions[key]
      raise

    return transaction

  def remove_transaction(self, transaction: Transaction):
    """Remove the transaction from the transaction manager.

    This will cause MCP events intended for this transaction to be
    ignored. This will do nothing if the transaction has already been
    removed, or was never added to this object.

    Parameters
    ----------
    transaction
      The transaction to remove.
    """
    try:
      del self.__transactions[transaction.key()]
      # Make sure the transaction's server side representation is destroyed
      # as well.
      transaction.delete_server_side()
    except KeyError:
      pass
