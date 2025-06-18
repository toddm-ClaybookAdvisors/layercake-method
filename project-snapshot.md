# PROJECT SNAPSHOT — LLM-Driven Game Development

## Purpose

This is not a game development project — it is a **demonstration of how to use an LLM as a complete software development assistant**. The end product happens to be a 2D adventure game, but the true goal is to showcase:

- Prompt-by-prompt development  
- A workflow where the human writes **no code**  
- The LLM performs all architectural, functional, and implementation tasks  
- Transparent, traceable iteration using Git  
- Best practices for writing and evolving effective prompts  

The human acts as **strategic lead, prompt author, reviewer, and tester**.  
The AI acts as **coder, collaborator, and documentarian**.

---

## Methodology

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

---

## Debugging Protocol

When bugs are encountered, the assistant enters a structured debug mode using isolated subdirectories (e.g., `debug-0012-a/a1/`) to safely test fixes.

- Each debug session is logged in a dedicated `README.md` under its debug path  
- Final fixes are promoted to the mainline after validation  
- Commit messages for debug fixes always begin with `fix:`

---

## Prompt Tracking

Prompts are tracked in two files:

- `PROMPTS.md` → Each prompt + clean instruction + resulting code/commit  
- `CHAT_LOG.md` → Linear chat history for recorded development  

Each has an entry labeled by prompt ID (e.g., 0006) and commit hash.  
There is also a `PROMPT_INDEX.md` to cross-reference them.

---

## Project Structure

```
game-example/
├── src/                     # Live application code
│   ├── game.py
│   └── mapgen.py
│
├── debug/                   # Isolated fix branches for debugging sessions
│   └── debug-XXXX-a/
│       ├── a1/
│       ├── a2/
│       └── README.md        # Full transcript and fix summary
│
├── chat-transition/         # Logs transitions between chat threads
│   ├── transition-001.md
│   └── transition-002.md    # Latest session boundary
│
├── PROMPTS.md               # Each prompt with clean instruction + result
├── CHAT_LOG.md              # Chronological log of recorded interactions
├── PROMPT_INDEX.md          # Prompt-to-commit index with links
├── AUTHOR_NOTES.md          # Optional human notes
└── README.md                # (This file)
```