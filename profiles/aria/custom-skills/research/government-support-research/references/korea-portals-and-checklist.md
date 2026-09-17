# Korean Government-Support Research Reference

Use this as a discovery map and eligibility checklist. Current notices and
attachments remain authoritative; portal summaries and annual patterns do not.

## Primary Portals

- **기업마당 (Bizinfo):** broad SME, regional, technology, finance, export, and
  management notices. Use filters for region, applicant type, and closing status.
- **K-Startup:** startup commercialization, accelerators, competitions, TIPS,
  legal/one-stop support, and founder-stage programs.
- **IRIS:** national R&D notices and submissions. Check lead/co-research
  institution rules, 3책5공, technology fees, matching cash, and prior-R&D gates.
- **SMTECH / 스마트공장 사업관리시스템:** SME R&D and smart-manufacturing
  programs, supplier pools, demand-company requirements, and consortium rules.
- **NIPA:** AI vouchers, SaaS/cloud, GovTech, ICT commercialization, and supplier
  pool registration.
- **KHIDI / 의료기기산업 종합정보시스템:** medical-device consultation,
  clinical/use evaluation, overseas expansion, digital-health exhibitions, and
  hospital-linked programs.
- **KIAT / KEIT / IITP:** industrial technology, demonstrations, infrastructure,
  and ICT R&D.
- **Regional sources:** local government, technopark, information-industry
  agency, economic promotion agency, and creative economy innovation center.

## Search Order

1. Company's region + exact technology keywords.
2. National startup and SME notices by business age.
3. Product-domain agencies: manufacturing, healthcare, mobility, energy, etc.
4. Supplier/provider registrations and demand-company consortium opportunities.
5. Closed annual programs for next-cycle preparation only.

## Hard-Gate Checklist

For every candidate record:

- Applicant: company, founder, manufacturer, medical institution, consortium.
- Business age and reference date.
- Headquarters, workplace, factory, or relocation requirement.
- Industry code, factory registration, manufacturing license, medical-device
  registration, certification, patent, or software ownership.
- Revenue, debt ratio, tax arrears, and employee requirements.
- Prior government support, first-R&D requirement, duplicate-funding rule.
- Lead versus partner eligibility and required partner count/type.
- Prototype, PoC, data, customer site, hospital, or factory evidence.
- Government share, company cash/in-kind match, VAT, technology fee.
- Submission system, exact closing time, and required account/registration.

## Full-Notice Retrieval Notes

- Bizinfo detail pages commonly use a stable `pblancId` URL. Related-notice HTML
  may reveal the exact ID when search indexing is incomplete.
- For direct Bizinfo title searches, discover the current form first. The verified list endpoint is `/sii/siia/selectSIIA200View.do` with `condition=searchPblancNm`, `condition1=AND`, `keyword=<query>`, and `cpage=1`. Omitting `condition1` can return HTTP 500. `schEndAt=Y` returns past notices and `schEndAt=N` ongoing notices; search both. Do not assume `rows=100` was honored: the site may still return 15 rows, requiring pagination and count checks.
- Some next-year notices appear during the current year. Distinguish program-operator recruitment from beneficiary/supplier recruitment; an operator notice may contain future program plans but does not open applications for individual firms. Do not blanket-label all next-year programs unannounced.
- Attachment download links may use `/cmm/fms/fileDown.do?atchFileId=...&fileSn=...`.
  Download the attachment and use document extraction; do not rely on a page
  snippet for hidden eligibility conditions.
- For dynamic official pages, fetch the full HTML with a normal browser user
  agent and extract the main notice text. If a portal page is incomplete, follow
  the originating agency link rather than citing a search snippet.

## Interpretation Rules

- `모집 중` means the date window is open, not that budget remains.
- `예산 소진 시까지` requires an operator balance check.
- `최대 N원` is a ceiling, not an expected award.
- Voucher funds usually buy from an approved supplier; they are not unrestricted
  cash to the demand company.
- Loan, interest subsidy, guarantee, consultation, booth, testing, and in-kind
  infrastructure must be named accurately.
- A founder's prior employer projects show capability, but the applicant company
  still needs ownership, references, staff, partners, and required registrations.

## Fast Decision Gate for Solo Companies

Recommend one primary application and one fallback:

1. Can every hard gate be proven now?
2. Can the missing partner be confirmed within 24–48 hours?
3. Is there a company-owned demo or project specification?
4. Can matching cash and delivery capacity be sustained?
5. Can a credible application be completed at least 2–3 days before closing?

If any answer is no, downgrade to `apply after one check`, `partner only`,
`capability-building`, or `next-cycle pipeline`.