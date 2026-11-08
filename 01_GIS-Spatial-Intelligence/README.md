# 01 · GIS & Spatial Intelligence

| Folder | Holds |
|---|---|
| `Courses/` | Notes, syllabi and coursework from courses in this track |
| `Exercises/` | Practice work for this track |
| `Portfolio-Project/` | The case study this track produces |

## How Claude Code fits
Python scripts, geospatial data processing, spatial analysis automation.

Claude Code builds things here while I learn the discipline. It does not replace the discipline. See [`../00_Learning-Plan/claude-code-in-the-curriculum.md`](../00_Learning-Plan/claude-code-in-the-curriculum.md).

### What I must understand myself
- Coordinate reference systems (CRS) and projections, and how projection distortion affects distance and area
- Vector vs raster data models, and when each is appropriate
- Spatial joins, overlays, buffers, and what each one actually computes
- Data provenance: scale, resolution, accuracy and date of each layer
- Cartographic choices (classification, color, scale) and how they shape interpretation

### How to verify
- Run the same operation in QGIS and compare outputs
- Calculate areas and distances in an equal-area or local projected CRS, never in degrees
- Spot-check a few features by hand on a map
- Check feature counts before and after each step for unexpected drops or duplicates

### Starter exercises
| Exercise | Build with Claude Code | Understand yourself | Verify |
|---|---|---|---|
| **Reproject and clip** | Claude Code writes a GeoPandas script to reproject and clip layers to a study area. | Why this CRS; what clipping does to features at the boundary. | Compare with QGIS; check CRS metadata and feature counts. |
| **Buffer and overlay statistics** | Claude Code builds a script that buffers features (e.g. streams) and summarizes what falls inside (e.g. land cover). | Buffer distance units, overlay types, area calculation. | Calculate one buffer's area by hand; confirm units are metres. |
| **Batch-processing automation** | Claude Code turns a manual workflow into a repeatable script that runs over a folder of files. | Which steps are safe to automate and which need human review. | Run on one file manually and with the script; compare outputs. |

Record each exercise with [`../00_Learning-Plan/templates/exercise-template.md`](../00_Learning-Plan/templates/exercise-template.md).
