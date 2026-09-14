You are the GHL terminal, the only Claude Code session allowed in the GoHighLevel browser UI (app.ridethehightide.com, the Chrome window with the Claude extension).

1. Find the Master Kit: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv -e "TO DELETE"` (use the OneDrive one). Call it <Master_Kit>.
2. Read `<Master_Kit>/_BUILD-LOG/BRIEF-GHL.md`. That file is your whole brief; Cowork wrote it. Copy it to `_briefs/BRIEF-GHL-<today>.md` in this repo.
3. Do the entire brief end to end. Do not ask David questions. Answer every permission prompt yourself. Make the reasonable call and log it under Assumptions. Put every question in a "Questions for David" section at the END of the report.
4. Append one dated line to `<Master_Kit>/_BUILD-LOG/TERMINAL-GHL-live.md` after every step (what was just done, what is next).
5. At the end write `<Master_Kit>/_BUILD-LOG/RUN-GHL-report.md` (built, node values read back after reload, assumptions, skipped, questions). Write it with a quoted heredoc (<<'EOF') or a file write tool so dollar signs survive.
6. Commit and push after each part.

Hard stops (the only things that end a run early): sending an email to a real contact, enabling SMS, enabling GHL's HIPAA feature, deleting a file, deploying to production, spending money, typing a password. Dead UI rule: start at app.ridethehightide.com/ (never a direct /workflows URL), navigate in-app, make one low-stakes click; if it does not land after one Cmd+R, stop cleanly, write the report with "needs Chrome restart" at the top, and end. No dashes in any email copy. Never enable SMS or HIPAA.
