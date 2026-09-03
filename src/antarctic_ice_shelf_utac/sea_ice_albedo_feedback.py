"""Sea-ice albedo feedback -- Riihela et al. (2021) -- and the linked
sea-ice-to-snowfall mechanism -- Kromer et al. (2023).

Explicitly NOT exposed-continental-rock albedo feedback: that mechanism
was searched for and not found as an existing, quantified,
Antarctica-specific result (see SEA_ICE_SNOWFALL_NOTE). Conflating the
two would misrepresent what is actually measured.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    KROMER_2023_CITATION,
    RIIHELAE_2021_CITATION,
    SEA_ICE_ALBEDO_FEEDBACK_1992_2015_W_M2_PER_DECADE,
    SEA_ICE_ALBEDO_FEEDBACK_2016_2018_COMBINED_W_M2,
    SEA_ICE_ALBEDO_FEEDBACK_PCT_OF_CO2_FORCING,
    SEA_ICE_SNOWFALL_NOTE,
)


@dataclass(frozen=True)
class SeaIceAlbedoFeedback:
    """Riihela et al. (2021)'s quantified Antarctic sea-ice albedo feedback trend."""

    expansion_era_w_m2_per_decade: float
    post_reversal_combined_w_m2: float
    pct_of_co2_forcing: float
    citation: dict[str, object]


FEEDBACK = SeaIceAlbedoFeedback(
    expansion_era_w_m2_per_decade=SEA_ICE_ALBEDO_FEEDBACK_1992_2015_W_M2_PER_DECADE,
    post_reversal_combined_w_m2=SEA_ICE_ALBEDO_FEEDBACK_2016_2018_COMBINED_W_M2,
    pct_of_co2_forcing=SEA_ICE_ALBEDO_FEEDBACK_PCT_OF_CO2_FORCING,
    citation=RIIHELAE_2021_CITATION,
)


def did_sea_ice_expansion_era_have_a_cooling_feedback() -> bool:
    """Whether 1992-2015 Antarctic sea-ice expansion produced a NEGATIVE
    (cooling) albedo-feedback trend. True -- the sign flipped only after
    the 2016-2018 sea-ice loss reversal."""
    return SEA_ICE_ALBEDO_FEEDBACK_1992_2015_W_M2_PER_DECADE < 0


def post_reversal_combined_feedback_w_m2() -> float:
    return SEA_ICE_ALBEDO_FEEDBACK_2016_2018_COMBINED_W_M2


def is_exposed_rock_albedo_a_quantified_antarctic_mechanism() -> bool:
    """Whether exposed-continental-bedrock albedo feedback (as opposed to
    sea-ice albedo) is an existing, quantified, Antarctica-specific
    finding in the literature.

    Always False as of this package's verification pass (2026-09-03) --
    searched for specifically and not found. This is an open research
    gap, not a citable result; do not conflate with the real, quantified
    sea-ice albedo mechanism above.
    """
    return False


def sea_ice_snowfall_note() -> str:
    return SEA_ICE_SNOWFALL_NOTE


KROMER_CITATION = KROMER_2023_CITATION
