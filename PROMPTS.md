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


## Prompt 0014: Transition to New Chat Thread (transfer-002)

**Original Prompt:**

ok, let's do the next commit. It is a transition commit since this chat is getting slow.

**Instruction:**

Document the transition to a new chat thread for performance reasons. Preserve the full development state and update `chat-transition/transfer-002.md` with a project snapshot, current status, and all standards. Include updated directory structure and `README.md` entry to reflect the new context boundary.

**Result:**

→ See: chat-transition/transfer-002.md  
→ Commit: 0014 (document chat thread transition in transfer-002)







