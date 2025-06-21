Here's the initial README that defines the scope, methodology, and file structure of this project. It reflects your choice to use Git commit messages and a running `PROMPTS.md` as the primary tracking method.

Here are clear, copy-paste-ready instructions for installing Python 3 on macOS and creating a virtual environment, intended for inclusion in a README. This assumes the user is starting from a clean macOS system and needs to install Homebrew and Python.

Here are copy-ready instructions for installing Python 3 using Homebrew and setting up a virtual environment. Everything is contained within a single fenced Markdown block to ensure correct rendering in GitHub's README viewer.

Here is a minimal Python implementation of a game loop that displays a 10x5 ASCII map, allows WASD movement, and updates the player’s position on each turn. It uses `input()` to get user commands, redraws the map by printing it each frame, and uses only built-in libraries.

Here's a `.gitignore` file tailored for Python development, including virtual environments, compiled files, cache directories, and VS Code-specific workspace metadata. This will keep unnecessary files out of version control.

## Prompt 0005: Add Screen Clearing and Real-Time Input to Game Loop

This update enhances the game loop by:
- Clearing the screen between frames using `os.system()`
- Capturing keypresses without requiring the Enter key
- Using platform-specific methods:
  - `msvcrt` on Windows
  - `termios` + `tty` on POSIX systems (macOS, Linux)

The code remains cross-platform and uses only built-in libraries.

## Prompt 0006: Expand Game Board and Add Explanatory Comments

The game board has been expanded from 10×5 to 30×15 to give the player more space to explore. All dimensions and boundary checks have been updated accordingly.

I also added strategic, high-value comments to the code — not just explaining *what* each function does, but *why* it exists, and how it contributes to the game loop.

These comments are intended to help someone new to game development understand the core structure of the loop, state management, and rendering model.

## Prompt 0007: Suggest Next Steps for Gameplay Evolution

**Instruction:**

One very powerful aspect of coding with an LLM is its ability to look ahead based on the current development direction and make strategic suggestions. Based on the current state of the game (a movable player on a large ASCII map), suggest five logical next steps to continue developing the game. Rank them in order of impact or importance to gameplay and user experience. Do not write any code.

**Result:**

→ See: PROMPTS.md  
→ Commit: 0007 (Suggest next steps for gameplay evolution)

## Prompt 0008: Add Static Obstacles and Expand Map to 100×100

The game map has been expanded from 30×15 to 100×100, giving the player significantly more navigable space and making future features (like items, enemies, and zones) much more meaningful.

This version also introduces **static obstacles** (`#`), which are impassable tiles placed randomly throughout the map. These obstacles add structure and navigation challenges, laying the groundwork for gameplay mechanics like pathfinding, chokepoints, and exploration.

The drawing function now renders a full 100×100 map (which may scroll fast in your terminal), and the logic for updating player position prevents movement into obstacles.

High-quality comments explain each architectural component: map generation, obstacle layout, rendering, and movement handling.

## Prompt 0009: Replace Random Obstacles with Room-and-Hallway Structure

The map generation logic has been replaced with a simple procedural system that creates rectangular rooms connected by horizontal and vertical hallways. This eliminates the visual noise caused by randomly scattered obstacles and introduces a more meaningful game space that mimics dungeon-like layouts.

Rooms are placed at fixed intervals, and hallways are carved between their centers. This structure will serve as the foundation for more advanced features like item placement, enemies, or triggers that rely on distinct areas.

Player spawning is updated to place the player at the center of the first room.

## Prompt 0010: Finalize Scrollable Viewport for Structured Map

The fix from debugging session `debug-0009-a2.py` has been incorporated into `game.py`. This version features a dynamic, scrollable viewport that follows the player while keeping within map bounds.

The player starts in a carved room, and only the portion of the map near the player is rendered to the terminal. The full 100×100 map remains intact but is no longer drawn in full each frame, solving the original visual clutter issue.

High-value comments have been restored throughout to clarify the responsibilities of each component.

## Prompt 0011: Archive Transition State

This prompt formally archives the state of the project prior to a conversational thread reset. No code or design changes were introduced in this commit. Instead, it generated metadata necessary to continue development seamlessly in a new thread.

The assistant was instructed to:
- Create a refreshed `PROMPT_INDEX.md` linking all prior prompt commits to their Git commit hashes and corresponding entries in `CHAT_LOG.md`
- Generate a new file `chat-transition/transfer-001.md` documenting the transfer event
- Adhere to project policy: no emoji, maintain prompt/response/commit traceability, and capture GitHub URLs for each prompt’s commit

The transition commit acts as a placeholder and continuity anchor before development resumes with Prompt 0012.

All prior state, including `PROMPTS.md`, `CHAT_LOG.md`, `src/game.py`, and `debug/`, was preserved and version-controlled.

## Prompt 0012: Irregular Room Generation with Reachable Exit

Todd asked for a more complex map layout with the following characteristics:
- Irregularly shaped and unevenly distributed rooms
- Maze-like hallways that connect them without blocking access
- A much larger portion of the map carved out (60–80%)
- An exit `>` placed at the far edge of the map

The assistant suggested moving all generation logic into a new file (`mapgen.py`) and confirmed modular separation.

Once approved, the assistant:
- Created `mapgen.py` with a randomized room placement strategy and flood-safe carving
- Connected rooms with twisty hallways
- Guaranteed exit placement in a reachable location
- Updated `game.py` to import and use the new module, preserving the scrolling renderer and movement system

All functionality is retained and logically separated. This commit finalizes Prompt 0012.

## Prompt 0013: Finalize Irregular Room Generation and Modular Map Architecture

This prompt integrates the successful outcome of debug session `debug-0012-a`. The game world now features:

- Irregular room sizes and placement
- Maze-like hallways connecting all rooms
- A clearly marked exit positioned near the map boundary
- Guaranteed connectivity between rooms and exit
- A fully modular `mapgen.py` file for reusable generation logic
- Dynamic use of terminal dimensions for map sizing and viewport control

This version was tested in candidate folder `debug/debug-0012-a/a2` and confirmed to resolve all previously identified bugs. The structure now supports future features like minimaps, fog of war, or room metadata tagging.

## Prompt 0014: Transition to New Chat Thread (transition-002)

This prompt marks the reset of the conversation thread due to slowdown. The assistant preserved all architectural, procedural, and stylistic conventions established to date and documented them in `chat-transition/transition-002.md`.

Changes included:
- Finalized debug session documentation for Prompt 0012
- Promotion of working fix in Prompt 0013
- New formatting and commit policies for debug sessions
- Updated `PROMPT_INDEX.md` with entries through Prompt 0013
- Regenerated `README.md` with latest directory structure
- Locked in naming standards and ASCII-only requirement for all future markdown files

## Prompt 0015: Refactor mapgen.py and game.py for clarity, structure, and performance

**Instruction:**
Refactor both `mapgen.py` and `game.py` for clarity, structure, and performance using GPT-4.1. Improve modularity, docstrings, high-value comments, and overall maintainability while preserving gameplay and UX.

**Result:**
Both files were refactored for modularity, clarity, and maintainability.  
Major functional changes:
- Input now requires pressing RETURN for each move
- Viewport size is now fixed, not dynamic

[sidebar]  
All follow-up dialog for this prompt occurred in sidebar and is not included in the official log.


## Prompt 0016: Config-driven map and viewport, dynamic version, persistent large map

**Instruction:**
Implement a persistent large map (100x100 by default), with a smaller, centered viewport window (default 40x20), all configurable via a new `config.json` in the project root. Update `game.py` to load map and viewport size from this config file at runtime. Ensure the version string remains dynamic, parsed from PROMPTS.md (+1), and visible in the upper left along with real-time FPS.

**Result:**
Added support for loading map/viewport size from `config.json`, dynamic version parsing, and ensured the viewport always shows a window into a large persistent map.

[sidebar]  
All further dialog for this prompt occurred in sidebar and is not included in the official log.

## Prompt 0017

**Instruction:**
Implement persistent fog-of-war and player trail in a large (300x300) map with a dynamic viewport that always fits within the terminal. The viewport is defined as the portion of the map, scrolling with the player, that is rendered at any given time, regardless of fog. Always reserve one line for the top status bar, three lines for controls/messages at the bottom, and one line for user input; never print more lines than fit in the terminal. All output remains on screen without scrolling.

**Result:**
Status bar, viewport, controls, and messages are always visible. Viewport follows player, fog-of-war and trail are persistent, and no scrolling occurs.

[sidebar]  
All further dialog for this prompt occurred in sidebar and is not included in the official log.

## Prompt 0018: Transition to New Chat Thread (transition-003)

**Instruction:**
Archive project state and all new conventions (devlog, prompt evolution, original prompt logging, viewport definition, etc.) in `chat-transition/transition-003.md`. Begin a new thread to maintain performance and clean context.

**Result:**
Transitioned to a new chat thread for performance; conventions and project state archived in transition log.

[sidebar]  
All further dialog occurred in sidebar and is not included in the official log.

### Prompt 0019

User requested a proper labyrinth near the door with multiple paths, more dungeon rooms, and guaranteed connectivity.

Assistant implemented a maze carving with recursive backtracker, multiple corridor connections, and loops between rooms.

Added BFS connectivity check with step limit to prevent hangs.

User reported a bug where quitting then restarting caused a hang in BFS.

Assistant patched BFS with max steps and improved connectivity fix carving corridors through midpoint.

User confirmed the fix works and approved commit.

Iteration closed successfully.

## Prompt 0020

**Instruction:**
Make the player green and have it leave a green trail behind it, indicating where it has been—only tiles it has passed over will be turned green. Place any color codes in a constant at the top of the file with the other color constants.

**Result:**
- The player `@` is drawn in green.
- Every tile stepped on by the player is marked with a green `·` trail.
- Only traversed tiles are marked; fog and UI are unchanged.
- All color codes are defined as top-level constants in `game.py`.

## Prompt 0021

**Instruction:**
Render the player as a green stick figure (`†`) and display the player’s (x, y) coordinates in the top info bar.

**Result:**
- The player is rendered as a green `†`.
- The top info bar now includes `Pos: (x, y)`.
- All other game functionality is unchanged.













