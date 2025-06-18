"""
mapgen.py

Procedural map generation for the LLM-driven 2D adventure game.

This module defines all logic for constructing grid-based dungeon maps, supporting:
    - Room/maze layouts
    - Randomized path carving
    - Exit placement

All functions are pure and self-contained, ensuring that map generation can be easily tested and reused.
"""

import random

def generate_map(width, height, room_min=4, room_max=8, max_rooms=10, seed=None):
    """
    Generates a dungeon map as a 2D grid (list of lists) with rooms and corridors.
    
    Parameters:
        width (int): Width of the map (columns).
        height (int): Height of the map (rows).
        room_min (int): Minimum size of rooms (both width and height).
        room_max (int): Maximum size of rooms (both width and height).
        max_rooms (int): Maximum number of rooms.
        seed (int, optional): Random seed for reproducibility.
    
    Returns:
        grid (list[list[str]]): 2D list representing the map.
        player_start (tuple): Coordinates (x, y) of player start.
        exit_pos (tuple): Coordinates (x, y) of the map's exit.
    """
    if seed is not None:
        random.seed(seed)

    grid = [['#' for _ in range(width)] for _ in range(height)]

    rooms = []
    for _ in range(max_rooms):
        w = random.randint(room_min, room_max)
        h = random.randint(room_min, room_max)
        x = random.randint(1, width - w - 1)
        y = random.randint(1, height - h - 1)
        new_room = (x, y, w, h)

        # Room overlap rejection: only add if it does not overlap with existing
        if any(_rooms_overlap(new_room, other) for other in rooms):
            continue
        _carve_room(grid, new_room)
        if rooms:
            # Connect this room to the previous room with a corridor
            prev_center = _room_center(rooms[-1])
            curr_center = _room_center(new_room)
            _carve_corridor(grid, prev_center, curr_center)
        rooms.append(new_room)

    # Player starts in the center of the first room
    player_start = _room_center(rooms[0]) if rooms else (1, 1)
    # Exit is placed in the center of the last room, or farthest from start
    exit_pos = _find_exit(rooms, player_start)

    # Mark player and exit
    _mark_cell(grid, player_start, '@')
    _mark_cell(grid, exit_pos, '>')
    return grid, player_start, exit_pos

# --- Helpers ---

def _carve_room(grid, room):
    """Open up all grid cells for a room rectangle."""
    x, y, w, h = room
    for i in range(y, y + h):
        for j in range(x, x + w):
            grid[i][j] = '.'

def _carve_corridor(grid, start, end):
    """Carve an L-shaped corridor between two points (center to center)."""
    x1, y1 = start
    x2, y2 = end
    # Randomly choose whether to go horizontal or vertical first
    if random.random() < 0.5:
        _carve_horiz(grid, x1, x2, y1)
        _carve_vert(grid, y1, y2, x2)
    else:
        _carve_vert(grid, y1, y2, x1)
        _carve_horiz(grid, x1, x2, y2)

def _carve_horiz(grid, x1, x2, y):
    """Carve a horizontal corridor at row y."""
    for x in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][x] = '.'

def _carve_vert(grid, y1, y2, x):
    """Carve a vertical corridor at column x."""
    for y in range(min(y1, y2), max(y1, y2) + 1):
        grid[y][x] = '.'

def _rooms_overlap(r1, r2, padding=1):
    """
    Returns True if two rooms overlap (optionally with padding between them).
    """
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    return (
        x1 - padding < x2 + w2 and
        x1 + w1 + padding > x2 and
        y1 - padding < y2 + h2 and
        y1 + h1 + padding > y2
    )

def _room_center(room):
    """Returns (x, y) center of a room rectangle."""
    x, y, w, h = room
    cx = x + w // 2
    cy = y + h // 2
    return (cx, cy)

def _find_exit(rooms, start):
    """
    Places the exit at the center of the room farthest from the player's start.
    If no rooms exist, places at (1, 1).
    """
    if not rooms:
        return (1, 1)
    sx, sy = start
    farthest = max(rooms, key=lambda r: _dist((sx, sy), _room_center(r)))
    return _room_center(farthest)

def _dist(a, b):
    """Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def _mark_cell(grid, pos, symbol):
    """Place a symbol at the given grid position."""
    x, y = pos
    grid[y][x] = symbol

# --- Optional: Simple ASCII pretty-printer for debugging ---

def print_map(grid):
    """Prints the map to terminal."""
    for row in grid:
        print("".join(row))

# Example usage (for debugging):
if __name__ == "__main__":
    grid, start, exit_pos = generate_map(40, 20, seed=42)
    print_map(grid)
