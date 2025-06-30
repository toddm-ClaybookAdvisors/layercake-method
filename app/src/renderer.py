"""
renderer.py

Handles all rendering and symbol/color logic for the game map and entities.
"""

import logging

COLOR_BOLD_RED = '\033[1;31m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

class Renderer:
    def __init__(self, config):
        self.config = config
        self.last_viewport_edge = None  # For edge logging throttling

    def render(self, game, player, adversary, exit_pos):
        import os

        debug = self.config.get("debug", False)

        px, py = player.x, player.y
        vw, vh = game.viewport_width, game.viewport_height
        rows, cols = len(game.map), len(game.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh

        # 1. Log only if the viewport *has just hit* the edge (not every frame!)
        edge = (left == 0 or right == cols or top == 0 or bottom == rows)
        if edge and self.last_viewport_edge != (left, right, top, bottom):
            logging.debug(
                f"Viewport reached edge: left={left}, right={right}, top={top}, bottom={bottom}, "
                f"map size=({cols},{rows})"
            )
            self.last_viewport_edge = (left, right, top, bottom)

        # 2. Log out-of-bounds ONCE per incident
        if not (0 <= player.x < cols and 0 <= player.y < rows):
            logging.warning(f"Player position out of bounds: ({player.x}, {player.y})")
        if not (0 <= adversary.x < cols and 0 <= adversary.y < rows):
            logging.warning(f"Adversary position out of bounds: ({adversary.x}, {adversary.y})")

        # 3. Log only every 100 ticks, for performance baseline (optional, can omit)
        if debug and game.tick % 100 == 0:
            logging.debug(
                f"Render snapshot: Layer={game.layer}, Tick={game.tick}, FPS={int(game.fps)}, "
                f"Player=({player.x},{player.y}), Adversary=({adversary.x},{adversary.y}), Exit={exit_pos}"
            )

        # --- No per-frame spam below here! ---

        os.system("cls" if os.name == "nt" else "clear")
        overlay = f"Layer: {game.layer}   Tick: {game.tick}   FPS: {int(game.fps)}   Pos: ({player.x}, {player.y})"
        print(overlay)

        for y in range(top, bottom):
            line = []
            for x in range(left, right):
                visible = True if debug else game.seen[y][x]
                if (x, y) == (player.x, player.y):
                    line.append(f"{COLOR_GREEN}†{COLOR_RESET}")
                elif visible and (x, y) == (adversary.x, adversary.y):
                    line.append(f"{COLOR_BOLD_RED}X{COLOR_RESET}")
                elif visible and (x, y) in player.trail and game.map[y][x] == '.':
                    line.append(f"{COLOR_GREEN}·{COLOR_RESET}")
                elif visible and (x, y) in adversary.trail and game.map[y][x] == '.':
                    line.append(f"{COLOR_BOLD_RED}·{COLOR_RESET}")
                elif visible and (x, y) == exit_pos:
                    line.append(f"{COLOR_BOLD_RED}0{COLOR_RESET}")
                elif visible:
                    line.append(game.map[y][x])
                else:
                    line.append(' ')
            print("".join(line))

        print("Controls: W/A/S/D = move   Q = quit")
        recent_msgs = game.messages[-2:] if game.messages or False else []
        for msg in recent_msgs:
            print(msg)
        for _ in range(2 - len(recent_msgs)):
            print()
