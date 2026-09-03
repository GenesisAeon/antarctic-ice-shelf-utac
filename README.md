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

## v2.0.0 (2026-09-03): six more real mechanisms

Following a Johann brainstorm prompted by a coral-reef article, six
independent research passes each verified a real, citable mechanism:

- **Subglacial hydrology** — Wilson et al. (2025, *Nat. Commun.*): 85
  newly detected active subglacial lakes (known inventory +58%), median
  drainage 2.2yr / recharge 3.5yr, 6 within 8km of the grounding zone.
  Dow et al. (2022, *Nat. Geosci.*): a 460km high-pressure subglacial
  river system. Physically distinct from the ice-shelf basal melting
  above — this is water beneath the *grounded* ice.
- **Southern Annular Mode (SAM)** — the real Antarctic analog to the
  Arctic polar vortex, but the "instability exports cold air" analogy
  does **not** transfer: the 2019 vortex weakening produced hot, dry
  conditions in Australia instead (Lim et al. 2019), a real contributor
  to the Black Summer bushfires. SAM does drive real, regionally
  asymmetric basal melt (+40 Gt/yr per +1 SD, opposite-signed in
  Amundsen vs. Bellingshausen/W. Pacific — Verfaillie et al. 2022), and
  SAM+ENSO are the two dominant decadal drivers of Antarctic ice-mass
  variability (King et al. 2023).
- **Sea-ice albedo feedback** — Riihelä et al. (2021, *Nat. Geosci.*):
  a real, quantified feedback that flipped sign, from −0.06±0.02
  W/m²/decade (1992-2015 expansion era) to +0.26 W/m² (2016-2018 sea-
  ice-loss reversal). Explicitly **not** exposed-continental-rock
  albedo — that mechanism was searched for and not found as a
  quantified Antarctica-specific result; don't conflate the two.
- **Seismic-ice interactions** — real, tidally-modulated basal
  stick-slip icequakes on the Whillans Ice Plain (~20,000 events on
  record, Wiens et al. 2008); permafrost-thaw debris flows documented
  at Potter Peninsula since 1956, though without a quantified trend
  like the (non-Antarctic) Alpine literature; the 1998 Balleny Islands
  Mw8.1 earthquake, GIA-triggered — but GIA itself is a *stabilizing*
  feedback on West Antarctic ice, not an amplifying one.
- **Black carbon deposition** — a different geography from
  `black-carbon-albedo-utac` (P105, Tibetan Plateau) — no overlap.
  Cordero et al. (2022, *Nat. Commun.*): local station/tourism
  emissions dominate on average. Magalhães et al. (2024, *Sci. Adv.*):
  extreme wildfire events (2019-2020 Australian megafires) can
  temporarily override that local baseline — both kept, not smoothed.
- **ENSO teleconnection** — Paolo et al. (2018, *Nat. Geosci.*): during
  strong El Niño, Amundsen Sea shelves gain surface mass from snowfall
  but lose ~5x more via basal melt — "the ocean ends up winning."
  Ayabilah et al. (2026, *The Cryosphere*): on ENSO timescales, West
  Antarctica *gains* mass during El Niño — the opposite short-term sign
  of this package's own core Davison et al. 2023 long-term trend. Two
  different timescales, not a contradiction — kept as an explicit
  honesty-check nuance.

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
