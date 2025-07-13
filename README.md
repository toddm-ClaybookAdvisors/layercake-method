# LLM-Driven Game Development (Dual-AI, Modular, Git-Native Experiment)

This project is not a typical game.
It is a **transparent, experiment-driven demonstration** of how to use Large Language Models (LLMs) as collaborative, role-specialized software development assistants.

The resulting product is a 2D terminal-based adventure game, but the **primary goal** is to document and refine a *repeatable, auditable methodology* for:

* Building software with **zero human-authored code**
* Capturing all changes as *numbered Git commit layers* with rich, structured commit messages
* Enforcing process through explicit, role-based AI protocols
* Making all rationale, design, and review steps machine- and human-readable for research, audit, and future automation

---

## Roles

**Human:**

* Strategic lead
* Prompt author
* Reviewer, tester, and auditor

**Architect-Laboratory AI (chatGPT, GPT-4o):**

* System architect and coder
* Implements all features/fixes as instructed by human prompts
* Documents rationale, process, and file attributions
* Prepares code and context for review

**Reviewer-Refactorer AI (Claude):**

* Code reviewer and refactorer
* Outputs focused patches/diffs, rationales, and recommendations
* Ensures code clarity, maintainability, and adherence to best practices
* Operates with strict token discipline and review protocol

---

## Layered, Git-Native Development

**Every Git commit is a “layer.”**

* Layer numbers are tracked in [`experiment/LAYER_INDEX.md`](experiment/LAYER_INDEX.md).
* No per-layer folders: all code/artifacts are tracked in Git; key process and persona files are under `experiment/protocol/`.

### **Layer Commit Format**

* First line:
  `[0038](1h 08m) Structure refactor: modular audit/AI workflow, no per-layer folders`
* Then, a JSON block with all structured layer metadata (prompt, rationale, reviewer notes, files, timestamps, roles).

---

## Process and Protocols

* **All AI/persona, workflow, directives, and prompt templates** are modularized under:

  * `experiment/protocol/persona/`
  * `experiment/protocol/workflow/`
  * `experiment/protocol/directives/`
  * `experiment/protocol/prompt-templates/`
* **Automation and reporting scripts:** `experiment/scripts/`
* **Devlogs (session transcripts):** `experiment/devlog/`
* **Project and experiment meta:** `experiment/README.md`, `experiment/LAYER_INDEX.md`, `experiment/AUTHOR_NOTES.md`
* All code generation, review, and commit behavior is governed by these modular protocol files.
* Each LLM follows a strict, role-specific workflow.

---

## Rules and Standards

* **No human-authored source code** — all implementation and changes must originate from the AI workflow.
* **All code changes are versioned as Git commits,** one per conceptual “layer.”
* **Commit messages** must begin with `[layer number](duration) Top-level summary` and include a full JSON metadata block.
* **All rationale, prompts, and reviewer notes** are included in the commit message for both machine and human readability.
* **No per-layer artifact folders.** All metadata and documentation for each layer is extractable from the commit log and `LAYER_INDEX.md`.
* **No emojis or non-ASCII symbols are permitted.**
* If a file is not present or in memory, the AI will prompt for upload before continuing.

---

## Repository Integration

**Clone this repo:**
`git clone https://github.com/toddm-ClaybookAdvisors/layercake-method.git`

**Layer Index:**
See [`experiment/LAYER_INDEX.md`](experiment/LAYER_INDEX.md) for the complete, up-to-date index of all layers, commits, durations, summaries, and artifact links.

**Author Notes:**
See `experiment/AUTHOR_NOTES.md` for project insights and history.

**Devlogs:**
See `experiment/devlog/` for per-layer, per-session transcripts.

**Protocols & Onboarding:**

* `experiment/protocol/README.md` — Overview and navigation for all protocol files
* `experiment/protocol/persona/` — Role-specific AI personas
* `experiment/protocol/workflow/` — Step-by-step process for each AI role
* `experiment/protocol/directives/` — Audit, commit, and artifact policies
* `experiment/protocol/prompt-templates/` — Output and prompt patterns

**Scripts:**

* `experiment/scripts/` — Post-processing, reporting, or artifact extraction

---

## Directory Structure (After Refactor)

```plaintext
project-root/
├── app/
│   ├── src/
│   │   ├── entities.py
│   │   ├── game.py
│   │   ├── mapgen.py
│   │   ├── renderer.py
│   │   ├── test_entities.py
│   │   └── utils.py
│   ├── config.json
│   ├── archive-for-next-layer/
│   ├── author-notes.txt
│   └── chat-boot.md
├── experiment/
│   ├── devlog/
│   ├── protocol/
│   │   ├── directives/
│   │   │   ├── chatgpt.md
│   │   │   ├── claude.md
│   │   │   └── shared.md
│   │   ├── persona/
│   │   │   ├── chatgpt.md
│   │   │   ├── claude.md
│   │   │   └── shared.md
│   │   ├── prompt-templates/
│   │   │   ├── chatgpt.md
│   │   │   ├── claude.md
│   │   │   └── shared.md
│   │   └── workflow/
│   │       ├── chatgpt.md
│   │       ├── claude.md
│   │       └── shared.md
│   ├── scripts/
│   ├── AUTHOR_NOTES.md
│   ├── LAYER_INDEX.md
│   └── README.md
├── README.md

```

---

## Getting Started

1. Clone the repository:
   `git clone https://github.com/toddm-ClaybookAdvisors/layercake-method.git`
2. Install Python 3.11+
3. Run the game from `app/src/game.py`
4. Start a new layer by making a prompt and using the AI workflow
5. All project and process files are under `experiment/`
6. All layer activity and rationale are captured in Git commits and [`experiment/LAYER_INDEX.md`](experiment/LAYER_INDEX.md)
7. See `experiment/protocol/README.md` for protocol and onboarding details

---


## Meta & History

**Author Notes:**  
See `experiment/AUTHOR_NOTES.md` for personal lessons, project insights, and process history.

