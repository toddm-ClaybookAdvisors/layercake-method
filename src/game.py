"""
game.py

Main game loop and interface for the LLM-driven 2D adventure game.

Responsibilities:
    - Handles player input and movement
    - Maintains game state (player, map, messages)
    - Renders the visible portion of the map (scrollable viewport)
    - Processes win condition (player reaches exit)
    - Delegates map generation to mapgen.py

All major operations are modularized for clarity and easy extension.
"""

import sys
import os
from mapgen import generate_map

# --- Configurable Settings ---
MAP_WIDTH = 40
MAP_HEIGHT = 20
VIEWPORT_WIDTH = 20
VIEWPORT_HEIGHT = 10

# --- Game State Classes ---

class Player:
    """
    Tracks player position and supports movement validation.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, game_map):
        """
        Attempt to move the player by (dx, dy).
        Only allows movement into open tiles ('.', '>').
        """
        nx, ny = self.x + dx, self.y + dy
        if _is_open_tile(game_map, nx, ny):
            self.x, self.y = nx, ny
            return True
        return False

class Game:
    """
    Encapsulates the entire game state and main loop.
    """
    def __init__(self, map_width, map_height, viewport_width, viewport_height):
        self.map, (px, py), self.exit_pos = generate_map(map_width, map_height)
        self.player = Player(px, py)
        self.messages = []
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.running = True

    def run(self):
        """
        Main game loop: renders, processes input, and checks win condition.
        """
        while self.running:
            self._render()
            command = input("Move (WASD or Q to quit): ").strip().lower()
            self._handle_input(command)
            if (self.player.x, self.player.y) == self.exit_pos:
                self._add_message("You found the exit! Congratulations!")
                self._render()
                break

    def _render(self):
        """
        Renders the visible portion of the map, player, and messages.
        """
        os.system("cls" if os.name == "nt" else "clear")
        viewport = _get_viewport(
            self.map, self.player.x, self.player.y,
            self.viewport_width, self.viewport_height
        )
        for row in viewport:
            print("".join(row))
        print(f"Position: ({self.player.x},{self.player.y})  |  Exit: {self.exit_pos}")
        if self.messages:
            print("\n".join(self.messages[-3:]))  # Show last 3 messages

    def _handle_input(self, command):
        """
        Handles player input, dispatching to the appropriate action.
        """
        dx, dy = 0, 0
        if command == "w":
            dy = -1
        elif command == "s":
            dy = 1
        elif command == "a":
            dx = -1
        elif command == "d":
            dx = 1
        elif command == "q":
            self.running = False
            print("Goodbye!")
            return
        else:
            self._add_message("Invalid input! Use W/A/S/D to move, Q to quit.")
            return
        moved = self.player.move(dx, dy, self.map)
        if not moved:
            self._add_message("You can't walk there.")

    def _add_message(self, msg):
        """
        Adds a status message for display.
        """
        self.messages.append(msg)

# --- Core Helpers ---

def _is_open_tile(game_map, x, y):
    """
    Returns True if (x, y) is within map bounds and walkable ('.' or '>').
    """
    if 0 <= y < len(game_map) and 0 <= x < len(game_map[0]):
        return game_map[y][x] in ('.', '>')
    return False

def _get_viewport(game_map, px, py, vw, vh):
    """
    Returns a 2D list representing the visible viewport centered on (px, py),
    clamped to the map edges.
    The player '@' is rendered on top of the base map.
    """
    rows, cols = len(game_map), len(game_map[0])
    # Center viewport on player
    left = max(0, min(px - vw // 2, cols - vw))
    top = max(0, min(py - vh // 2, rows - vh))
    right = left + vw
    bottom = top + vh

    # Deep copy map region
    view = [list(row[left:right]) for row in game_map[top:bottom]]
    # Place player marker (clamped to viewport)
    vx, vy = px - left, py - top
    if 0 <= vy < len(view) and 0 <= vx < len(view[0]):
        view[vy][vx] = '@'
    return view

# --- Entry Point ---

def main():
    """
    Initializes and starts the game.
    """
    game = Game(MAP_WIDTH, MAP_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
