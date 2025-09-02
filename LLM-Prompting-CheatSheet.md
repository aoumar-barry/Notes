# LLM Prompting Cheat‑Sheet (Conversation Summary)
_Last updated: 2025-09-01 22:36_

This file consolidates the key takeaways from our conversation so you can learn quickly.

---

## Table of Contents
- [1. Form‑Based Classification Prompts](#1-form-based-classification-prompts)
  - [1.1 Essentials Checklist](#11-essentials-checklist)
  - [1.2 Drop‑in Template (Single‑Label)](#12-drop-in-template-single-label)
  - [1.3 Multi‑Label Variant](#13-multi-label-variant)
  - [1.4 Concrete Example (Support Ticket Routing)](#14-concrete-example-support-ticket-routing)
  - [1.5 Practical Tips](#15-practical-tips)
- [2. Symbols for Structured Prompts](#2-symbols-for-structured-prompts)
  - [2.1 Delimiters](#21-delimiters)
  - [2.2 Headings & Structure](#22-headings--structure)
  - [2.3 Schemas & Machine-Readable Output](#23-schemas--machine-readable-output)
  - [2.4 Placeholders & Literals](#24-placeholders--literals)
  - [2.5 Tables & Mappings](#25-tables--mappings)
  - [2.6 Checklists & Flags](#26-checklists--flags)
  - [2.7 Copy‑Paste Skeletons](#27-copy-paste-skeletons)
  - [2.8 Usage Tips](#28-usage-tips)
- [3. Model Settings & QA](#3-model-settings--qa)

---

## 1. Form‑Based Classification Prompts

### 1.1 Essentials Checklist
- **Task**: State the classification task clearly (single‑label or multi‑label).
- **Labels + definitions**: Provide short, mutually exclusive definitions and **boundary rules**.
- **Scope rule**: *Use only the given form fields; no external inference.*
- **Abstain rule**: Define `other` / `unknown` and when to use them.
- **Tie‑breakers**: Deterministic rule if multiple labels seem plausible.
- **Output format**: Strict JSON schema; no extra prose.
- **Evidence**: Short, quoted phrases or field names that justify the label.
- **Error handling**: What to do with missing/invalid/contradictory fields.
- **Determinism**: Keep responses short; pair with low temperature.

### 1.2 Drop‑in Template (Single‑Label)
```
You are a classifier. Use ONLY the provided form fields. Do not add external facts.

Task: Classify the submission into exactly one label from LABELS.

LABELS (with definitions and boundaries):
- <LABEL_1>: <1–2 line definition>. Include when: <clear cues>. Exclude when: <boundary>.
- <LABEL_2>: ...
- <LABEL_3>: ...
- other: Use only if none of the above definitions fit.

Tie-break rule:
- If two labels fit, choose the one whose inclusion rules are more specific. If still tied, prefer <LABEL_X> over <LABEL_Y>.

Handling issues:
- If required fields are missing or contradictory, return label "unknown" and explain which fields block the decision in "notes".

Output:
Return STRICT JSON with this schema and nothing else:
{
  "label": "<one of: LABEL_1 | LABEL_2 | LABEL_3 | other | unknown>",
  "confidence": <number 0..1 with 2 decimals>,
  "evidence": ["<short quoted phrases or field names justifying the label>", "..."],
  "notes": "<very brief note on edge cases or missing data>"
}

Form fields:
<PASTE THE FORM DATA HERE AS JSON OR KEY: VALUE LINES>

Examples:
Input =>
{ ...minimal realistic example 1... }
Output =>
{"label":"<LABEL_?>","confidence":0.84,"evidence":["field_x: '...'", "field_y: '...'"],"notes":""}

Input =>
{ ...example 2 that forces tie-break... }
Output =>
{"label":"<LABEL_?>","confidence":0.61,"evidence":["..."],"notes":"tie with <other>, applied tie-break rule"}
```

### 1.3 Multi‑Label Variant
Change these lines:
- “Classify into **one or more** labels from LABELS (multi‑label).”
- Output schema:
```json
{
  "labels": ["LABEL_1", "LABEL_3"],
  "confidence_by_label": {"LABEL_1": 0.72, "LABEL_3": 0.55},
  "evidence": {"LABEL_1": ["..."], "LABEL_3": ["..."]},
  "notes": ""
}
```

### 1.4 Concrete Example (Support Ticket Routing)
**Labels & definitions**
- billing: charges, refunds, invoices, payment failure.
- technical: errors, bugs, app won’t load, integrations.
- account: login, password reset, profile/data requests.
- other: none of the above.
- unknown: blocking info missing.

**Prompt (fill the template’s sections)**
```
Task/labels/handling rules as above.

Form fields (JSON):
{
  "subject": "Charged twice this month",
  "category_selected_by_user": "Payment",
  "message": "I was billed two times for August, see attached receipt.",
  "attachments": ["receipt_august.pdf"],
  "priority": "medium"
}
```

**Expected output**
```json
{
  "label": "billing",
  "confidence": 0.92,
  "evidence": [
    "subject: 'Charged twice'",
    "message: 'billed two times'",
    "category_selected_by_user: 'Payment'"
  ],
  "notes": ""
}
```

### 1.5 Practical Tips
- **Few‑shot**: Add 2–5 varied examples, including edge cases/near‑misses.
- **Schema enforcement**: Use structured outputs/function‑calling when available.
- **Tight labels**: Reduce overlaps; write explicit inclusions/exclusions.
- **Logging**: Save form JSON + output for audits and rubric tuning.

---

## 2. Symbols for Structured Prompts

### 2.1 Delimiters
- Code fences: ````` ``` ... ``` ````` — best for verbatim data or output schemas  
- Triple quotes: `""" ... """` — long‑text delimiter  
- Markdown rules: `---` or `===` — section separators  
- Tags: `<CONTEXT>...</CONTEXT>` or `[CONTEXT] ... [/CONTEXT]` — easy to parse

### 2.2 Headings & Structure
- Markdown headings: `#`, `##`, `###` — sections like *Context, Task, Rules, Output*  
- Numbered steps: `1. 2. 3.` — deterministic procedures  
- Bullets: `-` — concise constraint lists

### 2.3 Schemas & Machine-Readable Output
- JSON braces: `{ ... }`, arrays: `[ ... ]` — strict, parseable results  
- Type hints in fences: ``` ```json ``` ``` — nudges the model to emit valid JSON

### 2.4 Placeholders & Literals
- Variables: `{{field_name}}`, `<FIELD_NAME>`, or `${var}` — obvious slots to fill  
- Literal strings in quotes: `"return exactly this key"` — prevents paraphrase

### 2.5 Tables & Mappings
- Pipes for tables: `| col | col |` — compact rubrics  
- Arrows: `->` / `=>` — mapping or if/then rules

### 2.6 Checklists & Flags
- Checkboxes: `- [ ] must`, `- [x] done` — validations  
- Emphasis for MUST/ONLY: Prefer ASCII quotes; **bold** sparingly

### 2.7 Copy‑Paste Skeletons

**A) Markdown + JSON (general tasks)**
```
# ROLE
You are an assessor.

# TASK
Classify the input into exactly one label.

# LABELS (definitions & boundaries)
| label | include when | exclude when |
|------|---------------|--------------|
| billing | charges/refunds | login issues |
| technical | errors/bugs | payment issues |

# RULES
- Use ONLY the provided input.
- If none fit, return "other".
- Be concise.

# OUTPUT (STRICT JSON)
```json
{"label":"<billing|technical|other>","confidence":0.0,"evidence":["..."]}
```

# INPUT
``` 
{{user_form_json}}
```
```

**B) XML‑style blocks (great for parsers)**
```
<SYSTEM>
Follow the rules exactly.
</SYSTEM>

<TASK>
Summarize to 3 bullets max.
</TASK>

<CONSTRAINTS>
- No opinions.
- Quote numbers verbatim.
</CONSTRAINTS>

<OUTPUT>
Return JSON only.
</OUTPUT>

<INPUT>
{{raw_text}}
</INPUT>
```

**C) Few‑shot with fenced examples**
```
### EXAMPLE 1
Input:
```
{"subject":"Charged twice","message":"..."}
```
Output:
```json
{"label":"billing","confidence":0.92}
```
```

### 2.8 Usage Tips
- **One delimiter style per section** to avoid confusion.
- **Put all parsable things in fences** and declare the language (e.g., `json`).
- **UPPER_SNAKE_CASE** or `{{curly}}` for placeholders.
- **Tables for rubrics, JSON for outputs**.
- **Number rules** when order matters.
- **Avoid nested fences** and fancy Unicode quotes.

---

## 3. Model Settings & QA
- **Model settings**: `temperature=0` (or very low), `top_p=1`, limit `max_tokens` to your JSON size.
- **Validation**: Post‑parse the JSON, assert keys/types, and fail fast.
- **Testing**: Create synthetic form payloads that intentionally trigger boundaries and tie‑breaks.
- **Monitoring**: Track confusion cases and refine label definitions over time.

---

*Need this adapted to your exact labels or domain? Replace the placeholders and drop in your own examples.*
