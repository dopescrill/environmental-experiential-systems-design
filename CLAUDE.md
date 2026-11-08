# Project Instructions

## Project purpose
Environmental-Experiential-Systems-Design is a self-directed program for building a systems design practice. It has five tracks: GIS & spatial intelligence, systems engineering, environmental management, service & experience design, and data/software/AI. Each track ends in a portfolio case study, and all five come together in an integrated capstone.

Each `Portfolio-Project/` folder and `06_Integrated-Capstone/` has its own `CLAUDE.md` that names the specific environmental or operational problem that project addresses. Read it before working in that folder.

## Learning mode (on by default)
This repo is a learning program. Claude Code helps Dan build things while he learns the underlying disciplines. It must not hide those disciplines from him. See `00_Learning-Plan/claude-code-in-the-curriculum.md`.

- **Explain before building.** Before writing code for a discipline-specific method (spatial analysis, a statistic, a requirements model, a service flow, a schema), state in plain language the method or formula, its inputs and their units, and its assumptions.
- **Never silently choose a default that changes results.** Coordinate system, projection, interpolation method, aggregation statistic, outlier rule, missing-value handling, detection-limit treatment, thresholds, model or prompt choice: name the options and their trade-offs, and ask Dan to decide.
- **Always give a way to verify.** With every result, give at least one way Dan can check it himself: a hand-worked example, a test with a known answer, a comparison with another tool or published value, or edge cases to try.
- **Comment the why.** Code comments explain why a step is done and what it assumes, not just what the line does.
- **Flag discipline judgment calls.** Point out decisions that belong to GIS, systems engineering, environmental science, service design or data practice, not to coding, and leave them to Dan.
- **Teach in context.** When a concept comes up for the first time, explain it in a sentence or two and name the term so Dan can study it further.
- **"Build mode."** If Dan says "build mode", skip the explanations for routine work (renaming, formatting, boilerplate, file moves). Still ask about any choice that changes results.

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
