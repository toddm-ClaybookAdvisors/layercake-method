# Chat Transition — transition-002

## Purpose

This file marks the transition from one chat thread to the next. It preserves full continuity of the development process, including philosophy, project layout, interaction modes, and newly established rules. This transition was initiated due to interface slowdowns caused by long conversation history.

---

## Summary of Changes Since transition-001

- Completed Prompt 0012: Modularized `mapgen.py`, added dynamic room generation
- Debug session `debug-0012-a` resolved terminal-size mismatch and import path issues
- Prompt 0013 promoted the working fix: irregular rooms, maze layout, modular architecture, terminal-dimension support, and exit placement at map edge
- README.md formatting was standardized: transcripts must be fully rendered (no code block), and each debug README must end with a Git commit
- All debug commit messages must begin with `fix:`
- PROMPT_INDEX.md was updated to reflect commits through Prompt 0013
- Transition commits now always update PROMPT_INDEX.md and include the latest directory structure in the main README.md

---

## Interaction Modes

To control what gets logged and committed during development, this project uses three explicit interaction modes:

### record

This mode is used for **standard prompt-driven development**. Everything that follows:
- Will be logged into `CHAT_LOG.md`
- Will result in entries in `PROMPTS.md` if a prompt leads to a code or commit
- Is considered part of the official project history

Use this when issuing any instruction that should influence the final product.

### record debug

This mode initiates a **structured debug session**. It signals that:
- We are investigating a bug or undesirable behavior introduced by a previous commit
- The assistant will switch to a Q and A format (with labeled turns: Todd, ai-agent)
- All discussion will be logged into a dedicated file: `debug/debug-XXXX-Y/README.md`
- Candidate fixes (e.g., `a1/`, `a2/`) will be tested
- Once validated, the fix will be promoted to the next numbered commit

End the session by stating "fixed" or confirming resolution. A transcript will then be finalized.

**Required:** All debug commits must begin with `fix:`  
**Required:** Every debug README must include a final `git commit` line  
**Required:** Transcripts must be rendered as standard markdown (no code block formatting)

### sidebar

This disables logging.

Use it for:
- Off-topic discussion
- Planning or design decisions
- Pre-prompt clarification or scratch work
- Working out ideas before formal commits

By default, nothing said in sidebar mode is included in `PROMPTS.md`, `CHAT_LOG.md`, or any git commit trail.  
**Exception:** If a sidebar prompt introduces a new rule, standard, or persistent instruction, that prompt text may be included in the corresponding `PROMPTS.md` entry under a "Sidebar Additions" section.


Return to a logged state at any time by saying either `record` or `record debug`.

---

## Project Structure Snapshot

```
game-example/
├── src/
│   ├── game.py
│   └── mapgen.py
│
├── debug/
│   └── debug-0012-a/
│       ├── a1/
│       ├── a2/
│       └── README.md
│
├── chat-transition/
│   ├── transition-001.md
│   └── transition-002.md
│
├── PROMPTS.md
├── CHAT_LOG.md
├── PROMPT_INDEX.md
├── AUTHOR_NOTES.md
└── README.md
```

---

## Current Status

- Prompt 0013: Modular generation with maze and exit logic confirmed
- Prompt 0014: This transition file created, prompt index updated, new policies locked in

---

## Transition Policy

Each chat thread must:
- End with a `chat-transition/transition-XXX.md` file
- Trigger a new commit (type: `chore`)
- Update `PROMPT_INDEX.md`
- Update the root `README.md` with the latest directory structure, and other additions either explicitly added by Todd (by saying "add to README") during the course of the chat or suggested by ai-agent and previewed for Todd before application
- Contain no emoji or Unicode icons — ASCII only

You are now in a fresh chat context. Say `record` to resume prompt-driven development or `record debug` to begin a bug investigation.
