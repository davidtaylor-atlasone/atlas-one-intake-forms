# AGENTS.md: for any AI coding tool (Codex CLI, Copilot, Cursor, Gemini CLI, Aider, Claude Code)

This repo is public and GitHub Pages serves `main` at forms.atlasonesolutions.com, so every file on `main` is on the
web. Read `CLAUDE.md` in this folder first: it is the working rules file for every tool, not only Claude. On David's
Mac, his global rules are in `~/.claude/CLAUDE.md` and the skills in `~/.claude/skills/`.

Hard stops (David does these himself): sending email, enabling SMS, GoHighLevel's HIPAA feature, deleting files,
deploying to production (a merge to `main` here IS a production deploy), spending money. Never put a key, token,
password or client data in this repo. Work on a new branch in its own `git worktree`.
