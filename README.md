# Building a Game with an LLM — A Prompt-Driven Dev Diary

## Purpose

This project is a transparent, prompt-by-prompt experiment in building a fully functional 2D adventure game using only natural language instructions to an AI assistant (ChatGPT).

The human (me) does not write any of the game’s code directly. Instead, the AI acts as the software engineer — generating all implementation details based on prompts I provide.

---

## Methodology

Each step of game development is initiated by a plain-language prompt and executed by the LLM.

Each commit includes:
- The exact prompt that led to the change
- The generated code that resulted from it
- A reference to the commit in a running log file

This creates a clear, traceable evolution of the project from zero to a playable game.

---

## Project Context Boot

To fully restore context for this project, use the following files:

- [project-snapshot.md](./project-snapshot.md)
- [transition-001.md](./chat-transition/transition-001.md)
- [transition-002.md](./chat-transition/transition-002.md)

In any new thread, say:

> Use the project files above to reinitialize context. Assume `record` mode. No emoji. Follow all documented rules.

---

## Debugging Protocol

When bugs are encountered, the assistant enters a structured debug mode using isolated subdirectories (e.g., `debug-0012-a/a1/`) to safely test fixes.

- Each debug session is logged in a dedicated `README.md` under its debug path
- Final fixes are promoted to the mainline after validation
- Commit messages for debug fixes always begin with `fix:`

---

## Prompt Tracking

Prompt and result pairs are tracked using Git commit history and a single file named `PROMPTS.md`.

- Each commit message includes the full prompt and a summary of the result.
- The prompt is also included as a comment at the top of any generated code files.
- `PROMPTS.md` serves as a human-readable index of the development process.

This avoids the need for managing dozens of small files while maintaining a full, navigable history.

---

## Directory Structure

game-example/
├── src/ # Live application code
│ ├── game.py # Main entry point, game loop, orchestration
│ ├── entities.py # Player, Adversary, and all entity logic/state
│ ├── renderer.py # Rendering, colorization, and display logic
│ ├── utils.py # Utility functions, terminal helpers, shared constants
│ └── mapgen.py # Map generation logic (unchanged from earlier layers)
│
├── debug/ # Isolated fix branches for debugging sessions
│ └── debug-XXXX-a/
│ ├── a1/
│ ├── a2/
│ └── README.md # Full transcript and fix summary
│
├── chat-transition/ # Logs transitions between chat threads
│ ├── transition-001.md
│ └── transition-002.md # Latest session boundary
│
├── PROMPTS.md # Each prompt with clean instruction + result
├── CHAT_LOG.md # Chronological log of recorded interactions
├── PROMPT_INDEX.md # Prompt-to-commit index with links (updated after merge to main)
├── AUTHOR_NOTES.md # Optional human notes
├── README.md # (This file)
└── PYTHON_SETUP.md # [See below: Python install instructions]


---

## Iteration Format

- All prompt/result pairs are committed to Git.
- Prompt is included in both the commit message and at the top of each modified code file.
- `PROMPTS.md` logs the high-level evolution in readable format.

---

## Why This Matters

This project is not just about building a game. It demonstrates:
- How large language models can be used as hands-on development collaborators
- What makes a prompt effective
- How to trace software evolution transparently from human intent to working code

---

## Prerequisites

- Python 3 installed
- Git for version control

For full instructions, see [PYTHON_SETUP.md](./PYTHON_SETUP.md).

---

## How to Run the Game

After following the environment setup, from the root of the project directory:

```bash
cd src
python3 game.py
