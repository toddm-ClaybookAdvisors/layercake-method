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



