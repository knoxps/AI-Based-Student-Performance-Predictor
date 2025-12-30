#!/usr/bin/env bash
set -euo pipefail

# Usage: ./deploy_to_github.sh [repo-name]
# If GitHub CLI (gh) is installed and authenticated, this script will create the repo and push.
# Otherwise it will print the git commands to run manually.

REPO_NAME=${1:-ai-student-performance-predictor}

echo "Preparing repository for deployment (name: $REPO_NAME)"

if ! command -v git >/dev/null 2>&1; then
  echo "git is not installed. Install git and re-run this script." >&2
  exit 1
fi

# Initialize git if necessary
if [ ! -d .git ]; then
  git init
  git branch -M main || true
fi

git add -A
if git status --porcelain | grep . >/dev/null 2>&1; then
  git commit -m "chore: prepare project for deployment" || true
else
  echo "No changes to commit"
fi

if command -v gh >/dev/null 2>&1; then
  echo "Found GitHub CLI (gh). Creating remote repo and pushing..."
  # create repo (public) and push current branch
  gh repo create "$REPO_NAME" --public --source=. --remote=origin --push
  echo "Repository created and pushed via gh. Visit: https://github.com/$(gh repo view --json owner -q .owner)/$REPO_NAME"
else
  echo "GitHub CLI (gh) not found. To push manually run the following commands:";
  echo "  git remote add origin git@github.com:<your-username>/$REPO_NAME.git";
  echo "  git branch -M main";
  echo "  git push -u origin main";
fi

echo "Done. Next: go to https://share.streamlit.io, create a new app, and set 'Main file' to app/app.py" 
