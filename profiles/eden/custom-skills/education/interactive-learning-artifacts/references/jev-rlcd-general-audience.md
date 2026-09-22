# Jev and RLCD for a General Audience

Session-derived reference for a researched 30-minute interactive HTML lesson. Checked 2026-09-21. Recheck official documentation before reuse because the product was in early access and model details can change.

## Plain-Language Teaching Model

- **Conversational AI:** like a staff member who writes an explanation for a person.
- **Decision AI:** like a triage clerk who must check one of the predefined boxes and report uncertainty.
- **Automation pattern:** unstructured or structured text state + bounded question → typed decision + probability/confidence → code branches, sorts, routes, or escalates.
- **Responsibility pattern:** AI handles narrow semantic judgment; deterministic code handles arithmetic, dates, exact rules, logging, and enforcement; people review uncertainty and high-risk decisions.

## Facts Safe to Teach with Attribution

1. Jev is TypeSafe AI's first “System One” model and is designed to return typed decisions and probabilities rather than generated prose.
   - https://docs.typesafe.ai/introduction
   - https://docs.typesafe.ai/concepts/system-one
2. The official primitives are Choice, Score, and Noul.
   - https://docs.typesafe.ai/introduction
3. RLCD means Reinforcement Learning for Calibrated Decisions. The stated target is decisions whose probabilities correspond to outcomes across groups of predictions.
   - https://docs.typesafe.ai/introduction/machine-learning-primer
4. An 0.8 probability is not a guarantee that one answer is correct. Calibration describes groups of comparable predictions.
   - https://docs.typesafe.ai/introduction/machine-learning-primer
5. Jev 1.13 accepts text, not image, audio, or video input, and does not generate replies, code, or reasoning explanations.
   - https://docs.typesafe.ai/concepts/system-one
   - https://docs.typesafe.ai/models
6. Officially documented weaknesses include exact arithmetic, counting, date comparison, multi-hop indirection, irrelevant long context, adversarial content, conflicting criteria, and text generation.
   - https://docs.typesafe.ai/model-jaggedness/jev-1.13

## Claims That Need a Caveat

- **“Zero hallucinations.”** Teach this only as constrained/schema-valid output. It does not imply zero wrong judgments. The Register explicitly distinguishes structured output from correctness.
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711
- **Speed and cost multipliers.** TypeSafe publishes its methodology and caveats, but these are company-designed evaluations rather than independent replications.
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://evals.typesafe.ai/
  - https://www.heise.de/en/news/AI-model-Jev-to-make-machines-decide-faster-11457071.html
- **Probabilities and thresholds.** A demonstration threshold is a policy illustration, not a recommended production threshold. Real thresholds require labeled validation data and error-cost analysis.

## Validated 30-Minute Structure

| Time | Activity | Mode |
|---|---|---|
| 0–3 min | Diagnostic vote: “May an AI decision be executed automatically?” | Activity |
| 3–10 min | Explain conversational vs decision AI and the four-step flow | Explanation |
| 10–15 min | Demonstrate a synthetic customer-ticket result and threshold slider | Guided activity |
| 15–23 min | Learner drafts one workplace decision workflow | Independent practice |
| 23–28 min | Three-item quiz with corrective feedback | Assessment |
| 28–30 min | Learner writes one mandatory human-review condition | Transfer |

The total is exactly 30 minutes. The design deliberately gives more time to decisions, writing, and feedback than to explanation.

## Capstone Worksheet Fields

1. Repetitive work task.
2. State or input the AI would read.
3. Bounded answer options.
4. Exact rules kept in code.
5. Harm if the result is wrong.
6. Data that must not be submitted.
7. Automatic-action condition.
8. Additional-verification condition.
9. Mandatory-human-review condition.

Completion threshold used in the validated artifact: at least three of the four core fields—task, answer options, code rule, human-review condition—are specific, and a human review is present for high-risk cases.

## Interaction Pattern That Worked

Use a synthetic duplicate-charge customer ticket. Show an illustrative department distribution, then give the learner a slider for the organization's auto-processing threshold while holding the example confidence fixed. The visible action changes between “automatic-processing candidate” and “human review.” Place `교육용 가상 출력이며 실제 API 결과가 아닙니다` directly under the simulated output.

Use three quiz items:

1. Interpret an 80% calibrated probability.
2. Choose code rather than AI for exact arithmetic and date differences.
3. Escalate high-risk or low-confidence decisions to a person or stronger review stage.

## Verified Technical Gate

The session artifact passed:

- HTML parsing, duplicate-ID, and internal-anchor checks.
- Embedded JavaScript syntax checking.
- Full-page desktop and mobile Chromium rendering.
- No horizontal overflow at 1440 px or 393 px widths.
- Threshold-slider state transition.
- Full quiz completion with `3/3` feedback.
- No browser console or page errors.
- Touch target measured above 44 px on the tested mobile viewport.
- Citation memo verification with ten registered sources and 68% declared-provenance coverage.

When Playwright's default browser cache is not writable, use a writable path consistently for installation and execution:

```bash
PLAYWRIGHT_BROWSERS_PATH=/path/to/workspace/pw-browsers npx -y playwright@VERSION install chromium
PLAYWRIGHT_BROWSERS_PATH=/path/to/workspace/pw-browsers node test_render.cjs
```

Do not preserve the original permission failure as a durable limitation; the custom writable cache path is the reusable fix.
