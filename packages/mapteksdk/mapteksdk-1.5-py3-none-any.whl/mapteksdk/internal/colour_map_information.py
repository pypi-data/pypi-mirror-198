"""Tuple representing colour map information."""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import typing

from ..data.primitive_type import PrimitiveType
from ..data.objectid import ObjectID

if typing.TYPE_CHECKING:
  from ..data.colourmaps import ColourMap

NO_COLOUR_MAP: typing.Literal["NO_COLOUR_MAP"] = "NO_COLOUR_MAP"
"""Constant used to mark the absence of a colour map."""

class ColourMapInformation(typing.NamedTuple):
  """Named tuple containing colour map information for a Topology object."""
  attribute_name: str
  """The name of the attribute the object is coloured by."""
  primitive_type: PrimitiveType
  """The primitive type of the attribute the object is coloured by."""
  colour_map_id: ObjectID[ColourMap]
  """Object ID of the colour map used to colour this object."""
