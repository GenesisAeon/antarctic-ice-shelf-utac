# DISCLAIMER — Real Ice Shelf Science, Real Regional Contradiction

> **Why no UTAC/CREP/AFET bridge:** not only because the cited literature
> already provides the necessary quantitative structure -- a deliberate
> choice. This project's highly speculative AFET/UTAC experiments must
> never stand in the way of climate/ecology topics being accessible and
> usable to people who don't work inside that construct and aren't
> looking for renormalization groups. Real, checkable science, without
> the burden of an unproven framework. See `PACKAGE_REGISTRY.md`'s "Why
> no UTAC/CREP/AFET bridge in the climate/ecology series" (2026-08-31) in
> the GenesisAeon workspace root for the full canonical note.

**Status: Real, independently verified science. NO UTAC/CREP/AFET bridge,
NO invented Gamma value.**

## Where this package came from

Built alongside `el-nino-amplification-utac` (P118) and
`marine-heatwave-utac` (P119), all three surfaced by a single broad
DeepResearch pass (2026-08-31). Checked directly against
`PACKAGE_REGISTRY.md`: `cascading-tipping-utac` (P87) references the
West Antarctic Ice Sheet only as one node in a 4-element tipping
network (Wunderling et al.), not a standalone quantified treatment of
ice-shelf mass loss -- this package fills that gap.

All three citations were independently verified via direct WebFetch
against publisher pages, 2026-08-31: `pmc.ncbi.nlm.nih.gov` for
Davison et al. (the original `science.org` URL for this paper was not
attempted directly; the NCBI PMC mirror was used and cross-confirmed
via search-result agreement), `tc.copernicus.org` (resolved directly,
open access), and cross-referenced press coverage (nature.com,
phys.org, sciencedaily.com, National Institute of Polar Research) for
the Nature Geoscience Holocene paper.

## Why this package deliberately includes a real internal tension

It would have been easy to build this package from only two citations:
the observed 1997-2021 mass loss (Davison et al. 2023) and the Holocene
feedback mechanism (Nature Geoscience 2025) -- together telling a clean
story of "ice shelves are losing mass, and meltwater feedback can make
that self-reinforcing." But Muilwijk et al. (2026) found that under a
standardized meltwater perturbation across 10 CMIP6 models, **East and
West Antarctica respond with opposite signs**: East Antarctic sectors
show the expected feedback-amplified warming (+0.16 to +0.26 degC
median, rising to +0.64 to +0.82 degC by 2100 under SSP5-8.5), while
the Amundsen and Bellingshausen sectors of West Antarctica show
**cooling or suppressed warming** (-0.5 to -1.5 degC anomalies) under
the same perturbation.

This directly complicates a naive "meltwater feedback always
accelerates melting everywhere" reading of the Holocene mechanism.
`do_east_and_west_responses_share_the_same_sign()` returns `False` on
purpose -- this package documents the contradiction rather than
resolving it in favor of the more dramatic-sounding story.

## What this is NOT

- **Not a claim that West Antarctica is currently undergoing a
  Holocene-style cascading collapse.** `does_this_module_claim_current_active_cascade()`
  returns `False`. The Holocene mechanism is documented as evidence it
  is physically real, not as a description of the present-day system.
- **Not a claim of continent-wide uniformity.** `is_loss_uniform_east_vs_west()`
  returns `False` for the observed 1997-2021 record, and the CMIP6
  regional module documents an even sharper sign-flip under a modeled
  perturbation.
- **Not a UTAC/CREP/AFET-bridged package.** No Gamma value is assigned.

## References

- Davison, B.J., Hogg, A.E., Gourmelen, N., Jakob, L., Wuite, J.,
  Nagler, T., Greene, C.A., Andreasen, J., Engdahl, M.E. (2023).
  "Annual mass budget of Antarctic ice shelves from 1997 to 2021."
  *Science Advances*, 9(41). DOI: 10.1126/sciadv.adi0186.
- (2025). "Antarctic ice-shelf collapse in Holocene driven by
  meltwater release feedbacks." *Nature Geoscience*, 18, 1216-1223.
  (Author Correction subsequently published.)
- Muilwijk, M., Hattermann, T., Beadling, R.L., Swart, N.C., et al.
  (2026). "Large regional differences in Antarctic ice shelf mass loss
  from Southern Ocean warming and meltwater feedbacks." *The
  Cryosphere*, 20(2), 1087-1117. DOI: 10.5194/tc-20-1087-2026.

All verified directly (2026-08-31) via WebFetch and WebSearch against
publisher/press pages. Originating context: a broad DeepResearch pass
on El Nino/ENSO and climate topics, requested by Johann.
