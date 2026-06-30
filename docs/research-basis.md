# Research basis

This file records the published research that motivated specific canon and runtime rules in this skill. It is provenance for *why a rule exists*, not a literature review and not a claim that the skill implements any paper's method.

**Honesty note.** These references were identified from paper abstracts and search summaries, not from full readings of every PDF. arXiv IDs and dates should be confirmed against the source before citing externally. Nothing here is a benchmark, accuracy, or compliance-usefulness result for this skill.

## Why these rules exist

| Canon / runtime rule | Motivating finding | Reference |
|---|---|---|
| **False-premise hard stop** (`AGENTS.md` → Stop-and-request; overlays → Response-Mode Hard Stops; failure mode "False-premise acceptance") | Abstention benchmarks show false premises and underspecified/unanswerable questions as a distinct failure class that scaling does not solve; models should detect and refuse rather than analyze a bad premise. For sanctions/AML work an unconfirmed designation or ownership link is exactly such a premise. | "AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions" — arXiv:2506.09038; "The Art of Refusal: A Survey of Abstention in LLMs" — arXiv:2407.18418 |
| **Tag faithfulness, not tag presence** (`AGENTS.md` → Per-claim provenance; rubric item 13; failure mode "Citation post-rationalization") | Attributed answers frequently carry citations that look correct but do not support the claim; post-rationalization is prevalent and a large share of citations are unfaithful. Highest stakes here for sanctions-status, beneficial-ownership, and enforcement claims. | "Correctness is not Faithfulness in RAG Attributions" — arXiv:2412.18004; "Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs" — arXiv:2605.28565 |
| **Verbalized-confidence calibration is checkable** (`AGENTS.md` → Linguistic faithfulness; failure mode "Verbalized-confidence miscalibration") | LLMs systematically fail to make linguistic uncertainty markers track intrinsic confidence; faithful natural-language uncertainty is a measurable property, not a style preference. | "MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs" — arXiv:2505.24858; "Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?" — arXiv:2605.28778 |
| **Spotlighting / provenance separation for retrieved content** (`AGENTS.md` → Retrieved-content trust) | Inline concatenation of retrieved text gives indirect prompt injection no boundary; a poisoned filing or list export then reaches every downstream read. Provenance-based instruction hierarchy and datamarking/spotlighting materially reduce attack success. | "A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots" — arXiv:2606.19660; "Document-Authored Control-Signal Impersonation" — arXiv:2606.09005 |
| **Self-scoring honesty (SPB disclosure)** (`AGENTS.md` → B2.7; `evals/starter-rubric.md` limitations) | LLM judges exhibit self-preference bias, marking rubric criteria "satisfied" more often for their own model family — even on objective binary criteria. Self-scored agent-evals must not be presented as external validation. | "Self-Preference Bias in Rubric-Based Evaluation of LLMs" — arXiv:2604.06996; "Reliability without Validity: ... LLM-as-a-Judge ... Agreement, Consistency, and Bias" — arXiv:2606.19544 |
| **Competing-hypotheses discipline** (failure mode "Single-hypothesis lock-in") | Evidence-first hypothesis tracking — maintain rivals, update plausibility, converge only after sufficient diagnostic evidence — improves robustness over single-hypothesis confirmation. The full Competing-Hypotheses (ACH) memo mode lives in the horizontal [Global Think Tank Analyst](https://github.com/vassiliylakhonin/global-think-tank-analyst) skill, which this specialist composes on top of. | "LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis" — arXiv:2606.13220 |

## What this is not

- Not a claim that this skill was evaluated with any of these methods.
- Not a benchmark, accuracy, or compliance-usefulness claim.
- Not a substitute for the honesty and safety rules in `AGENTS.md`. If a future change cites a result here as evidence of skill quality, that is a misuse of this file.
