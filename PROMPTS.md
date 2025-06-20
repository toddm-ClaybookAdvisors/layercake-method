## Prompt 0001: Define Project Purpose, Structure, and Prompt Tracking

**Instruction:**

Generate the README.md file explaining the purpose of this project and the way it will be structured. This project demonstrates how an LLM can be used to build a 2D game in layers through prompt-based iteration. Each commit will include the full prompt, the generated result, and a reference in a running log file. The chosen tracking method is a single PROMPTS.md file and Git commit messages as the primary source of truth.

**Result:**

→ See: README.md  
→ Commit: 0001 (Define project purpose, structure, and prompt tracking)

## Prompt 0002: Add Python Environment Setup Instructions for macOS

**Instruction:**

Create instructions for setting up a Python 3 virtual environment on macOS that I can include in a README file. Assume the user does not have Python installed.

**Result:**

→ See: README.md  
→ Commit: 0002 (Add Python environment setup instructions for macOS)

## Prompt 0002: Add Python Environment Setup Instructions for macOS - *NOTE* I had a sidebar with our friend because it kept breaking the instructions into steps that were part of the chat, not the contiguous code block I had asked for

**Instruction:**

Create instructions for setting up a Python 3 virtual environment on macOS that I can include in a README file. Assume the user does not have Python installed.

**Result:**

→ See: README.md  
→ Commit: 0002 (Add Python environment setup instructions for macOS)

## Prompt 0003: Add Basic ASCII Game Loop with WASD Movement

**Instruction:**

Create the simplest possible game loop in Python that runs in the terminal and redraws a small ASCII map on every iteration. The player should be represented by `@` and should be able to move up, down, left, and right using the WASD keys. Use only built-in libraries. Do not worry about real-time input or screen clearing yet — just focus on the loop and basic movement logic.

**Result:**

→ See: game/game.py
→ Commit: 0003 (Add basic ASCII game loop with WASD movement)

## Prompt 0004: Add .gitignore for Python and VS Code

**Instruction:**

Create a `.gitignore` file for a Python project that includes standard Python exclusions as well as common Visual Studio Code settings and folders.

**Result:**

→ See: .gitignore  
→ Commit: 0004 (Add .gitignore for Python and VS Code)

## Prompt 0005: Add Screen Clearing and Real-Time Input to Game Loop

**Instruction:**

Update the basic ASCII game loop so that the screen clears on every frame and player movement works without pressing Enter. Use only built-in libraries. It should work on macOS and Linux in the terminal (no GUI). If necessary, use `msvcrt` only on Windows, and fallback to `termios` and `tty` elsewhere.

**Result:**

→ See: game/game.py  
→ Commit: 0005 (Add screen clearing and real-time input to game loop)

## Prompt 0006: Expand Game Board and Add Explanatory Comments

**Instruction:**

Triple the size of the game board in the existing loop and add high-quality comments to the code. With each code iteration, explain what you've changed and why.

**Result:**

→ See: game/game.py  
→ Commit: 0006 (Expand game board and add explanatory comments)

## Prompt 0007: Suggest Next Steps for Gameplay Evolution

Here are five potential next steps for evolving the game from its current state (a real-time, grid-based map with free-form movement). These are ranked based on their likely impact on gameplay depth, development momentum, and demonstrating structured game architecture.

### 1. Add Static Obstacles or Walls (Rank 1)
Introduce impassable tiles (`#`) to the map. This adds structure, pathing, and environmental interaction — critical for almost all future mechanics (like enemies or loot). It transforms the space from an open sandbox into something navigable.

### 2. Implement a Bounded Camera Viewport (Rank 2)
Instead of printing the entire 30x15 map, show only a window (e.g., 10x5) around the player. This introduces the concept of *exploration*, a key adventure game mechanic, and prepares the game for much larger maps without overwhelming the terminal.

### 3. Place Interactive Items on the Map (Rank 3)
Randomly spawn objects (`!`, `*`, `$`) that the player can pick up or trigger by moving onto them. This introduces stateful gameplay and sets the foundation for inventory systems, rewards, or power-ups.

### 4. Add NPCs or Enemies (Rank 4)
Place AI-controlled characters (`E`, `N`) on the map that move or react to the player. Even simple random movement makes the world feel alive. This opens doors to stealth, combat, or quests.

### 5. Implement Game State Persistence (Rank 5)
Allow saving and loading of the game world, player position, and item states to disk. Useful for longer games, debugging, or sharing progress. While not essential right now, this becomes powerful once more mechanics are added.

Each of these can be layered modularly, but I recommend starting with **obstacles** for prompt 0008 — it delivers the fastest gameplay payoff with minimal complexity.

## Prompt 0008: Add Static Obstacles and Expand Map to 100×100

**Original Prompt:**

I like suggestion #1, however, we'll need a bigger board for it to really work. Let's go to 100 x 100, or should we go bigger?

**Instruction:**

Implement static obstacles in the game map by adding impassable tiles (`#`) and expand the map size from 30×15 to 100×100 to give meaningful room for navigation. Consider whether an even larger map would be beneficial. Update all related logic and preserve previous functionality (movement, drawing, boundaries). Include high-quality comments and describe what changed and why.

**Result:**

→ See: game/game.py  
→ Commit: 0008 (Add static obstacles and expand map to 100x100)


## Prompt 0009: Replace Random Obstacles with Room-and-Hallway Structure

**Original Prompt:**

the obstacles make the screen really busy. give them more structure, like rooms and hallways

**Instruction:**

Replace the randomly scattered obstacles with a more structured map layout that resembles rooms and hallways. Maintain the 100×100 dimensions, but generate navigable spaces with connected rectangular rooms separated by walls, using simple procedural generation. Preserve movement and boundary logic, and include explanatory comments to describe how the map is constructed.

**Result:**

→ See: game/game.py  
→ Commit: 0009 (Replace random obstacles with room-and-hallway structure)

## Prompt 0010: Finalize Scrollable Viewport for Structured Map

**Original Prompt:**

Ok, let's do commit 0010 update game.py with our changes from the debug session and reinstate the high value comments

**Instruction:**

Finalize the fix for the visual clutter issue introduced in prompt 0009 by implementing the dynamic scrollable viewport used in `debug-0009-a2.py`. Update `game.py` with this logic and reinstate all high-value comments describing each major function and design decision.

**Related Debugging:**
See: [debug/debug-0009-a/README.md](debug/debug-0009-a/README.md)

**Result:**

→ See: game/game.py  
→ Commit: 0010 (add scrollable viewport and restore annotated game logic)

## Prompt 0011: Archive Transition State

**Original Prompt:**

If I give you a git clone url, and a list of commits from the git history, can you generate a table of contents that links the PROMPTS.md entry to the CHATLOG.md?

**Instruction:**

This prompt formally captures the state of the project prior to transitioning to a new chat thread. No changes to `game.py` or system logic were made. Instead, this commit introduces:

- `PROMPT_INDEX.md` — a navigable table mapping each prompt to its Git commit and chat log anchor
- `chat-transition/transfer-001.md` — metadata explaining the reason, timing, and structure of the conversation reset

This commit also enforces ongoing project policies:
- No emoji are used in any file, ever
- All prompts, commits, and responses are clearly logged and versioned

**Result:**

→ See: chat-transition/transfer-001.md  
→ See: PROMPT_INDEX.md  
→ Commit: 0011 (Archive transition state and generate prompt index)

## Prompt 0012: Irregular Room Generation with Reachable Exit

**Original Prompt:**

Change the simple room structure to include multiple room shapes and maze like hallways between them. Include an exit

**Instruction:**

Replace the uniform grid of rectangular rooms with a procedurally generated layout featuring:
- Unevenly distributed rooms of different shapes and sizes
- Maze-like hallways that connect all rooms via valid, walkable paths
- An exit `>` placed at the far edge of the map and reachable from the player start
- A much higher room density, filling 60–80% of the map

Move all map-generation logic into a new module: `mapgen.py`. Update `game.py` to import from this module, preserving viewport, player movement, and display features.

**Result:**

→ See: src/mapgen.py  
→ See: src/game.py  
→ Commit: 0012 (Irregular room generation, maze-like connections, modular mapgen)

## Prompt 0013: Finalize Irregular Room Generation and Modular Map Architecture

**Original Prompt:**

Change the simple room structure to include multiple room shapes and maze like hallways between them. Include an exit.

**Instruction:**

Introduce irregularly shaped rooms and maze-like hallways into the game map, ensuring all rooms are accessible and connected. Add a visible exit near the edge of the playable area. Expand the usable screen space to make the layout feel open. Modularize the map generation logic by moving it into a new `mapgen.py` file.

This prompt promotes the successful fix from debug session `debug-0012-a`, ensuring all bugs were resolved and the viewport adapts dynamically to terminal dimensions.

**Related Debugging:**
See: [debug/debug-0012-a/README.md](debug/debug-0012-a/README.md)

**Result:**

→ See: `src/game.py`, `src/mapgen.py`  
→ Commit: 0013 (irregular rooms, maze layout, modular mapgen architecture)


## Prompt 0014: Transition to New Chat Thread (transition-002)

**Original Prompt:**

ok, let's do the next commit. It is a transition commit since this chat is getting slow.

**Instruction:**

Initiate a chat thread reset to preserve performance and continue clean iteration. Generate a new `chat-transition/transition-002.md` file containing:

- A summary of changes since transition-001
- Consolidated interaction mode policies
- All rules added since the previous thread
- An updated project directory snapshot
- Clarification that emoji and non-ASCII characters are prohibited

**Sidebar Additions:**

> **"all debug session commit messages need to start with 'fix:'"**  
> [sidebar] Rule: All debug commits must begin with `fix:`

> **"the entire README.md should be in a markdown window"**  
> [sidebar] Rule: All debug `README.md` transcripts must be fully rendered in standard markdown, not in code blocks

> **"all debug readmes must include the git commit command at the end"**  
> [sidebar] Rule: Each debug `README.md` must include the `git commit` line for the fix

> **"this chat is getting slow. give me a preview of the chat transition file"**  
> [sidebar] Rule: Each chat thread must end with a transition file (`transition-XXX.md`)

> **"when doing a transition, update the prompt index. ask for the git log if necessary."**  
> [sidebar] Rule: Every transition must update `PROMPT_INDEX.md`. If not already cached, the assistant must ask for `git log`.

> **"the main README.md is out of date and doesn't include the transition directory"**  
> [sidebar] Rule: Transitions must regenerate the root `README.md` to reflect current structure and incorporate any explicitly requested additions via "add to README", or any assistant-suggested updates previewed for Todd

> **"mark changes that happened during a sidebar with [sidebar]"**  
> [sidebar] Rule: Any rules, file changes, or documentation instructions that originate in sidebar must be marked `[sidebar]` in logs

> **"what would the PROMPT addition look like if you added all of the original side bar prompts that led to a [sidebar] instruction line?"**  
> [sidebar] Rule: Sidebar prompts that directly introduce new rules or conventions may be listed in full within the `PROMPTS.md` entry

**Result:**

→ See: chat-transition/transition-002.md  
→ See: PROMPT_INDEX.md  
→ See: README.md  
→ Commit: 0014 (document chat thread transition in transition-002)


## Prompt 0015: Refactor mapgen.py and game.py for clarity, structure, and performance

**Original Prompt:**
I've switched to 4.1 and am curious to see how you will refactor my existing code.  I've attached the files here, please refactor them for clarity, structure and performance.

**Instruction:**
Refactor both `mapgen.py` and `game.py` for clarity, structure, and performance using GPT-4.1. Improve modularity, docstrings, high-value comments, and overall maintainability while preserving gameplay and UX.

**Result:**
Both files were refactored for modularity, clarity, and maintainability:

- Code was organized into cleanly separated classes and helpers
- Strategic docstrings and high-value explanatory comments were added
- Viewport logic, game loop, and map generation are easier to follow and extend
- All core gameplay logic (player movement, win condition, scrolling viewport) was retained
- **User input now requires pressing RETURN for each move**, rather than supporting single-key movement; this changes user experience for improved cross-platform compatibility and simplicity
- **Viewport dimensions are now fixed rather than auto-sizing to the terminal window**; this alters how much of the map is visible at once and may affect player navigation
- No other major gameplay features were added or removed

→ See: src/mapgen.py, src/game.py  
→ Commit: 0015 (refactor: modularize and clarify mapgen and game logic)

## Prompt 0016

**Original Prompt:**
My intention was for the view port to be a view into a much larger map underneath, can you do that?

**Instruction:**
Implement a persistent large map (100x100 by default), with a smaller, centered viewport window (default 40x20), all configurable via a new `config.json` in the project root. Update `game.py` to load map and viewport size from this config file at runtime. Ensure the version string remains dynamic, parsed from PROMPTS.md (+1), and visible in the upper left along with real-time FPS. Do not log PROMPTS.md, CHAT_LOG.md, or the commit line until instructed.

**Result:**
- Created `config.json` in the project root (supports `map_width`, `map_height`, `viewport_width`, `viewport_height`)
- `game.py` now loads all sizing from config at startup
- The visible game area is always a viewport window onto a persistent large map (default 100x100)
- Version string is dynamically parsed from PROMPTS.md and incremented for "work-in-progress" state
- FPS and version are shown in the upper left; input, movement, and all other logic unchanged
- Future viewport or map size changes only require editing config.json

→ See: src/game.py, config.json  
→ Commit: 0016 (config-driven map and viewport, dynamic version, persistent large map)

## Prompt 0017

**Original Prompt:**
Ok, we're ready for our next feature.  We're going to add an "adversary".  there are no goals or intelligence yet, but the adversary is red and shows up on the map with its own view window.  We will also introduce a tick system that will be used later to move the adversary when the player moves

**Instruction:**
Implement persistent fog-of-war and player trail in a large (300x300) map with a dynamic viewport that always fits within the terminal. The viewport is defined as the portion of the map, scrolling with the player, that is rendered at any given time, regardless of fog. Always reserve one line for the top status bar, three lines for controls/messages at the bottom, and one line for user input; never print more lines than fit in the terminal. All output remains on screen without scrolling.

**Prompt Evolution:**
- **Initial intent:** Add an adversary with its own viewport and tick system.
- **Changed feature:** Pivoted to adding fog of war, making explored tiles permanently visible as the player moves.
- **Clarified:** Explored tiles remain visible as they appear in the viewport; unexplored tiles appear as they do now (blank).
- **Further refined:** Specified that the player’s trail should persist—tiles ever seen remain visible even when outside the viewport.
- **Final implementation:** Map is now 300x300, with dynamic viewport, persistent fog/trail, and correct status/message bar layout.

**Result:**
- Status bar (version, tick, FPS) is always visible at the top.
- Controls and messages are always visible at the bottom, never scrolled off.
- Viewport dynamically fits the terminal and scrolls with the player.
- Fog-of-war and player trail work as intended across a 300x300 map.
- Code now prints at most terminal height - 1 lines, reserving the last line for user input.
- All indentation and padding issues fixed.

→ See: src/game.py  
→ Commit: 0017 (fix: status bar and persistent viewport rendering for fog-of-war)








