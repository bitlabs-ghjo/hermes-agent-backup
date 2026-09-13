---
name: ai-crew-role-design
description: "Use when designing or onboarding specialized AI staff."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ai-crew, bots, profiles, role-design, soul, onboarding, slack]
---

# AI Crew Role Design

Design and onboard durable, role-separated AI staff for a company or team. Use this for executives, chiefs of staff, research analysts, marketers, project managers, and other recurring organizational roles—not for one-off task personas.

## When to Use

Use this skill when the user wants to:

- define a durable AI employee, specialist, executive assistant, or crew member
- interview for and author a role-specific SOUL.md and operating charter
- create an isolated Hermes profile for an organizational role
- establish reporting lines, evidence standards, approval boundaries, and confidentiality
- expose a specialist profile as a distinct Slack bot or other messaging identity

Do not use it for a temporary role-play prompt or a single delegated task.

## Supporting files

- `references/hermes-slack-profile-onboarding.md` — proven Hermes profile + distinct Slack bot workflow, security boundaries, and verification.
- `references/profile-assignment-handoff.md` — durable real-profile assignment packets, observable handoff states, artifact verification, and timeout-safe recovery.
- `templates/role-interview.md` — staged interview checklist for identity, outcomes, authority, reporting, evidence, and security.
- `templates/soul-role.md` — reusable SOUL.md and ROLE.md structure.

## Core design principle

Treat each crew member as an independently governed worker:

- **SOUL.md** defines who the agent is, how it communicates, what it challenges, and durable standing behavior.
- **ROLE.md** is the human-readable operating charter: duties, deliverables, reporting line, authority, workflows, and security.
- **Profile metadata** supplies name, title, and routing description.
- **Skills and toolsets** define capability.
- **Credentials and platform bots** define actual access and external identity.

Do not collapse all of these into a long generic persona prompt.

## Workflow

### 1. Establish the organization before the role

Capture only facts needed to shape the worker:

- organization, mission, products, customers, maturity, geography
- executive owner and reporting chain
- existing systems of record
- sensitive information classes

Do not invent missing company facts. Keep profile facts in memory where appropriate; keep the agent’s identity in SOUL.md.

### 1a. Check portfolio fit before creating another worker

Inventory the existing crew and map each worker's inputs, outputs, and handoffs before interviewing for a new role. Recruit for a recurring bottleneck, not merely because a familiar department title is missing.

A separate worker is justified when it has:

- a distinct, recurring outcome and measurable success criteria
- inputs it owns and outputs another worker or human consumes
- a clear manager, approval path, and confidentiality boundary
- enough recurring work to merit separate memory and operating context

If the proposed role mostly repeats an existing worker's duties, extend that worker's ROLE.md or skills instead of adding another profile. In small organizations, excess agents create review and coordination overhead.

A useful sequencing test is:

1. **Coordination:** calendar, approvals, commitments, information flow
2. **Discovery:** market, policy, customer, and product research
3. **Revenue:** lead qualification, proposals, partnerships, pipeline
4. **Delivery:** curriculum, implementation, production, quality assurance
5. **Amplification:** marketing and content after the offer and customer are sufficiently clear
6. **Control:** finance, legal, and compliance support with qualified human review where required

This is a diagnostic order, not a fixed org chart. Choose the next worker based on the current constraint. Distinguish discovery from execution—for example, a research worker may find a grant, while a proposal specialist owns the application package. Define the handoff explicitly.

### 2. Interview in focused rounds

Use 4–5 questions per round. Prefer selectable defaults for operational choices and open questions for business context.

Round 1 — outcomes and scope:

- What result makes this role successful?
- What recurring work products are required?
- Who receives the work first?
- What is explicitly out of scope?

Round 2 — standards and initiative:

- Which sources or systems are authoritative?
- What evidence quality and citation standard is required?
- Does the agent work proactively, on a schedule, or only on request?
- What should happen when evidence is insufficient?

Round 3 — authority and identity:

- What may happen without approval?
- Which writes, messages, submissions, purchases, or commitments need explicit approval?
- What information is confidential?
- How should the agent address people and describe itself?

Resolve ambiguous answers before writing. If a combined question receives only one value, ask which part it answers rather than silently applying it to both.

### 3. Convert answers into explicit controls

Write observable rules, not personality adjectives alone.

Weak:

> Be a careful analyst.

Strong:

> Verify the official source, distinguish fact from inference, cite the source URL and checked date, and escalate when eligibility remains uncertain.

At minimum encode:

- mission and success criteria
- core responsibilities and required outputs
- reporting path
- proactive vs request-only behavior
- source hierarchy and verification standard
- communication style and challenge behavior
- unapproved action boundary
- approval protocol for external state changes
- confidentiality classes
- uncertainty and escalation behavior

### 4. Separate identity from operating detail

SOUL.md should remain readable and durable across sessions. ROLE.md may be more procedural and can include checklists and report schemas. Important authority and security boundaries should appear in both so the live agent cannot miss them.

Do not rely on ROLE.md being injected automatically. Hermes loads the profile’s SOUL.md as primary identity; duplicate critical role boundaries there.

### 5. Create a fresh profile by default

For a specialist worker, prefer a fresh profile. Avoid full cloning from an executive or chief-of-staff profile because it can copy irrelevant memory, secrets, OAuth state, and authority.

After creation:

1. Write SOUL.md and ROLE.md.
2. Set the model/provider deliberately.
3. Enable only role-relevant skills and toolsets.
4. Share or add credentials only when required.
5. Verify the profile can start and accurately state its name, title, and reporting line.

A successful file write is not sufficient verification. Run a one-shot identity probe or open the canonical Bot Chat.

### 6. Apply least privilege

Start with research and drafting access. Add external write capabilities only when the role needs them.

Default approval boundary for business crew:

- autonomous: read, search, classify, analyze, draft, recommend
- explicit approval: send, publish, submit, create/update/delete records, share files, change permissions, spend money, sign, or commit the company

Make approval payloads complete. For a message, show recipients, subject, full body, attachments, and material effects. A changed payload requires renewed approval.

### 7. Design reporting, not just output

Specify who sees the work first and what happens next. Examples:

```text
Researcher → Chief of Staff → Executive
Marketing → Chief of Staff → Executive approval → Publish
```

The worker should lead with deadlines, risks, blockers, and decisions required—not bury them at the end of a report.

### 7a. Make cross-agent assignments observable

A reporting line on paper does not make work visible to the manager. When an executive assigns work directly to a specialist profile:

1. Inspect that specialist’s own durable session/task state rather than the manager’s in-process delegation list alone.
2. Confirm the exact request received, current execution state, expected deliverable, and whether a final artifact exists.
3. Distinguish a handoff to the real specialist profile from an internal subagent merely prompted to imitate that specialist’s role. Do not report the latter as profile-to-profile delegation.
4. Reconcile the commitment into the organization’s task system as a `waiting` item with the real owner and source provenance. Leave deadline and review date unset when the executive did not provide them; surface the omission instead of guessing.
5. Close the waiting item only after the deliverable is received and reviewed, not merely when a delegation process reports completion.
6. For complex source material, send a file-backed assignment packet to the specialist’s real profile and require an absolute artifact path; see `references/profile-assignment-handoff.md`.
7. If the profile run times out, inspect the expected artifact, active process, and durable specialist state before retrying. A timed-out caller can coexist with a successfully written artifact, and a blind retry can duplicate work or reports.

A useful status report separates **request confirmed**, **work running**, **deliverable produced**, **managerial review complete**, and **authorized report delivered**. These are different states. When a platform lacks readback access, distinguish “send command accepted” from “post independently verified.”

### 8. Add a distinct messaging identity only when needed

A separate Hermes profile does not automatically become a separate Slack user. A distinct `@Name` requires a distinct Slack app, bot token, app token, and profile-scoped gateway configuration.

Follow `references/hermes-slack-profile-onboarding.md` and keep platform credentials out of chat transcripts.

Validate the human allowlist before declaring the worker ready: Slack Member IDs are not DM/channel IDs. If the bot is connected but silent, inspect its profile-scoped logs for authorization rejection before changing tokens, reinstalling the app, or testing the model. Compare only non-secret allowlist values against a trusted operator identity; do not infer identity from display names. Correcting an allowlist changes access permissions and needs the applicable explicit approval. Distinguish configuration saved, process running, Socket Mode connected, authorized message accepted, response delivered, and restart persistence—none proves the next. When an operator posts `@Specialist` inside the manager's DM, explain the routing rather than impersonating the specialist or claiming a handoff.

### 8a. Make staff visually distinguishable in messaging

For bitlabs, preserve the approved character portraits and requested name labels, but give each worker a distinct full-background color. The user found identical backgrounds hard to distinguish in Slack messages; a shared name-band color or thin colored border alone is not enough. Keep typography and composition consistent while varying the dominant background. Enlarge faces rather than shrinking an entire employee badge into an avatar. Do not rely on tiny name text or color alone for identity.

Read `references/staff-avatar-qa.md` when preparing or revising profile icons. Verify a contact sheet at actual small-message sizes as well as the full-resolution exports before delivery.

### 8b. Resume onboarding after approval interruptions

A protected-file approval timeout is not consent. Stop the blocked write and do not route around it through a different tool. Explain the incomplete stage and request explicit renewed approval. Once the user renews approval, retry through the normal guarded tool, finish both SOUL.md and ROLE.md, and run a no-tools identity probe that checks name, role, reporting line, and external-send approval policy. Do not recreate an existing profile or copy another worker's credentials to make the probe pass. Report profile creation, identity verification, manifest preparation, and live Slack connection as separate readiness states.

## Verification checklist

- [ ] Profile exists under the intended Hermes data root.
- [ ] SOUL.md names the agent, organization, role, and reporting line.
- [ ] ROLE.md matches the interview and does not contradict SOUL.md.
- [ ] Model/provider is configured and an identity probe succeeds.
- [ ] No executive memory or credentials were copied unintentionally.
- [ ] Skills/toolsets match duties and exclude unnecessary write access.
- [ ] External actions have an explicit approval protocol.
- [ ] Confidential information classes are named.
- [ ] If Slack is required, the app has a unique bot identity and its own credentials.
- [ ] Gateway health and a real DM or mention are verified before claiming onboarding complete.

## Pitfalls

- **Role without authority boundaries:** produces a capable agent that cannot tell drafting from acting.
- **SOUL-only documentation:** detailed procedures become hard to audit; keep ROLE.md too.
- **ROLE-only documentation:** Hermes may not inject it; repeat critical controls in SOUL.md.
- **Clone-all convenience:** leaks authority, memory, or credentials across roles.
- **Unverified creation:** profile files can exist while inference provider or gateway is unconfigured.
- **One Slack app for two names:** profiles stay distinct internally but Slack still exposes one bot identity.
- **Duplicate Slack slash commands:** multiple apps in one workspace may conflict; prefer DMs/mentions for secondary bots or deliberately namespace/remove duplicate commands.
- **Manifest overwritten during setup:** `gateway setup` may regenerate a default manifest; run the final branded manifest generation after setup and verify its name before delivery.
- **Credentials pasted into chat:** never echo them; use a masked PTY or secret store, advise message deletion, and recommend rotation when exposure is uncertain.
- **Process-only gateway check:** a PID does not prove Slack is connected; verify the profile, bot identity, workspace, Socket Mode state, and then a real authorized DM/mention.
- **Automatic routines despite request-only policy:** do not create cron jobs unless the interview explicitly authorizes proactive work.
