"""Subglacial (under-grounded-ice) meltwater hydrology -- Wilson et al.
(2025) and Dow et al. (2022).

Distinct from mass_budget_1997_2021.py's basal melting, which is
ocean-driven melt at the underside of FLOATING ice shelves. This module
covers water beneath the GROUNDED ice sheet itself (subglacial lakes,
drainage, and basal lubrication) -- a physically different process.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    DOW_2022_CITATION,
    SUBGLACIAL_HYDROLOGY_NOTE,
    SUBGLACIAL_LAKES_EAST_ANTARCTICA_COUNT,
    SUBGLACIAL_LAKES_KNOWN_AFTER,
    SUBGLACIAL_LAKES_KNOWN_BEFORE,
    SUBGLACIAL_LAKES_MEDIAN_DRAINAGE_TIME_YEARS,
    SUBGLACIAL_LAKES_MEDIAN_RECHARGE_TIME_YEARS,
    SUBGLACIAL_LAKES_NEAR_GROUNDING_ZONE_COUNT,
    SUBGLACIAL_LAKES_NEWLY_DETECTED,
    SUBGLACIAL_LAKES_STUDY_PERIOD_YEARS,
    SUBGLACIAL_LAKES_WEST_ANTARCTICA_COUNT,
    SUBGLACIAL_RIVER_HIGH_PRESSURE_FLUX_M3_S,
    SUBGLACIAL_RIVER_SYSTEM_LENGTH_KM,
    WILSON_2025_CITATION,
)


@dataclass(frozen=True)
class SubglacialLakeInventory:
    """Wilson et al. (2025)'s CryoSat-2-based active subglacial lake inventory."""

    newly_detected: int
    known_before: int
    known_after: int
    study_period_years: tuple[int, int]
    median_drainage_time_years: float
    median_recharge_time_years: float
    near_grounding_zone_count: int
    citation: dict[str, object]


LAKE_INVENTORY = SubglacialLakeInventory(
    newly_detected=SUBGLACIAL_LAKES_NEWLY_DETECTED,
    known_before=SUBGLACIAL_LAKES_KNOWN_BEFORE,
    known_after=SUBGLACIAL_LAKES_KNOWN_AFTER,
    study_period_years=SUBGLACIAL_LAKES_STUDY_PERIOD_YEARS,
    median_drainage_time_years=SUBGLACIAL_LAKES_MEDIAN_DRAINAGE_TIME_YEARS,
    median_recharge_time_years=SUBGLACIAL_LAKES_MEDIAN_RECHARGE_TIME_YEARS,
    near_grounding_zone_count=SUBGLACIAL_LAKES_NEAR_GROUNDING_ZONE_COUNT,
    citation=WILSON_2025_CITATION,
)


def known_inventory_growth_pct() -> float:
    """How much the known active-lake inventory grew from this single decade of data."""
    return round(
        100.0 * SUBGLACIAL_LAKES_NEWLY_DETECTED / SUBGLACIAL_LAKES_KNOWN_BEFORE, 1
    )


def east_vs_west_lake_count() -> dict[str, int]:
    """Regional split of the known active lakes -- East Antarctica dominates by count."""
    return {
        "east_antarctica": SUBGLACIAL_LAKES_EAST_ANTARCTICA_COUNT,
        "west_antarctica": SUBGLACIAL_LAKES_WEST_ANTARCTICA_COUNT,
    }


def is_east_antarctica_lake_count_higher() -> bool:
    """East Antarctica has more known active subglacial lakes than West --
    a separate regional pattern from the mass-budget East/West asymmetry,
    not to be conflated with it (more lakes does not mean more mass loss;
    East Antarctica is the mass-budget-stable region)."""
    return SUBGLACIAL_LAKES_EAST_ANTARCTICA_COUNT > SUBGLACIAL_LAKES_WEST_ANTARCTICA_COUNT


@dataclass(frozen=True)
class SubglacialRiverSystem:
    """Dow et al. (2022)'s high-pressure dendritic subglacial river system."""

    length_km: float
    high_pressure_flux_m3_s: float
    citation: dict[str, object]


RIVER_SYSTEM = SubglacialRiverSystem(
    length_km=SUBGLACIAL_RIVER_SYSTEM_LENGTH_KM,
    high_pressure_flux_m3_s=SUBGLACIAL_RIVER_HIGH_PRESSURE_FLUX_M3_S,
    citation=DOW_2022_CITATION,
)


def does_basal_water_pressure_have_a_single_universal_speedup_relationship() -> bool:
    """Whether basal water pressure has one clean, universal relationship
    to ice-flow speedup across all of Antarctica.

    Always False -- the mechanism (water lubricates the bed, plausibly
    enabling faster flow) is real and documented, but this package does
    not assert a single universal quantitative relationship, and does
    NOT cite the unverified grounding-zone-breakdown claim as fact. See
    SUBGLACIAL_HYDROLOGY_NOTE for what is and is not established.
    """
    return False


def subglacial_hydrology_note() -> str:
    return SUBGLACIAL_HYDROLOGY_NOTE
