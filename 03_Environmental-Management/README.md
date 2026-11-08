# 03 · Environmental Management

| Folder | Holds |
|---|---|
| `Courses/` | Notes, syllabi and coursework from courses in this track |
| `Field-Research/` | Practice work for this track |
| `Portfolio-Project/` | The case study this track produces |

## How Claude Code fits
Build environmental data-processing and monitoring tools.

Claude Code builds things here while I learn the discipline. It does not replace the discipline. See [`../00_Learning-Plan/claude-code-in-the-curriculum.md`](../00_Learning-Plan/claude-code-in-the-curriculum.md).

### What I must understand myself
- Units and unit conversion for each measured parameter
- Sampling design: frequency, location, representativeness and bias
- Detection limits, censored data and QA/QC flags
- Which regulatory threshold or guideline applies, and where it comes from
- How to handle missing data without hiding it

### How to verify
- Calculate at least one result by hand (a spreadsheet is fine)
- Confirm units at input and output
- Compare against published reference values or agency summaries where they exist
- Test edge cases: empty periods, single readings, values at the detection limit, outliers
- Never fill a gap with an invented measurement; document it instead

### Starter exercises
| Exercise | Build with Claude Code | Understand yourself | Verify |
|---|---|---|---|
| **Monitoring data loader** | Claude Code writes a loader that reads a monitoring CSV, standardizes units and flags QA issues. | Parameter units, QA/QC flags, metadata. | Check five rows by hand against the raw file. |
| **Summary statistics by site and period** | Claude Code calculates monthly or seasonal statistics per site (see the worked example in the curriculum doc). | Mean vs median, minimum sample size, censored values. | Hand-calculate one site-period; test the edge cases. |
| **Threshold-exceedance alerts** | Claude Code builds a simple tool that flags readings over a regulatory threshold. | Which threshold applies and why; acute vs chronic criteria. | Confirm the threshold value and its citation; test values just above and below it. |

Record each exercise with [`../00_Learning-Plan/templates/exercise-template.md`](../00_Learning-Plan/templates/exercise-template.md).
