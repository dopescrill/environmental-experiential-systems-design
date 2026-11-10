# Environment

Record of the software environment used for EESD work. Update this file whenever QGIS or a key library is upgraded, so results can be traced back to the setup that produced them.

## QGIS

- **Recorded:** 2026-11-08
- **Installed from:** official macOS installer, `qgis_pr_final-4_2_3.dmg` (download.qgis.org), regular release (not LTR)
- **QGIS profile:** EESD
- **Profile folder (not in git):** `/Users/danielmeier/Library/Application Support/QGIS/QGIS4/profiles/EESD/`. It holds machine-specific settings and possibly saved credentials. Export individual items (styles, models) into the repo instead.

| Item | Version |
|---|---|
| QGIS | 4.2.3 – Belém do Pará |
| QGIS code revision | b041a189 |

### Libraries

| Library | Version |
|---|---|
| Qt | 6.11.1 |
| Python | 3.12.11 |
| GDAL | 3.13.3 – Iowa City |
| PROJ | 9.8.1 |
| EPSG Registry database | v12.029 (2025-10-02) |
| GEOS | 3.14.1-CAPI-1.20.5 |
| SFCGAL | 2.3.0 |
| GeographicLib | No support |
| SQLite | 3.53.4 |
| PDAL | 2.10.1 |
| PostgreSQL client | 18.4 |
| SpatiaLite | 5.1.0 |
| QWT | 6.3.0 |
| QScintilla2 | 2.14.1 |

### System

| Item | Value |
|---|---|
| OS | macOS Tahoe 26.6.2 |
| Hardware / OpenGL | Apple M1 Pro, OpenGL 4.1 (Core Profile) |

### Active Python plugins

| Plugin | Version |
|---|---|
| MetaSearch | 0.3.6 |
| db_manager_community | 1.0.1 |
| grassprovider | 2.12.99 |
| processing | 2.12.99 |

## Notes

- GeographicLib "No support" is expected for this build. Ellipsoidal measurements use PROJ.
- 4.2 is a regular release. QGIS 4.4 is in feature freeze as of this date, so check for an update and log it here when upgrading.

## Change log

| Date | Change |
|---|---|
| 2026-11-08 | Initial install, QGIS 4.2.3 |
| 2026-11-08 | Smoke test passed (Python console, GDAL, PROJ/EPSG:2964, GDAL + GRASS providers) |
| 2026-11-09 | Created EESD QGIS profile; profile picker set at startup |
| 2026-11-09 | Verified core plugins active in EESD profile (processing, grassprovider, MetaSearch, db_manager_community) |
| 2026-11-09 | Downloaded QGIS sample data (Alaska) to 01_GIS-Spatial-Intelligence/data/raw/ (git-ignored); provenance in data/README.md |
