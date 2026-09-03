from __future__ import annotations

from antarctic_ice_shelf_utac import (
    AYABILAH_2026,
    BALLENY_EARTHQUAKE,
    COMPETING_EFFECTS,
    CONCENTRATION,
    DAVISON_2023_CITATION,
    DEBRIS_FLOW_EVIDENCE,
    FEEDBACK,
    HOLOCENE_FEEDBACK_CITATION,
    ICEQUAKE_RECORD,
    KING_2023,
    KROMER_CITATION,
    LAKE_INVENTORY,
    LIM_2019,
    LIPOVSKY_2016,
    MUILWIJK_2026_CITATION,
    PACKAGE_ID,
    RIVER_SYSTEM,
    SAM_BASAL_MELT,
    SEASONAL_PATTERN,
    __version__,
    annual_mass_loss_rate_tonnes,
    antarctic_vortex_note,
    average_annual_rate_matches_total_over_period,
    basal_melt_dominant_fraction_pct,
    black_carbon_antarctica_note,
    can_extreme_wildfire_events_override_the_local_emissions_baseline,
    cmip6_model_count,
    did_sea_ice_expansion_era_have_a_cooling_feedback,
    do_east_and_west_responses_share_the_same_sign,
    documented_sudden_stratospheric_warming_years,
    does_basal_water_pressure_have_a_single_universal_speedup_relationship,
    does_el_nino_produce_net_ice_shelf_mass_gain,
    does_gia_seismicity_amplify_ice_sheet_collapse,
    does_this_module_claim_current_active_cascade,
    does_vortex_weakening_export_cold_air_to_mid_latitudes,
    does_west_antarctica_gain_mass_during_el_nino_on_enso_timescales,
    east_antarctic_end_century_warming_range_c,
    east_antarctic_median_warming_range_c,
    east_vs_west_lake_count,
    enso_cascade_note,
    enso_timescale_asymmetry_note,
    feedback_mechanism_description,
    holocene_event_years_before_present,
    is_antarctic_bc_comparable_in_magnitude_to_arctic,
    is_antarctic_rockfall_trend_as_well_quantified_as_the_alps,
    is_east_antarctica_lake_count_higher,
    is_exposed_rock_albedo_a_quantified_antarctic_mechanism,
    is_icequake_recurrence_tidally_modulated,
    is_local_or_long_range_transport_the_dominant_source,
    is_loss_uniform_east_vs_west,
    is_meltwater_feedback_self_reinforcing,
    is_sam_ice_response_regionally_uniform,
    known_inventory_growth_pct,
    meltwater_perturbation_sv,
    pct_shelves_losing_mass,
    pct_shelves_losing_more_than_30pct_of_mass,
    post_reversal_combined_feedback_w_m2,
    sam_basal_mass_loss_per_sd_gt_yr,
    sam_enso_dominant_decadal_drivers_note,
    sea_ice_snowfall_note,
    seismic_ice_note,
    shelf_outcome_breakdown,
    statistically_significant_loss_fraction,
    subglacial_hydrology_note,
    total_mass_loss_tonnes,
    west_antarctic_anomaly_range_c,
    west_antarctic_regions,
)


def test_version() -> None:
    assert __version__ == "2.0.0"


def test_package_id() -> None:
    assert PACKAGE_ID == 120


def test_citation_dois_and_titles() -> None:
    assert DAVISON_2023_CITATION["doi"] == "10.1126/sciadv.adi0186"
    assert MUILWIJK_2026_CITATION["doi"] == "10.5194/tc-20-1087-2026"
    assert HOLOCENE_FEEDBACK_CITATION["journal"] == "Nature Geoscience"


def test_mass_budget_percentages() -> None:
    assert pct_shelves_losing_mass() == 43.8  # 71/162
    assert pct_shelves_losing_more_than_30pct_of_mass() == 29.6  # 48/162


def test_shelf_outcome_breakdown_sums_to_total() -> None:
    breakdown = shelf_outcome_breakdown()
    assert sum(breakdown.values()) == 162
    assert breakdown["lost_mass"] == 71
    assert breakdown["gained_mass"] == 29
    assert breakdown["no_significant_change"] == 62


def test_statistically_significant_fraction() -> None:
    frac = statistically_significant_loss_fraction()
    assert 0.0 < frac <= 1.0
    assert frac == round(68 / 71, 3)


def test_total_and_annual_mass_loss_consistent() -> None:
    assert total_mass_loss_tonnes() == 8.3e12
    assert annual_mass_loss_rate_tonnes() == 3.3e11
    assert average_annual_rate_matches_total_over_period() is True


def test_basal_melt_is_dominant() -> None:
    assert basal_melt_dominant_fraction_pct() == 68.0


def test_loss_is_not_uniform_east_vs_west() -> None:
    assert is_loss_uniform_east_vs_west() is False


def test_holocene_feedback_mechanism() -> None:
    assert holocene_event_years_before_present() == 9000
    assert "meltwater" in feedback_mechanism_description()
    assert is_meltwater_feedback_self_reinforcing() is True


def test_holocene_module_does_not_overclaim_present_state() -> None:
    assert does_this_module_claim_current_active_cascade() is False


def test_cmip6_regional_asymmetry() -> None:
    assert cmip6_model_count() == 10
    assert meltwater_perturbation_sv() == 0.1

    east_low, east_high = east_antarctic_median_warming_range_c()
    assert east_low > 0 and east_high > 0

    west_low, west_high = west_antarctic_anomaly_range_c()
    assert west_low < 0 and west_high < 0

    assert "Amundsen Sea" in west_antarctic_regions()


def test_end_century_projection_exceeds_median() -> None:
    median_low, median_high = east_antarctic_median_warming_range_c()
    end_low, end_high = east_antarctic_end_century_warming_range_c()
    assert end_low >= median_low
    assert end_high >= median_high


def test_east_west_responses_have_opposite_signs() -> None:
    # The paper's central finding, and this package's honesty check.
    assert do_east_and_west_responses_share_the_same_sign() is False


# --- subglacial_hydrology.py (v2.0.0) ----------------------------------


def test_lake_inventory_values() -> None:
    assert LAKE_INVENTORY.newly_detected == 85
    assert LAKE_INVENTORY.known_before == 146
    assert LAKE_INVENTORY.known_after == 231
    assert LAKE_INVENTORY.median_drainage_time_years == 2.2
    assert LAKE_INVENTORY.median_recharge_time_years == 3.5
    assert LAKE_INVENTORY.near_grounding_zone_count == 6
    assert LAKE_INVENTORY.citation["doi"] == "10.1038/s41467-025-63773-9"


def test_known_inventory_growth_pct() -> None:
    assert known_inventory_growth_pct() == round(100.0 * 85 / 146, 1)


def test_east_vs_west_lake_count_and_dominance() -> None:
    counts = east_vs_west_lake_count()
    assert counts == {"east_antarctica": 73, "west_antarctica": 12}
    assert is_east_antarctica_lake_count_higher() is True


def test_river_system_values() -> None:
    assert RIVER_SYSTEM.length_km == 460
    assert RIVER_SYSTEM.high_pressure_flux_m3_s == 24.0
    assert RIVER_SYSTEM.citation["doi"] == "10.1038/s41561-022-01059-1"


def test_no_universal_basal_water_speedup_relationship_claimed() -> None:
    assert does_basal_water_pressure_have_a_single_universal_speedup_relationship() is False
    assert "grounding zone" in subglacial_hydrology_note()


# --- southern_annular_mode.py (v2.0.0) ---------------------------------


def test_documented_ssw_years() -> None:
    assert documented_sudden_stratospheric_warming_years() == (2002, 2019)


def test_vortex_does_not_export_cold_air() -> None:
    # The Arctic analogy does not transfer -- 2019 produced hot/dry
    # conditions in Australia, not a cold outbreak.
    assert does_vortex_weakening_export_cold_air_to_mid_latitudes() is False
    assert "Australia" in antarctic_vortex_note()
    assert LIM_2019["year"] == 2019
    assert KING_2023["doi"] == "10.1038/s41561-023-01317-w"


def test_sam_basal_melt_values() -> None:
    assert SAM_BASAL_MELT.mass_loss_per_sd_gt_yr == 40.0
    assert SAM_BASAL_MELT.citation["doi"] == "10.1038/s43247-022-00458-x"
    assert sam_basal_mass_loss_per_sd_gt_yr() == 40.0


def test_sam_response_not_regionally_uniform() -> None:
    assert is_sam_ice_response_regionally_uniform() is False


def test_sam_enso_dominant_drivers_note_mentions_amundsen_caveat() -> None:
    assert "Amundsen" in sam_enso_dominant_decadal_drivers_note()


# --- sea_ice_albedo_feedback.py (v2.0.0) --------------------------------


def test_feedback_values() -> None:
    assert FEEDBACK.expansion_era_w_m2_per_decade == -0.06
    assert FEEDBACK.post_reversal_combined_w_m2 == 0.26
    assert FEEDBACK.pct_of_co2_forcing == 10.0
    assert FEEDBACK.citation["doi"] == "10.1038/s41561-021-00841-x"


def test_expansion_era_was_cooling() -> None:
    assert did_sea_ice_expansion_era_have_a_cooling_feedback() is True
    assert post_reversal_combined_feedback_w_m2() == 0.26


def test_exposed_rock_albedo_not_a_quantified_mechanism() -> None:
    # Deliberate honesty check: searched for and not found.
    assert is_exposed_rock_albedo_a_quantified_antarctic_mechanism() is False
    assert KROMER_CITATION["doi"] == "10.1029/2023GL104436"
    assert "open research gap" in sea_ice_snowfall_note()


# --- seismic_ice_interactions.py (v2.0.0) -------------------------------


def test_icequake_record_values() -> None:
    assert ICEQUAKE_RECORD.events_in_record == 20000
    assert ICEQUAKE_RECORD.recurrence_minutes == 25
    assert ICEQUAKE_RECORD.large_slip_events_per_day == 2.0
    assert ICEQUAKE_RECORD.citation["doi"] == "10.1038/nature06990"
    assert LIPOVSKY_2016["doi"] == "10.5194/tc-10-385-2016"


def test_icequakes_are_tidally_modulated() -> None:
    assert is_icequake_recurrence_tidally_modulated() is True


def test_debris_flow_evidence_values() -> None:
    assert DEBRIS_FLOW_EVIDENCE.location == "Potter Peninsula, King George Island"
    assert DEBRIS_FLOW_EVIDENCE.documented_since_year == 1956


def test_antarctic_rockfall_not_as_quantified_as_alps() -> None:
    assert is_antarctic_rockfall_trend_as_well_quantified_as_the_alps() is False


def test_balleny_earthquake_values() -> None:
    assert BALLENY_EARTHQUAKE.year == 1998
    assert BALLENY_EARTHQUAKE.magnitude_mw == 8.1
    assert BALLENY_EARTHQUAKE.citation["doi"] == "10.1186/BF03351621"


def test_gia_seismicity_does_not_amplify_collapse() -> None:
    assert does_gia_seismicity_amplify_ice_sheet_collapse() is False
    assert "STABILIZING" in seismic_ice_note()


# --- black_carbon_deposition.py (v2.0.0) --------------------------------


def test_concentration_values() -> None:
    assert CONCENTRATION.background_ng_g == 1.0
    assert CONCENTRATION.near_station_ng_g_range == (2.0, 4.0)
    assert CONCENTRATION.extra_snowpack_loss_kg_m2_range == (5.0, 23.0)
    assert CONCENTRATION.citation["doi"] == "10.1038/s41467-022-28560-w"


def test_local_emissions_dominate() -> None:
    assert is_local_or_long_range_transport_the_dominant_source() == "local"


def test_seasonal_pattern_values() -> None:
    assert SEASONAL_PATTERN.seasonal_range_ng_g == (0.01, 3.73)
    assert SEASONAL_PATTERN.albedo_reduction_pct == 0.4
    assert SEASONAL_PATTERN.radiative_forcing_increase_w_m2 == 0.6
    assert SEASONAL_PATTERN.citation["doi"] == "10.1126/sciadv.adp1682"


def test_wildfires_can_override_baseline() -> None:
    assert can_extreme_wildfire_events_override_the_local_emissions_baseline() is True


def test_antarctic_bc_smaller_than_arctic() -> None:
    assert is_antarctic_bc_comparable_in_magnitude_to_arctic() is False
    assert "P105" in black_carbon_antarctica_note()


# --- enso_teleconnection.py (v2.0.0) -------------------------------------


def test_competing_effects_values() -> None:
    assert COMPETING_EFFECTS.basal_melt_vs_snowfall_ratio == 5.0
    assert COMPETING_EFFECTS.citation["doi"] == "10.1038/s41561-017-0033-0"


def test_el_nino_does_not_produce_net_mass_gain() -> None:
    assert does_el_nino_produce_net_ice_shelf_mass_gain() is False
    assert "ocean ends up winning" in enso_cascade_note()


def test_west_antarctica_gains_mass_during_el_nino_short_term() -> None:
    assert does_west_antarctica_gain_mass_during_el_nino_on_enso_timescales() is True
    assert AYABILAH_2026["doi"] == "10.5194/tc-20-1237-2026"
    assert "not a contradiction" in enso_timescale_asymmetry_note()
