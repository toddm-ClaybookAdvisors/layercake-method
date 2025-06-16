# CHAT TRANSITION — TRANSFER-001

This is the original transition document provided by the user to prime a new conversation thread.

````markdown
# PROJECT SNAPSHOT — LLM-Driven Game Development

## 𝕝𝕒𝔽 Purpose

This is not a game development project — it is a **demonstration of how to use an LLM as a complete software development assistant**. The end product happens to be a 2D adventure game, but the true goal is to showcase:

- Prompt-by-prompt development
- A workflow where the human writes **no code**
- The LLM performs all architectural, functional, and implementation tasks
- Transparent, traceable iteration using Git
- Best practices for writing and evolving effective prompts

The human acts as **strategic lead, prompt author, reviewer, and tester**. The AI acts as **coder, collaborator, and documentarian**.

---

## 𝓐𝓲 Methodology

### Iteration Workflow

Each prompt → commit cycle includes:

- An original prompt (as written by the human, with typos preserved)
- An interpreted instruction (cleaned up for clarity)
- A chat response from the LLM (technical result, decision, or code)
- A corresponding Git commit
- An entry in both:
  - `PROMPTS.md` → prompt/commit log
  - `CHAT_LOG.md` → chronological conversational log

All generated files (e.g., `game.py`) include a comment linking to the relevant prompt/commit.

### Debugging Protocol

When the result of a prompt leads to unexpected behavior, a **debug session** begins:

- The human says `record debug` to initiate
- The assistant adopts a Q&A format (Todd ↔ ai-helper)
- The root bug is identified and documented
- One or more test candidates are produced (e.g. `debug-0009-a1.py`)
- Fix is promoted to a proper commit only after successful testing
- Debug sessions are stored in `debug/debug-xxxx-y/`, with:
  - A `README.md` (session summary, outcome, and transcript)
  - All test iterations

The debug transcript is included **in full at the bottom** of the session's README.

---

## 𝓁𝑝 Current Directory Layout

```
├── AUTHOR_NOTES.md     # Human reflection (optional)
├── CHAT_LOG.md         # All AI-human interactions in chronological order
├── PROMPTS.md          # Each prompt + result, in commit order
├── README.md           # Explains philosophy and methodology (project root)
├── debug/
│   └── debug-0009-a/   # Scrollable viewport implementation (bug fix)
│       ├── debug-0009-a1.py
│       ├── debug-0009-a2.py
│       └── README.md   # Summary + full transcript
├── src/
│   └── game.py         # Live, runnable state of the game (generated only)
```

---

## ✓ Current Status (Prompt 0010)

- Fixed visual clutter caused by structured room layouts filling the screen with `#` characters
- Implemented a **scrollable viewport**:
  - Terminal-sized
  - Follows the player
  - Clamps at map edges
- Adopted logic from debug test `debug-0009-a2.py`
- High-value explanatory comments restored in all major functions
- `game.py` is now properly readable and structurally sound

---

## ⚒️ Next Possible Directions

You’re ready to:

- Add interactable elements (objects, enemies, doors)
- Implement turn-based or real-time combat
- Add metadata (e.g. minimap, messages, inventory)
- Introduce save/load mechanics
- Start a new debug branch if another bug arises
- Evolve UX/visual fidelity within terminal constraints

---

## ⛔ What This Is *Not*

- This is **not** a typical game project.
- This is **not** focused on outputting playable content for its own sake.
- This is **not** about LLM novelty — it's about a repeatable, testable, scalable development methodology for **software engineering via prompt-driven workflows**.

---

## Interaction Modes

To control what gets logged and committed during development, this project uses three explicit interaction modes:

### `record`
This mode is used for **standard prompt-driven development**. Everything that follows:
- Will be logged into `CHAT_LOG.md`
- Will result in entries in `PROMPTS.md` if a prompt leads to a code or commit
- Is considered part of the official project history

Use this when issuing any instruction that should influence the final product.

---

### `record debug`
This mode initiates a **structured debug session**. It signals that:
- We are investigating a bug or undesirable behavior introduced by a previous commit
- The assistant will switch to a Q&A format (with labeled turns: **Todd**, **ai-helper**)
- All discussion will be logged into a dedicated `debug/debug-XXXX-Y/README.md` file
- Candidate fixes (e.g. `debug-XXXX-Y1.py`) will be generated and tested
- Once validated, the fix will be promoted to the next numbered commit (e.g. Prompt 0011)

End the session by stating **“fixed”** or confirming resolution. At that point, a transcript will be finalized.

---

### `sidebar`
This disables logging.

Use it for:
- Off-topic discussion
- Planning
- Clarifying instructions
- Backchannel troubleshooting
- Working out design decisions before formalizing them

While in `sidebar` mode:
- Nothing is added to `PROMPTS.md`, `CHAT_LOG.md`, or commit history
- This remains private “scratch space” between the developer and the assistant

Return to a logged state at any time by saying either `record` or `record debug`.

---

## 𝗕𝓽𝗶𝗲 Restarting

When you restart this thread, simply paste this markdown block to resume seamlessly.

Then say:
> `record`  
> to continue development mode, or  
> `record debug`  
> to start a new debug session.
````
