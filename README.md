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

The first prompt will set up the Python environment for development.

---

## Python Environment Setup (macOS)

Follow these steps to install Python 3 and create a development environment for the project.

### 1. Install Homebrew

If you don’t already have Homebrew (a macOS package manager), install it using the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python 3

Once Homebrew is installed, use it to install Python:

```bash
brew install python
```

Verify installation:

```bash
python3 --version
```

### 3. Create and Activate a Virtual Environment

From the root of the project directory:

```bash
python3 -m venv venv
source venv/bin/activate
```

Your shell prompt should now begin with `(venv)` indicating the environment is active.

### 4. Upgrade Pip and Track Dependencies

```bash
pip install --upgrade pip
pip freeze > requirements.txt
```

This upgrades pip and creates a requirements file that can be used to reproduce the environment.

### 5. Run the Game (Once Code Is Added)

Later, when the first game loop is implemented, you can run the game like this:

```bash
cd src
python3 game.py
```
