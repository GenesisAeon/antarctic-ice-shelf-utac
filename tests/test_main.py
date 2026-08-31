from __future__ import annotations

from antarctic_ice_shelf_utac import (
    DAVISON_2023_CITATION,
    HOLOCENE_FEEDBACK_CITATION,
    MUILWIJK_2026_CITATION,
    PACKAGE_ID,
    annual_mass_loss_rate_tonnes,
    average_annual_rate_matches_total_over_period,
    basal_melt_dominant_fraction_pct,
    cmip6_model_count,
    do_east_and_west_responses_share_the_same_sign,
    does_this_module_claim_current_active_cascade,
    east_antarctic_end_century_warming_range_c,
    east_antarctic_median_warming_range_c,
    feedback_mechanism_description,
    holocene_event_years_before_present,
    is_loss_uniform_east_vs_west,
    is_meltwater_feedback_self_reinforcing,
    meltwater_perturbation_sv,
    pct_shelves_losing_mass,
    pct_shelves_losing_more_than_30pct_of_mass,
    shelf_outcome_breakdown,
    statistically_significant_loss_fraction,
    total_mass_loss_tonnes,
    west_antarctic_anomaly_range_c,
    west_antarctic_regions,
)


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
