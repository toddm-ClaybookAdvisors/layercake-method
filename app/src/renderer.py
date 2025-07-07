"""
renderer.py

Handles all rendering and symbol/color logic for the game map and entities.
Now uses Python curses for sticky HUD and map rendering. Requires curses.
"""

import curses
import logging

COLOR_BOLD_RED = 1
COLOR_GREEN = 2

def render_player_stats_inline(player):
    """
    Return the player's stats as a horizontal string.
    """
    return f"Health: {player.health}   Speed: {player.speed}   Vision: {player.vision_radius}"

class Renderer:
    def __init__(self, config):
        self.config = config
        self.last_viewport_edge = None

    def draw(self, win, game, player, adversary, exit_pos):
        win.clear()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(COLOR_BOLD_RED, curses.COLOR_RED, -1)
        curses.init_pair(COLOR_GREEN, curses.COLOR_GREEN, -1)

        height, width = win.getmaxyx()
        debug = self.config.get("debug", False)
        px, py = player.x, player.y
        vw, vh = game.viewport_width, game.viewport_height
        rows, cols = len(game.map), len(game.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh

        # Overlay at top
        overlay = f"Layer: {game.layer}   Tick: {game.tick}   FPS: {int(game.fps)}   Pos: ({player.x}, {player.y})"
        stats = render_player_stats_inline(player)
        win.addstr(0, 0, overlay[:width - 1])
        win.addstr(1, 0, stats[:width - 1])

        # Map rendering starts from line 2
        map_top = 2
        for y in range(top, min(bottom, top + height - 5)):  # Reserve last lines for controls/messages
            for x in range(left, min(right, left + width)):
                visible = True if debug else game.seen[y][x]
                char, color = ' ', 0
                if (x, y) == (player.x, player.y):
                    char = '†'
                    color = COLOR_GREEN
                elif visible and (x, y) == (adversary.x, adversary.y):
                    char = 'X'
                    color = COLOR_BOLD_RED
                elif visible and (x, y) in player.trail and game.map[y][x] == '.':
                    char = '·'
                    color = COLOR_GREEN
                elif visible and (x, y) in adversary.trail and game.map[y][x] == '.':
                    char = '·'
                    color = COLOR_BOLD_RED
                elif visible and (x, y) == exit_pos:
                    char = '0'
                    color = COLOR_BOLD_RED
                elif visible:
                    char = game.map[y][x]
                else:
                    char = ' '
                if color:
                    win.addstr(map_top + y - top, x - left, char, curses.color_pair(color))
                else:
                    win.addstr(map_top + y - top, x - left, char)

        # Controls and messages at the bottom
        control_line = "Controls: W/A/S/D = move   Q = quit"
        win.addstr(height - 3, 0, control_line[:width - 1])

        recent_msgs = game.messages[-2:] if getattr(game, "messages", None) else []
        for i, msg in enumerate(recent_msgs):
            win.addstr(height - 2 + i, 0, msg[:width - 1])
        for i in range(2 - len(recent_msgs)):
            win.addstr(height - 2 + len(recent_msgs) + i, 0, " " * (width - 1))

        win.refresh()
