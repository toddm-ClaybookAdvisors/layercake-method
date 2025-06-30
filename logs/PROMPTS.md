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

## Prompt 0018: Transition to New Chat Thread (transition-003)

**Original Prompt:**
you are slow now, let's do a transition

**Instruction:**
Archive project state and all new conventions (devlog, prompt evolution, original prompt logging, viewport definition, etc.) in `chat-transition/transition-003.md`. Begin a new thread to maintain performance and clean context.

**Result:**
- Documented transition and all new conventions in `chat-transition/transition-003.md`.
- No code or design changes; state and policy only.
- Ready for immediate context re-init and continuation in new thread.

→ See: chat-transition/transition-003.md  
→ Commit: 0018 (chore: document thread transition and new conventions)

## Prompt 0019: Enhance dungeon with labyrinth near exit and guaranteed connectivity

**Original Prompt:**  
Make the door reachable with multiple paths, add labyrinth near door, and increase dungeon complexity with more rooms and loops.

**Instruction:**  
- Implement a maze area near the exit door with multiple corridor connections to nearby rooms.  
- Increase number and size variation of rooms for a more dungeon-like feel.  
- Add loops and cross corridors between rooms.  
- Add connectivity check (BFS) to ensure exit is reachable, and fix if unreachable.  
- Improve BFS with step limit to avoid infinite loops.

**Result:**  
Updated `mapgen.py` with recursive backtracker maze near exit, multiple corridor connections, additional loops, and BFS connectivity check with timeout.  
Updated connectivity fix to carve corridors through midpoint for better reachability.  
Also updated `game.py` to render the door as bold red '0' visible when on screen.

**Commit:** fix: prevent infinite BFS in connectivity check and improve connectivity fix

## Prompt 0020: Make the player green and leave a green trail

**Original Prompt:**
Make the player green and add have it leave a green trail behind it indicating where it has been only tiles it has passed over will be turned green.   Put any color codes in a constant that goes at the top of the file with the other color constants.

**Instruction:**
Update the game so that:
- The player `@` is drawn in green (using a `COLOR_GREEN` constant).
- As the player moves, each tile it has passed over is marked with a green `·`.
- Only tiles actually stepped on by the player are marked with the green trail.
- Color codes are stored as top-level constants in the file.
- Fog-of-war, viewport, and status bar behavior are unchanged.

**Result:**
- The player `@` appears green in the terminal.
- Every tile stepped on by the player permanently shows a green `·` (unless covered by the player, wall, or exit).
- Color constants are defined at the top of `game.py`.
- All fog-of-war and UI features work as before.

→ See: src/game.py  
→ Commit: 0020 (feat: player and trail rendered in green using COLOR_GREEN constant)

## Prompt 0021: Render player as a green stick figure and display coordinates

**Original Prompt:**
Visual, Sterling would like the player to look more like a stick figure  
before we finish this layer, one more thing. Please add the x,y coordinates to the top info bar

**Instruction:**
- Change the player symbol from green `@` to a green stick figure, using the Unicode `†` character (COLOR_GREEN).
- Update the status/info bar at the top of the game to include the player’s coordinates as `Pos: (x, y)`.
- All other features and conventions remain unchanged.

**Result:**
- The player is now rendered as a green `†` in the viewport.
- The top info bar shows the player’s current position as `Pos: (x, y)`.
- All prior features (trail, fog, status bar, etc.) are preserved.

→ See: src/game.py  
→ Commit: 0021 (feat: player is green stick figure, position added to info bar (0021))

## Prompt 0022: Adversary lock-on, exploration, and hallway-following

**Original Prompt:**
let's add the adversary.  
icon: a bold red X  
behavior: moves randomly until it finds a wall then it follows the wall. If it encounters the players green trail it follows it until it encounters the player. the adversary has a red trail. if it touches the player the player loses. the adversary can see two tiles around it.
(the prompt evolved to require robust pathfinding lock-on, hallway-following, fog-of-war, and player slow on red trail—see devlog for full dialog.)

**Instruction:**
- Add an adversary (`X`, bold red) that explores the dungeon, leaves a red trail, and is hidden under fog.
- When the adversary sees any part of the player's green trail, it robustly “locks on” using BFS from its position to the player *only along green trail tiles*, and pursues as far as the trail leads.
- When in a 1-tile-wide hallway or gap, the adversary commits to moving straight through, only turning at intersections or dead ends.
- When the adversary locks on, the player receives a message ("You feel a chill...").
- If the player stands on a red trail tile, they are slowed and can only move every other turn.
- The adversary is only rendered if visible to the player (i.e., not under fog-of-war).
- If the adversary reaches the player, the player loses.

**Result:**
- The adversary actively explores, commits to hallway movement, and robustly pursues the player via green trail when possible.
- All visuals and features are fog-of-war-aware.
- Slowing, trail, and win/loss conditions function as described.

→ See: src/game.py  
→ Commit: 0022 (feat: adversary robustly locks on, explores, and follows hallways (0022))

## Prompt 0023: Refactor codebase to improve modularity and maintainability

**Original Prompt:**
Layer 23 is going to be a refactor. what are your suggestions  
yes, let's go with your plan  
test  
complete

**Instruction:**
- Move entity logic (`Player`, `Adversary`) to `entities.py` with self-contained state for trail and exploration.
- Move all rendering and color/symbol logic to `renderer.py`.
- Move all utility functions and magic constants to `utils.py`.
- Refactor `game.py` to handle only the main game loop, orchestration, and state, using the above modules.
- Add docstrings and high-level comments throughout.
- Ensure all imports, behaviors, and fog/trail/lock-on logic are preserved and tested.

**Result:**
- The codebase is fully modular: entities, rendering, and utilities are each separated into their own files.
- `game.py` is clean, orchestrates all modules, and remains the main entry point.
- All previous features (adversary logic, trails, slow effect, fog-of-war, etc.) are fully preserved.
- Code is ready for future expansion.

→ See: src/game.py, src/entities.py, src/renderer.py, src/utils.py  
→ Commit: 0023 (refactor: modularize entities, rendering, utils, and docstrings (0023))

## Prompt 0024 — move chat

**Instruction:**  
Move to a new chat thread due to growing session length.  
Update the bootstrapping files and logs to reflect the current state of the project:

- Regenerate `README.md` with updated layer model, lifecycle, and structure
- Regenerate `chat-boot.md` to match
- Update `PROMPT_INDEX.md` with real commit links and prompt anchors

**Artifacts:**
- `README.md`  
- `chat-boot.md`  
- `docs/PROMPT_INDEX.md`

**Commit:**  
[`9c2d1f6`](https://github.com/toddm-ClaybookAdvisors/layercake-method/commit/9c2d1f6) — `chore: move chat and refresh README, chat boot, and prompt index (0024)`


## Prompt 0025: Refactor config and version logic to use LAYER throughout the project

Refactor the project to remove all “version” references, replacing them with “layer” across all runtime config, utilities, and rendering.

- Add a `"LAYER"` key to `app/config.json` and update it with each layer commit.
- Remove `get_version()` and related logic from `utils.py`, replacing with `get_layer()` and a `load_config()` function.
- Update all affected modules (including `game.py` and `renderer.py`) to use the new `layer` config and logic, so that the current layer is shown in the game overlay.
- Ensure all file loads use paths relative to the project root.

## Prompt 0026: Add config-driven debug mode that disables fog of war

**Original Prompt:**

feature: add a debug mode. it will be a new line in the config.json. When it is set to true, for now just the fog of war is removed. here are all the source files that may be need to be modified by this change

**Instruction:**

Add a debug mode. Add a `"debug"` boolean to config.json. When `"debug"` is true, fog of war is disabled and the full map is revealed to the player. Pass config to Game and Renderer; use config to control fog logic in rendering. Do not refactor beyond what is needed for this feature. Any constructor or wiring changes required for config-driven fog must be approved as a minimal refactor.

**Result:**

→ See: src/game.py, src/renderer.py, config.json  
→ Commit: 0026 (Add config-driven debug mode that disables fog of war)

## Prompt 0027: Major chat-boot.md policy refactor and workflow enhancement

**Original Prompt:**

restructure my chat-boot.md file remove any mention of files that are mention as ignored now

**Instruction:**

Refactor the `chat-boot.md` to remove any mention of excluded or obsolete files, consolidate and clarify all explicit rules, and add/enhance policies to ensure:  
- No refactoring outside of refactor layers  
- Strict workflow step enforcement and state visibility  
- State transition and workflow completeness reminders  
- File header standards with model, layer, and purpose  
- Session definition, audit/compliance, and layer number management  
- A manual edit detection and review flow before commit  
- An improved `merge` step that requires both README.md updates (if merging to main) and a current `git log --oneline` for LAYER_INDEX.md commit hashes.

**Result:**

→ See: `chat-boot.md`  
→ Commit: 0027 (Major policy, workflow, and compliance refactor; replaces all prior boot policies)

## Prompt 0028: Refactor dungeon map generation for clarity, modularity, and config-driven flexibility

**Original Prompt:**

start refractor layer 28

**Instruction:**

Refactor the dungeon map generation module (`mapgen.py`) for clarity, modularity, and stateless operation. Output the dungeon as a row-major map to ensure correct downstream logic. Integrate a `map_config` section into the global `config.json` for all procedural generation options, supporting custom tilesets and random seed. Update all entity placement logic (player, exit, adversary) to use a robust `place_entity` helper requiring explicit floor tile configuration. Update `game.py` to use the new config-driven interface. Add a utility to `utils.py` to strip `_comment` keys from JSON configs. Guarantee robust and correct spawning regardless of mapgen settings. Document the rationale and conventions directly in code.

**Result:**

→ See: `app/src/mapgen.py`, `app/src/game.py`, `config.json`, `utils.py`  
→ Commit: 0028 (Refactor dungeon map generation for clarity, modularity, and config-driven flexibility)

## Prompt 0029: Refactor entity system for modularity, readability, and hallway robustness

**Original Prompt:**

we will be refactoring the entity modularization and readability

**Instruction:**

Restructure the `entities.py` module to maximize modularity and readability. Refactor the adversary AI to use intent-driven helper methods (lock-on, hallway movement, exploration, random fallback), replace grid math with the `adjacent_tiles` helper, and ensure all navigation and state updates are cleanly separated. Fix the edge case where adversaries spawned in hallways could become stuck due to an unset movement direction. Do not alter any gameplay features or interfaces.

**Result:**

→ See: `app/src/entities.py`  
→ Commit: 0029 (Refactor entity system for clarity and maintainability; modular adversary AI; hallway bug fix)

















