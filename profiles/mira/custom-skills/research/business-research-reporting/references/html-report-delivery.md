# HTML Report and Delivery Checklist

Use this checklist for recurring or one-off executive research reports.

## Artifact contract

- [ ] Starts with `<!doctype html>` and declares `<html lang="ko">` when Korean.
- [ ] Includes `<meta charset="utf-8">` and a responsive viewport.
- [ ] Uses a specific `<title>` containing the report subject and date.
- [ ] Contains an executive decision panel before detailed evidence.
- [ ] Uses semantic sections, headings, lists, and accessible tables.
- [ ] Gives material claims stable source markers such as `[1]` linked to the source list.
- [ ] Includes publisher, publication date or verification date, and original URL for each source.
- [ ] Includes `@media print` rules; avoids clipped tables and hidden URLs.
- [ ] Avoids remote scripts, analytics, trackers, and remote fonts by default.
- [ ] Masks confidential or identifying information not required by the approved audience.

## Recommended decision panel

Place these fields near the top:

- decision requested;
- recommendation;
- deadline or next review date;
- owner;
- approval required;
- key uncertainty or blocker.

## Scheduled-report prompt clause

Add a clause equivalent to:

> Produce a standalone HTML5 report with UTF-8, responsive and print CSS, semantic headings and tables, inline numbered citations, and a complete source list. Do not use external scripts or trackers. Save it as an `.html` file when file tools are available and include the absolute path plus a short decision summary in the final response. Address the report to the designated decision owner and put decisions, deadlines, and approvals first.

Preserve the rest of the existing research prompt. Do not replace it with this clause alone.

## Routing evidence

Record and verify the exact state you can prove:

| State | Minimum evidence |
|---|---|
| Prepared | File write confirmed and artifact checks passed |
| Posted to channel | Exact channel target plus delivery success and read-back where supported |
| Sent to person | Verified recipient identifier/address plus delivery/read-back |
| Scheduled | Exact job ID and read-back of updated definition |
| Active | Scheduler/gateway health plus next-run state |

If the platform cannot directly notify a named person, do not claim personal delivery. State that the report was posted to the shared channel or addressed in prose and identify the limitation.

## Final response language

Prefer precise status lines:

- “HTML report prepared: `<path>`.”
- “Posted to `<verified channel>` and delivery verified.”
- “Scheduled job `<id>` updated; new HTML clause confirmed by read-back.”
- “Job is saved but not active because the scheduler is stopped.”

Avoid ambiguous statements such as “reported to ARIA” unless an exact, verified ARIA destination was used.