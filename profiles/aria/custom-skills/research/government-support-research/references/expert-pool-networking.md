# Expert-pool participation and regional customer discovery

## Dated evidence: Ulsan TP technology doctors

Reviewed during a September 2026 strategy discussion. These are historical document facts, not proof of current recruitment or future rules.

Official notice: https://www.utp.or.kr/board/board.php?bo_table=sub0501&wr_id=39921

The notice was posted 2024-04-12 with `상시` in its title. Its attached four-page PDF states a recruitment deadline of **2024-11-15**. This is a concrete example of why a rolling-recruitment title cannot establish current availability.

Document findings:
- Local business/workplace or residence in Ulsan required.
- General AND field-specific qualifications apply. A general route includes ten years of relevant industrial experience; that alone does not establish the technical field-specific qualification.
- Technical routes include research/academic credentials, qualified consulting expertise, a narrowly specified retired-expert route, and discretionary recognition of equivalent expertise and advisory ability.
- The business-registration restriction appears within the retired-expert subcategory; do not generalize it to all applicants.
- Activities include matched company visits, technical problem diagnosis, policy linkage, R&D opportunity identification, demand analysis, and reports.
- Appointment is non-employed and nonresident; allowances follow cited rules. The document does not establish guaranteed assignments or income.
- Registration materials include an application, personal-information consent, integrity pledge, and evidence of claimed education/career.
- The attachment's contact and the webpage footer's contact differ. Confirm the present program owner rather than treating the footer as the application recipient.

An older comparison notice, https://www.utp.or.kr/board/board.php?bo_table=sub0203_02&wr_id=617, also says `상시` but displays a 2023 application window. Do not conflate annual cohorts.

## Pre-application questions

1. Is registration currently open, and does it carry into the next year?
2. Which exact general and technical qualification routes fit the applicant's evidence?
3. Are industrial software, MES, and AI inspection within the accepted specialty scope?
4. What demand, matching process, availability, visits, and reports should an expert expect?
5. What are compensation and travel terms?
6. What restrictions apply to later paid contracts, supplier participation, referrals, and reuse of information?

Recommend a suitability inquiry before a full application when qualification recognition is unresolved. Inquiry drafts are not authorization to send.

## Verified public attachment retrieval

The legacy board uses links of this form:

`javascript:file_download('./download.php?bo_table=sub0501&wr_id=39921&no=0', '<encoded filename>')`

A working retrieval pattern was:
1. Open the public article in an HTTP session with a cookie jar.
2. Extract the actual relative download URL; resolve it against the article URL.
3. Fetch with the same session and the article URL as Referer.
4. Verify PDF magic bytes before saving or parsing; an HTTP-success HTML response is not the PDF.
5. Extract every page with pypdf and report per-page coverage. The four pages here yielded text. Use visual inspection for load-bearing table alignment or unclear footnote scope.

Example for an already downloaded PDF when an isolated dependency environment is appropriate:

`uv run --with pypdf python -c "from pypdf import PdfReader; r=PdfReader('notice.pdf'); print('\n'.join('PAGE '+str(i+1)+'\n'+(p.extract_text() or '[EMPTY]') for i,p in enumerate(r.pages)))"`

For discovery, the site's global search needs `sfl=wr_subject||wr_content` and an encoded `stx`. Results span board categories rather than one chronological sequence: early pages may show old beneficiary notices while later pages contain newer expert notices. Inspect relevant categories/pages before drawing recency conclusions. Extract each anchor independently with an HTML parser rather than a regex that can span several closing anchors. The current support board is a separate index; see `agency-board-inventory.md`.

## Transferable strategy framing

An expert pool can provide a legitimate setting for contributing expertise and understanding regional needs. It is not automatically a sales funnel. Keep service obligations and confidential information separate from business development. Track actual matching, problems confirmed with permission, and agreed follow-up rather than merely registration or meetings. Maintain independent evaluation of commercial demand, own-product R&D merit, and supplier eligibility.
