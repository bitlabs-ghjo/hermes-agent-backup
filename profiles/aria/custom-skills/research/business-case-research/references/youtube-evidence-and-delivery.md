# YouTube Evidence and Approved Delivery

Use this reference for research jobs that combine YouTube evidence, executive reporting, and an approved Slack handoff.

## 1. Transcript collection

Use the `youtube-content` helper with timestamped output and save one file per video.

```bash
PY=/path/to/venv/bin/python
FETCH="$SKILL_DIR/../youtube-content/scripts/fetch_transcript.py"
"$PY" "$FETCH" "https://www.youtube.com/watch?v=VIDEO_ID" --timestamps --language ko,en
```

Reliable fallback order:

1. Requested language plus English fallback, such as `--language ko,en`.
2. Retry without `--language` to accept any available transcript.
3. If captions remain unavailable, use the video description and a first-party company or vendor page; label the transcript as unavailable rather than inventing quotations.

If `youtube-transcript-api` is absent and the environment has no active virtual environment, create a dedicated venv and install into that interpreter:

```bash
uv venv /path/to/cache/yt-venv
uv pip install --python /path/to/cache/yt-venv/bin/python youtube-transcript-api
```

Do not stream many long transcript JSON documents through a terminal capture. Save each result immediately; terminal output caps can truncate otherwise valid JSON.

## 2. Minimal metadata without giant yt-dlp JSON

Avoid `--dump-single-json` when only title, channel, date, and duration are required. It can emit formats and subtitle manifests hundreds of kilobytes long.

```bash
uv tool run yt-dlp --skip-download \
  --print '%(id)s\t%(upload_date)s\t%(duration_string)s\t%(channel)s\t%(title)s' \
  'https://www.youtube.com/watch?v=VIDEO_ID'
```

For title and author only, YouTube oEmbed is lighter:

```text
https://www.youtube.com/oembed?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DVIDEO_ID&format=json
```

## 3. Evidence record

Store each selected case with these fields:

```text
company
industry
business_function
problem_before
ai_tool
workflow_after
reported_metric
metric_definition_and_period
claim_strength
video_title
channel
upload_date
video_url
timestamp_range
corroborating_url
transferable_lesson
```

Treat auto-captions as navigational evidence. Verify names, numbers, and qualifiers against the surrounding timestamp and a first-party source when possible.

## 4. Citation QA for table-heavy reports

The grounded-citations coverage metric intentionally excludes Markdown table rows. Therefore a low prose coverage percentage can coexist with fully cited case rows.

Run both checks:

1. `sources.py verify report.md --strict` to catch unknown, stale, or unused source IDs.
2. A deterministic row audit that checks every case row containing external claims for at least one `\[n\]` citation.

Do not lower a coverage threshold merely to make a red command green. Explain why the metric is unsuitable for the document structure and replace it with the row-level check.

## 5. HTML artifact QA

After conversion, parse the HTML and verify:

- exactly one report `<h1>`;
- expected `<h2>` sections and table count;
- every internal citation link resolves to a source anchor;
- no raw Markdown headings leaked into the output;
- expected organization footer and contact fields are present;
- declared case and source totals match programmatic counts.

A structural parser check is not a visual review. If browser rendering is available, inspect a screenshot as an additional check; do not claim visual verification when only structure was parsed.

## 6. Approved Slack delivery

Build the final approval packet before sending: recipient, full body, attachment names, links, and impact/risks. Send only after the required explicit approval phrase is received.

Hermes attachments are referenced inside the message body:

```text
Executive summary text...

MEDIA:/absolute/path/report.html
```

Then send the prepared text file:

```bash
hermes -p PROFILE send --to slack:CHANNEL_ID --file /path/post.txt --json
```

A mixed text-plus-attachment send may appear in Slack as two adjacent messages: one containing the text and one containing the file. The returned `message_id` can identify the file-share message rather than the text message.

Verification therefore needs a small history window around the returned timestamp, not only one exact message. Confirm:

- destination channel ID;
- approved text appears unchanged in a nearby message;
- attachment filename and title match;
- no extra confidential material was included.

Never print or log the Slack token while performing the read-back.
