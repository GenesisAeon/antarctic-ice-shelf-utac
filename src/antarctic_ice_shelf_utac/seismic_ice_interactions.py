"""Seismic <-> ice interactions: icequakes, deglaciation-triggered
debris flows, and glacial-isostatic-adjustment (GIA) seismicity.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    BALLENY_1998_MAGNITUDE_MW,
    HEREDIA_BARION_2023_CITATION,
    LIPOVSKY_2016_CITATION,
    SEISMIC_ICE_NOTE,
    TSUBOI_2000_CITATION,
    WHILLANS_ICEQUAKE_RECURRENCE_MINUTES,
    WHILLANS_ICEQUAKES_PER_RECORD_COUNT,
    WHILLANS_LARGE_SLIP_EVENTS_PER_DAY,
    WIENS_2008_CITATION,
)


@dataclass(frozen=True)
class WhillansIcequakeRecord:
    """Wiens et al. (2008) + Lipovsky & Dunham (2016)'s Whillans Ice
    Plain stick-slip icequake record."""

    events_in_record: int
    recurrence_minutes: float
    large_slip_events_per_day: float
    citation: dict[str, object]


ICEQUAKE_RECORD = WhillansIcequakeRecord(
    events_in_record=WHILLANS_ICEQUAKES_PER_RECORD_COUNT,
    recurrence_minutes=WHILLANS_ICEQUAKE_RECURRENCE_MINUTES,
    large_slip_events_per_day=WHILLANS_LARGE_SLIP_EVENTS_PER_DAY,
    citation=WIENS_2008_CITATION,
)

LIPOVSKY_2016 = LIPOVSKY_2016_CITATION


def is_icequake_recurrence_tidally_modulated() -> bool:
    """Whether Whillans Ice Plain icequake timing is paced by ocean tides.

    True -- Wiens et al. 2008's central finding. A real, well-quantified
    Antarctic-specific basal stick-slip mechanism.
    """
    return True


@dataclass(frozen=True)
class DeglaciationDebrisFlowEvidence:
    """Heredia Barion et al. (2023)'s Potter Peninsula debris-flow record."""

    location: str
    documented_since_year: int
    citation: dict[str, object]


DEBRIS_FLOW_EVIDENCE = DeglaciationDebrisFlowEvidence(
    location="Potter Peninsula, King George Island",
    documented_since_year=1956,
    citation=HEREDIA_BARION_2023_CITATION,
)


def is_antarctic_rockfall_trend_as_well_quantified_as_the_alps() -> bool:
    """Whether Antarctic deglaciation-triggered debris flows/mudflows have
    a quantified frequency/volume trend, as the Alpine rockfall
    literature does.

    Always False -- the mechanism is real and documented at Potter
    Peninsula since 1956 (failure scars 20-180m wide), but without a
    quantified trend, unlike Hartmeyer et al. 2020's Alps-specific
    (Austria) study, which is NOT used here as an Antarctic citation.
    """
    return False


@dataclass(frozen=True)
class BallenyGiaEarthquake:
    """Tsuboi et al. (2000)'s GIA-triggered 1998 Balleny Islands earthquake."""

    year: int
    magnitude_mw: float
    citation: dict[str, object]


BALLENY_EARTHQUAKE = BallenyGiaEarthquake(
    year=1998,
    magnitude_mw=BALLENY_1998_MAGNITUDE_MW,
    citation=TSUBOI_2000_CITATION,
)


def does_gia_seismicity_amplify_ice_sheet_collapse() -> bool:
    """Whether glacial-isostatic-adjustment-triggered seismicity feeds
    back to accelerate West Antarctic ice-sheet collapse.

    Always False -- GIA uplift itself is documented elsewhere as a
    STABILIZING negative feedback (reduces marine ice-sheet
    instability), even though it can independently trigger real
    earthquakes like Balleny 1998. Do not frame GIA seismicity as an
    amplifying mechanism.
    """
    return False


def seismic_ice_note() -> str:
    return SEISMIC_ICE_NOTE
