"""Southern Annular Mode (SAM) / stratospheric polar vortex.

The real Antarctic analog to the Arctic polar-vortex story -- but the
"instability pushes cold air toward mid-latitudes" analogy does NOT
transfer. The honesty-check module for this addition.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    ANTARCTIC_SSW_DOCUMENTED_YEARS,
    ANTARCTIC_VORTEX_NOTE,
    KING_2023_CITATION,
    LIM_2019_CITATION,
    SAM_BASAL_MASS_LOSS_PER_SD_GT_YR,
    SAM_ENSO_ARE_DOMINANT_DECADAL_DRIVERS_NOTE,
    SAM_REGIONAL_NOTE,
    VERFAILLIE_2022_CITATION,
)

LIM_2019 = LIM_2019_CITATION
KING_2023 = KING_2023_CITATION


def documented_sudden_stratospheric_warming_years() -> tuple[int, int]:
    """The only two documented Antarctic SSW events -- rare, unlike the Arctic."""
    return ANTARCTIC_SSW_DOCUMENTED_YEARS


def does_vortex_weakening_export_cold_air_to_mid_latitudes() -> bool:
    """Whether a weakened Antarctic vortex pushes cold air toward
    mid-latitudes, mirroring the Arctic polar-vortex-disruption story.

    Always False -- the documented 2019 event produced the OPPOSITE
    effect: hot, dry conditions in southeastern Australia (Lim et al.
    2019), a real contributing driver of the 2019-2020 bushfires. The
    Arctic analogy does not transfer to the Southern Hemisphere.
    """
    return False


def antarctic_vortex_note() -> str:
    return ANTARCTIC_VORTEX_NOTE


@dataclass(frozen=True)
class SamBasalMeltResponse:
    """Verfaillie et al. (2022)'s SAM-to-basal-melt sensitivity."""

    mass_loss_per_sd_gt_yr: float
    regional_note: str
    citation: dict[str, object]


SAM_BASAL_MELT = SamBasalMeltResponse(
    mass_loss_per_sd_gt_yr=SAM_BASAL_MASS_LOSS_PER_SD_GT_YR,
    regional_note=SAM_REGIONAL_NOTE,
    citation=VERFAILLIE_2022_CITATION,
)


def sam_basal_mass_loss_per_sd_gt_yr() -> float:
    return SAM_BASAL_MASS_LOSS_PER_SD_GT_YR


def is_sam_ice_response_regionally_uniform() -> bool:
    """Whether a positive SAM increases basal melt uniformly across Antarctica.

    Always False -- Bellingshausen/Western Pacific sectors see increased
    melt, the Amundsen sector sees the opposite response (Verfaillie et
    al. 2022) -- another real regional asymmetry, parallel to this
    package's East/West mass-budget theme.
    """
    return False


def sam_enso_dominant_decadal_drivers_note() -> str:
    return SAM_ENSO_ARE_DOMINANT_DECADAL_DRIVERS_NOTE
