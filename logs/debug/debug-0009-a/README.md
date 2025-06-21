# Debugging Session 0009-A — Visual Clutter in Structured Room Map

This debugging session addresses an issue introduced in Prompt 0009, where structured rooms and hallways were correctly carved into the game map, but the screen at game start appeared filled with wall (`#`) characters. The player could move, but the visual experience was overwhelming.

## Objective

Introduce a scrollable viewport that limits the visible portion of the map to a manageable area around the player. This allows the full 100x100 game world to exist while only rendering a portion of it, reducing visual clutter and preparing for future gameplay expansion.

## Problem Summary

- The full map was initialized to 100x100 tiles, defaulting to walls (`#`)
- Only a portion of the map was carved into rooms (`.`), leaving most of it untouched
- The rendering logic displayed the entire map each frame, overwhelming the screen
- Player visibility and navigation were compromised by excessive wall characters

## Proposed Strategy

- Keep the full map intact (100x100 or larger)
- Introduce a fixed-size viewport that moves with the player
- Clamp the viewport to stay within map bounds
- Render only the visible portion of the map each frame

## Iterations

### `debug-0009-a1.py`

- Viewport size: 40x20 (hardcoded)
- Player stays centered except when near map edges
- Solved the visual clutter issue while preserving the full game map

### `debug-0009-a2.py`

- Viewport and map size both match the terminal dimensions
- Terminal size is detected using `shutil.get_terminal_size()`
- Player spawns near the center of the map
- Viewport remains centered around the player
- Fully adapts to terminal constraints while supporting room layout and scrolling

## Outcome

The strategy was validated by both test iterations. The logic from `debug-0009-a2.py` was adopted as the final solution and incorporated into the main project as part of [Prompt 0010](../../PROMPTS.md#prompt-0010).

## Files

- [`debug-0009-a1.py`](./debug-0009-a1.py) — Fixed 40x20 viewport implementation
- [`debug-0009-a2.py`](./debug-0009-a2.py) — Dynamic terminal-sized viewport implementation

## Transcript

**Todd:** After implementing structured rooms and hallways in prompt 0009, the screen appears filled with `#` characters at game start. The player spawns inside a room and can move, but the screen is dominated by walls.

**Todd:** Is the map actually larger than 100×100?

**ai-helper:** No. `WIDTH` and `HEIGHT` are explicitly set to 100, and the map is initialized as: game_map = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

So the dimensions are correct — the issue is how much of the map is carved vs. left as walls.

**ai-helper:** The carving logic creates only 16 rooms (~2400 tiles) out of 10,000. The rest remain as `#`, which is faithfully rendered in full by the draw_map() function. The result is not a bug per se, but a case of rendering everything, including the untouched majority of the map.

**Todd:** I think I know why you are pushing the viewport. It allows us to have map that is ‘off the screen’ or not in the visible terminal window. Is that correct?

**ai-helper:** Confirmed. A viewport lets us:
- Maintain a large map
- Display only the visible portion
- Avoid wrapping, clutter, and full-map redraws

**Todd:** Can we detect the size of the terminal and use that to determine our map or viewport?

**ai-helper:** Yes. Python’s shutil.get_terminal_size() allows us to dynamically set viewport dimensions based on the actual size of the terminal window. This lets the map remain 100×100 (or larger) while the visible area adapts to the user’s screen.

**Todd:** I like the idea of not being constrained to the terminal size and instead be able to have a large map with a viewport that moves with the player.

**ai-helper:** Excellent — that gives you the best of both worlds: a scrollable world and a manageable visual window.

**Todd:** Start with the player centered, then pan the screen when they approach the edge of the map.

**ai-helper:** We'll implement a center-then-clamp strategy:
- Player is centered most of the time
- Viewport stops scrolling at map edges

**Todd:** Fixed viewport.

**ai-helper:** Viewport size set to VIEW_WIDTH = 40, VIEW_HEIGHT = 20. Candidate fix debug-0009-a1.py implements this logic.

**Todd:** Let's do one more test iteration. Extend the map size to the size of the terminal window and put the view window the same size but put it in the middle of the terminal window.

**ai-helper:** Great — we’ll:
- Use shutil.get_terminal_size() to determine MAP_WIDTH, MAP_HEIGHT
- Set VIEW_WIDTH and VIEW_HEIGHT equal to that
- Keep the player centered on the map
- Render a viewport that fills the terminal entirely

This test will use candidate file debug-0009-a2.py


