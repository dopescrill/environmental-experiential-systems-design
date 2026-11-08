# 02 · Systems Engineering

| Folder | Holds |
|---|---|
| `Courses/` | Notes, syllabi and coursework from courses in this track |
| `Diagrams/` | Practice work for this track |
| `Portfolio-Project/` | The case study this track produces |

## How Claude Code fits
Generate and maintain architecture diagrams, requirements, and technical documentation.

Claude Code builds things here while I learn the discipline. It does not replace the discipline. See [`../00_Learning-Plan/claude-code-in-the-curriculum.md`](../00_Learning-Plan/claude-code-in-the-curriculum.md).

### What I must understand myself
- What makes a requirement good: necessary, unambiguous, testable, traceable
- System boundaries, context diagrams, and stakeholders
- Functional vs non-functional requirements
- The V-model and verification vs validation
- Interfaces and how components depend on each other

### How to verify
- Trace each requirement to a component and to a test (a traceability matrix)
- Review diagrams against the actual build, not against the previous diagram
- Have each requirement answer: how would I test this?
- Check that documentation and code changed together

### Starter exercises
| Exercise | Build with Claude Code | Understand yourself | Verify |
|---|---|---|---|
| **Requirements with traceability** | Claude Code drafts a requirements document with IDs (REQ-001…) from a problem statement. | Requirement quality; which requirements are really design choices. | Rewrite any untestable requirement; build the traceability matrix yourself. |
| **Architecture diagrams as code** | Claude Code generates Mermaid context and component diagrams and updates them when the system changes. | Levels of abstraction (context, container, component). | Walk the diagram against the code or system; mark anything stale. |
| **Interface specification** | Claude Code drafts an interface spec (inputs, outputs, errors) between two components. | Contracts, failure modes, versioning. | Write two test cases per interface from the spec alone. |

Record each exercise with [`../00_Learning-Plan/templates/exercise-template.md`](../00_Learning-Plan/templates/exercise-template.md).
