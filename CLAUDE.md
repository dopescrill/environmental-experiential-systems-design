# Project Instructions

## Project purpose
Environmental-Experiential-Systems-Design is a self-directed program for building a systems design practice. It has five tracks: GIS & spatial intelligence, systems engineering, environmental management, service & experience design, and data/software/AI. Each track ends in a portfolio case study, and all five come together in an integrated capstone.

Each `Portfolio-Project/` folder and `06_Integrated-Capstone/` has its own `CLAUDE.md` that names the specific environmental or operational problem that project addresses. Read it before working in that folder.

## Development principles
- Explain the approach before substantial changes.
- Prefer simple, maintainable architecture.
- Keep existing functionality working.
- Avoid unnecessary dependencies.
- Use clear naming and documentation.

## Data principles
- Document data sources and assumptions.
- Never invent environmental measurements.
- Protect private and confidential information.
- Validate AI-generated outputs.

## Development workflow
- Inspect before editing.
- Break work into small tasks.
- Explain files changed.
- Run appropriate tests.
- Summarize remaining risks and limitations.

## Portfolio documentation
Record:
- Problem being addressed
- Design decisions
- Technical architecture
- Tools used
- What was tested
- Known limitations

## Repository conventions
- Folders: numbered prefix + Title-Case-With-Hyphens, no spaces.
- Dated files: `YYYY-MM-DD_short-description.ext`.
- Large or raw data stays out of git (see `.gitignore`). Put it in a `data/` subfolder and record its source in that folder's README.
