# YouTube Evidence Workflow

Use this reference when a case-study source is a YouTube video.

## 1. Compact metadata

Prefer a field-only extractor call over full JSON:

```bash
yt-dlp --skip-download \
  --print '%(id)s\t%(upload_date)s\t%(duration_string)s\t%(channel)s\t%(title)s' \
  'https://www.youtube.com/watch?v=VIDEO_ID'
```

Store the exact output in the working evidence ledger. Do not infer upload dates from relative labels such as “one year ago.”

## 2. Transcript fallback order

1. Fetch timestamped transcript with automatic language selection.
2. If the helper reports no transcript and suggests a language, retry with explicit likely source languages, for example `--language ko,en`.
3. If explicit languages fail, list available transcript languages when the helper/API supports it.
4. Only then classify captions as unavailable. A disabled transcript, an unavailable video, and a language mismatch are different failure states.

For long videos, save complete output to a file before parsing. Tool display limits can truncate JSON and make an otherwise valid transcript appear malformed.

## 3. Evidence windows

For each claim, record:

```text
Organization:
Workflow:
Metric or qualitative outcome:
Timestamp start–end:
Transcript excerpt:
Video URL:
Evidence label: A/B/C/D
Corroborating URL:
Caveat:
```

Prefer a 20–90 second interval. If workflow and metric occur in different sections, keep two intervals rather than one broad timestamp.

## 4. Cross-check order

Search in this order:

1. Adopting organization's newsroom, investor relations, or technical blog.
2. Official platform-provider customer story.
3. Conference page or speaker material.
4. Reputable third-party reporting.

A second page owned by the same vendor improves detail but is not independent corroboration. Preserve that distinction in the evidence label.

## 5. Report verification

Before delivery, confirm programmatically or with a deterministic checklist:

- Number of requested cases equals number of case rows.
- Video IDs are unique unless one compilation intentionally supports several distinct cases.
- Every metric has a citation and attribution qualifier.
- Every internal citation target resolves.
- Source URLs are not hand-renumbered.
- The final HTML/document contains the requested title, tables, source section, and caveat.

## 6. Recommended wording

Use:

- “회사가 발표했습니다.”
- “공식 고객사례는 …로 추정했습니다.”
- “정량 성과는 공개되지 않았습니다.”
- “독립 감사 수치가 아니므로 PoC 가설로 사용해야 합니다.”

Avoid:

- “AI가 검증된 ROI를 냈습니다” when only a vendor claim exists.
- “직원 700명을 대체했습니다” when the source says “equivalent workload.”
- “전사 도입에 성공했습니다” when the evidence only describes a pilot.
