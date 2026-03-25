# Project Constitution

## Data Schemas
(To be defined in gemini.md)

## Behavioral Rules
- Prioritize reliability over speed.
- Never guess at business logic.
- Data-First: Define JSON Data Schema before coding.
- Self-Annealing: Analyze, Patch, Test, Update Architecture.

## Architectural Invariants
- 3-Layer Architecture: Architecture (SOPs), Navigation (Decision Making), Tools (Deterministic scripts).
- Logic changes update SOP before code.
- Tools are deterministic Python scripts within `tools/`.
- Temporary workbench operations stay in `.tmp/`.
