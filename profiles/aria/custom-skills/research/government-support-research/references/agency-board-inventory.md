# Exhaustive agency-board inventories

## Validated example: Ulsan Technopark

The following public read-only retrieval pattern was exercised in September 2026.
Reinspect the live site before reuse; endpoints, fields, and pagination can change.
These are retrieval mechanics, not durable claims about which grants remain open.

### Two independent indexes

- Current support board:
  `https://www.utp.or.kr/include/contents.php?mnuno=M0000018&menu_group=1&sno=0102`
- Legacy/global search:
  `https://www.utp.or.kr/board/search.php`

The current board's initial HTML contains an empty table and a placeholder count.
Its actual listings are loaded by JavaScript. The global search can return legacy
support notices, announcements, and press releases while missing current-board
calls. Both indexes must be checked.

### Current board discovery and extraction

1. Read the current page's script references. The inspected implementation loaded
   `/sub02/js/re_ancmt.js?v=20240901`.
2. That script revealed these public GET requests:
   - List: `/proc/re_ancmt/list.php?task=list&page=1&sear=<URL-encoded keyword>`
   - Detail: `/proc/re_ancmt/list.php?task=getItem&seq=<notice ID>`
   - Attachment: `/proc/re_ancmt/download.php?seq=<notice ID>&no=<file number>`
3. The list response contains `code`, `data`, and `page`. Inspect
   `page.numberOfRecords`, `currentPageNo`, and `finalPageNo`; do not mistake
   `endPageNo` (the current pagination block) for the final page.
4. Persist every response, dedupe by `seq`, and verify the unique count against the
   declared total. Repeat for synonyms. An unfiltered sweep of the target-year
   listing summaries can catch candidates that keyword searches missed.
5. Details return `data` plus `files`. Relevant fields include `title`, `content`,
   `outline`, `supported_target`, `notice_start_date`, `notice_end_date`,
   `apply_start_dt`, `apply_end_dt`, `created_dt`, and `last_modified_dt`.
   Download using the attachment's `re_seq` and `f_no`, retaining `f_source`.
   Do not expose internal author/IP fields in the report.
6. The browser-facing detail permalink is the current board URL plus
   `&task=view&seq=<notice ID>`. Its HTML shell may still be empty; verify the
   corresponding public detail response and attachment, not only HTTP 200.

Example (curl URL-encodes the Korean query):

```bash
curl --fail --get 'https://www.utp.or.kr/proc/re_ancmt/list.php' \
  --data-urlencode 'task=list' --data-urlencode 'page=1' \
  --data-urlencode 'sear=스마트팜' -o list-page-1.json
```

### Global search requirements

Use the actual form fields:

```text
sfl=wr_subject||wr_content
stx=스마트팜
page=1
```

URL-encode the values. Omitting `sfl` returned a misleading zero-result response;
including the form's field selector returned real results. Retrieve all declared
pages and dedupe article links by board identifier plus `wr_id` (not `wr_id`
alone). Review target-year press releases for additional program names, but do
not count publicity, prior-year results, or a proposed R&D project as an open call.

### Coverage and chronology

Keyword variants used included 스마트팜, 스마트 팜, 스마트농업, 농업, 농식품,
청년농, 식물공장, 스마트파머. Adapt the list to the requested domain.

If traversing unfiltered listings newest-first, verify the ordering and handle
pinned notices separately before stopping at older records. Search target-year
terms across prior-year records too: a year's programs may have been announced
before January. A year-posting-date sweep alone cannot establish full coverage.

### Attachment checks that mattered

- Read every page of each round's PDF; record text coverage. A nonempty first page
  does not establish complete extraction.
- For merged tables, render the relevant page and inspect it. In the exercised
  case, round comparison revealed changed site ownership/lease and area criteria,
  changed eligible crops, and a new in-kind relocation track.
- Distinguish a cash grant from reused equipment supplied in kind.
- Do not infer a reopened track from a leftover application-table label when the
  round's support overview and detailed track list omit it.
- Preserve contradictions: a stated age range versus birth-year dates; minimum
  cash amounts versus a general percentage clause; an unspecified percentage
  denominator. Ask the operator for written interpretation before eligibility or
  budget decisions.
- Keep recipient and supplier routes distinct. A farmer grant permitting AI
  development/purchase does not prove that any software firm can directly apply,
  invoice any cost category, or bypass supplier-pool registration.

### Deliverable structure

Use a complete notice inventory and round-by-track matrix, then a selective
company-fit recommendation. Include source permalinks, attachment links, dates,
status at the local-time cutoff, unmet checks, exclusions, and a coverage note.
Count parent programs, notices, and tracks separately. Persist raw responses and
structured records for verification; do not replace them with remembered totals.
