"""
game.py

LLM-driven 2D game demonstration — all logic, features, and refactors generated via prompt.
"""

import os
import sys
import time
import re
import json
from mapgen import generate_map

if os.name == "nt":
    import msvcrt
else:
    import termios
    import tty

# === Terminal Color Constants ===
COLOR_BOLD_RED = '\033[1;31m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

def load_config():
    default = {
        "map_width": 300,
        "map_height": 300,
        "viewport_width": 0,
        "viewport_height": 0
    }
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    try:
        with open(config_path) as f:
            user_config = json.load(f)
        for k in default:
            if k not in user_config:
                user_config[k] = default[k]
        return user_config
    except Exception:
        return default

CONFIG = load_config()
MAP_WIDTH = CONFIG["map_width"]
MAP_HEIGHT = CONFIG["map_height"]

def _get_version():
    path = os.path.join(os.path.dirname(__file__), "../PROMPTS.md")
    try:
        with open(path) as f:
            text = f.read()
        matches = re.findall(r'## Prompt (\d+):', text)
        if matches:
            latest = max(int(n) for n in matches)
            return f"version 0.{latest + 1}"
    except Exception:
        pass
    return "version unknown"

VERSION = _get_version()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, game_map):
        nx, ny = self.x + dx, self.y + dy
        if _is_open_tile(game_map, nx, ny):
            self.x, self.y = nx, ny
            return True
        return False

class Game:
    def __init__(self, map_width, map_height):
        self.map, (px, py), self.exit_pos = generate_map(map_width, map_height)
        self.player = Player(px, py)
        self.messages = []
        self.running = True
        self.last_frame_time = time.time()
        self.fps = 0.0
        self.tick = 0

        # FOG OF WAR: tracks which tiles have been seen
        self.seen = [[False for _ in range(map_width)] for _ in range(map_height)]
        self._reveal_visible_area()  # Reveal initial vision

        # === TRAIL: track all tiles the player has ever stepped on ===
        self.trail = set()
        self.trail.add((px, py))

        # Viewport size determined at runtime
        self.viewport_width, self.viewport_height = self._get_dynamic_viewport_size()

    def _get_dynamic_viewport_size(self):
        term_w, term_h = _get_terminal_size()
        reserved_top = 1         # Status bar
        reserved_bottom = 3      # Controls and two messages
        reserved_input = 1       # Leave the last line free for user input
        available_h = max(term_h - reserved_top - reserved_bottom - reserved_input, 1)
        vp_w = min(term_w, len(self.map[0]))
        vp_h = min(available_h, len(self.map))
        return vp_w, vp_h

    def run(self):
        while self.running:
            frame_start = time.time()
            self._render()
            command = _getch()
            moved = self._handle_input(command)
            if moved:
                self.trail.add((self.player.x, self.player.y))
            self._reveal_visible_area()  # Reveal after move
            if (self.player.x, self.player.y) == self.exit_pos:
                self._add_message("You found the exit! Congratulations!")
                self._render(final=True)
                break
            self.tick += 1
            frame_end = time.time()
            self._update_fps(frame_end - frame_start)

    def _update_fps(self, frame_duration):
        if frame_duration > 0:
            self.fps = 1.0 / frame_duration
        else:
            self.fps = 0.0

    def _reveal_visible_area(self):
        """Mark all tiles in a radius-2 around the player as seen."""
        px, py = self.player.x, self.player.y
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                x = px + dx
                y = py + dy
                if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]):
                    self.seen[y][x] = True

    def _render(self, final=False):
        os.system("cls" if os.name == "nt" else "clear")

        overlay = f"{VERSION}   Tick: {self.tick}   FPS: {int(self.fps)}   Pos: ({self.player.x}, {self.player.y})"
        print(overlay)

        # Compute viewport bounds
        px, py = self.player.x, self.player.y
        vw, vh = self.viewport_width, self.viewport_height
        rows, cols = len(self.map), len(self.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh

        for y in range(top, bottom):
            line = []
            for x in range(left, right):
                if (x, y) == (self.player.x, self.player.y):
                    line.append(f"{COLOR_GREEN}†{COLOR_RESET}")  # stick figure
                elif (x, y) in self.trail and self.seen[y][x] and self.map[y][x] == '.':
                    line.append(f"{COLOR_GREEN}·{COLOR_RESET}")
                elif (x, y) == self.exit_pos and self.seen[y][x]:
                    line.append(f"{COLOR_BOLD_RED}0{COLOR_RESET}")
                elif self.seen[y][x]:
                    line.append(self.map[y][x])
                else:
                    line.append(' ')
            print("".join(line))


        # Always print three lines at the bottom
        print("Controls: W/A/S/D = move   Q = quit")
        recent_msgs = self.messages[-2:] if self.messages or final else []
        for msg in recent_msgs:
            print(msg)
        for _ in range(2 - len(recent_msgs)):
            print()

    def _handle_input(self, command):
        dx, dy = 0, 0
        if command in ("w", "W"):
            dy = -1
        elif command in ("s", "S"):
            dy = 1
        elif command in ("a", "A"):
            dx = -1
        elif command in ("d", "D"):
            dx = 1
        elif command in ("q", "Q"):
            print("Are you sure you want to quit? (y/N)", end=' ', flush=True)
            confirm = _getch()
            print(confirm)  # Echo the character so the user sees what they pressed
            if confirm in ("y", "Y"):
                self.running = False
                print("Goodbye!")
                return False
            else:
                self._add_message("Quit canceled.")
                return False
        else:
            self._add_message("Invalid input! Use W/A/S/D to move, Q to quit.")
            return False
        moved = self.player.move(dx, dy, self.map)
        if moved:
            self.tick += 1
        else:
            self._add_message("You can't walk there.")
        return moved


    def _add_message(self, msg):
        self.messages.append(msg)

def _is_open_tile(game_map, x, y):
    if 0 <= y < len(game_map) and 0 <= x < len(game_map[0]):
        return game_map[y][x] in ('.', '>')
    return False

def _get_terminal_size():
    try:
        if os.name == 'nt':
            from shutil import get_terminal_size as gts
            size = gts()
            return size.columns, size.lines
        else:
            import fcntl, termios, struct
            h, w, _, _ = struct.unpack('HHHH',
                fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
            return w, h
    except Exception:
        return 80, 24

def _getch():
    if os.name == "nt":
        ch = msvcrt.getch()
        try:
            return ch.decode("utf-8")
        except Exception:
            return ""
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def main():
    game = Game(MAP_WIDTH, MAP_HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
