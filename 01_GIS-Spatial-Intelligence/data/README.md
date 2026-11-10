# Data

Raw data for the GIS track lives in `data/raw/`, which is **ignored by git** (`**/data/raw/` in the repo `.gitignore`). Only this README is committed. Anyone cloning the repo can rebuild `data/raw/` from the sources listed here.

## Datasets

### QGIS sample data (Alaska dataset)

| Field | Value |
|---|---|
| Local path | `data/raw/qgis-sample-data/qgis_sample_data/` |
| Source | https://github.com/qgis/QGIS-Sample-Data/archive/master.zip |
| Downloaded | 2026-11-09 |
| Size | ~86 MB unzipped |
| Purpose | Examples and exercises from the QGIS User Manual |
| Default CRS | Alaska Albers Equal Area, NAD27, US survey feet (EPSG:2964), unless noted below |
| Licenses | Mixed. Each source keeps its own license (see the dataset's own `README.md`). GADM regions are free for academic and non-commercial use only. **Do not reuse this data in client or commercial work.** |

**Contents**

| Folder | What's inside | Format | Notes |
|---|---|---|---|
| `shapefiles/` | VMAP0 layers: alaska, airports, builtups, grassland, lakes, landice, majrivers, pipelines, popp, railroads, rivers, storagep, swamp, trails, trees, tundra, plus GADM `regions` | Shapefile | `.prj` files are ESRI WKT with no EPSG code. Check how QGIS identifies the CRS (exercise for step 5). |
| `raster/` | AVHRR land cover (`landcover.img`) and Natural Earth hillshade (`SR_50M_alaska_nad.tif`) | ERDAS IMG, GeoTIFF | Land cover color table included |
| `grassdata/alaska` | GRASS location with VMAP0 vectors and GTOPO30 elevation (~1 km grid) | GRASS database | Needs the GRASS provider |
| `climate/` | Points with 1971–2000 mean temperatures (°F): Jan, Jul, annual | Shapefile | For the diagram overlay exercises |
| `csv/` | `elevp.csv`: 150 random elevation points | Delimited text | For delimited-text import and interpolation |
| `gml/` | Alaska lakes | GML | |
| `gps/` | 4 national monuments | GPX | **WGS84 lat/lon (EPSG:4326), not 2964** |
| `point_cloud_testing_data/` | Korodvar, Croatia test point cloud | COPC (.laz) | Not Alaska. Different CRS. |
| `projects/` | `relations.qgs` example project | QGIS project | |

## Adding a dataset

For each new dataset, add a section here with the local path, source URL, download date, CRS, license, and any processing done before use. Raw files go in `data/raw/`. Never edit them in place; write derived outputs elsewhere.
