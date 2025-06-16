# mapgen.py
# Prompt 0012 — Irregular Room Generation and Maze Connectivity

import random

MAP_WIDTH = 100
MAP_HEIGHT = 40
FLOOR = '.'
WALL = '#'
EXIT = '>'

WALKABLE_TILES = {FLOOR, EXIT}

def make_empty_map():
    return [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def carve_room(game_map, x, y, w, h):
    for i in range(y, y + h):
        for j in range(x, x + w):
            if 0 <= j < MAP_WIDTH and 0 <= i < MAP_HEIGHT:
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

def generate_map():
    game_map = make_empty_map()
    rooms = []

    # Create 8-12 irregularly placed rooms
    for _ in range(random.randint(8, 12)):
        w = random.randint(6, 15)
        h = random.randint(4, 10)
        x = random.randint(1, MAP_WIDTH - w - 2)
        y = random.randint(1, MAP_HEIGHT - h - 2)

        # Check for overlap
        overlaps = any(
            abs(x - rx) < rw and abs(y - ry) < rh
            for (rx, ry, rw, rh) in rooms
        )
        if overlaps:
            continue

        carve_room(game_map, x, y, w, h)
        rooms.append((x, y, w, h))

    # Connect all rooms with winding hallways
    centers = [(x + w // 2, y + h // 2) for (x, y, w, h) in rooms]
    for i in range(1, len(centers)):
        carve_hallway(game_map, *centers[i - 1], *centers[i])

    # Place player in first room
    player_start = centers[0]

    # Place exit at edge of farthest room
    ex, ey = centers[-1]
    ex = min(MAP_WIDTH - 2, ex + random.randint(0, 3))
    ey = min(MAP_HEIGHT - 2, ey + random.randint(0, 3))
    game_map[ey][ex] = EXIT

    return game_map, player_start
