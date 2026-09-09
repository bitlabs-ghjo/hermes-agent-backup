---
name: conversational-task-management
description: "Use when building or operating task management through chat."
version: 0.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [tasks, gtd, chat, reminders, cron, slack]
    related_skills: [weekly-review-planning, google-workspace, notion]
---

# Conversational Task Management

Build and operate a trustworthy task system where users capture, clarify, review, and complete work through a messaging conversation. The chat is an interface; a durable task store is the system of record.

## When to Use

- A user wants to assign and manage tasks in Slack, Telegram, Discord, or another chat.
- A chat-based assistant must maintain GTD-style inbox, next actions, projects, waiting items, and reviews.
- Recurring task briefs or weekly reviews must be delivered back to a conversation.
- A previous task-management setup needs to be inspected or repaired.

Do not use this skill merely to extract action items from a single document or meeting; use `document-to-action-items` or `meeting-action-items` for those inputs, then hand resulting tasks to this workflow.

## Core Invariants

1. **Durable source of truth:** Never rely on conversation memory as the official task list. Use one declared database, task provider, or structured file.
2. **Chat is capture, not storage:** Record accepted tasks promptly and return a stable ID so later updates are unambiguous.
3. **No invented metadata:** Do not guess deadlines, owners, recurrence, confidentiality, or external recipients. Keep the item in Inbox or ask when ambiguity materially changes execution.
4. **Projects need next actions:** A multi-step outcome is not actionable until it has at least one concrete next action.
5. **Calendar is separate:** A `scheduled` task status does not prove a calendar event exists. Calendar writes require the applicable approval and readback.
6. **External action remains gated:** Tracking a task does not authorize sending messages, spending money, sharing documents, or changing third-party systems.
7. **Platform limits are explicit:** Do not imply passive access to all channel history. State exactly which routed messages, mentions, threads, or webhooks are captured.

## Procedure

### 1. Define the operating contract

Declare:

- authoritative task store and backup expectations;
- input surface and what messages are actually observable;
- timezone, active hours, review cadence, and reminder destinations;
- statuses, priorities, stable ID format, and required fields;
- approval boundary between recording work and executing it.

Prefer natural-language capture with optional compact syntax. Do not require users to learn a rigid command language before they can delegate work.

### 2. Design the task model

Minimum useful fields:

- stable ID;
- title / desired outcome;
- status: inbox, next, project, waiting, scheduled, someday, reference, done;
- project link and context;
- due time and defer/start time;
- waiting owner and next review time;
- priority, notes, source provenance;
- created, updated, and completed timestamps.

Use timezone-aware ISO 8601 timestamps internally. Preserve the user's natural-language phrasing in the title or notes while storing normalized metadata separately.

### 3. Build with vertical verification

For custom local tooling, follow strict TDD:

1. Write a failing capture test and see it fail.
2. Implement capture and stable IDs.
3. Add tests one behavior at a time for clarification/update, completion, listing, validation, and review grouping.
4. Run the full suite.
5. Exercise the production store separately and confirm its initial or migrated state.

A green unit suite is not enough: also run an end-to-end capture/list/complete or equivalent provider readback against the intended store.

### 4. Clarify each incoming item

For every routed task message:

1. Capture it before doing optional enrichment so it cannot be lost.
2. Decide whether it is actionable.
3. If one action, make the next physical/visible action explicit.
4. If multiple actions, create or link a project and ensure a next action exists.
5. If delegated, record `waiting_for` and a review/follow-up date.
6. If not currently actionable, classify as someday, reference, or discard proposal.
7. Return the stable ID, interpreted deadline/status, and any blocking question.

When the user says “complete G-…”, update exactly that record; do not infer completion from silence.

### 5. Add bounded automated reviews

A useful daily brief checks:

- overdue tasks;
- tasks due within the chosen horizon;
- waiting items whose review date has arrived;
- unprocessed Inbox items;
- active projects without a next action.

A useful weekly review additionally covers completion evidence, stalled commitments, the next 7–14 days, capacity, and consciously deferred work. Load `weekly-review-planning` for the full review procedure.

Cron prompts must be self-contained because scheduled runs begin without chat context. Include the task-store location/provider, timezone command, exact read-only commands, output order, prohibited writes, and empty-state behavior.

### 6. Verify scheduler activation, not just creation

After creating or changing scheduled jobs:

1. List jobs and read back the exact schedule, destination, work directory, and enabled state.
2. Check the gateway/scheduler for the correct profile or tenant.
3. Run one job manually when safe.
4. Confirm run status and delivery result.
5. If tool-reported scheduler state conflicts with a profile-aware process/status check, report the conflict and trust neither blindly; verify by a real test run.

Convert local-time schedules deliberately. Record both the user-facing timezone/cadence and the scheduler expression so daylight-saving or host-timezone assumptions are visible.

### 7. Report the usable interface

The completion report should lead with what the user can now say, then summarize automation and verification. Include:

- 4–6 natural-language examples;
- what is stored and how IDs work;
- automatic review schedule and destination;
- verified test/run results;
- current task count;
- any channel-observability or approval limitation.

Avoid flooding the user with implementation internals unless needed for maintenance.

## Failure Modes and Corrections

- **Claiming “all channel messages are managed” without API/history access:** narrow the promise to messages actually routed to the assistant.
- **Scheduling without runtime verification:** a persisted cron record may never fire; verify scheduler/gateway and perform a safe manual run.
- **Treating task assignment as execution authorization:** record the task, but preserve approval gates for external side effects.
- **Putting every task on the calendar:** reserve the calendar for hard date/time constraints.
- **Project records with no next action:** flag them in every review until clarified or paused.
- **Silent date normalization:** echo the interpreted date, time, and timezone when recording it.
- **Mutable human-readable titles as identifiers:** return stable IDs and require them for destructive or ambiguous changes.

## Verification Checklist

- [ ] The source of truth is durable and documented.
- [ ] Capture returns a stable ID.
- [ ] All timestamps are timezone-aware.
- [ ] Every active project has a next action or is flagged.
- [ ] Waiting items have owners and review dates when available.
- [ ] Unit tests failed first and now pass.
- [ ] Production-store behavior was exercised.
- [ ] Scheduled jobs were listed/read back and manually test-run where safe.
- [ ] Delivery destination and channel-access limitations are stated accurately.
- [ ] External side effects remain approval-gated.

## References

- `references/bitlabs-slack-gtd.md` — verified example of a SQLite-backed Slack GTD setup with cron reviews and profile-aware scheduler validation.
