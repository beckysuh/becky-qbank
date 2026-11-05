# Becky Qbank handoff

Last updated: 2026-11-05. Local project; no remote hosting or GitHub remote.

## Read first
AGENTS.md → docs/QUESTION_STYLE.md → docs/APPROVED_EXAMPLES.md → resources/catalog.json → README.md. Maintain the user's concise pattern-based format. The original chat is not required to continue.

## Current content and interface
112 Cardiovascular questions. All 110 rows of the original cardio inventory are accounted for, including deliberate overlaps and the seven original questions. Five expansion batches added 105 new questions. NBME questions: zero. Future NBME entries require `source: "nbme"` and actual provenance; journal mentions of NBME are not NBME question sources.

Blue Becky Qbank header. Create Test with All Questions / NBME Forms, All / Unanswered / Incorrect / Previously Missed, organ-system counts and test size. No subtopics, flagging, timers or difficulty. Explanation is fully hidden until submission. Sources and full drug scenes enlarge on click. Reset requires confirmation. Source preference is remembered. Progress stays under `personal-qbank-v1`.

2026-11-05 setup added Export Progress / Import Progress controls. Export downloads a versioned JSON containing history, current test and preferred source. Import validates, previews replacement, and requires confirmation. Unknown history IDs are retained; saved tests with missing question IDs are skipped. Storage failures do not overwrite the current in-memory state. No migration of the existing storage key or output path.

## Canonical files / rebuild caveats
See README. Question JSON batches and the assembler starter definitions are canonical; generated HTML/data are not. Asset catalogs and extraction scripts are canonical mappings. The numbered question-authoring Python scripts are historical drafts, and old per-batch checks can overwrite status files: do not run them as a general workflow. In particular the batch3/batch4/batch5 JSON files include later corrections that rerunning draft authoring scripts would discard.

Original images and PDFs stay local/ignored by Git. Rebuild needs local cached images, while re-extraction also needs the original PDFs. resources/asset-index.json lists 126 image keys with paths and hashes. New PDF editions get separate catalog IDs. FA 2017: printed page = PDF page −21. Mehlman HY Cardio: page numbers align. Pharm scenes cite PDF page only.

Golden examples: eight frozen existing questions in docs/approved-examples.json. User explicitly approved the brief SVT style; other examples illustrate its use, not individual sign-off of each medical statement. Preserve source matching and short wording. The existing Marfan/MVP explanation includes Ehlers-Danlos to absorb a duplicate note. Down ASD/VSD notes are combined into the endocardial-cushion pattern. TXA means thromboxane A2 in this journal.

## Validation last completed
- Rebuilt the standalone HTML at outputs/svt-qbank.html: 112 questions.
- Runtime regression tests: counts, question-source filters, creation, hidden/revealed explanations, retry history, persistence, reset, completion.
- Backup tests: download payload, replacement preview, round trip, cancellation, malformed/oversized data, unavailable question IDs, inconsistent answers, storage failure.
- General integrity/style checks: unique stable IDs, frozen examples, answer structures, source image integrity, word/character limits and UI/storage invariants.
- New source image crops were visually inspected during content batches.

Interactive browser QA of local file URLs was blocked by browser policy in this thread. No bypass attempted. VM tests cover logic; they do not prove that an actual browser download/file-picker UI works. User can check Export Progress, then Import Progress and cancel the preview without changing progress. PDF medical sourcing is a separate editorial task from code tests.

## Next work
No outstanding cardio additions. User intends to add more Mehlman PDFs and eventually NBME practices. Register the supplied PDF, inspect it, match relevant complete boxes, and author in batches of 20 unless user says otherwise. Keep source gaps honest. Update this handoff, asset index and coverage records after substantive work. Future questions must not silently broaden the app scope or change its style.

## Version history / portability
Local Git baseline covers code, authored data, documentation and mappings, not ignored resources or generated output. No remote/push authorized. To move machines: copy the complete project including ignored assets, export browser progress separately, then import it into the reopened Qbank. Local Git alone does not back up your answers or the image bundle.
