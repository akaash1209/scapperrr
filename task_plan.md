# B.L.A.S.T. Task Plan

## 🟢 Protocol 0: Initialization [COMPLETED]
- [x] Create `task_plan.md` (Phases, goals, checklists)
- [x] Create `findings.md` (Research, discoveries, constraints)
- [x] Create `progress.md` (What was done, errors, tests, results)
- [x] Initialize `claude.md` as the Project Constitution (Data schemas, Behavioral rules, Architectural invariants)
- [x] Halt Execution: Strictly forbidden from writing in `tools/` until Discovery, Data Schema, and Blueprint are approved

## 🏗️ Phase 1: B - Blueprint (Vision & Logic) [COMPLETED]
- [x] Discovery: Ask North Star question
- [x] Discovery: Ask Integrations question
- [x] Discovery: Ask Source of Truth question
- [x] Discovery: Ask Delivery Payload question
- [x] Discovery: Ask Behavioral Rules question
- [x] Data-First Rule: Define the JSON Data Schema (Input/Output shapes) in `gemini.md`
- [x] Ensure Payload shape is confirmed before coding
- [x] Research: Search github repos and other databases for helpful resources

## ⚡ Phase 2: L - Link (Connectivity) [PENDING]
- [ ] Verification: Test all API connections
- [ ] Verification: Test all `.env` credentials
- [ ] Handshake: Build minimal scripts in `tools/`
- [ ] Handshake: Verify external services are responding correctly
- [ ] Verification Gate: Do not proceed to full logic if the "Link" is broken

## ⚙️ Phase 3: A - Architect (The 3-Layer Build) [PENDING]
- [ ] Layer 1 (`architecture/`): Write Technical SOPs in Markdown for tools
- [ ] Layer 1 (`architecture/`): Define goals, inputs, tool logic, and edge cases
- [ ] Layer 1 (`architecture/`): Establish Golden Rule (update SOP before code on logic change)
- [ ] Layer 2 (Navigation): Route data between SOPs and Tools logically
- [ ] Layer 2 (Navigation): Enforce reasoning layer (call tools in order, do not guess at business logic)
- [ ] Layer 3 (`tools/`): Write deterministic, atomic, testable Python scripts
- [ ] Layer 3 (`tools/`): Ensure env variables/tokens are stored and retrieved from `.env`
- [ ] Layer 3 (`tools/`): Ensure all intermediate file operations use `.tmp/`

## ✨ Phase 4: S - Stylize (Refinement & UI) [COMPLETED]
- [x] Payload Refinement: Format all outputs (Slack blocks, Notion layouts, Email HTML) for professional delivery
- [x] UI/UX: Apply clean CSS/HTML and intuitive layouts for dashboard/frontend
- [x] Feedback: Present the stylized results to the user for feedback before final deployment

## 🛰️ Phase 5: T - Trigger (Deployment) [PENDING]
- [ ] Cloud Transfer: Move finalized logic from local testing to the production cloud environment
- [ ] Automation: Set up execution triggers (Cron jobs, Webhooks, or Listeners)
- [ ] Documentation: Finalize the Maintenance Log in `gemini.md` for long-term stability

## 🛠️ Operating Principles Observance [ONGOING]
- [x] Data-First: Data Schema defined before Tools
- [x] Routine: Update `progress.md` with what happened and errors after any meaningful task
- [x] Routine: Store discoveries in `findings.md`
- [x] Rigidity: Only update `gemini.md` when schema changes, a rule is added, or architecture is modified
- [ ] Self-Annealing Loop: Analyze (Read stack trace/error, do not guess)
- [ ] Self-Annealing Loop: Patch (Fix the Python script in `tools/`)
- [ ] Self-Annealing Loop: Test (Verify the fix works)
- [ ] Self-Annealing Loop: Update Architecture (Update corresponding `.md` SOP in `architecture/` so the error never repeats)
- [ ] Manage Deliverables: Ensure ephemeral logs go to `.tmp/` and global variables go to Cloud. Project complete only when payload is deployed.
