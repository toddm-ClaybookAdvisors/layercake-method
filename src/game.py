import os
import sys
import time
import re
import json
import random
from collections import deque
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

class Adversary:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mode = "explore"
        self.last_dir = (0, 0)
        self.explored = set()
        self.explored.add((x, y))
        self.locked_on = False
        self.in_hallway = False

    def move(self, game, player_trail, player_pos):
        # 1. Robust Lock-On: BFS from adversary to player along green trail tiles
        vision_trails = []
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                tx, ty = self.x + dx, self.y + dy
                if (tx, ty) in player_trail and game._is_floor(tx, ty):
                    vision_trails.append((tx, ty))
        lockon_path = None
        if vision_trails:
            lockon_path = self._find_trail_path_to_player(game, player_trail, player_pos)
        if lockon_path and len(lockon_path) > 1:
            if not self.locked_on:
                game._add_message("You feel a chill... something is following your trail!")
            self.locked_on = True
            self.x, self.y = lockon_path[1]
            self.last_dir = (lockon_path[1][0] - lockon_path[0][0], lockon_path[1][1] - lockon_path[0][1])
            self.mode = "trail_follow"
            self.explored.add((self.x, self.y))
            return
        else:
            self.locked_on = False

        # 2. Hallway following: detect 1-tile-wide gaps/hallways and follow them
        if self._in_hallway(game):
            self.in_hallway = True
            dx, dy = self.last_dir
            nx, ny = self.x + dx, self.y + dy
            if game._is_floor(nx, ny):
                self.x, self.y = nx, ny
                self.explored.add((self.x, self.y))
                return
            else:
                # At the end of hallway, pick new direction
                self.in_hallway = False

        # 3. Exploration: seek adjacent unexplored floor tiles
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = self.x + dx, self.y + dy
            if game._is_floor(nx, ny) and (nx, ny) not in self.explored:
                self.x, self.y = nx, ny
                self.last_dir = (dx, dy)
                self.mode = "explore"
                self.explored.add((self.x, self.y))
                return

        # 4. If all neighbors explored, pick random direction (can backtrack)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = self.x + dx, self.y + dy
            if game._is_floor(nx, ny):
                self.x, self.y = nx, ny
                self.last_dir = (dx, dy)
                self.mode = "explore"
                self.explored.add((self.x, self.y))
                return

    def _find_trail_path_to_player(self, game, player_trail, player_pos):
        # BFS from adversary to player, only traversing green trail tiles
        queue = deque()
        visited = set()
        prev = {}
        start = (self.x, self.y)
        queue.append(start)
        visited.add(start)
        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) == player_pos:
                path = [(cx, cy)]
                while (cx, cy) != start:
                    cx, cy = prev[(cx, cy)]
                    path.append((cx, cy))
                path.reverse()
                return path
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = cx + dx, cy + dy
                if (
                    (nx, ny) not in visited and
                    (nx, ny) in player_trail and
                    game._is_floor(nx, ny)
                ):
                    visited.add((nx, ny))
                    prev[(nx, ny)] = (cx, cy)
                    queue.append((nx, ny))
        return None

    def _in_hallway(self, game):
        # A hallway/gap is a 1-tile-wide passage: surrounded by walls except front/back
        wall_count = 0
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = self.x + dx, self.y + dy
            if not game._is_floor(nx, ny):
                wall_count += 1
        return wall_count >= 2  # 1-tile passage

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

        # Player trail
        self.trail = set()
        self.trail.add((px, py))

        # Adversary: spawn far from player
        ax, ay = self._find_far_spawn(px, py)
        self.adversary = Adversary(ax, ay)
        self.adversary_trail = set()
        self.adversary_trail.add((ax, ay))

        # For player slow effect
        self.player_slow_counter = 0

        # Viewport size determined at runtime
        self.viewport_width, self.viewport_height = self._get_dynamic_viewport_size()

    def _find_far_spawn(self, px, py):
        # Place adversary as far from player as possible on a floor tile
        best = (0, 0)
        max_dist = -1
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '.':
                    d = abs(x - px) + abs(y - py)
                    if d > max_dist:
                        best = (x, y)
                        max_dist = d
        return best

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
            # --- PLAYER SLOW ON RED TRAIL ---
            player_on_red_trail = (self.player.x, self.player.y) in self.adversary_trail
            if player_on_red_trail:
                if self.player_slow_counter == 0 and moved:
                    self.player_slow_counter = 1
                    self._add_message("You are slowed by the adversary's trail!")
                elif self.player_slow_counter > 0:
                    self.player_slow_counter -= 1
                    moved = False  # Skip move this turn
                    self._add_message("You are slowed by the adversary's trail!")
            else:
                self.player_slow_counter = 0  # Reset when off red trail
            if moved:
                self.trail.add((self.player.x, self.player.y))
            self._reveal_visible_area()  # Reveal after move

            # --- Adversary moves on every tick ---
            self.adversary.move(self, self.trail, (self.player.x, self.player.y))
            self.adversary_trail.add((self.adversary.x, self.adversary.y))

            # Loss condition
            if (self.adversary.x, self.adversary.y) == (self.player.x, self.player.y):
                self._add_message("You lose! The adversary caught you!")
                self._render(final=True)
                break

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

    def _is_floor(self, x, y):
        return (
            0 <= y < len(self.map) and
            0 <= x < len(self.map[0]) and
            self.map[y][x] == '.'
        )

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
                visible = self.seen[y][x]
                if (x, y) == (self.player.x, self.player.y):
                    line.append(f"{COLOR_GREEN}†{COLOR_RESET}")
                elif visible and (x, y) == (self.adversary.x, self.adversary.y):
                    line.append(f"{COLOR_BOLD_RED}X{COLOR_RESET}")
                elif visible and (x, y) in self.trail and self.map[y][x] == '.':
                    line.append(f"{COLOR_GREEN}·{COLOR_RESET}")
                elif visible and (x, y) in self.adversary_trail and self.map[y][x] == '.':
                    line.append(f"{COLOR_BOLD_RED}·{COLOR_RESET}")
                elif visible and (x, y) == self.exit_pos:
                    line.append(f"{COLOR_BOLD_RED}0{COLOR_RESET}")
                elif visible:
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
            print(confirm)
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
