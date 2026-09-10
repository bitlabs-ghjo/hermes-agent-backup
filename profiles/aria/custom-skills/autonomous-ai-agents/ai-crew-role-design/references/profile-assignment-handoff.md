# Durable Assignment Handoffs to Specialist Profiles

Use this pattern when work must be performed by the real specialist profile rather than by a temporary subagent imitating that role.

## Assignment packet

Put the full request in a file so quoting, URLs, source text, and acceptance criteria survive intact:

```bash
hermes -p <profile> chat \
  --query-file /absolute/path/assignment.md \
  --continue <stable-assignment-thread> \
  --create-if-missing \
  --run-budget 480 -Q
```

Attach source media when the specialist must inspect it:

```bash
hermes -p <profile> chat \
  --query-file /absolute/path/assignment.md \
  --image /absolute/path/source.png \
  --continue <stable-assignment-thread> \
  --create-if-missing \
  --run-budget 480 -Q
```

The packet should state:

- requester and business purpose;
- verified source material and provenance;
- exact deliverables and acceptance criteria;
- correctness, confidentiality, copyright, and approval constraints;
- required artifact path;
- who may publish or send the result.

A profile run is an internal handoff, not authorization for external publication. Prefer asking the specialist to write an internal artifact and return its path; the manager reviews before any routed report or external send.

## Observable states

Track these separately:

1. **Captured** — assignment is in the task system.
2. **Delivered** — the real profile received the exact packet.
3. **Artifact produced** — the requested path exists.
4. **Manager reviewed** — content and acceptance criteria were checked.
5. **Reported** — any authorized destination accepted the report.
6. **Closed** — the task record was reconciled without stale waiting language.

Do not mark a waiting task complete at step 2 or 3.

## Timeout-safe recovery

A shell or orchestration timeout is not proof that the specialist failed. The child process may have completed an artifact before its final response was returned.

Before retrying:

1. Check whether the expected artifact exists.
2. Read and review the artifact against every acceptance criterion.
3. Check whether a matching specialist process is still running before launching a duplicate.
4. Inspect the specialist’s durable session/task state when available.
5. Retry only if the artifact is missing or incomplete and no active run owns the work.

This avoids duplicate assignments and duplicate external reports.

## Verification rules

- Confirm the profile identity and expected output path before launch.
- Require an absolute artifact path in the assignment.
- Verify citations and source URLs independently when they materially support the deliverable.
- For a send command, capture the exact destination and command result. If the platform offers no readback API, report only that the send command succeeded; do not claim visual posting/readback verification.
- After closure, update task notes to describe the final state. Remove phrases such as “awaiting follow-up” from completed records.
