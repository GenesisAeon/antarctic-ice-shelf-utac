# antarctic-ice-shelf-utac

GenesisAeon Package 120 — real Antarctic ice shelf mass budget, a real
Holocene meltwater-release feedback mechanism, and a real, sign-flipped
regional asymmetry under CMIP6 projections. **Deliberately has no
UTAC/CREP/AFET bridge** — see [DISCLAIMER.md](DISCLAIMER.md).

For a plain-language explanation of the same topic (German, no jargon,
written for general audiences), see [WHITEPAPER.md](WHITEPAPER.md).

## Where this package came from

Built alongside `el-nino-amplification-utac` (P118) and
`marine-heatwave-utac` (P119) from a single broad DeepResearch pass
(2026-08-31). `cascading-tipping-utac` (P87) only references WAIS as
one node in a tipping-element network, not a standalone quantified
treatment — this package fills that gap.

## What's real here

- **Davison et al. (2023, *Science Advances*)** — of 162 Antarctic ice
  shelves studied 1997-2021, **71 lost mass** (48 lost more than 30% of
  their initial mass), 29 gained, 62 showed no significant change.
  Total loss: **8.3 trillion tonnes**. Basal melting was the dominant
  driver (68%). West Antarctica predominantly lost mass; East
  Antarctica predominantly stayed stable or gained.
- **Nature Geoscience (2025)** — sediment-record and ocean-model
  evidence for a real, self-reinforcing meltwater-release feedback that
  drove an ice-shelf collapse ~9000 years ago: meltwater strengthens
  stratification, which enhances warm deep-water inflow, which
  accelerates melting, which releases more meltwater.
- **Muilwijk et al. (2026, *The Cryosphere*)** — 10 CMIP6 models under
  a standardized meltwater perturbation show **opposite-sign regional
  responses**: East Antarctica's feedback amplifies warming (+0.16 to
  +0.26 degC median, up to +0.82 degC by 2100 under SSP5-8.5), while
  the Amundsen/Bellingshausen sectors of West Antarctica show
  **cooling or suppressed warming** (-0.5 to -1.5 degC).

## Deliberately not one-sided

`do_east_and_west_responses_share_the_same_sign()` returns `False` —
the CMIP6 regional finding directly complicates a naive "meltwater
feedback always accelerates melting everywhere" reading of the
Holocene mechanism documented alongside it. Both are real findings,
kept explicit rather than smoothed into one narrative.

## Installation

```bash
pip install antarctic-ice-shelf-utac
```

## Quick start

```python
from antarctic_ice_shelf_utac import (
    pct_shelves_losing_mass,
    is_loss_uniform_east_vs_west,
    do_east_and_west_responses_share_the_same_sign,
)

pct_shelves_losing_mass()  # 43.8
is_loss_uniform_east_vs_west()  # False
do_east_and_west_responses_share_the_same_sign()  # False -- the honesty check
```

## License

Code: MIT. Documentation/data notes: see [DISCLAIMER.md](DISCLAIMER.md).

## Citation

See [CITATION.cff](CITATION.cff).
