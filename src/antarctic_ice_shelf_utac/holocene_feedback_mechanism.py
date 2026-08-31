"""Holocene meltwater-release feedback -- Nature Geoscience 2025.

A real, self-reinforcing feedback loop documented from sediment records
and ocean-climate modeling of an ice-shelf collapse ~9000 years ago:
meltwater strengthens ocean stratification, which enhances warm
deep-water inflow, which accelerates basal melting, which releases more
meltwater. This module documents that historical mechanism -- it does
not claim the modern system is currently in this exact cascading state,
only that the mechanism is real and demonstrated.
"""

from __future__ import annotations

from .constants import HOLOCENE_EVENT_YEARS_BP, HOLOCENE_FEEDBACK_MECHANISM


def holocene_event_years_before_present() -> int:
    return HOLOCENE_EVENT_YEARS_BP


def feedback_mechanism_description() -> str:
    return HOLOCENE_FEEDBACK_MECHANISM


def is_meltwater_feedback_self_reinforcing() -> bool:
    """Whether the documented mechanism is a positive (self-reinforcing)
    feedback loop, per the source paper -- not a self-limiting one."""
    return "self-reinforcing" in HOLOCENE_FEEDBACK_MECHANISM


def does_this_module_claim_current_active_cascade() -> bool:
    """Whether this module asserts the modern Antarctic system is
    currently undergoing this exact cascading collapse. Always False --
    the cited paper documents a real historical (~9000 BP) mechanism as
    evidence that such cascades are physically possible, not a claim
    about present-day state. See mass_budget_1997_2021.py and
    regional_asymmetry_cmip6.py for what the modern/projected record
    actually shows (a real but regionally uneven trend, not a runaway
    cascade)."""
    return False
