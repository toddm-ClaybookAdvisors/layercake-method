#!/bin/zsh

# =============================================================================
# Script: start.sh
# Purpose:
#   - Set up local dev session
#   - Prepend ./bin to PATH
#   - Start a Poetry-managed shell environment
#   - Customize the shell prompt to show your preferred name
# Usage:
#   source ./start.sh
# =============================================================================

# --- Ensure the script is being sourced ---
if [[ "$ZSH_EVAL_CONTEXT" != *:file ]]; then
  echo "ERROR: This script must be run using 'source ./start.sh'"
  return 1 2>/dev/null || exit 1
fi

echo "[1/3] Adding ./bin to PATH"
export PATH="./bin:$PATH"

echo "[2/3] Launching Poetry shell"
poetry shell

# --- (Optional) Override the prompt for aesthetic purposes ---
# Note: This line executes *after* poetry shell only if run interactively inside the current shell
# You may not see this take effect if poetry shell spawns a new shell process
#export PS1="(game) $PS1"

echo "[3/3] Dev session ready."