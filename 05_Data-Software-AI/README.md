# 05 · Data, Software & AI

| Folder | Holds |
|---|---|
| `Courses/` | Notes, syllabi and coursework from courses in this track |
| `Python/` | Scripts and notebooks |
| `SQL/` | Queries, schemas, practice databases |
| `AI-Experiments/` | Prompting, model and tooling experiments |
| `Portfolio-Project/` | The case study this track produces |

## How Claude Code fits
Build databases, applications, APIs, dashboards, and AI-assisted workflows.

Claude Code builds things here while I learn the discipline. It does not replace the discipline. See [`../00_Learning-Plan/claude-code-in-the-curriculum.md`](../00_Learning-Plan/claude-code-in-the-curriculum.md).

### What I must understand myself
- Data modeling and normalization; keys and relationships
- SQL joins and aggregation, well enough to write them by hand
- API design: resources, methods, status codes, errors
- Dashboard design: which question each chart answers
- How to evaluate AI output: an evaluation set, failure cases, and what 'good enough' means

### How to verify
- Write some of the queries yourself and compare with Claude Code's
- Add automated tests for the core logic
- Check dashboard numbers against a direct query
- Score AI outputs against a small, hand-labelled evaluation set

### Starter exercises
| Exercise | Build with Claude Code | Understand yourself | Verify |
|---|---|---|---|
| **Database schema** | Claude Code designs a schema (SQLite or Postgres) for an environmental dataset. | Normalisation, keys, constraints. | Draw the ER diagram yourself first; write three queries by hand. |
| **API and dashboard** | Claude Code builds a small API over the database and a dashboard on top of it. | Endpoints, error handling, chart choice. | Compare dashboard figures with direct SQL; test bad requests. |
| **AI-assisted workflow with evaluation** | Claude Code builds a workflow that uses an AI model (e.g. classifying field notes) plus an evaluation script. | Prompt design, failure modes, evaluation metrics. | Hand-label 20 examples; measure accuracy; review every error. |

Record each exercise with [`../00_Learning-Plan/templates/exercise-template.md`](../00_Learning-Plan/templates/exercise-template.md).
