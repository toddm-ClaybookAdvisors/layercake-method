"""
mapgen.py

Procedural map generation for the LLM-driven 2D adventure game.

Generates rooms, corridors, and a maze near the exit with guaranteed connectivity.
"""

import random
from collections import deque

def generate_map(width, height, room_min=4, room_max=12, max_rooms=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [['#' for _ in range(width)] for _ in range(height)]
    rooms = []
    for _ in range(max_rooms):
        # Vary room size more for variety
        w = random.randint(room_min, room_max)
        h = random.randint(room_min, room_max)
        x = random.randint(1, width - w - 2)
        y = random.randint(1, height - h - 2)
        new_room = (x, y, w, h)

        if any(_rooms_overlap(new_room, other) for other in rooms):
            continue
        _carve_room(grid, new_room)
        if rooms:
            prev_center = _room_center(rooms[-1])
            curr_center = _room_center(new_room)
            _carve_corridor(grid, prev_center, curr_center)
        rooms.append(new_room)

    player_start = _room_center(rooms[0]) if rooms else (1, 1)
    exit_room = _find_exit_room(rooms, player_start)
    exit_pos = _room_center(exit_room)

    # Maze area near exit room
    maze_area = _define_maze_area(exit_room, width, height)
    _carve_maze(grid, maze_area)

    # Connect maze to rooms with multiple corridors (more connections for accessibility)
    _connect_maze_to_rooms(grid, maze_area, rooms, connections=4)

    # Place exit door inside maze center
    maze_center = ((maze_area[0] + maze_area[2]) // 2, (maze_area[1] + maze_area[3]) // 2)
    exit_pos = maze_center
    _mark_cell(grid, exit_pos, '>')

    # Add extra loops and cross connections between rooms
    _add_extra_loops(grid, rooms)

    # Ensure connectivity from player to exit, fix if necessary
    if not _is_reachable(grid, player_start, exit_pos):
        _fix_connectivity(grid, player_start, exit_pos)

    return grid, player_start, exit_pos

def _define_maze_area(exit_room, map_width, map_height):
    x, y, w, h = exit_room
    maze_w, maze_h = max(10, w), max(10, h)

    if y + h + maze_h + 2 < map_height:
        x1 = x
        y1 = y + h + 2
        x2 = min(x1 + maze_w - 1, map_width - 3)
        y2 = min(y1 + maze_h - 1, map_height - 3)
    elif x + w + maze_w + 2 < map_width:
        x1 = x + w + 2
        y1 = y
        x2 = min(x1 + maze_w - 1, map_width - 3)
        y2 = min(y1 + maze_h - 1, map_height - 3)
    else:
        x1 = max(1, x - maze_w - 2)
        y1 = max(1, y - maze_h - 2)
        x2 = min(x1 + maze_w - 1, map_width - 3)
        y2 = min(y1 + maze_h - 1, map_height - 3)
    return (x1, y1, x2, y2)

def _carve_maze(grid, area):
    x1, y1, x2, y2 = area
    width = x2 - x1 + 1
    height = y2 - y1 + 1

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            grid[y][x] = '#'

    maze_w = width if width % 2 == 1 else width - 1
    maze_h = height if height % 2 == 1 else height - 1

    start_x = x1 + 1
    start_y = y1 + 1

    visited = [[False for _ in range(maze_w // 2)] for _ in range(maze_h // 2)]

    def carve(cx, cy):
        visited[cy][cx] = True
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < maze_w // 2 and 0 <= ny < maze_h // 2 and not visited[ny][nx]:
                wx = start_x + cx * 2 + dx
                wy = start_y + cy * 2 + dy
                grid[wy][wx] = '.'
                grid[start_y + ny * 2][start_x + nx * 2] = '.'
                carve(nx, ny)

    grid[start_y][start_x] = '.'
    carve(0, 0)

def _connect_maze_to_rooms(grid, maze_area, rooms, connections=4):
    x1, y1, x2, y2 = maze_area
    maze_edges = []

    for x in range(x1, x2 + 1):
        maze_edges.append((x, y1))
        maze_edges.append((x, y2))
    for y in range(y1 + 1, y2):
        maze_edges.append((x1, y))
        maze_edges.append((x2, y))

    # Shuffle edges to connect randomly
    random.shuffle(maze_edges)

    connected_rooms = set()
    conn_made = 0
    for edge_pos in maze_edges:
        # Find nearest room center
        nearest_room = min(rooms, key=lambda r: _dist(edge_pos, _room_center(r)))
        room_center = _room_center(nearest_room)
        # Connect if not already connected enough
        if (nearest_room not in connected_rooms or conn_made < connections):
            _carve_corridor(grid, edge_pos, room_center)
            connected_rooms.add(nearest_room)
            conn_made += 1
        if conn_made >= connections:
            break

def _add_extra_loops(grid, rooms):
    # Randomly add cross corridors between random pairs of rooms for loops
    room_pairs = []
    n = len(rooms)
    for i in range(n):
        for j in range(i + 1, n):
            room_pairs.append((rooms[i], rooms[j]))
    random.shuffle(room_pairs)

    for (r1, r2) in room_pairs[:max(3, n//3)]:
        c1 = _room_center(r1)
        c2 = _room_center(r2)
        _carve_corridor(grid, c1, c2)



def _is_reachable(grid, start, goal, max_steps=100000):
    queue = deque([start])
    visited = set()
    steps = 0
    while queue:
        if steps > max_steps:
            # Fail fast if BFS takes too long
            return False
        x, y = queue.popleft()
        if (x, y) == goal:
            return True
        visited.add((x, y))
        steps += 1
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] in ('.', '>') and (nx, ny) not in visited:
                    queue.append((nx, ny))
    return False

def _fix_connectivity(grid, start, goal):
    # Try carving corridors from start and goal towards center to improve connectivity
    cx = (start[0] + goal[0]) // 2
    cy = (start[1] + goal[1]) // 2
    _carve_corridor(grid, start, (cx, cy))
    _carve_corridor(grid, (cx, cy), goal)


def _carve_room(grid, room):
    x, y, w, h = room
    for i in range(y, y + h):
        for j in range(x, x + w):
            grid[i][j] = '.'

def _carve_corridor(grid, start, end):
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:
        _carve_horiz(grid, x1, x2, y1)
        _carve_vert(grid, y1, y2, x2)
    else:
        _carve_vert(grid, y1, y2, x1)
        _carve_horiz(grid, x1, x2, y2)

def _carve_horiz(grid, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        grid[y][x] = '.'

def _carve_vert(grid, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        grid[y][x] = '.'

def _rooms_overlap(r1, r2, padding=1):
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    return (
        x1 - padding < x2 + w2 and
        x1 + w1 + padding > x2 and
        y1 - padding < y2 + h2 and
        y1 + h1 + padding > y2
    )

def _room_center(room):
    x, y, w, h = room
    cx = x + w // 2
    cy = y + h // 2
    return (cx, cy)

def _find_exit_room(rooms, start):
    sx, sy = start
    farthest = max(rooms, key=lambda r: _dist((sx, sy), _room_center(r)))
    return farthest

def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def _mark_cell(grid, pos, symbol):
    x, y = pos
    grid[y][x] = symbol

def print_map(grid):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    grid, start, exit_pos = generate_map(60, 30, seed=42)
    print_map(grid)
