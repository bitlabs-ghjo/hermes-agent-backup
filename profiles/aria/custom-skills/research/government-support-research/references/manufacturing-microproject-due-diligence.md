# Manufacturing microproject funding: source-reading pattern

This is a methodological example, not a live opportunity list. Re-fetch the
current notice and amendments before applying any dates, amounts, or conditions.

## 1. Separate three questions

1. Is the pain evidenced? Distinguish explicit RFP demand, a supplier's reported
   pilot result, an analyst's proposed feature, and current willingness to pay.
2. Is the proposed MVP small enough? One team, one input type/line, read-only
   processing, preserved originals, human confirmation; no automatic plant
   control or blanket support commitment.
3. Is funding economically usable by this company? Determine legal role,
   expense eligibility, cash flow, IP, disclosure, and continuing obligations.

A useful comparison includes AS intake structuring, existing inspection-alarm
normalization, and inspection-document reconciliation. These are candidate
classes, not proven markets. Document reconciliation can be technically easier
while having weaker demand evidence; alarm normalization does not establish
that deduplication is needed. Do not promote either merely for technical ease.

## 2. Worked notice: reimbursement is not supplier revenue

The 2026 Ulsan PBL notice provides a concrete example of why attachments matter:

- Official portal detail:
  https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/view.do?pblancId=PBLN_000000000126119
- Official HWP:
  https://www.bizinfo.go.kr/cmm/fms/fileDown.do?atchFileId=FILE_000000000771918&fileSn=1

The inspected notice described a Ulsan automotive-parts manufacturer plus a
Ulsan IT/SW supplier. Its headline consortium allocation did not mean money
paid directly to the supplier: the manufacturer was the spending party and
received payment after education, project completion, reporting, and expense
review. The broad implementation description mentioned source-code work, while
the cost table named materials and SW infrastructure. This left supplier labor
and development-service fee eligibility unresolved.

The same attachment required scrutiny of:

- supplier-registration language without a clear registration procedure;
- historical financial statements that a newly opened company cannot possess;
- participation/employment evidence for a sole owner;
- already-completed or in-progress project exclusions;
- source-code/results submission, partial data/model disclosure, and three-year
  system-log duties;
- fixed dates alongside an inconsistent early-closure clause;
- email submission alongside an online-submission statement elsewhere.

Report those as unresolved conditions, not inferred waivers. Obtain written
operator clarification through the applicable approved contact process. Never
use a grant's headline amount as the supplier's expected development revenue.

## 3. Official portal retrieval pattern

When search discovery is insufficient, inspect the current public portal form
before choosing query fields. The following GET pattern returned real filtered
Bizinfo results during this investigation:

```text
https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/list.do?rows=15&cpage=1&schPblancDiv=&schJrsdCodeTy=&schWntyAt=&schAreaDetailCodes=&schEndAt=N&condition=searchPblancNm&condition1=AND&preKeywords=&keyword=AI
```

- Preserve the form's condition fields, including `condition1=AND`; URL-encode
  Korean keywords. Reinspect the form if it changes rather than treating this
  URL as a permanent API contract.
- Verify the returned search term, result count, and rows. A generic list or
  error page with HTTP content is not a successful filtered search.
- Read row links and retain their `pblancId`; follow the actual detail and
  attachment links. Do not infer eligibility from the list.
- A closed first round does not close later rounds. Search for `추가`, `2차`,
  `수정`, and `재공고` and reconcile notices before reporting current status.
- Save each batch and its source URLs. Dedupe by notice identifier and version;
  if claiming every result, follow pagination and verify the count.

Use the document-extraction skill for PDF/HWP processing. Validate text coverage
and important tables; preserve internal contradictions rather than silently
repairing source text.

## 4. Team review acceptance criteria

For existing staff, use real profile handoffs under `ai-crew-role-design`.
A practical split is funding eligibility, commercial demand, and MVP/education
scope. Require evidence paths/URLs and explicit objections from each worker.
The manager checks load-bearing attachments independently, sends newly found
rounds or conflicting clauses back for correction, and reads the revised
artifacts before claiming re-review.

Remove unsupported fixed percentage targets and arbitrary personnel minima
from the final report. Choose one main commercial-validation item and, if
necessary, a distinct conditional funding candidate. Do not quietly authorize
two simultaneous builds. Record research completion, approval, send-command
acceptance, and independent destination readback as separate states.
