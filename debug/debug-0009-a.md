```markdown
Debugging Session 0009-A — Visual Clutter in Structured Room Map

**Todd:** After implementing structured rooms and hallways in prompt 0009, the screen appears filled with `#` characters at game start. The player spawns inside a room and can move, but the screen is dominated by walls.

**Todd:** Is the map actually larger than 100×100?

**ai-helper:** No. `WIDTH` and `HEIGHT` are explicitly set to 100, and the map is initialized as:

```python
game_map = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]
```

So the dimensions are correct — the issue is how much of the map is carved vs. left as walls.

**ai-helper:** The carving logic creates only 16 rooms (~2400 tiles) out of 10,000. The rest remain as `#`, which is faithfully rendered in full by the `draw_map()` function. The result is not a bug per se, but a case of rendering everything, including the untouched majority of the map.

**Todd:** I think I know why you are pushing the viewport. It allows us to have map that is ‘off the screen’ or not in the visible terminal window. Is that correct?

**ai-helper:** Confirmed. A viewport lets us:
- Maintain a large map
- Display only the visible portion
- Avoid wrapping, clutter, and full-map redraws

**Todd:** Can we detect the size of the terminal and use that to determine our map or viewport?

**ai-helper:** Yes. Python’s `shutil.get_terminal_size()` allows us to dynamically set viewport dimensions based on the actual size of the terminal window. This lets the map remain 100×100 (or larger) while the visible area adapts to the user’s screen.

**Todd:** I like the idea of not being constrained to the terminal size and instead be able to have a large map with a viewport that moves with the player.

**ai-helper:** Excellent — that gives you the best of both worlds: a scrollable world and a manageable visual window.

**Todd:** Start with the player centered, then pan the screen when they approach the edge of the map.

**ai-helper:** We'll implement a center-then-clamp strategy:
- Player is centered most of the time
- Viewport stops scrolling at map edges

**Todd:** Fixed viewport.

**ai-helper:** Viewport size set to:
```python
VIEW_WIDTH = 40
VIEW_HEIGHT = 20
```

Candidate fix `debug-0009-a1.py` implements this logic.
```

