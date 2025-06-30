#!/bin/zsh

# =============================================================================
# Script: start.sh
# Purpose:
#   - Set up local dev session
#   - Prepend ./bin to PATH
#   - Add ./app/src to PYTHONPATH (fixes local imports)
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

echo "[1/4] Adding ./bin to PATH"
export PATH="./bin:$PATH"

echo "[2/4] Adding ./app/src to PYTHONPATH"
export PYTHONPATH="./app/src:$PYTHONPATH"

echo "[3/4] Launching Poetry shell"
poetry shell

# --- (Optional) Override the prompt for aesthetic purposes ---
#export PS1="(game) $PS1"

echo "[4/4] Dev session ready."
