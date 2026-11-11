# Progress Log

Day-to-day record of work on the program. The plan itself lives in [`master-curriculum.md`](master-curriculum.md), which this log references but never changes. Ticking a curriculum milestone needs evidence: an entry here with an output and a verification.

## How to use this log

- **One row per work item** (a setup task, an exercise, a reading block, a review). Add new rows at the bottom, oldest first.
- **Fill every column** each time. Leave Hours blank if you didn't track time; don't estimate after the fact.
- **Keep each cell to one line.** No line breaks and no `|` characters inside cells. Use `;` to separate items.
- **Use only the values listed below** for Track, Type, Status and Evidence. Consistent values become clean Notion select options.
- **Weekly summary:** at the end of each week, add one row to the second table (about 10 minutes, per the roadmap's weekly rhythm).

### Field reference (Notion property types)

| Field | Notion type | Allowed values / format |
|---|---|---|
| Entry | Title | Short description of the work item |
| Date | Date | YYYY-MM-DD |
| Week | Select | ISO week, YYYY-Www (e.g. 2026-W46) |
| Month | Select | Curriculum month, e.g. M01 Nov 2026 |
| Track | Select | 00 Program; 01 GIS; 02 Systems Eng; 03 Env Mgmt; 04 Service Design; 05 Data-AI; 06 Capstone |
| Type | Select | Setup; Learning; Exercise; Project; Review; Admin |
| Status | Select | Not started; In progress; Needs review; Complete (curriculum §15) |
| Evidence | Select | FIELD-OBSERVED; SOURCE-DERIVED; ANALYZED; HYPOTHESIS; CONCEPTUAL; PROTOTYPED; IMPLEMENTED; UNKNOWN-TO-VALIDATE; n/a (curriculum §1.6) |
| Curriculum ref | Text | Section and checklist item in master-curriculum.md |
| Output | Text | Repo paths or artifacts produced; separate with ; |
| Verified by | Text | How the result was checked |
| Hours | Number | Decimal hours, or blank |
| Next action | Text | The single next step, or blank if done |

### Importing into Notion

1. In Notion, choose **Import → Text & Markdown** and select this file. Each table becomes a simple table.
2. On each table, open the **⋯** menu and choose **Turn into database**.
3. Set each property's type to the one in the field reference. For Select fields, Notion builds the options from the existing values.
4. Re-import or paste new rows as the log grows. The columns stay the same, so new rows line up with the existing database.

---

## Log

| Entry | Date | Week | Month | Track | Type | Status | Evidence | Curriculum ref | Output | Verified by | Hours | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reviewed QGIS manual §1.1 install options and chose a version | 2026-11-07 | 2026-W45 | M01 Nov 2026 | 01 GIS | Setup | Complete | SOURCE-DERIVED | §4.3 Initial baseline | Decision: QGIS 4.2 (current) over 3.44 LTR; skip build-from-source and flash-drive install | Checked qgis.org download page and QGIS 4.0/4.2 release notes | | |
| Installed QGIS 4.2.3 on macOS and recorded environment | 2026-11-08 | 2026-W45 | M01 Nov 2026 | 01 GIS | Setup | Complete | SOURCE-DERIVED | §4.3 Initial baseline: record QGIS and macOS version | environment.md | Help → About values copied into environment.md | | |
| Python console smoke test | 2026-11-08 | 2026-W45 | M01 Nov 2026 | 01 GIS | Setup | Complete | ANALYZED | §3.2 Installation sequence | environment.md (change log) | 5 of 5 checks passed: QGIS version; Python 3.12; GDAL 3.13.3; EPSG:2964 valid; GDAL and GRASS providers present | | |
| Created EESD QGIS profile | 2026-11-09 | 2026-W46 | M01 Nov 2026 | 01 GIS | Setup | Complete | n/a | §3.2 Installation sequence | EESD profile; profile path recorded in environment.md | active_plugins shows processing; grassprovider; MetaSearch; db_manager_community | | Confirm startup profile picker is enabled |
| Downloaded Alaska sample data and documented provenance | 2026-11-09 | 2026-W46 | M01 Nov 2026 | 01 GIS | Setup | Complete | SOURCE-DERIVED | §4.3 Initial baseline: record sample-data source; location; date; license | 01_GIS-Spatial-Intelligence/data/README.md; data/raw/qgis-sample-data (git-ignored) | Data README lists source URL; date; CRS; licenses | | |
| Fixed .gitignore rule so data/raw is ignored in every track | 2026-11-09 | 2026-W46 | M01 Nov 2026 | 00 Program | Admin | Complete | ANALYZED | §3.6 Git and GitHub workflow | .gitignore: data/raw/ → **/data/raw/ | git check-ignore confirms sample data ignored; git log shows it was never committed | | |
| Loaded alaska.shp and investigated ballpark-transform warning | 2026-11-09 | 2026-W46 | M01 Nov 2026 | 01 GIS | Exercise | Complete | ANALYZED | §4.3 CRS checklist: record warnings; project CRS vs layer CRS | Project CRS set to EPSG:2964 | Status bar shows EPSG:2964; warning gone | | |
| Installed NOAA Alaska grid and measured datum shift | 2026-11-10 | 2026-W46 | M01 Nov 2026 | 01 GIS | Exercise | Complete | ANALYZED | §4.3 CRS checklist: inspect coordinate operations; record grid availability and accuracy | us_noaa_alaska.tif in EESD profile; Exercises/2026-11-08_qgis-setup-and-crs/datum_shift_check.py | Script: op 85 available (~5 m); ballpark error 133.6 m at Anchorage; hand check √(118² + 61²) ≈ 133 m | | |
| Set preferred transformation and loaded GPS waypoints | 2026-11-10 | 2026-W46 | M01 Nov 2026 | 01 GIS | Exercise | Needs review | ANALYZED | §4.3 CRS checklist: record which transformation QGIS uses; check expected location | Exercises/2026-11-08_qgis-setup-and-crs/qgis-setup-and-crs.qgz (op 85 set for 2964 ↔ 4326) | GPX loaded with no ballpark warning; project CRS found reset to 4326 (first layer added); antimeridian caused tiny zoom | | Reset project CRS to 2964; confirm 4 waypoints fall inside Alaska; save |
| CRS concept check: projection; units; datum grid | 2026-11-10 | 2026-W46 | M01 Nov 2026 | 01 GIS | Learning | In progress | n/a | §4.3 CRS checklist: explain geographic vs projected CRS; explain datums | | | | Write the three sentences and have them checked |
| Added Master Curriculum section to root CLAUDE.md | 2026-11-10 | 2026-W46 | M01 Nov 2026 | 00 Program | Admin | Complete | n/a | §3.5 Claude Code project instructions | CLAUDE.md; curriculum renamed to 00_Learning-Plan/master-curriculum.md | Section present in CLAUDE.md; no other files referenced the old filename | | Commit and push |
| Created progress log | 2026-11-10 | 2026-W46 | M01 Nov 2026 | 00 Program | Admin | Complete | n/a | §2.3 Session checklist: After | 00_Learning-Plan/progress-log.md | | | |

---

## Weekly summary

| Week | Dates | Main focus | Did | Verified | Next | Hours |
|---|---|---|---|---|---|---|
| 2026-W45 | 2026-11-02 – 2026-11-08 | 01 GIS | Planned QGIS install; installed QGIS 4.2.3; recorded environment; passed smoke test | Help → About; 5-check console smoke test | EESD profile; sample data | |
| 2026-W46 | 2026-11-09 – 2026-11-15 | 01 GIS | EESD profile; sample data and provenance; .gitignore fix; NAD27 → WGS 84 datum investigation with NOAA grid; progress log | Datum shift 133.6 m measured and hand-checked; git ignore rules verified | CRS concept check; exercise write-up; §4.3 baseline items (baseline project copy; project README; layer and CRS inventory) | |
