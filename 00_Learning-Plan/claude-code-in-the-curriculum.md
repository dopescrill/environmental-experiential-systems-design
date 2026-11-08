# Claude Code in the Curriculum

## The principle

**Claude Code helps me build things while I learn the underlying disciplines. It does not hide those disciplines from me.**

Claude Code can write the script, the schema, the diagram or the interface. I still need to understand:
- **the data:** where it came from, its units, how it was collected, and what is missing;
- **the method:** what is being calculated or designed, and why this approach fits;
- **the assumptions:** what has to be true for the result to mean anything;
- **the check:** how I would know if the result were wrong.

If I can't explain those four things for an exercise, the exercise isn't finished, even if the code runs.

## How Claude Code fits each learning area

| Learning area | How Claude Code fits |
|---|---|
| **01 · GIS & Spatial Intelligence** | Python scripts, geospatial data processing, spatial analysis automation |
| **02 · Systems Engineering** | Generate and maintain architecture diagrams, requirements, and technical documentation |
| **03 · Environmental Management** | Build environmental data-processing and monitoring tools |
| **04 · Service & Experience Design** | Turn Figma concepts and service workflows into functional interfaces |
| **05 · Data, Software & AI** | Build databases, applications, APIs, dashboards, and AI-assisted workflows |

Each track README has a **How Claude Code fits** section. It lists what I must understand myself, how to verify results, and some starter exercises.

## The exercise loop

Every practical exercise goes through the same five steps:

1. **Frame:** what question am I answering, and for whom? What would a useful answer look like?
2. **Understand:** learn the concept before building. Read the course material, look at the raw data, and write down the method and its assumptions in my own words.
3. **Build with Claude Code:** ask Claude Code to build it. In this repo it explains the method, inputs, units and assumptions *before* writing code (see "Learning mode" in the root `CLAUDE.md`).
4. **Verify yourself:** check the result without relying on Claude. Use at least one of these:
   - work one case by hand;
   - run a test with a known answer;
   - compare with another tool (QGIS, a spreadsheet, a published value);
   - check units and edge cases (empty data, zeros, outliers, missing values).
5. **Reflect:** record what Claude Code built, what I checked, what I learned, and what I still question.

Record each exercise with [`templates/exercise-template.md`](templates/exercise-template.md).

## Worked example: environmental statistics

**Task:** calculate monthly mean dissolved-oxygen readings from a water-quality monitoring CSV, and flag months below a threshold.

| Step | What happens |
|---|---|
| **Frame** | Who uses this? A watershed manager deciding where to sample next. They need monthly means per site and the months below threshold. |
| **Understand** | Look at the raw CSV first. Check: what units (mg/L or % saturation)? How often was it sampled, and is that even across months? What do missing values look like? Is there a detection limit? Which threshold applies, from which regulation or guideline, and does it differ by water body or season? |
| **Build** | Claude Code first explains its approach: group by site and month, take the mean, exclude missing values, and report the count of readings per month. It names the choices that change results (mean vs median, minimum readings per month, how to treat values below the detection limit) and asks me to decide. Then it writes the script, with comments explaining *why*. |
| **Verify** | Calculate one site-month by hand in a spreadsheet and compare. Check the units in the output. Test edge cases: a month with one reading, a month with none, a value at the detection limit. Check that the threshold value and its source are written in the README. |
| **Reflect** | Record that Claude Code wrote the script, that I chose the threshold and the treatment of values below the detection limit, and which checks I ran. Note the limitation: monthly means can hide short low-oxygen events. |

## What "learning mode" means for Claude Code

The root `CLAUDE.md` turns learning mode on for the whole repo. In short, Claude Code:
- explains the method, inputs, units and assumptions before writing discipline-specific code;
- never silently chooses a default that changes results;
- always gives me a way to verify the output;
- comments code to explain *why*;
- flags judgment calls that belong to the discipline, not to the code.

If I say **"build mode"**, Claude Code skips the explanations for routine work like renaming, formatting or boilerplate. It still asks about choices that change results.

## Portfolio honesty

Every portfolio project log records **How Claude Code was used** and **What I verified independently**. A case study should show clearly which judgments were mine, which parts AI built, and how I know the result is right.
