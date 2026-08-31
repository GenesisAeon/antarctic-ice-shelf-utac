"""antarctic-ice-shelf-utac -- real Antarctic ice shelf mass loss, mechanism, and asymmetry.

GenesisAeon Package 120. Surfaced via a broad DeepResearch pass
(2026-08-31) on El Nino/ENSO and climate topics, alongside
el-nino-amplification-utac (P118) and marine-heatwave-utac (P119).

Davison et al. (2023, Science Advances): observed mass budget of all
162 Antarctic ice shelves, 1997-2021 -- 71 lost mass (48 lost >30% of
initial mass), 29 gained, 62 no significant change; 8.3 trillion tonnes
lost total; basal melting the dominant driver (68%); a real West-loses/
East-stable-or-gains asymmetry, not a uniform continental trend.

A 2025 Nature Geoscience paper documents a real, self-reinforcing
meltwater-release feedback mechanism from a ~9000-year-old Holocene
ice-shelf collapse -- included as evidence the mechanism is physically
real, not as a claim about the present-day system's state.

Muilwijk et al. (2026, The Cryosphere): 10 CMIP6 models under a
standardized meltwater perturbation show OPPOSITE-SIGN regional
responses -- East Antarctica's feedback amplifies warming/melting,
West Antarctica (Amundsen/Bellingshausen) shows cooling/suppressed
warming. This directly complicates a naive "meltwater always
accelerates melting everywhere" reading of the Holocene mechanism --
this package's honesty-check module.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

All citations independently verified via direct WebFetch on
publisher pages, 2026-08-31.
"""

from .constants import (
    DAVISON_2023_CITATION,
    HOLOCENE_FEEDBACK_CITATION,
    MUILWIJK_2026_CITATION,
    PACKAGE_ID,
)
from .holocene_feedback_mechanism import (
    does_this_module_claim_current_active_cascade,
    feedback_mechanism_description,
    holocene_event_years_before_present,
    is_meltwater_feedback_self_reinforcing,
)
from .mass_budget_1997_2021 import (
    annual_mass_loss_rate_tonnes,
    average_annual_rate_matches_total_over_period,
    basal_melt_dominant_fraction_pct,
    is_loss_uniform_east_vs_west,
    pct_shelves_losing_mass,
    pct_shelves_losing_more_than_30pct_of_mass,
    shelf_outcome_breakdown,
    statistically_significant_loss_fraction,
    total_mass_loss_tonnes,
)
from .regional_asymmetry_cmip6 import (
    cmip6_model_count,
    do_east_and_west_responses_share_the_same_sign,
    east_antarctic_end_century_warming_range_c,
    east_antarctic_median_warming_range_c,
    meltwater_perturbation_sv,
    west_antarctic_anomaly_range_c,
    west_antarctic_regions,
)

__version__ = "1.0.1"

__all__ = [
    "DAVISON_2023_CITATION",
    "HOLOCENE_FEEDBACK_CITATION",
    "MUILWIJK_2026_CITATION",
    "PACKAGE_ID",
    "annual_mass_loss_rate_tonnes",
    "average_annual_rate_matches_total_over_period",
    "basal_melt_dominant_fraction_pct",
    "cmip6_model_count",
    "do_east_and_west_responses_share_the_same_sign",
    "does_this_module_claim_current_active_cascade",
    "east_antarctic_end_century_warming_range_c",
    "east_antarctic_median_warming_range_c",
    "feedback_mechanism_description",
    "holocene_event_years_before_present",
    "is_loss_uniform_east_vs_west",
    "is_meltwater_feedback_self_reinforcing",
    "meltwater_perturbation_sv",
    "pct_shelves_losing_mass",
    "pct_shelves_losing_more_than_30pct_of_mass",
    "shelf_outcome_breakdown",
    "statistically_significant_loss_fraction",
    "total_mass_loss_tonnes",
    "west_antarctic_anomaly_range_c",
    "west_antarctic_regions",
]
