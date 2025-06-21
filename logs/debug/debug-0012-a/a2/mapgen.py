# mapgen.py — debug-0012-a2
# Dynamic-size procedural map generator matching viewport

import random

FLOOR = '.'
WALL = '#'
EXIT = '>'
WALKABLE_TILES = {FLOOR, EXIT}

def make_empty_map(width, height):
    return [[WALL for _ in range(width)] for _ in range(height)]

def carve_room(game_map, x, y, w, h):
    height = len(game_map)
    width = len(game_map[0])
    for i in range(y, y + h):
        for j in range(x, x + w):
            if 0 <= j < width and 0 <= i < height:
                game_map[i][j] = FLOOR

def carve_hallway(game_map, x1, y1, x2, y2):
    cx, cy = x1, y1
    while cx != x2:
        game_map[cy][cx] = FLOOR
        cx += 1 if x2 > cx else -1
    while cy != y2:
        game_map[cy][cx] = FLOOR
        cy += 1 if y2 > cy else -1
    game_map[cy][cx] = FLOOR

def generate_map(map_width, map_height):
    game_map = make_empty_map(map_width, map_height)
    rooms = []

    for _ in range(random.randint(8, 12)):
        w = random.randint(6, 15)
        h = random.randint(4, 10)
        x = random.randint(1, map_width - w - 2)
        y = random.randint(1, map_height - h - 2)

        overlaps = any(
            abs(x - rx) < rw and abs(y - ry) < rh
            for (rx, ry, rw, rh) in rooms
        )
        if overlaps:
            continue

        carve_room(game_map, x, y, w, h)
        rooms.append((x, y, w, h))

    centers = [(x + w // 2, y + h // 2) for (x, y, w, h) in rooms]
    for i in range(1, len(centers)):
        carve_hallway(game_map, *centers[i - 1], *centers[i])

    player_start = centers[0]

    ex, ey = centers[-1]
    ex = min(map_width - 2, ex + random.randint(0, 3))
    ey = min(map_height - 2, ey + random.randint(0, 3))
    game_map[ey][ex] = EXIT

    return game_map, player_start

