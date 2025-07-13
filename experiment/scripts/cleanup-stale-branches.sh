#!/bin/zsh

set -e

# Option parsing
QUIET=0

for arg in "$@"; do
  if [[ "$arg" == "--quiet" || "$arg" == "-q" ]]; then
    QUIET=1
  fi
done

echo "Checking out and updating 'main'..."
git checkout main >/dev/null 2>&1
git pull origin main

echo ""
echo "Scanning for local feature branches fully included in main..."

stale_local_branches=()

for branch in $(git branch --format='%(refname:short)' | grep '^feature/'); do
  if [ -z "$(git cherry main "$branch" | grep '^+')" ]; then
    stale_local_branches+=("$branch")
  fi
done

if [ ${#stale_local_branches[@]} -eq 0 ]; then
  echo "No local feature branches are fully included in main."
else
  echo "The following local feature branches have no unique commits and are safe to delete:"
  for branch in "${stale_local_branches[@]}"; do
    echo "  - $branch"
  done

  echo ""
  printf "Do you want to delete these local branches? [y/N]: "
  read confirm_local
  confirm_local=$(echo "$confirm_local" | tr '[:upper:]' '[:lower:]')

  if [[ "$confirm_local" == "y" || "$confirm_local" == "yes" ]]; then
    for branch in "${stale_local_branches[@]}"; do
      if git branch -d "$branch" >/dev/null 2>&1; then
        echo "Deleted branch: $branch"
      else
        if [[ "$QUIET" -eq 0 ]]; then
          echo "Branch '$branch' could not be deleted with -d (safe delete)."
        fi
        printf "Do you want to force delete it? [y/N]: "
        read confirm_force
        confirm_force=$(echo "$confirm_force" | tr '[:upper:]' '[:lower:]')
        if [[ "$confirm_force" == "y" || "$confirm_force" == "yes" ]]; then
          git branch -D "$branch" >/dev/null 2>&1
          echo "Force-deleted branch: $branch"
        else
          echo "Skipped branch: $branch"
        fi
      fi
    done
  else
    echo "Skipped local branch deletion."
  fi
fi

echo ""
echo "Scanning for remote feature branches fully included in origin/main..."

git fetch --prune

stale_remote_branches=()

for branch in ${(f)"$(git branch -r | grep '^origin/feature/')"}; do
  remote_branch=${branch#origin/}
  if [ -z "$(git cherry origin/main "origin/$remote_branch" | grep '^+')" ]; then
    stale_remote_branches+=("$remote_branch")
  fi
done

if [ ${#stale_remote_branches[@]} -eq 0 ]; then
  echo "No remote feature branches are fully included in origin/main."
else
  echo "The following remote feature branches have no unique commits and are safe to delete:"
  for branch in "${stale_remote_branches[@]}"; do
    echo "  - $branch"
  done

  echo ""
  printf "Do you want to delete these remote branches from origin? [y/N]: "
  read confirm_remote
  confirm_remote=$(echo "$confirm_remote" | tr '[:upper:]' '[:lower:]')

  if [[ "$confirm_remote" == "y" || "$confirm_remote" == "yes" ]]; then
    for branch in "${stale_remote_branches[@]}"; do
      git push origin --delete "$branch" >/dev/null 2>&1
      echo "Deleted remote branch: $branch"
    done
  else
    echo "Skipped remote branch deletion."
  fi
fi

echo ""
echo "Branch cleanup complete."
