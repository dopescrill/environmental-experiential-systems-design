"""
Datum shift check: NAD27 (EPSG:2964) -> WGS 84 (EPSG:4326) in Alaska.

Run inside the QGIS Python Console (EESD profile):
    exec(open("/Users/danielmeier/Documents/Environmental-Experiential-Systems-Design/01_GIS-Spatial-Intelligence/Exercises/2026-11-08_qgis-setup-and-crs/datum_shift_check.py").read())

What it does:
1. Lists every transformation PROJ knows between the two CRSs, and whether
   its grid file is installed.
2. Takes one test point (downtown Anchorage, in EPSG:2964 feet).
3. Converts it two ways:
   - "ballpark": projection math only, NAD27 lat/lon treated as if it were WGS 84
     (what QGIS falls back to when the grid is missing)
   - "accurate": the NOAA Alaska grid shift (us_noaa_alaska.tif)
4. Prints how far apart the two answers are, in meters.
"""
from qgis.core import (
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsDatumTransform,
    QgsDistanceArea, QgsPointXY, QgsProject,
)

src = QgsCoordinateReferenceSystem("EPSG:2964")      # NAD27 / Alaska Albers (US ft)
wgs84 = QgsCoordinateReferenceSystem("EPSG:4326")    # WGS 84 lat/lon
nad27 = QgsCoordinateReferenceSystem("EPSG:4267")    # NAD27 lat/lon (no datum change)
ctx = QgsProject.instance().transformContext()

# 1. Available operations
print("Transformations EPSG:2964 -> EPSG:4326")
grid_op = None
for op in QgsDatumTransform.operations(src, wgs84):
    grids = ", ".join(g.shortName for g in op.grids) or "none"
    status = "available" if op.isAvailable else "MISSING GRID"
    print(f"  [{status}] accuracy {op.accuracy} m | grids: {grids} | {op.name}")
    if any(g.shortName == "us_noaa_alaska.tif" for g in op.grids):
        grid_op = op

# 2. Test point: downtown Anchorage, EPSG:2964 coordinates (feet)
pt = QgsPointXY(719677.93, 4118486.11)

# 3a. Ballpark: NAD27 lat/lon, labeled as if it were WGS 84
ballpark = QgsCoordinateTransform(src, nad27, ctx).transform(pt)

if grid_op is None or not grid_op.isAvailable:
    print("\nThe us_noaa_alaska.tif grid isn't installed yet, so there's no accurate result to compare.")
    print(f"Ballpark lon/lat: {ballpark.x():.6f}, {ballpark.y():.6f}")
else:
    # 3b. Accurate: force the grid-based operation, no silent fallback
    ct = QgsCoordinateTransform(src, wgs84, ctx)
    ct.setCoordinateOperation(grid_op.proj)
    ct.setAllowFallbackTransforms(False)
    accurate = ct.transform(pt)

    # 4. Distance between the two answers, on the WGS 84 ellipsoid
    d = QgsDistanceArea()
    d.setSourceCrs(wgs84, ctx)
    d.setEllipsoid("EPSG:7030")
    shift_m = d.measureLine(ballpark, accurate)

    print(f"\nBallpark lon/lat: {ballpark.x():.6f}, {ballpark.y():.6f}")
    print(f"Accurate lon/lat: {accurate.x():.6f}, {accurate.y():.6f}")
    print(f"Difference: {shift_m:.1f} m  ({shift_m * 3.28084:.0f} ft)")
