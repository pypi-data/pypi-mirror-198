"""Desurvey methods available for drillhole databases."""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import enum

class DesurveyMethod(enum.Enum):
  """Desurvey methods for drillhole databases."""
  NONE = 0
  """Placeholder indicating no desurvey information."""

  SEGMENT_FOLLOWING = 1
  """The segment following desurvey algorithm.

  Each drillhole interval following a survey measurement is positioned using
  that measurement.
  """

  SEGMENT_PRECEDING = 2
  """The segment preceding desurvey algorithm.

  Each drillhole interval preceding a survey measurement is positioned using
  that measurement.
  """

  TANGENT = 3
  """The tangent desurvey algorithm.

  Each drillhole interval about a survey measurement is positioned using
  that measurement as a tangent.
  """

  TANGENT_WITH_LENGTH = 4
  """The tangent with length desurvey algorithm.

  Interpolate additional survey information at a given distance down the
  hole. Each drillhole interval about a survey measurement is positioned
  using that measurement as a tangent.
  """

  UNDEFINED = 254
  """The desurvey method is not defined.

  This is often the desurvey method for drillhole databases created
  prior to Vulcan GeologyCore 2022.1 (Prior to this version, the desurvey
  method was stored on the Drillhole rather than the DrillholeDatabase.).
  """

  UNKNOWN = 255
  """The desurvey method is not recognised by the Python SDK."""
