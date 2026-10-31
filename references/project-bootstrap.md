# Empty-project bootstrap

For a new/empty website repository, finish a reviewable planning baseline before application code. For an established project, map to its existing files instead of renaming or duplicating them. User instructions and governing workflow/review gates determine when implementation can begin; prior approval remains valid. Ask only consequential unknowns and label assumptions. Do not invent approved requirements, chosen branding or implemented features.

## Compact mode

For a small site or single-slice feature, use one `PLAN.md` (or an existing equivalent) plus the project's normal README/setup instructions. Keep the goal, pages/flow, design decision, dependencies, feature acceptance/evidence and next action in that one record. Do not create sprint folders, separate testing manifests or four root briefs merely to follow a template. A one-line fix reuses existing context and needs no new plan file.

Use expanded mode below when multiple slices, roles or data contracts need independent records. Split a compact record only when its growing content has distinct owners or becomes difficult to maintain; preserve links and one source per fact. Existing repository conventions win in both modes.

## Expanded project shape

```text
README.md
PROJECT.md
PRODUCT.md
DESIGN.md
docs/
  sprint-plan.md
  testing.md
  sprints/
    S01.md
tests/
  sprints/
    S01/
      README.md
# application folders follow the selected stack after planning
```

These case-sensitive names are defaults for expanded mode. If the user specifies different names, use those consistently. Create records/folders for the first actionable sprint now; create later ones when activated, not empty placeholder trees. A test README is a plan, not executable coverage.

## One owner per fact

| File | Owns | Keep out |
| --- | --- | --- |
| README.md | What exists, local setup/access, actual run commands and links to planning/status | Duplicated specs, invented live URL or commands |
| PROJECT.md | Selected stack, architecture/folder map, conventions, environment names, deployment/testing workflow | Secrets and repeated product/design prose |
| PRODUCT.md | Problem, users/roles, critical flow, MVP/non-goals and observable acceptance; ownership/permissions for systems | Future features described as shipped |
| DESIGN.md | Approved/proposed visual direction, tokens, type, layout, components/states, responsive/accessibility rules | A second competing design system in docs/ |
| docs/sprint-plan.md | Whole agreed MVP as ordered, dependency-aware vertical slices; the single status ledger and current handoff | Detailed implementation logs |
| docs/testing.md | Real test commands, test-discovery layout, environments and overall verification expectations | Copies of every test result |
| docs/sprints/S01.md | Sprint goal, scope, acceptance checklist, changes, verification evidence and next action | Repeated global specs |
| tests/sprints/S01/README.md | Acceptance-to-test map, how to run, coverage gaps | Claims that planned tests passed |

Prefer roughly 100-250 words per root brief, 150-300 per sprint record, and a short tracker table. These are editing targets, not limits that remove critical rules. Link instead of repeating. When setup or a decision is unknown, write "pending" with the needed decision; verify commands after the runtime is scaffolded.

Add docs/decisions.md only for consequential decisions worth retaining; add a backlog or architecture/security/integration document only when its content earns a separate file. Don't copy game-specific documents or generate empty manuals.

## Sprint ledger and live updates

Use a compact table: ID, outcome, acceptance summary, dependencies, status, record/tests. Plan the full MVP without fixed sprint counts or invented dates; optional expansion stays outside MVP. Each slice should produce a small usable flow, not separate disconnected UI and backend batches.

Statuses:
- Planned: scope drafted or dependencies pending.
- Ready: sufficiently defined and required approvals/inputs available.
- In progress: the single active implementation slice.
- Implemented: code exists; required verification or user review may remain. Record which checks passed separately.
- Done: acceptance evidence and required review complete.
- Blocked: concrete obstacle and smallest next action recorded.

At sprint start, update the active row and acceptance-to-test map before coding. During work, update checked acceptance and material blockers/scope decisions in the same change. After checks, record commands/outcomes and remaining limits; never infer user acceptance. At handoff, update the current sprint/next action and references. Don't append a diary entry for every tool call. Keep both ledger and detailed record consistent.

## Compact sprint record

Use this shape inside docs/sprints/S01.md; replace examples with real scope, not blank sections:

```markdown
# S01: <outcome>
Status: <status>
Goal: <one sentence>
Scope: <included work>; excludes <important boundary>
Depends on: <IDs or none>
Acceptance:
- [ ] <observable result>
- [ ] <relevant invalid/denied/failure behavior>
Tests: <link to tests/sprints/S01/README.md>
Changes: <short summary or not started>
Verification: <command/flow, result, environment; or not run>
Limits/blockers: <material limit or none known>
Next: <one concrete action or required review>
```

## Tests per sprint

In expanded mode, create tests/sprints/<ID>/ for each active sprint. Its README maps acceptance IDs to actual tests, commands and relevant manual checks, with pending coverage labelled. Compact mode keeps that mapping in its single plan and uses the normal project test layout. Place new executable sprint-specific tests in the sprint folder when compatible with the selected runner. Keep shared regression tests in their existing locations and reference them. Preserve prior sprint tests as regression coverage.

If the framework requires colocated tests or a different layout, keep the per-sprint folder as a manifest linking to those executable tests. Verify discovery/configuration so the intended tests actually run. Don't move an established suite only to fit this tree. A new test command must be checked, not guessed.

Test meaningful behavior and risk: successful user flow plus relevant invalid input, authorization, persistence, concurrency, timeout or recovery cases. Use existing runners and focused checks; a documentation typo doesn't need an artificial test. Record browser/device/provider coverage honestly. Keep heavy captures, private payloads and logs out of published docs; link to safe evidence where needed.

## Context budget

On continuation, read the ledger's current handoff, active sprint and only affected owning specs. Reuse unchanged context; don't reload every completed sprint or all four briefs for each edit. Update the existing evidence instead of producing duplicate reports. Minimal documentation means concise source-of-truth records, not omitted security, data integrity or acceptance criteria.
