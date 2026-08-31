"""Verified constants for Antarctic ice shelf mass loss: observed
mass budget, the Holocene meltwater feedback mechanism, and the CMIP6
regional East/West asymmetry.

GenesisAeon Package 120. One of three candidate topics surfaced by a
broad DeepResearch pass (2026-08-31) on El Nino/ENSO and climate
topics. All three citations independently verified via direct
WebFetch on the publisher/press page, 2026-08-31.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md and
PACKAGE_REGISTRY.md's "Why no UTAC/CREP/AFET bridge in the
climate/ecology series" note.
"""

PACKAGE_ID = 120

# =====================================================================
# Davison et al. (2023), Science Advances -- observed 1997-2021 mass budget
# =====================================================================

DAVISON_2023_CITATION = {
    "authors": (
        "Davison, B.J., Hogg, A.E., Gourmelen, N., Jakob, L., Wuite, J., "
        "Nagler, T., Greene, C.A., Andreasen, J., Engdahl, M.E."
    ),
    "year": 2023,
    "title": "Annual mass budget of Antarctic ice shelves from 1997 to 2021",
    "journal": "Science Advances",
    "volume": 9,
    "issue": 41,
    "doi": "10.1126/sciadv.adi0186",
    "verified": "2026-08-31, direct WebFetch of pmc.ncbi.nlm.nih.gov/articles/PMC11650781/",
}

TOTAL_ICE_SHELVES_STUDIED = 162
SHELVES_LOST_MASS = 71
SHELVES_GAINED_MASS = 29
SHELVES_NO_SIGNIFICANT_CHANGE = 62
SHELVES_LOST_MASS_STATISTICALLY_SIGNIFICANT = 68
SHELVES_LOST_MORE_THAN_30PCT = 48

TOTAL_MASS_LOST_TONNES = 8.3e12  # 8.3 trillion tonnes, 1997-2021
STUDY_PERIOD_YEARS = 25  # 1997-2021
ANNUAL_MASS_LOSS_RATE_TONNES = 3.3e11  # ~330 billion tonnes/year average

BASAL_MELT_DOMINANT_FRACTION_PCT = 68.0  # basal melting = 68% of mass-loss contribution

# West vs East Antarctica: almost all West Antarctic shelves lost ice;
# most East Antarctic shelves stayed stable or gained volume. A real,
# documented regional asymmetry, not a uniform continental trend.
WEST_ANTARCTICA_TREND = "predominantly mass loss"
EAST_ANTARCTICA_TREND = "predominantly stable or mass gain"

# =====================================================================
# Holocene meltwater-release feedback -- Nature Geoscience 2025
# (with a subsequent Author Correction)
# =====================================================================

HOLOCENE_FEEDBACK_CITATION = {
    "year": 2025,
    "title": "Antarctic ice-shelf collapse in Holocene driven by meltwater release feedbacks",
    "journal": "Nature Geoscience",
    "volume": 18,
    "pages": "1216-1223",
    "publication_date": "2025-11-07",
    "note": "An Author Correction was subsequently published for this article.",
    "verified": (
        "2026-08-31, via WebSearch cross-referencing nature.com, "
        "phys.org, sciencedaily.com, and National Institute of Polar "
        "Research (Japan) press coverage"
    ),
}

HOLOCENE_EVENT_YEARS_BP = 9000
HOLOCENE_FEEDBACK_MECHANISM = (
    "meltwater release -> increased ocean stratification -> enhanced "
    "warm deep-water inflow -> accelerated basal melting -> more "
    "meltwater release (self-reinforcing cascade)"
)

# =====================================================================
# Regional CMIP6 asymmetry -- Muilwijk et al. (2026), The Cryosphere
# =====================================================================

MUILWIJK_2026_CITATION = {
    "authors": (
        "Muilwijk, M., Hattermann, T., Beadling, R.L., Swart, N.C., "
        "Nummelin, A., Guo, C., Chandler, D.M., Langebroek, P.M., et al."
    ),
    "year": 2026,
    "title": (
        "Large regional differences in Antarctic ice shelf mass loss "
        "from Southern Ocean warming and meltwater feedbacks"
    ),
    "journal": "The Cryosphere",
    "volume": 20,
    "issue": 2,
    "pages": "1087-1117",
    "doi": "10.5194/tc-20-1087-2026",
    "publication_date": "2026-02-12",
    "verified": "2026-08-31, direct WebFetch of tc.copernicus.org/articles/20/1087/2026/",
}

CMIP6_MODEL_COUNT = 10
MELTWATER_PERTURBATION_SV = 0.1  # standardized 0.1 Sverdrup perturbation applied

# East Antarctic sectors: meltwater feedback AMPLIFIES basal melting.
EAST_ANTARCTIC_MEDIAN_WARMING_RANGE_C = (0.16, 0.26)
EAST_ANTARCTIC_END_CENTURY_WARMING_RANGE_C = (0.64, 0.82)  # under SSP5-8.5

# West Antarctic sectors (Amundsen, Bellingshausen): feedback response
# is COOLING or SUPPRESSED warming -- the opposite sign of the East
# Antarctic response. This asymmetry is the paper's central finding.
WEST_ANTARCTIC_ANOMALY_RANGE_C = (-1.5, -0.5)
WEST_ANTARCTIC_REGIONS = ("Amundsen Sea", "Bellingshausen Sea")
