"""ENSO (El Nino/La Nina) teleconnection to Antarctic ice.

Distinct from el-nino-amplification-utac (P118, ENSO strengthening
itself) and marine-heatwave-utac (P119, SE-Asia marine-heatwave/ENSO
coupling) -- neither of those packages touches Antarctica.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    AYABILAH_2026_CITATION,
    ENSO_BASAL_MELT_VS_SNOWFALL_RATIO,
    ENSO_CASCADE_NOTE,
    ENSO_TIMESCALE_ASYMMETRY_NOTE,
    PAOLO_2018_CITATION,
)


@dataclass(frozen=True)
class EnsoCompetingEffects:
    """Paolo et al. (2018)'s El Nino snowfall-gain-vs-basal-melt-loss competition."""

    basal_melt_vs_snowfall_ratio: float
    citation: dict[str, object]


COMPETING_EFFECTS = EnsoCompetingEffects(
    basal_melt_vs_snowfall_ratio=ENSO_BASAL_MELT_VS_SNOWFALL_RATIO,
    citation=PAOLO_2018_CITATION,
)


def does_el_nino_produce_net_ice_shelf_mass_gain() -> bool:
    """Whether El Nino's increased snowfall produces a net mass GAIN for
    Pacific-sector Antarctic ice shelves.

    Always False -- surface snowfall gain is real but submarine (basal)
    melting is roughly 5x larger during strong El Nino (Paolo et al.
    2018): 'the ocean ends up winning.' A competing-effects mechanism,
    not a single-direction cascade.
    """
    return False


def enso_cascade_note() -> str:
    return ENSO_CASCADE_NOTE


def does_west_antarctica_gain_mass_during_el_nino_on_enso_timescales() -> bool:
    """Whether West Antarctica gains mass during El Nino specifically on
    interannual (ENSO) timescales.

    True -- Ayabilah et al. (2026): surface-mass-balance/snowfall-driven
    gain during El Nino, loss during La Nina, via the Amundsen Sea Low.
    This is the OPPOSITE short-term sign of Davison et al. (2023)'s
    long-term (1997-2021), ocean-driven net basal-melt loss trend -- two
    different, non-contradictory timescales/mechanisms, not a
    contradiction of this package's core finding.
    """
    return True


AYABILAH_2026 = AYABILAH_2026_CITATION


def enso_timescale_asymmetry_note() -> str:
    return ENSO_TIMESCALE_ASYMMETRY_NOTE
