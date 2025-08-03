## Commit Message JSON Structure

All layer commits **must** use the following JSON structure after the oneline summary:

```json
{
  "layer": 38,
  "duration": "1h 8m",
  "commit_sha": "TO_BE_FILLED_AFTER_COMMIT",
  "summary": "Major structure refactor for dual-AI pair programming; protocol files stubbed for future layers",
  "prompt": "Transition to pair programming model: establish clean GPT-4o and Claude role separation, consolidate all protocol/persona/workflow/docs under protocol/ as stubs. Each Git commit is now a layer.",
  "interpreted_instruction": "Reorganized project by eliminating per-layer artifact folders, centralizing protocol/persona/workflow/templates as stubs under experiment/protocol/. Devlogs and author notes preserved. All commit messages now use rich JSON metadata. Ready for future expansion with dual-AI, pair programming workflow.",
  "pair_programming": {
    "architect": {
      "role": "Architect-Laboratory Partner",
      "model": "GPT-4o",
      "focus": "Feature authoring, documentation, audit log"
    },
    "reviewer": {
      "role": "Reviewer-Refactorer",
      "model": "Claude",
      "focus": "Code review, patching, audit trail"
    }
  },
  "reviewer_notes": [],
  "files_changed": [
    "experiment/protocol/directives/chatgpt.md",
    "experiment/protocol/directives/claude.md",
    "experiment/protocol/directives/shared.md",
    "experiment/protocol/persona/chatgpt.md",
    "experiment/protocol/persona/claude.md",
    "experiment/protocol/persona/shared.md",
    "experiment/protocol/prompt-templates/chatgpt.md",
    "experiment/protocol/prompt-templates/claude.md",
    "experiment/protocol/prompt-templates/shared.md",
    "experiment/protocol/workflow/chatgpt.md",
    "experiment/protocol/workflow/claude.md",
    "experiment/protocol/workflow/shared.md",
    "experiment/AUTHOR_NOTES.md",
    "experiment/LAYER_INDEX.md",
    "experiment/README.md",
    "experiment/devlog/",
    "app/src/",
    "README.md"
  ],
  "developer_notes": "All protocol/persona/workflow/template files are stubs to be filled in future layers. This structure enables clean, modular role separation for dual-AI (pair programming) development, preserves audit trails, and prepares for future automation and onboarding.",
  "timestamp_start": "2025-07-13T12:52:00-06:00",
  "timestamp_end": "2025-07-13T14:00:00-06:00",
  "author": "Architect-Laboratory Partner (GPT-4o)",
  "reviewer": "Reviewer-Refactorer (Claude)",
  "devlog": "experiment/devlog/devlog-0038.md"
}
