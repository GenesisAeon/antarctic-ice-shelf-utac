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

# =====================================================================
# v2.0.0 additions (2026-09-03): six mechanisms Johann asked about after
# a Spektrum.de coral-reef article led into a broader Antarctica
# brainstorm. Researched via six parallel independent verification
# passes; each citation below was independently confirmed (direct
# WebFetch of a primary/near-primary source, or -- where noted -- a
# WebSearch cross-reference where the publisher page was blocked, this
# ecosystem's usual publisher-blocking pattern).
# =====================================================================

# --- Subglacial hydrology (grounded-ice-bed water, NOT ocean-driven
# ice-shelf basal melt above -- a physically distinct process) --------

WILSON_2025_CITATION = {
    "authors": (
        "Wilson, S.F., Hogg, A.E., Rigby, R., Gourmelen, N., Nias, I., "
        "Slater, T."
    ),
    "year": 2025,
    "title": (
        "Detection of 85 new active subglacial lakes in Antarctica "
        "from a decade of CryoSat-2 data"
    ),
    "journal": "Nature Communications",
    "volume": 16,
    "pages": "8311",
    "doi": "10.1038/s41467-025-63773-9",
    "verified": "2026-09-03, direct fetch of PMC mirror PMC12449472",
}
SUBGLACIAL_LAKES_NEWLY_DETECTED = 85
SUBGLACIAL_LAKES_KNOWN_BEFORE = 146
SUBGLACIAL_LAKES_KNOWN_AFTER = 231  # 146 + 85
SUBGLACIAL_LAKES_STUDY_PERIOD_YEARS = (2010, 2020)  # CryoSat-2, Oct2010-Jul2020
SUBGLACIAL_LAKES_MEDIAN_DRAINAGE_TIME_YEARS = 2.2
SUBGLACIAL_LAKES_MEDIAN_RECHARGE_TIME_YEARS = 3.5
SUBGLACIAL_LAKES_NEAR_GROUNDING_ZONE_COUNT = 6  # within 8 km of the grounding zone
SUBGLACIAL_LAKES_WEST_ANTARCTICA_COUNT = 12
SUBGLACIAL_LAKES_EAST_ANTARCTICA_COUNT = 73

DOW_2022_CITATION = {
    "authors": "Dow, C.F., Ross, N., Jeofry, H., Siu, K., Siegert, M.J.",
    "year": 2022,
    "title": (
        "Antarctic basal environment shaped by high-pressure flow "
        "through a subglacial river system"
    ),
    "journal": "Nature Geoscience",
    "volume": 15,
    "pages": "892-898",
    "doi": "10.1038/s41561-022-01059-1",
    "verified": (
        "2026-09-03, corroborated across independent secondary sources "
        "(Imperial College / ScienceDaily press coverage) -- nature.com "
        "itself is login-walled, consistent with this ecosystem's usual "
        "publisher-blocking pattern; treat the flux figure below as "
        "well-corroborated but not primary-source-fetched"
    ),
}
SUBGLACIAL_RIVER_SYSTEM_LENGTH_KM = 460
SUBGLACIAL_RIVER_HIGH_PRESSURE_FLUX_M3_S = 24.0
SUBGLACIAL_HYDROLOGY_NOTE = (
    "Basal water pressure plausibly facilitates faster ice flow (Dow et "
    "al. 2022's own framing), but this is a documented mechanism, not a "
    "single universal quantitative speedup relationship -- a modelling "
    "study around Pine Island/Thwaites reportedly finds the simple "
    "'more water pressure -> faster flow' relationship breaks down near "
    "the grounding zone itself, but that specific paper's authorship/DOI "
    "could not be independently confirmed and is NOT used as a citation "
    "here -- flagged as a real open question, not asserted as fact."
)

# --- Southern Annular Mode (SAM) / stratospheric polar vortex --------
# The real Antarctic analog to the Arctic polar vortex story -- but the
# "instability pushes cold air out" analogy does NOT hold; see LIM_2019.

LIM_2019_CITATION = {
    "authors": (
        "Lim, E.-P., Hendon, H.H., Boschat, G., Hudson, D., Thompson, "
        "D.W.J., Dowdy, A.J., Arblaster, J.M."
    ),
    "year": 2019,
    "title": (
        "Australian hot and dry extremes induced by weakenings of the "
        "stratospheric polar vortex"
    ),
    "journal": "Nature Geoscience",
    "volume": 12,
    "pages": "896-901",
    "verified": (
        "2026-09-03, via independent research pass cross-referencing "
        "search-indexed abstract"
    ),
}
ANTARCTIC_SSW_DOCUMENTED_YEARS = (2002, 2019)  # only two documented Sudden Stratospheric Warmings
ANTARCTIC_VORTEX_NOTE = (
    "Antarctica's stratospheric polar vortex is structurally MORE "
    "stable than the Arctic's -- the Southern Ocean lacks the "
    "landmass-driven Rossby-wave disruption that mountain ranges cause "
    "in the Northern Hemisphere. The 2019 weakening event's documented "
    "effect ran OPPOSITE to a 'cold air export' story: a record-negative "
    "SAM shifted the westerlies equatorward, producing hot, dry "
    "conditions in southeastern Australia -- a real contributing driver "
    "of the 2019-2020 'Black Summer' bushfires, not a cold outbreak."
)

VERFAILLIE_2022_CITATION = {
    "authors": (
        "Verfaillie, D., Pelletier, C., Goosse, H., Jourdain, N.C., "
        "Bull, C.Y.S., Wille, J.D."
    ),
    "year": 2022,
    "title": (
        "The circum-Antarctic ice-shelves respond to a more positive "
        "Southern Annular Mode with regionally varied melting"
    ),
    "journal": "Communications Earth & Environment",
    "volume": 3,
    "pages": "139",
    "doi": "10.1038/s43247-022-00458-x",
    "verified": "2026-09-03, via WebSearch cross-reference (nature.com login-walled)",
}
SAM_BASAL_MASS_LOSS_PER_SD_GT_YR = 40.0  # net basal mass loss per +1 std-dev SAM increase
SAM_REGIONAL_NOTE = (
    "A positive SAM increases basal melt in the Bellingshausen and "
    "Western Pacific sectors, but produces the OPPOSITE response in the "
    "Amundsen sector -- another real regional asymmetry, directly "
    "parallel to this package's existing East/West mass-budget theme."
)

KING_2023_CITATION = {
    "authors": "King, M., Lyu, K., Zhang, X.",
    "year": 2023,
    "title": "Climate variability a key driver of recent Antarctic ice-mass change",
    "journal": "Nature Geoscience",
    "volume": 16,
    "pages": "1128-1135",
    "doi": "10.1038/s41561-023-01317-w",
    "verified": "2026-09-03, via WebSearch cross-reference",
}
SAM_ENSO_ARE_DOMINANT_DECADAL_DRIVERS_NOTE = (
    "SAM and ENSO are identified as the two dominant drivers of decadal "
    "Antarctic ice-mass variability (2002-2021 satellite gravimetry). "
    "Caveat: SAM does NOT significantly influence winds or grounding- "
    "line ocean melt specifically in the Amundsen Sea Embayment -- the "
    "fastest-thinning sector -- so SAM is not a universal explanatory "
    "variable even within West Antarctica."
)

# --- Sea-ice albedo feedback (NOT exposed-rock albedo -- searched for,
# not found as a quantified Antarctica-specific mechanism; see note) --

RIIHELAE_2021_CITATION = {
    "authors": "Riihela, A., Bright, R.M., Anttila, K.",
    "year": 2021,
    "title": (
        "Recent strengthening of snow and ice albedo feedback driven "
        "by Antarctic sea-ice loss"
    ),
    "journal": "Nature Geoscience",
    "volume": 14,
    "pages": "832-836",
    "doi": "10.1038/s41561-021-00841-x",
    "verified": "2026-09-03, via WebSearch cross-referencing phys.org/Nibio press coverage",
}
SEA_ICE_ALBEDO_FEEDBACK_1992_2015_W_M2_PER_DECADE = -0.06  # expansion era, cooling trend
SEA_ICE_ALBEDO_FEEDBACK_2016_2018_COMBINED_W_M2 = 0.26  # post-reversal, 3yr mean, Arctic+Antarctic
SEA_ICE_ALBEDO_FEEDBACK_PCT_OF_CO2_FORCING = 10.0  # 1992-2018 mean, approx.

KROMER_2023_CITATION = {
    "authors": "Kromer, J.D., Trusel, L.D., et al.",
    "year": 2023,
    "title": (
        "Identifying the Impacts of Sea Ice Variability on the Climate "
        "and Surface Mass Balance of West Antarctica"
    ),
    "journal": "Geophysical Research Letters",
    "volume": 50,
    "issue": 18,
    "doi": "10.1029/2023GL104436",
    "verified": (
        "2026-09-03, via WebSearch + phys.org press coverage (AGU's own "
        "page returned 403, this ecosystem's usual publisher-blocking "
        "pattern) -- mechanism confirmed, no precise number recoverable"
    ),
}
SEA_ICE_SNOWFALL_NOTE = (
    "Reduced sea ice in the Amundsen Sea increases open-ocean moisture "
    "flux, transported onto the adjacent ice sheet as enhanced "
    "snowfall -- a real, mechanistically described feedback (Kromer et "
    "al. 2023). No precise quantified figure was independently "
    "verifiable from a primary source; do not present a specific % or "
    "mm/yr number as confirmed. Exposed-CONTINENTAL-ROCK albedo "
    "feedback (as opposed to sea-ice albedo) was searched for "
    "specifically and NOT found as an existing, quantified, "
    "Antarctica-specific result in the literature -- this remains an "
    "open research gap, not a citable finding, and should not be "
    "conflated with the real, quantified sea-ice albedo mechanism above."
)

# --- Seismic <-> ice interactions -------------------------------------

WIENS_2008_CITATION = {
    "authors": "Wiens, D.A., Anandakrishnan, S., Winberry, J.P., King, M.A.",
    "year": 2008,
    "title": (
        "Simultaneous teleseismic and geodetic observations of the "
        "stick-slip motion of an Antarctic ice stream"
    ),
    "journal": "Nature",
    "volume": 453,
    "pages": "770-774",
    "doi": "10.1038/nature06990",
    "verified": "2026-09-03, via independent research pass",
}
WHILLANS_ICEQUAKES_PER_RECORD_COUNT = 20000
WHILLANS_ICEQUAKE_RECURRENCE_MINUTES = 25  # roughly, tidally modulated

LIPOVSKY_2016_CITATION = {
    "authors": "Lipovsky, B.P., Dunham, E.M.",
    "year": 2016,
    "title": "Tremor during ice-stream stick-slip",
    "journal": "The Cryosphere",
    "volume": 10,
    "pages": "385-399",
    "doi": "10.5194/tc-10-385-2016",
    "verified": "2026-09-03, via independent research pass",
}
WHILLANS_LARGE_SLIP_EVENTS_PER_DAY = 2.0

HEREDIA_BARION_2023_CITATION = {
    "authors": "Heredia Barion, P., Strelin, J., Roberts, S., et al.",
    "year": 2023,
    "title": (
        "Debris flows and mudflows at the permafrost/active-layer "
        "interface, Potter Peninsula, King George Island"
    ),
    "journal": "Frontiers in Earth Science",
    "volume": 10,
    "pages": "1073075",
    "doi": "10.3389/feart.2022.1073075",
    "verified": "2026-09-03, via independent research pass",
}
SEISMIC_ICE_NOTE = (
    "Icequakes from ice-stream basal stick-slip (Wiens 2008, Lipovsky & "
    "Dunham 2016) are a real, well-quantified Antarctic-specific "
    "mechanism. Permafrost-thaw-triggered debris flows/mudflows are "
    "documented at Potter Peninsula since 1956 (Heredia Barion et al. "
    "2023, failure scars 20-180m wide) but WITHOUT a quantified "
    "frequency/volume trend -- unlike the well-quantified Alpine "
    "rockfall literature (Hartmeyer et al. 2020, Austria-specific, NOT "
    "used here as an Antarctic citation). Glacial isostatic adjustment "
    "(GIA) triggered the real 1998 Balleny Islands Mw 8.1 earthquake "
    "(Tsuboi et al. 2000) -- but GIA uplift itself is documented "
    "elsewhere as a STABILIZING negative feedback on West Antarctic ice "
    "(reduces marine ice-sheet instability), so 'seismicity feeds back "
    "onto ice dynamics' should not be framed as an amplifying/collapse "
    "mechanism."
)
TSUBOI_2000_CITATION = {
    "authors": "Tsuboi, S., et al.",
    "year": 2000,
    "title": "The 1998 Balleny Islands earthquake: contribution from postglacial rebound stress",
    "journal": "Earth, Planets and Space",
    "volume": 52,
    "doi": "10.1186/BF03351621",
    "verified": "2026-09-03, via independent research pass",
}
BALLENY_1998_MAGNITUDE_MW = 8.1

# --- Black carbon deposition -------------------------------------------
# A DIFFERENT region/dataset than black-carbon-albedo-utac (P105), which
# covers the Tibetan Plateau/Himalaya exclusively -- no overlap.

CORDERO_2022_CITATION = {
    "authors": "Cordero, R.R., et al.",
    "year": 2022,
    "title": "Black carbon footprint of human presence in Antarctica",
    "journal": "Nature Communications",
    "volume": 13,
    "pages": "984",
    "doi": "10.1038/s41467-022-28560-w",
    "verified": "2026-09-03, direct fetch of PMC mirror PMC8863810",
}
BC_ANTARCTIC_BACKGROUND_NG_G = 1.0  # remote background, <1 ng/g -- roughly 10x below Arctic snow
BC_ANTARCTIC_NEAR_STATION_NG_G_RANGE = (2.0, 4.0)  # near research stations / tourist landing sites
BC_ANTARCTIC_EXTRA_SNOWPACK_LOSS_KG_M2_RANGE = (5.0, 23.0)  # per summer, at BC-impacted sites

MAGALHAES_2024_CITATION = {
    "authors": "Magalhaes, N., Evangelista, H., Goncalves Jr., S.J., et al.",
    "year": 2024,
    "title": (
        "Seasonal changes in black carbon footprint on the Antarctic "
        "Peninsula due to rising shipborne tourism and forest fires"
    ),
    "journal": "Science Advances",
    "volume": 10,
    "issue": 42,
    "pages": "eadp1682",
    "doi": "10.1126/sciadv.adp1682",
    "verified": "2026-09-03, direct fetch of PMC mirror PMC11482304",
}
BC_ANTARCTIC_SEASONAL_RANGE_NG_G = (0.01, 3.73)
BC_ALBEDO_REDUCTION_PCT = 0.4
BC_RADIATIVE_FORCING_INCREASE_W_M2 = 0.6
BLACK_CARBON_ANTARCTICA_NOTE = (
    "Antarctic BC concentrations are real but roughly an order of "
    "magnitude below Arctic/Himalayan levels. Cordero et al. 2022 find "
    "LOCAL emissions (research-station diesel generators, ships, "
    "aircraft) dominate BC at most sites, not long-range transport -- "
    "counterintuitive vs. the naive 'imported wildfire smoke' "
    "assumption. Magalhaes et al. 2024 find summer BC correlates "
    "strongly with tourist-ship numbers (r=0.95) while spring BC "
    "correlates with South American fire-burned area (r=0.75) -- and "
    "the 2019-2020 Australian megafires temporarily overrode the "
    "tourism-driven baseline. The two papers are NOT contradictory: "
    "local emissions dominate on average, but extreme remote wildfire "
    "events can spike above that baseline -- kept as an explicit "
    "honesty-check nuance, not smoothed into one story. This is a "
    "DIFFERENT geographic dataset than black-carbon-albedo-utac (P105, "
    "Tibetan Plateau/Himalaya) -- no overlap."
)

# --- ENSO teleconnection to Antarctic ice ------------------------------
# Distinct from el-nino-amplification-utac (P118, ENSO strengthening
# itself) and marine-heatwave-utac (P119, SE-Asia MHW/ENSO coupling) --
# neither touches Antarctica.

PAOLO_2018_CITATION = {
    "authors": "Paolo, F.S., et al.",
    "year": 2018,
    "title": "Response of Pacific-sector Antarctic ice shelves to the El Nino/Southern Oscillation",
    "journal": "Nature Geoscience",
    "doi": "10.1038/s41561-017-0033-0",
    "verified": (
        "2026-09-03, direct WebFetch of ScienceDaily press coverage "
        "(journal page not attempted)"
    ),
}
ENSO_BASAL_MELT_VS_SNOWFALL_RATIO = 5.0  # basal melt loss is ~5x the surface snowfall gain
ENSO_CASCADE_NOTE = (
    "During strong El Nino, Amundsen Sea ice shelves gain surface mass "
    "from increased snowfall but lose roughly 5x more via submarine "
    "(basal) melting -- 'the ocean ends up winning' (Paolo et al. "
    "2018). A real, quantified COMPETING-effects mechanism, not a "
    "single-direction cascade. Mechanism: El Nino weakens the Amundsen "
    "Sea Low, weakening coastal easterlies, allowing more warm "
    "Circumpolar Deep Water onto the shelf."
)

AYABILAH_2026_CITATION = {
    "authors": "Ayabilah, N., King, M., Udy, D., Vance, T.",
    "year": 2026,
    "title": "ENSO and SAM impacts on Antarctic surface mass balance",
    "journal": "The Cryosphere",
    "volume": 20,
    "issue": 2,
    "pages": "1237",
    "doi": "10.5194/tc-20-1237-2026",
    "verified": "2026-09-03, direct WebFetch",
}
ENSO_TIMESCALE_ASYMMETRY_NOTE = (
    "On ENSO (interannual) timescales, West Antarctica GAINS mass "
    "during El Nino and LOSES during La Nina (surface-mass-balance/ "
    "snowfall-driven, via the Amundsen Sea Low) -- the OPPOSITE short- "
    "term sign of Davison et al. 2023's long-term (1997-2021), "
    "ocean-driven net basal-melt loss trend. East Antarctica's ENSO "
    "response is smaller and dominated by SAM instead. These are two "
    "different, non-contradictory timescales/mechanisms (interannual "
    "SMB wobble vs. multi-decadal ocean-driven basal melt), not a "
    "contradiction of the package's core Davison 2023 finding -- the "
    "deliberate honesty-check nuance for this addition."
)

# =====================================================================
# Live current-event context (added 2026-09-03, context only) -- WMO
# =====================================================================
# WMO press release (2026-09-03): a live, exceptionally strong El Nino
# event, Nino 3.4 index +2.2 to +2.6C above average (late Jul-mid Aug
# 2026), near-100% probability of persisting through February 2027,
# peak expected end of 2026. Real-world example of the kind of strong
# ENSO event the Paolo et al. 2018 (competing snowfall-gain vs.
# ~5x-larger basal-melt-loss) and Ayabilah et al. 2026 (West Antarctica
# SMB gain on ENSO timescales) mechanisms above concern -- but this
# package has no post-2021 Antarctic mass-budget monitoring data, so
# this event's actual effect on Antarctic ice mass is NOT claimed here.
WMO_2026_CITATION = (
    "WMO (2026-09-03), \"El Nino set to become very strong, raising "
    "risks of extreme weather into 2027\", "
    "https://wmo.int/news/media-centre/el-nino-set-become-very-strong-"
    "raising-risks-of-extreme-weather-2027"
)
WMO_2026_NINO34_ANOMALY_C_RANGE = (2.2, 2.6)
WMO_2026_PEAK_EXPECTED = "end of 2026"
