"""CMIP6 regional East/West Antarctic asymmetry -- Muilwijk et al. (2026).

The honesty-check module for this package: a standardized meltwater
perturbation applied across 10 CMIP6 models produces OPPOSITE-SIGN
responses in East vs. West Antarctica. This directly complicates any
simple "meltwater feedback accelerates melting everywhere" reading of
the Holocene mechanism in holocene_feedback_mechanism.py.
"""

from __future__ import annotations

from .constants import (
    CMIP6_MODEL_COUNT,
    EAST_ANTARCTIC_END_CENTURY_WARMING_RANGE_C,
    EAST_ANTARCTIC_MEDIAN_WARMING_RANGE_C,
    MELTWATER_PERTURBATION_SV,
    WEST_ANTARCTIC_ANOMALY_RANGE_C,
    WEST_ANTARCTIC_REGIONS,
)


def cmip6_model_count() -> int:
    return CMIP6_MODEL_COUNT


def meltwater_perturbation_sv() -> float:
    return MELTWATER_PERTURBATION_SV


def east_antarctic_median_warming_range_c() -> tuple[float, float]:
    return EAST_ANTARCTIC_MEDIAN_WARMING_RANGE_C


def east_antarctic_end_century_warming_range_c() -> tuple[float, float]:
    """Projected East Antarctic shelf-temperature warming by end of
    century under SSP5-8.5, in the meltwater-feedback-amplified regions."""
    return EAST_ANTARCTIC_END_CENTURY_WARMING_RANGE_C


def west_antarctic_anomaly_range_c() -> tuple[float, float]:
    """Amundsen/Bellingshausen Sea sector temperature anomaly under the
    same standardized meltwater perturbation -- negative (cooling/
    suppressed warming), not amplified warming."""
    return WEST_ANTARCTIC_ANOMALY_RANGE_C


def west_antarctic_regions() -> tuple[str, ...]:
    return WEST_ANTARCTIC_REGIONS


def do_east_and_west_responses_share_the_same_sign() -> bool:
    """Whether the East Antarctic (amplifying) and West Antarctic
    (suppressing) meltwater-feedback responses point the same direction.

    They do NOT -- this is the paper's central finding, and directly
    complicates a naive reading of the Holocene feedback mechanism as
    "meltwater always accelerates melting." Always False.
    """
    east_low, _east_high = EAST_ANTARCTIC_MEDIAN_WARMING_RANGE_C
    west_low, _west_high = WEST_ANTARCTIC_ANOMALY_RANGE_C
    east_sign_positive = east_low > 0
    west_sign_positive = west_low > 0
    return east_sign_positive == west_sign_positive
