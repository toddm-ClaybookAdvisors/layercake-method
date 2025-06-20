# Transition 003: Thread Refresh After Commit 0017

**Date:** [Insert date of transition]

## Reason for Transition

Performance in the previous thread degraded due to session length and large transcript size. To maintain responsiveness and ensure all recent project rules and conventions are preserved, we are starting a fresh thread.

---

## Project Context and New Conventions

- **Devlog:** Every commit now includes a full development log (devlog) in `devlog/devlog-<commit>.md`, capturing all back-and-forth dialog and design evolution.
- **Prompt Evolution:** Each PROMPTS.md entry for a feature with significant discussion now includes a "Prompt Evolution" section, documenting how the requirement evolved.
- **Original Prompt Logging:** All PROMPTS.md entries use the *original initiating prompt* for the "Original Prompt" section, regardless of later pivots.
- **Command Keywords:**  
  - `record` — log prompts and responses  
  - `sidebar` — pause logging  
  - `debug` — initiate structured debug log  
  - `commit` — create PROMPTS.md, CHAT_LOG.md, devlog, and commit entry
- **Viewport Definition:**  
  - The viewport is the portion of the map (if larger than the viewport) that is rendered at any given time, regardless of what is "visible" to the player.
- **Session Flow:** All dialog beyond the initial prompt is captured in the devlog; only the initiating prompt appears in PROMPTS.md.

---

## Next Steps

- Continue development in a new chat thread.
- Immediately re-establish context if necessary (via record mode and config upload).
- Update the chat name to reflect the next commit or feature.

---

## Transition Commit

- No code or feature changes in this commit; documentation and logging conventions only.
- All rules above carried forward.
