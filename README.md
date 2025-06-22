# LLM-Driven Game Development

This project is not a typical game.  
It is a **transparent, prompt-by-prompt demonstration** of how to use a Large Language Model (LLM) as a complete software development assistant.

The final product happens to be a 2D terminal-based adventure game.  
The true purpose is to document and refine a repeatable methodology for:

- Building real software without writing code directly  
- Capturing all changes through Git-based prompt versioning  
- Treating the LLM as coder, collaborator, and documentarian  

---

## Roles

**Human:**  
- Strategic lead  
- Prompt author  
- Reviewer and tester  

**LLM:**  
- Architect  
- Implementer  
- Logger and documentarian  

---

## Layer Types

All work is performed in numbered **layers**, each with one of the following types:

- `feature` — Adds new capabilities  
- `refactor` — Restructures code or logic without changing behavior  
- `fix` — Resolves bugs or regressions (replaces `debug`)  
- `move chat` — Begins a new thread, regenerates `README.md` and `chat-boot.md`, refreshes prompt index  

---

## Layer Lifecycle

Each layer follows a strict lifecycle:

1. **`create layer`**  
   Declare layer type and goal.

2. **Prompt**  
   Describe the desired change.  
   The original prompt is recorded **only in the devlog**.

3. **`test`**  
   LLM returns a full preview of all changed files in a **single markdown block**.

4. **Iterate**  
   Back-and-forth discussion and refinements are logged in `devlog/devlog-XXXX.md`.

5. **`complete`**  
   Locks the implementation for finalization.

6. **`commit`**  
   Generates all artifacts:  
   - `PROMPTS.md` (cleaned instruction only)  
   - `CHAT_LOG.md`  
   - `devlog/` transcript  
   - Commit with suffix `(XXXX)`  
   - Updates `PROMPT_INDEX.md` with real links  
   - Updates `README.md` and `chat-boot.md` if `move chat`  

> `PROMPT_INDEX.md` is updated only after merge to `main`.

---

## Rules and Standards

- All code must be LLM-generated — no human-authored source code  
- Devlogs include complete conversational transcripts  
- Code previews must be rendered as **single markdown blocks**  
- Commits must end with the layer number  
- All `fix:` commits must begin with `fix:`  
- No emojis or non-ASCII symbols are permitted  
- If a file is not in memory, the assistant will prompt you to upload it before proceeding  

---

## Repository Integration

**Commit Links:**  
`https://github.com/toddm-ClaybookAdvisors/layercake-method/commit/<hash>`

**Prompt Anchors:**  
`logs/PROMPTS.md#prompt-XXXX`

**Devlogs:**  
`logs/devlog/devlog-XXXX.md`

---

## Directory Structure

└── README.md  
├── app  
│   └── config.json  
│   ├── src  
│   │   └── entities.py  
│   │   └── game.py  
│   │   └── mapgen.py  
│   │   └── renderer.py  
│   │   └── utils.py  
├── bin  
│   └── get_project_structure.sh  
│   └── play_game.sh  
└── chat-boot.md  
├── docs  
│   └── AUTHOR_NOTES.md  
│   └── PROMT_INDEX.md  
│   └── PYTHON_SETUP.md  
├── logs  
│   └── CHAT_LOG.md  
│   └── PROMPTS.md  
│   ├── debug  
│   │   ├── debug-0009-a  
│   │   │   └── README.md  
│   │   │   └── debug-0009-a1.py  
│   │   │   └── debug-0009-a2.py  
│   │   ├── debug-0012-a  
│   │   │   └── README.md  
│   │   │   ├── a1  
│   │   │   │   └── game.py  
│   │   │   │   └── mapgen.py  
│   │   │   ├── a2  
│   │   │   │   └── game.py  
│   │   │   │   └── mapgen.py  
│   ├── devlog  
│   │   └── devlog-0017  
│   │   └── devlog-0019  
│   │   └── devlog-0020  
│   │   └── devlog-0021  
│   │   └── devlog-0022  
│   │   └── devlog-0023  
└── start_dev_session.sh


---

## Getting Started

1. Install Python 3.11+ — see [PYTHON_SETUP.md](docs/PYTHON_SETUP.md)  
2. Run the game from `app/src/game.py`  
3. Start a new layer using `create layer`  
4. If asked to upload a file, provide the most recent committed version  

---

## Status

- Latest completed layer: `0023` (modular refactor, new structure)  
- Current layer: `0024` — `move chat`  
- Next step: Begin `0025` with `create layer`
