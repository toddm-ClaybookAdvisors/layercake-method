# Debug Session: debug-0012-a

## Summary
This debug session addressed an `IndexError` in `draw_map()` caused by a mismatch between the terminal's viewport size and the fixed map dimensions in `mapgen.py`. The error was resolved by:

- Passing dynamic terminal dimensions from `game.py` into `generate_map()`
- Updating `mapgen.py` to use those dimensions rather than hardcoded values
- Adjusting the game loop and rendering logic to clamp viewport bounds properly
- Verifying the fix via a testable subdirectory structure (`a1/`, `a2`)

The working candidate (`a2`) resolved the original traceback and displayed the map correctly. This fix is associated with **Prompt 0012** and will be merged into the mainline.

## Final Git Commit
```bash
git commit -am "fix: irregular room generation, maze-like connections, modular mapgen (prompt 0012)"
```

---

## Transcript

**Todd:**  
record debug

**ai-agent:**  
Confirmed. We're now logging a debug session on the `IndexError` in `draw_map()` caused by out-of-bounds access.

**ai-agent:**  
Please confirm:
- Your terminal size at runtime
- Whether `VIEW_WIDTH` or `VIEW_HEIGHT` might exceed `MAP_WIDTH` or `MAP_HEIGHT`

**Todd:**  
The terminal size hasn't changed, and I thought we were getting it dynamically which is my preference. However, I ran this command line to get it:

```
tput cols  
tput lines  
zsh: unknown file attribute: i  
zsh: unknown file attribute: h  
echo $COLUMNS  
echo $LINES  
198  
57
```

**ai-agent:**  
Thanks for the confirmation. Your terminal is 198×57, but `mapgen.py` is still hardcoding the map to 100×40.

To fix this, I suggest:  
1. Make `MAP_WIDTH` and `MAP_HEIGHT` dynamic in `mapgen.py`  
2. Pass the terminal size from `game.py` into `generate_map()`

Would you like me to generate a fix candidate (`debug-0012-a1`) that applies this change?

**Todd:**  
yes

**ai-agent:**  
Fix candidate `debug-0012-a1` is now applied. You’ll also need to update `game.py` to call:

```python
generate_map(VIEW_WIDTH, VIEW_HEIGHT)
```

Let me know if you'd like me to patch that in too, or test this version first.

**Todd:**  
record debug

**ai-agent:**  
Debug session resumed: **debug-0012-a**

```
debug/debug-0012-a/
├── a1/
│   ├── mapgen.py
│   └── game.py  ← generated now
```

**Todd:**  
Looks like we have a structural issue that should be easy to address, however, due to the nature of this project, I will not be editing it by hand.

```
ModuleNotFoundError: No module named 'a1'
```

**ai-agent:**  
Acknowledged. I’ll revise `game.py` in `a1/` to use local imports only and avoid package-style paths.

**Todd:**  
We’ve got another one: Let's put any fixes into `a2`. I will be running in the `a2` directory to test.

**ai-agent:**  
Understood. Generating `game.py` for `debug/debug-0012-a/a2/` now with clamped viewport bounds.

**Todd:**  
I forgot to include the error:

```
AttributeError: module 'mapgen' has no attribute 'generate_map'
```

**ai-agent:**  
That means `a1/mapgen.py` isn't the updated version. Copying the correct version to `a2` now.

**Todd:**  
That worked

**ai-agent:**  
Confirmed — candidate `a2` is a working fix.

**Todd:**  
Create a git commit with the comment for 0012 first

**ai-agent:**  
```bash
git commit -am "fix: irregular room generation, maze-like connections, modular mapgen (prompt 0012)"
```
