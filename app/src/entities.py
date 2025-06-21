"""
entities.py

Defines Player and Adversary classes, including movement, trail tracking, exploration, and AI logic.
"""

import random
from collections import deque

class Entity:
    """Base class for all moving entities."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trail = set()
        self.trail.add((x, y))
        self.explored = set()
        self.explored.add((x, y))

class Player(Entity):
    """Player character: handles movement."""
    def move(self, dx, dy, game_map, is_open_tile):
        nx, ny = self.x + dx, self.y + dy
        if is_open_tile(game_map, nx, ny):
            self.x, self.y = nx, ny
            self.trail.add((self.x, self.y))
            self.explored.add((self.x, self.y))
            return True
        return False

class Adversary(Entity):
    """
    Adversary: explores the map, leaves a red trail, and robustly locks onto the player via their trail.
    """
    def __init__(self, x, y, vision_radius=2):
        super().__init__(x, y)
        self.mode = "explore"
        self.last_dir = (0, 0)
        self.locked_on = False
        self.in_hallway = False
        self.vision_radius = vision_radius

    def move(self, game, player_trail, player_pos, is_floor, add_message):
        # 1. Robust Lock-On: BFS from adversary to player along green trail tiles
        vision_trails = []
        for dx in range(-self.vision_radius, self.vision_radius + 1):
            for dy in range(-self.vision_radius, self.vision_radius + 1):
                tx, ty = self.x + dx, self.y + dy
                if (tx, ty) in player_trail and is_floor(game.map, tx, ty):
                    vision_trails.append((tx, ty))
        lockon_path = None
        if vision_trails:
            lockon_path = self._find_trail_path_to_player(game, player_trail, player_pos, is_floor)
        if lockon_path and len(lockon_path) > 1:
            if not self.locked_on:
                add_message("You feel a chill... something is following your trail!")
            self.locked_on = True
            self.x, self.y = lockon_path[1]
            self.last_dir = (lockon_path[1][0] - lockon_path[0][0], lockon_path[1][1] - lockon_path[0][1])
            self.mode = "trail_follow"
            self.trail.add((self.x, self.y))
            self.explored.add((self.x, self.y))
            return
        else:
            self.locked_on = False

        # 2. Hallway following: detect 1-tile-wide gaps/hallways and follow them
        if self._in_hallway(game, is_floor):
            self.in_hallway = True
            dx, dy = self.last_dir
            nx, ny = self.x + dx, self.y + dy
            if is_floor(game.map, nx, ny):
                self.x, self.y = nx, ny
                self.trail.add((self.x, self.y))
                self.explored.add((self.x, self.y))
                return
            else:
                # At the end of hallway, pick new direction
                self.in_hallway = False

        # 3. Exploration: seek adjacent unexplored floor tiles
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = self.x + dx, self.y + dy
            if is_floor(game.map, nx, ny) and (nx, ny) not in self.explored:
                self.x, self.y = nx, ny
                self.last_dir = (dx, dy)
                self.mode = "explore"
                self.trail.add((self.x, self.y))
                self.explored.add((self.x, self.y))
                return

        # 4. If all neighbors explored, pick random direction (can backtrack)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = self.x + dx, self.y + dy
            if is_floor(game.map, nx, ny):
                self.x, self.y = nx, ny
                self.last_dir = (dx, dy)
                self.mode = "explore"
                self.trail.add((self.x, self.y))
                self.explored.add((self.x, self.y))
                return

    def _find_trail_path_to_player(self, game, player_trail, player_pos, is_floor):
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
                    is_floor(game.map, nx, ny)
                ):
                    visited.add((nx, ny))
                    prev[(nx, ny)] = (cx, cy)
                    queue.append((nx, ny))
        return None

    def _in_hallway(self, game, is_floor):
        # A hallway/gap is a 1-tile-wide passage: surrounded by walls except front/back
        wall_count = 0
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = self.x + dx, self.y + dy
            if not is_floor(game.map, nx, ny):
                wall_count += 1
        return wall_count >= 2  # 1-tile passage

