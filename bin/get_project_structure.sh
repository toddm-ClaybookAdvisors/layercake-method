#!/bin/zsh

# ==============================================================================
# Script: show-structure-clean
# Purpose:
#   1. Print Git commit history in single-line format (for prompt index generation)
#   2. Print a filtered, Git-aware project file tree (for inclusion in README.md)
# ==============================================================================

PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

if [[ -z "$PROJECT_ROOT" ]]; then
  echo "ERROR: Not inside a Git repository."
  exit 1
fi

echo '```markdown'
echo "## FULL COMMIT HISTORY USE TO GENERATE PROMPT INDEX"
git -C "$PROJECT_ROOT" log --pretty=format:"%h %ad | %s [%an]  " --date=short

echo
echo "## PROJECT FILE STRUCTURE (filtered, Git-aware) FOR USE IN README.md"
git -C "$PROJECT_ROOT" ls-files | \
grep -vE '(^|/)(\.gitignore|\.archive.*|poetry\.lock|pyproject\.toml|\.venv|\.cache|requirements\.txt)$' | \
awk '
BEGIN { FS="/" }
{
  path = ""
  for (i = 1; i <= NF; i++) {
    path = (path ? path "/" : "") $i
    if (!(path in seen)) {
      seen[path] = 1
      indent = ""
      for (j = 1; j < i; j++) indent = indent "│   "
      branch = (i == NF ? "└── " : "├── ")
      print indent branch $i "  "
    }
  }
}'
echo '```'
