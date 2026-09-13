# Korean reimbursed-training supplier research

## Source snapshot — checked 2026-09-12, not evergreen eligibility

A claim that SME AI training is “90% reimbursed” matched the 2026
중소기업 인재 키움 프리미엄 훈련 scheme. This does not establish which
program a particular unidentified video discussed. Re-fetch current notices
before giving an application decision; do not roll these terms into future years.

### Official evidence

1. Ministry of Employment and Labor, 2026-01-26 announcement and annex:
https://www.moel.go.kr/common/downloadFile.do?file_seq=20260101590&bbs_seq=18889&bbs_id=12&file_ext=pdf

The annex states support of at least 90% of the training cost actually borne by
the employer. Its 95% conditions include AI-convergence courses conducted
outside Seoul/Gyeonggi/Incheon, or training delivered by the institution at the
company or a nearby training facility. Eligibility and employer support limits
still apply. The purchaser receives the support; this is not an unrestricted
grant to the instructor. The annex distinguishes course submission, supported
course-pool announcement, learner participation/payment, and reimbursement.

2. HRDK 2026 third-round course recruitment, notice 제2026-090호:
https://www.hrd4u.or.kr/portal/cmm/fms/FileDown.do?atchFileId=FILE_000000000602121&fileSn=1&bbsId=
Landing page: https://www.hrdkorea.or.kr/3/1/1?k=55841

Exact eligibility wording:
“참여대상 : 우수한 훈련과정을 보유한 기관”
“직업능력심사평가원 인증등급 미보유 기관도 가능하며, 별도 자격요건 없음”

Required submissions listed: stamped institutional cover letter, requested-course
spreadsheet, self-diagnosis confirmation, and applicable classroom-training
infrastructure evidence (facilities/equipment, instructor pool, major customers).
Infrastructure evidence is mandatory for uncertified institutions and institutions
certified for distance training. The verified round ran June 25–July 1, 2026;
it was closed at the research cutoff. No subsequent round was established by
that lookup. Do not confuse ongoing course enrollment with new-provider intake.

These excerpts support investigating direct participation without prior
certification, not promising selection. Sole-proprietor acceptance, education
business registration/reporting requirements, acceptable rented facilities, and
adequacy of a one-person provider's evidence need separate confirmation.

## Reusable discovery and retrieval pattern

- Search both the benefit and supplier terms, e.g. `AI 교육 90% 환급`, then
  `중소기업 인재키움 프리미엄 훈련 훈련기관 모집 신청 자격`.
- If one search route fails, use another engine. Naver search HTML was a working
  discovery route: `https://search.naver.com/search.naver?query=` plus a properly
  URL-encoded query. Parse anchor labels and hrefs with Python HTMLParser;
  retain official agency links and fetch their actual pages/attachments.
- Encode Korean query strings using `urllib.parse.quote`, not raw non-ASCII
  characters in a URL. Remove script/style content before reading HTML text.
- For downloaded attachments, inspect file signatures instead of assuming the
  format from a download URL. A `FileDown.do` endpoint can return a normal PDF.
- A working text-layer PDF extraction route is
  `uv run --with pypdf python <extraction_script.py>` using `PdfReader` and
  per-page `extract_text()`. Preserve page boundaries and check empty pages;
  use the PDF/OCR skills when coverage is incomplete.
- Search snippets are discovery aids only. Use full attachment language for
  load-bearing eligibility claims and register the official URLs in the
  task-specific citation ledger before drafting.

## Decision lesson

Do not default to “partner with a certified institution first” before reading
the scheme-specific supplier notice. Compare direct entry and partnership only
after checking the actual gates, evidence workload, and recruitment status.
