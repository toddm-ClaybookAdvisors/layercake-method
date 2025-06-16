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





