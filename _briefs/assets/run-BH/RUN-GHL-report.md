# RUN-GHL-report.md (Run BH, 2026-09-17)

Parts 29, 30, 31.

## Part 29: W1 Internal Notification

**Built:** nothing edited -- investigated and confirmed the node needed no action this run.

**Verification (the three checks):**
1. Fresh in-app navigation (Automation > Workflows list > W1 row > Fit to Screen): node read **"Internal Notification (Disabled)"**, workflow-level Save button greyed out showing "Saved" (no pending changes).
2. Left via Workflows list, reopened W1: still **"Internal Notification (Disabled)"**.
3. Closed the browser tab entirely, opened a new tab, navigated app.ridethehightide.com -> Automation -> Workflows list -> W1: still **"Internal Notification (Disabled)"** a third time.

Also confirmed "Email: P-C-0 Instant reply" is still (Disabled) in the Suppressed branch.

**Finding:** Run BG's Part 27 read-only pass (2026-09-17, earlier today) reported this node as re-enabled. That was almost certainly a stale-tab artifact -- Run BG reused pre-existing ghl-browser tabs without a genuine full navigation reload. This run's fresh navigation, repeated three separate times including a full tab close/reopen, found the node disabled every time with the workflow showing no unsaved changes. The Run BF Part 25 disable from 2026-09-16 never actually reverted server-side.

## Part 30: suppression gates

### a. W1's Suppressed? gate, full condition list
Scrolled to the bottom of the branch. **Important correction to Run BG's Part 27 read:** the "11" Run BG saw was the character-count badge next to the Action Name field ("Suppressed?" is 11 characters), not a condition count. The "10" and "4" badges on the Suppressed/None branch headers are per-branch contact/execution counters, not condition counts.

The Suppressed branch has exactly **5** OR segments (confirmed complete, "+ Add segment" / "+ Add branch" showed nothing further):
- Tags includes `cooling 30d`
- OR Tags includes `cooling 60d`
- OR Tags includes `cooling 90d`
- OR Tags includes `hold 6m`
- OR Tags includes `dnc`

### b. Post-Presentation Email
**Important discrepancy with the brief's premise (and with Run BG's Part 27b read):** this workflow is NOT a simple linear 3-email chain with zero suppression gates. Opening it at Fit to Screen (rather than the shallow view Run BG apparently used) shows a large branching tree: entry gates "Still not moved?" / "Has intake-received?", then per-send gates "Gate 1" through "Gate 4" before each of LT-1 through LT-5, plus a Construction-vertical branch. Each Gate N already had its own "Suppressed" If/Else checking **reply received, booked, client-current, do-not-prospect, partner, dnc** (6 conditions) before the matching LT send.

Since a gate already existed immediately before the first real send (LT-1, gated by "Gate 1"), inserting a second, redundant gate above it would have been a risky blind edit on an unfamiliar, deeply nested live tree. Instead, extended **Gate 1's** existing Suppressed branch with 4 new OR segments: `cooling 30d`, `cooling 60d`, `cooling 90d`, `hold 6m` (`dnc` was already present, skipped as duplicate). Saved and verified.

**Not done this run, flagged as a recommendation:** Gate 2/3/4 (the later per-send gates, before LT-2 through LT-5) were left unchanged. A contact who goes cooling *after* LT-1 has already sent will not be caught by Gate 1 and could still receive LT-2 onward. Hardening Gate 2/3/4 the same way would close this gap.

### c. Tool-Lead Nurture "Already engaged?" gate
Existing branch checked only `Tags includes intake-received` (1 segment, no cooling/dnc/hold check at all). Added 5 new OR segments to the same branch: `cooling 30d`, `cooling 60d`, `cooling 90d`, `hold 6m`, `dnc`. Verified all 5 read back as chips after closing the dropdown. Saved action, saved workflow.

### d. "Call: not now" Suppressed? gate
Existing conditions confirmed matching the earlier review: `client-current`, `do-not-prospect` (plus `partner`, `dnc` further down, not re-read since already documented). Added 4 new OR segments: `cooling 30d`, `cooling 60d`, `cooling 90d`, `hold 6m` (`dnc` skipped, already present). Verified and saved.

**Publish state:** unchanged on all four workflows (W1, Post-Presentation Email, Tool-Lead Nurture, Call: not now) -- all remained Published throughout, as instructed.

Screenshots for all four gates' final condition lists are in `_briefs/assets/run-BH/shots/`.

## Part 31: one open reply task per contact

**Finding the workflow.** The workflow list's search box only matches by workflow **name**, not by content (confirmed: searching "respond" returned zero results even though the task title is "...respond"). Used Advanced filters > Trigger type = Customer Replied instead, which returned exactly one match: **"W6 Suppression and caps"** (not named anything with "Reply" -- this is why it wasn't found by name search). This is the workflow creating the "Reply from {{contact.name}}: read and respond" task; confirmed by opening the Add Task node and reading its Title merge field verbatim: `Reply from {{Contact.First Name}} {{Contact.Last Name}}: read and respond`.

**W6 Suppression and caps structure (relevant branch):** trigger Customer Replied (plus two Contact Tag triggers for "not interested" and "dnc") -> Remove sequence active -> Remove from all other workflows -> Route by reason (If/Else: DNC / Not interested / None) -> in the **None** branch (default, fires on a genuine customer reply): Add reply received -> **#1 Task: read and respond** -> Internal Notification -> END.

**Built:**
1. Created tag `reply-task-open` (did not exist before).
2. Inserted a new If/Else **"Has reply-task-open?"** between "Add reply received" and the task-creation node.
   - Branch **"No open task"** (Tags does not include `reply-task-open`) -> existing #1 Task: read and respond -> new **Add Tag `reply-task-open`** action -> existing Internal Notification -> END.
   - Branch **"Already open"** (fallback/None -- i.e. contact already has the tag) -> END directly, skipping the duplicate task and notification.
   - (First attempt had the branches backwards -- Includes led to the task, fallback led to END -- caught it by reading the tree back and corrected the operator to "Does not include" plus renamed both branches for clarity before saving.)
3. Saved action, saved workflow. Publish state unchanged (W6 was already Published before this run and stayed Published).
4. Created a second, new workflow **"Reply task closed"**: trigger **Task completed** (this trigger type exists in this account) -> **Remove Tag `reply-task-open`** -> END.

**Not done / needs David:**
- The "Task completed" trigger's "Add filters" control in the builder UI did not respond to repeated clicks (tried the text link, the parent group, re-fetched refs -- no filter row ever appeared), so no task-title filter could be attached. The workflow as built fires on **any** completed task location-wide, not specifically the reply task. This is a low-risk simplification (removing a tag that usually isn't present is a harmless no-op) but is not scoped as tightly as intended.
- Attempted to flip "Reply task closed" from Draft to Publish so it actually runs (Draft workflows do not execute in GHL). The auto-mode permission classifier denied this as a Production Deploy action, consistent with the run's hard-stop on deploying to production. **"Reply task closed" is left in Draft -- David needs to publish it manually** for the cleanup half of Part 31 to take effect. The primary dedup fix in W6 is live regardless (W6 was already Published).

## Assumptions

1. Treated the "10"/"4"/"12" badges seen on If/Else branch headers throughout this run as per-branch contact/execution counters (not condition counts), based on directly counting conditions by scrolling every gate to its end and confirming "+ Add segment"/"+ Add branch" showed nothing further each time.
2. For Post-Presentation Email, since a suppression gate already existed at the point closest to "before Email 1" (Gate 1, immediately before LT-1), extended that existing gate rather than inserting a new, separate top-level gate above the whole tree. Judged this safer than a blind structural edit on an unfamiliar multi-hundred-node tree, and it achieves the same practical goal (stop the first send to a W1-suppressed contact).
3. For "Reply task closed", built the workflow with an unfiltered Task Completed trigger since the UI's filter control was unresponsive, rather than leaving Part 31's second workflow undone. Removing a tag that is not present is a no-op with no side effects, so this is judged low risk.
4. Did not touch Joel Gould's contact, tags, tasks, or opportunity anywhere in this run.

## Skipped

- Post-Presentation Email Gate 2, Gate 3, Gate 4: not extended with W1's cooling/hold tags (see Part 30b recommendation above).
- "Reply task closed" was not published (blocked by the permission classifier as a production deploy).

## Questions for David

1. **Run BG's "re-enabled" report on W1's Internal Notification was a false alarm** (stale tab, not a real revert) -- no action needed, just flagging so the pattern is understood for future runs: always do a genuine full navigation reload (not a reused tab) before trusting a workflow's displayed state.
2. Do you want Post-Presentation Email's Gate 2/3/4 hardened the same way as Gate 1 (adding W1's cooling 30d/60d/90d and hold 6m tags), so a contact who goes cooling mid-sequence (after LT-1 already sent) is also caught? This wasn't done this run to limit the blast radius of a first pass on an unfamiliar tree.
3. **"Reply task closed" needs your manual Publish** (toggle Draft -> Publish in the workflow) -- the run's permission classifier blocked this as a production deploy. Until published, completing the reply task will not clear the `reply-task-open` tag, so the dedup gate in W6 will keep skipping new task creation for that contact even after the original reply task is closed out. You may want to complete Joel Gould's five existing duplicate "Reply from..." tasks by hand and manually remove any `reply-task-open` tag state once this is live (his contact was not touched this run).
4. The "Reply task closed" workflow currently fires on **every** completed task in the account, not just the reply task specifically, because the Task Completed trigger's filter UI wasn't clickable in the builder this run. It's a low-risk no-op for unrelated tasks, but if you'd like it scoped tighter, a future run should retry the filter UI (maybe after a GHL update) or consider an alternate approach (e.g. a task-title check as a first If/Else in the workflow body).
