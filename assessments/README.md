# OCR J277 Year 10 Component 2 — Basics, Selection, Loops Assessment

A two-series Dodona course that delivers the OCR J277 Year 10 Component 2 *Basics, Selection, Loops* assessment as automatically-tested programming exercises (Section A) and teacher-graded open questions (Section B).

- **Section A — Programming Tasks (50 marks):** five Python programs auto-graded by the TESTed judge.
- **Section B — Exam Questions (30 marks):** five open-ended questions graded by the teacher reading the student's free-text Markdown submission.

**Total: 80 marks across 10 activities.**

## Structure

```
output/
├── 01-section-a-programming-tasks/         (5 TESTed/Python exercises, 50 marks)
│   ├── 01-user-details/                    Task 1, 8 marks
│   ├── 02-grade-calculator/                Task 2, 10 marks
│   ├── 03-times-table/                     Task 3, 10 marks
│   ├── 04-validation-loop/                 Task 4, 12 marks
│   └── 05-mini-quiz/                       Task 5, 10 marks  (questions invented during conversion — review)
└── 02-section-b-exam-questions/            (5 Markdown exercises, 30 marks)
    ├── 01-explain-type-casting/            Q1, 6 marks
    ├── 02-debug-the-program/               Q2, 6 marks  (boilerplate contains the broken snippet)
    ├── 03-largest-of-three/                Q3, 6 marks  (pseudocode or Python both accepted)
    ├── 04-selection-vs-iteration/          Q4, 6 marks
    └── 05-theme-park-ride-condition/       Q5, 6 marks
```

## Teacher notes

- Each activity's `README.md` is teacher-facing only — it carries the marks line, attribution, and (for Section A) the OCR marking checklist as a per-submission rubric. Students do not see `README.md` files on Dodona.
- Section A reference solutions in `solution/solution.py` are written so that every checklist item is visible in the code — they represent what a full-marks submission looks like.
- Section B reference answers in `solution/solution.md` are teacher-visible model answers, not auto-grading templates.
- Mini Quiz (Task 5) uses three invented questions because the OCR source supplies only the framework. The TODO comment in its `README.md` flags this for review.

## Attribution

Source: OCR J277 Year 10 Component 2 — Python Programming & Computational Thinking, *Basics, Selection, Loops Assessment*. Exam-board material; provided to learners under standard educational use.

Converted to Dodona format with the `dodona:convert-course` Claude skill, following the conversion rules in this folder's `CLAUDE.md`.
