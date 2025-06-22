"""
renderer.py

Handles all rendering and symbol/color logic for the game map and entities.
"""

COLOR_BOLD_RED = '\033[1;31m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

class Renderer:
    def __init__(self, config):  # <<< CHANGED: accept config
        self.config = config     # <<< CHANGED: store config

    def render(self, game, player, adversary, exit_pos):
        import os

        debug = self.config.get("debug", False)  # <<< CHANGED: use config debug flag

        os.system("cls" if os.name == "nt" else "clear")
        overlay = f"Layer: {game.layer}   Tick: {game.tick}   FPS: {int(game.fps)}   Pos: ({player.x}, {player.y})"
        print(overlay)

        px, py = player.x, player.y
        vw, vh = game.viewport_width, game.viewport_height
        rows, cols = len(game.map), len(game.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh

        for y in range(top, bottom):
            line = []
            for x in range(left, right):
                visible = True if debug else game.seen[y][x]  # <<< CHANGED
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
