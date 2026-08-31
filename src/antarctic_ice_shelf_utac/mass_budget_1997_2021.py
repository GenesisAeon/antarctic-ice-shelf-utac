"""Observed Antarctic ice shelf mass budget, 1997-2021 -- Davison et al. (2023).
"""

from __future__ import annotations

from .constants import (
    ANNUAL_MASS_LOSS_RATE_TONNES,
    BASAL_MELT_DOMINANT_FRACTION_PCT,
    EAST_ANTARCTICA_TREND,
    SHELVES_GAINED_MASS,
    SHELVES_LOST_MASS,
    SHELVES_LOST_MASS_STATISTICALLY_SIGNIFICANT,
    SHELVES_LOST_MORE_THAN_30PCT,
    SHELVES_NO_SIGNIFICANT_CHANGE,
    STUDY_PERIOD_YEARS,
    TOTAL_ICE_SHELVES_STUDIED,
    TOTAL_MASS_LOST_TONNES,
    WEST_ANTARCTICA_TREND,
)


def pct_shelves_losing_mass() -> float:
    """Percentage of the 162 studied ice shelves that lost mass, 1997-2021."""
    return round(100.0 * SHELVES_LOST_MASS / TOTAL_ICE_SHELVES_STUDIED, 1)


def pct_shelves_losing_more_than_30pct_of_mass() -> float:
    """Percentage of shelves that lost more than 30% of their initial mass."""
    return round(100.0 * SHELVES_LOST_MORE_THAN_30PCT / TOTAL_ICE_SHELVES_STUDIED, 1)


def shelf_outcome_breakdown() -> dict[str, int]:
    """(lost mass, gained mass, no significant change) counts, summing to 162."""
    breakdown = {
        "lost_mass": SHELVES_LOST_MASS,
        "gained_mass": SHELVES_GAINED_MASS,
        "no_significant_change": SHELVES_NO_SIGNIFICANT_CHANGE,
    }
    assert sum(breakdown.values()) == TOTAL_ICE_SHELVES_STUDIED
    return breakdown


def statistically_significant_loss_fraction() -> float:
    """Fraction of the mass-losing shelves whose negative trend was
    statistically significant (not all 71 were)."""
    return round(SHELVES_LOST_MASS_STATISTICALLY_SIGNIFICANT / SHELVES_LOST_MASS, 3)


def total_mass_loss_tonnes() -> float:
    return TOTAL_MASS_LOST_TONNES


def annual_mass_loss_rate_tonnes() -> float:
    return ANNUAL_MASS_LOSS_RATE_TONNES


def average_annual_rate_matches_total_over_period(tolerance_pct: float = 5.0) -> bool:
    """Sanity check: annual_rate * period_years should approximate the
    total loss within a reasonable tolerance (this is an average rate
    over a noisy multi-year record, not an exact identity)."""
    implied_total = ANNUAL_MASS_LOSS_RATE_TONNES * STUDY_PERIOD_YEARS
    deviation_pct = 100.0 * abs(implied_total - TOTAL_MASS_LOST_TONNES) / TOTAL_MASS_LOST_TONNES
    return deviation_pct <= tolerance_pct


def basal_melt_dominant_fraction_pct() -> float:
    """Percentage of the mass loss attributable to basal (underside) melting."""
    return BASAL_MELT_DOMINANT_FRACTION_PCT


def is_loss_uniform_east_vs_west() -> bool:
    """Whether the East and West Antarctic trends are the same.

    They are NOT: West Antarctica predominantly lost mass, East
    Antarctica predominantly stayed stable or gained. Always False --
    this package does not claim a single continent-wide trend.
    """
    return WEST_ANTARCTICA_TREND == EAST_ANTARCTICA_TREND
