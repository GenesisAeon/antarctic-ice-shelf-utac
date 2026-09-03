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

v2.0.0 (2026-09-03): six new mechanisms, following a Johann brainstorm
prompted by a coral-reef article -- researched via six parallel
independent verification passes, each citation individually confirmed:
subglacial hydrology (Wilson et al. 2025, Dow et al. 2022 -- a
physically distinct process from ice-shelf basal melt above), the
Southern Annular Mode / stratospheric polar vortex (Lim et al. 2019,
Verfaillie et al. 2022, King et al. 2023 -- the Arctic "vortex
instability exports cold air" analogy does NOT transfer, see
southern_annular_mode.py), sea-ice albedo feedback (Riihela et al.
2021 -- explicitly NOT exposed-rock albedo, which was searched for and
not found as a quantified Antarctica-specific result), seismic-ice
interactions (Wiens et al. 2008, Lipovsky & Dunham 2016, Heredia Barion
et al. 2023, Tsuboi et al. 2000), black carbon deposition (Cordero et
al. 2022, Magalhaes et al. 2024 -- a different geography than
black-carbon-albedo-utac/P105's Tibetan Plateau focus, no overlap),
and ENSO teleconnection (Paolo et al. 2018, Ayabilah et al. 2026 -- a
real, deliberate honesty-check tension with the package's own core
Davison 2023 finding, resolved as two different timescales, not a
contradiction).
"""

from .black_carbon_deposition import (
    CONCENTRATION,
    SEASONAL_PATTERN,
    BlackCarbonConcentration,
    SeasonalBlackCarbonPattern,
    black_carbon_antarctica_note,
    can_extreme_wildfire_events_override_the_local_emissions_baseline,
    is_antarctic_bc_comparable_in_magnitude_to_arctic,
    is_local_or_long_range_transport_the_dominant_source,
)
from .constants import (
    DAVISON_2023_CITATION,
    HOLOCENE_FEEDBACK_CITATION,
    MUILWIJK_2026_CITATION,
    PACKAGE_ID,
)
from .enso_teleconnection import (
    AYABILAH_2026,
    COMPETING_EFFECTS,
    EnsoCompetingEffects,
    does_el_nino_produce_net_ice_shelf_mass_gain,
    does_west_antarctica_gain_mass_during_el_nino_on_enso_timescales,
    enso_cascade_note,
    enso_timescale_asymmetry_note,
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
from .sea_ice_albedo_feedback import (
    FEEDBACK,
    KROMER_CITATION,
    SeaIceAlbedoFeedback,
    did_sea_ice_expansion_era_have_a_cooling_feedback,
    is_exposed_rock_albedo_a_quantified_antarctic_mechanism,
    post_reversal_combined_feedback_w_m2,
    sea_ice_snowfall_note,
)
from .seismic_ice_interactions import (
    BALLENY_EARTHQUAKE,
    DEBRIS_FLOW_EVIDENCE,
    ICEQUAKE_RECORD,
    LIPOVSKY_2016,
    BallenyGiaEarthquake,
    DeglaciationDebrisFlowEvidence,
    WhillansIcequakeRecord,
    does_gia_seismicity_amplify_ice_sheet_collapse,
    is_antarctic_rockfall_trend_as_well_quantified_as_the_alps,
    is_icequake_recurrence_tidally_modulated,
    seismic_ice_note,
)
from .southern_annular_mode import (
    KING_2023,
    LIM_2019,
    SAM_BASAL_MELT,
    SamBasalMeltResponse,
    antarctic_vortex_note,
    documented_sudden_stratospheric_warming_years,
    does_vortex_weakening_export_cold_air_to_mid_latitudes,
    is_sam_ice_response_regionally_uniform,
    sam_basal_mass_loss_per_sd_gt_yr,
    sam_enso_dominant_decadal_drivers_note,
)
from .subglacial_hydrology import (
    LAKE_INVENTORY,
    RIVER_SYSTEM,
    SubglacialLakeInventory,
    SubglacialRiverSystem,
    does_basal_water_pressure_have_a_single_universal_speedup_relationship,
    east_vs_west_lake_count,
    is_east_antarctica_lake_count_higher,
    known_inventory_growth_pct,
    subglacial_hydrology_note,
)

__version__ = "2.0.0"

__all__ = [
    "AYABILAH_2026",
    "BALLENY_EARTHQUAKE",
    "COMPETING_EFFECTS",
    "CONCENTRATION",
    "DAVISON_2023_CITATION",
    "DEBRIS_FLOW_EVIDENCE",
    "FEEDBACK",
    "HOLOCENE_FEEDBACK_CITATION",
    "ICEQUAKE_RECORD",
    "KING_2023",
    "KROMER_CITATION",
    "LAKE_INVENTORY",
    "LIM_2019",
    "LIPOVSKY_2016",
    "MUILWIJK_2026_CITATION",
    "PACKAGE_ID",
    "RIVER_SYSTEM",
    "SAM_BASAL_MELT",
    "SEASONAL_PATTERN",
    "BallenyGiaEarthquake",
    "BlackCarbonConcentration",
    "DeglaciationDebrisFlowEvidence",
    "EnsoCompetingEffects",
    "SamBasalMeltResponse",
    "SeaIceAlbedoFeedback",
    "SeasonalBlackCarbonPattern",
    "SubglacialLakeInventory",
    "SubglacialRiverSystem",
    "WhillansIcequakeRecord",
    "annual_mass_loss_rate_tonnes",
    "antarctic_vortex_note",
    "average_annual_rate_matches_total_over_period",
    "basal_melt_dominant_fraction_pct",
    "black_carbon_antarctica_note",
    "can_extreme_wildfire_events_override_the_local_emissions_baseline",
    "cmip6_model_count",
    "did_sea_ice_expansion_era_have_a_cooling_feedback",
    "do_east_and_west_responses_share_the_same_sign",
    "documented_sudden_stratospheric_warming_years",
    "does_basal_water_pressure_have_a_single_universal_speedup_relationship",
    "does_el_nino_produce_net_ice_shelf_mass_gain",
    "does_gia_seismicity_amplify_ice_sheet_collapse",
    "does_this_module_claim_current_active_cascade",
    "does_vortex_weakening_export_cold_air_to_mid_latitudes",
    "does_west_antarctica_gain_mass_during_el_nino_on_enso_timescales",
    "east_antarctic_end_century_warming_range_c",
    "east_antarctic_median_warming_range_c",
    "east_vs_west_lake_count",
    "enso_cascade_note",
    "enso_timescale_asymmetry_note",
    "feedback_mechanism_description",
    "holocene_event_years_before_present",
    "is_antarctic_bc_comparable_in_magnitude_to_arctic",
    "is_antarctic_rockfall_trend_as_well_quantified_as_the_alps",
    "is_east_antarctica_lake_count_higher",
    "is_exposed_rock_albedo_a_quantified_antarctic_mechanism",
    "is_icequake_recurrence_tidally_modulated",
    "is_local_or_long_range_transport_the_dominant_source",
    "is_loss_uniform_east_vs_west",
    "is_meltwater_feedback_self_reinforcing",
    "is_sam_ice_response_regionally_uniform",
    "known_inventory_growth_pct",
    "meltwater_perturbation_sv",
    "pct_shelves_losing_mass",
    "pct_shelves_losing_more_than_30pct_of_mass",
    "post_reversal_combined_feedback_w_m2",
    "sam_basal_mass_loss_per_sd_gt_yr",
    "sam_enso_dominant_decadal_drivers_note",
    "sea_ice_snowfall_note",
    "seismic_ice_note",
    "shelf_outcome_breakdown",
    "statistically_significant_loss_fraction",
    "subglacial_hydrology_note",
    "total_mass_loss_tonnes",
    "west_antarctic_anomaly_range_c",
    "west_antarctic_regions",
]
