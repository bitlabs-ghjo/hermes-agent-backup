# Verified example: bitlabs Slack GTD

This reference captures the reusable shape of a working deployment built for a Korean executive-assistant workflow. It is implementation detail, not a universal path contract.

## Operating model

- Slack messages routed to the assistant are the capture surface.
- A local SQLite database is the authoritative task ledger.
- A dependency-free Python CLI performs capture, update, complete, list, show, and review operations.
- Stable IDs use `G-0001` style identifiers.
- Human-facing timezone is Asia/Seoul.
- External actions such as calendar creation and message sending remain separately approval-gated.

## Task schema

The validated schema stored title, status, project, context, due time, defer time, waiting owner, review time, priority, notes, source, and created/updated/completed timestamps. Statuses were inbox, next, project, waiting, scheduled, someday, reference, and done.

## Review query behavior

The review command grouped:

- deadlines earlier than now as overdue;
- deadlines between now and a configurable horizon as due soon;
- waiting items with review times at or before now;
- projects whose title had no linked `next` item;
- unprocessed Inbox items.

All comparisons normalized timezone-aware timestamps to UTC while retaining the supplied ISO 8601 strings for display and provenance.

## Test sequence

The implementation used vertical TDD with Python `unittest` and temporary SQLite databases:

1. Capture creates an Inbox item and stable ID.
2. Update clarifies status, project, deadline, and priority.
3. Complete records completion and removes the item from active lists.
4. Review classifies overdue, due-soon, waiting-review, and stalled-project items.
5. Invalid statuses are rejected.

The full five-test suite passed, and the production ledger was then listed separately to confirm an empty initial state.

## Scheduled reviews

Two self-contained cron jobs were created:

- Daily 06:00 Asia/Seoul: 24-hour review horizon.
- Sunday 21:00 Asia/Seoul: 168-hour review horizon plus active-list inspection.

Each prompt named the ledger, read-only command, timezone lookup, output order, empty-state wording, and prohibited writes. Cron records were listed after creation. A safe manual run of the daily job completed successfully.

## Scheduler verification lesson

A scheduler tool may report a generic “gateway not running” warning even when a profile-specific gateway is running. Do not encode a fixed binary path or dismiss the warning. Instead:

1. inspect running jobs and their last status;
2. use the installation’s profile-aware gateway status mechanism;
3. perform a safe manual job run;
4. report any remaining disagreement between generic and profile-specific status checks.

The successful manual execution is stronger evidence than either status signal alone, but future scheduled delivery should still be monitored on its first natural tick.

## Platform boundary wording

Use: “messages in this channel that are delivered/routed to me are captured.”

Avoid: “I automatically manage every message in this channel,” unless channel-history or event-subscription access has been explicitly verified.
