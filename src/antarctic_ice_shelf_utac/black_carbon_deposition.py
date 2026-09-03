"""Black carbon (soot) deposition on Antarctic snow/ice.

A different geographic dataset than black-carbon-albedo-utac (P105),
which covers the Tibetan Plateau/Himalaya exclusively -- no overlap.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    BC_ALBEDO_REDUCTION_PCT,
    BC_ANTARCTIC_BACKGROUND_NG_G,
    BC_ANTARCTIC_EXTRA_SNOWPACK_LOSS_KG_M2_RANGE,
    BC_ANTARCTIC_NEAR_STATION_NG_G_RANGE,
    BC_ANTARCTIC_SEASONAL_RANGE_NG_G,
    BC_RADIATIVE_FORCING_INCREASE_W_M2,
    BLACK_CARBON_ANTARCTICA_NOTE,
    CORDERO_2022_CITATION,
    MAGALHAES_2024_CITATION,
)


@dataclass(frozen=True)
class BlackCarbonConcentration:
    """Cordero et al. (2022)'s measured Antarctic BC concentration levels."""

    background_ng_g: float
    near_station_ng_g_range: tuple[float, float]
    extra_snowpack_loss_kg_m2_range: tuple[float, float]
    citation: dict[str, object]


CONCENTRATION = BlackCarbonConcentration(
    background_ng_g=BC_ANTARCTIC_BACKGROUND_NG_G,
    near_station_ng_g_range=BC_ANTARCTIC_NEAR_STATION_NG_G_RANGE,
    extra_snowpack_loss_kg_m2_range=BC_ANTARCTIC_EXTRA_SNOWPACK_LOSS_KG_M2_RANGE,
    citation=CORDERO_2022_CITATION,
)


def is_local_or_long_range_transport_the_dominant_source() -> str:
    """Cordero et al. (2022)'s attribution finding: local emissions
    (research-station diesel generators, ships, aircraft) dominate BC at
    most measured sites -- a real, counterintuitive result versus the
    naive 'imported wildfire smoke' assumption."""
    return "local"


@dataclass(frozen=True)
class SeasonalBlackCarbonPattern:
    """Magalhaes et al. (2024)'s seasonal BC / tourism / wildfire pattern."""

    seasonal_range_ng_g: tuple[float, float]
    albedo_reduction_pct: float
    radiative_forcing_increase_w_m2: float
    citation: dict[str, object]


SEASONAL_PATTERN = SeasonalBlackCarbonPattern(
    seasonal_range_ng_g=BC_ANTARCTIC_SEASONAL_RANGE_NG_G,
    albedo_reduction_pct=BC_ALBEDO_REDUCTION_PCT,
    radiative_forcing_increase_w_m2=BC_RADIATIVE_FORCING_INCREASE_W_M2,
    citation=MAGALHAES_2024_CITATION,
)


def can_extreme_wildfire_events_override_the_local_emissions_baseline() -> bool:
    """Whether an extreme remote wildfire event can push BC deposition
    above the normally local-emissions-dominated baseline.

    True -- the 2019-2020 Australian megafires temporarily overrode the
    tourism-driven baseline (Magalhaes et al. 2024). This does NOT
    contradict Cordero et al. 2022's "local emissions dominate on
    average" finding -- both are kept as an explicit honesty-check
    nuance, not smoothed into one story.
    """
    return True


def is_antarctic_bc_comparable_in_magnitude_to_arctic() -> bool:
    """Whether Antarctic BC concentrations match Arctic/Himalayan levels.

    Always False -- background Antarctic BC (<1 ng/g) is roughly an
    order of magnitude below Arctic snow. Real and measurable, but a
    smaller-magnitude effect than the Arctic case.
    """
    return False


def black_carbon_antarctica_note() -> str:
    return BLACK_CARBON_ANTARCTICA_NOTE
