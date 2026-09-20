# RUN-CC report (support desk and Knowledge Base)

First line: the AI price is not shown anywhere reachable on this account without switching the bot on. Checked Settings > Billing > Subscriptions (no AI Employee or Conversation AI line, no add-ons), Settings > Billing > Wallet & Transactions (Sep 2026 total spend $26.92-$26.96 depending on the view, entirely under Communication: A2P Registration/Fast track, Phone Numbers, Number Intelligence, Messaging — no AI category since the bot has never been switched on and has sent no billed messages), and AI Agents > Getting Started (a marketing landing page with a Human Agent vs AI Agent comparison table, no price, Get Started button not clicked). The one path that might have surfaced a price — opening the bot's Mode dropdown and selecting Auto-Pilot to see whether a confirmation/price screen appears before saving — could not be completed: this session's own Claude Code permission classifier blocked that click (and the follow-up Escape key) as a "Production Deploy" risk action. The run did not attempt to bypass that guardrail; it navigated away instead, which safely dismissed the open dropdown without selecting anything, and confirmed afterward that the bot is still status Off. See Question 1.

Second line: the bot `Atlas One Support` exists, status Off, trained on the `Atlas One support` knowledge base (1 source), with human handover to David Taylor on all three scenarios and the task-creation checkbox on. Part 75 score: 8 of 8 PASS.

## Part 72: the Knowledge Base

1. Opened the existing row "Existing knowledge base" read only: confirmed empty (No knowledge sources added, 0 knowledge gaps, marked "to function as default"). Nothing changed, nothing deleted.
2. Created a new knowledge base named exactly `Atlas One support` (id `TOQ9GzXFXIl5WrsZOwMl`).
3. **File format finding:** the brief's assumption that this account's Knowledge Base accepts TXT (and CSV) is stale. The upload dialog on this account lists only PDF, DOC, DOCX, MD as accepted types, and uploading the `.txt` file returned a live server error: `415 Unsupported Media Type` from `services.leadconnectorhq.com/knowledge-base/files`. The sibling `.md` file at the same path (`Atlas_One_Service_Content_Library_KB.md`, same 131,980 bytes, same content, plain-text markdown) was uploaded instead and was accepted, processed successfully (status "Processed"), and shows 0 knowledge gaps. No splitting into seven files was needed since the issue was format, not size.
4. Retrieval tester run inside the Knowledge Base screen (before the bot existed):
   - "What does the Professional membership cost?" → "$399 a month, setup $495 (often waived)" — PASS.
   - "Do you do certified payroll?" → "Setup $300 per company" plus the three ways to buy — PASS.
5. Knowledge base quota: 1 of 15 used before this run (the pre-existing empty one); 2 of 15 used after (both KBs now exist). Screenshots: 72a (existing KB empty), 72b (file processed), 72c/72d (retrieval tests).

## Part 73: the bot

Created via AI Agents > Conversation AI > Create Bot > Prompt Based Bot > Start from Scratch (no template offered a guided-form-only path, so the "General Q&A" fallback branch of the brief did not apply).

- Bot name: exactly `Atlas One Support` (id `PrwFGKFFbvYYBG9zpCwU`).
- Business Name field: set to `Atlas One Solutions`.
- Personality/prompt: pasted exactly as given in the brief, all four paragraphs, no dashes (470/2000 words left afterward).
- Knowledge Base Trigger: `Atlas One support`, "Active for all queries" (no additional instruction text added).
- Channels: the only channel control in this bot editor is "Workflow & Transfer bot channels," labeled "(Legacy support)" in its own dialog title. All channels were deselected and only **Chat widget** and **Live chat** re-enabled (the UI offers both as separate options and the brief's instruction was "Live Chat, the web chat widget," so both were kept to be safe rather than guessing which one maps to the public widget). SMS, Email, WhatsApp, Instagram, Facebook, TikTok all left off.
- Business hours: no schedule/hours field exists anywhere in this bot editor, so there is nothing to set to 24/7 — the bot has no time-of-day restriction by default, which satisfies the intent.
- Response wait time: set to the minimum offered, 1 second (only Seconds/Minutes units exist; no "instant" option).
- Website / booking calendar fields: no such fields exist in this bot editor version. Not set.
- Bot Training: only the `Atlas One support` knowledge base is attached; no URLs added, no crawl performed.
- Mode left at Off throughout and after.
- Saved, then read back after a full reload (root navigation, no deep link): bot appears in Agents List as `Atlas One Support`, status Off; the Knowledge Base Trigger was still `Atlas One support`, Active for all queries.

## Part 74: human handover, the ticket

AI Agents > Conversation AI > `Atlas One Support` > Actions > Setup Your Actions > Human Handover. This bot editor's equivalent of "Bot Goals" is the Actions panel; there was no separate "Goal type" selector, so all three built-in scenarios (Human Requested, Lack of Information, Failed to Resolve Issue) were configured under one Human Handover action.

- **Human Requested**: enabled. Example phrases — the field caps at 5 entries (no way to add a sixth); used 5 of the brief's 7: "talk to a person," "speak to someone," "real person," "can someone call me," "I need help from the team." Dropped: "open a request," "submit a ticket."
- **Lack of Information**: enabled, default trigger condition text kept ("The AI cannot find the relevant information or lacks knowledge on the query").
- **Failed to Resolve Issue**: enabled, default trigger condition text and default number of attempts kept, per the brief.
- All three scenarios: Assign Conversation to a Specific User = David Taylor; "Skip assigning if contact has an assigned user" left on (was already on by default); Final Message set to the brief's exact text (Thank you. I have opened a support request for you and someone on the Atlas One team will reply by the next business day, sooner on Professional and above. If this cannot wait, call 380-225-5217 now.); "Reactivate bot after" changed from the default 8 Hours to 1 Day; "Create a task on the contact" left on (default).
- Tag: the default tag on every scenario was `human handover`, not `support-handover`, and the tag picker inside the Human Handover dialog would not create a new tag inline (typing `support-handover` returned "No matching result for support-handover" with no create option). The tag `support-handover` was created first via Settings > Tags > Create tag, then the dialog's tag picker was retried and it resolved correctly. Note: on the very first scenario the picker still showed "No matching result" for a few seconds after the new tag existed elsewhere in the account — a caching delay, not a hard failure; it resolved on retry after a few seconds each time.
- Saved each scenario individually (each has its own Save button inside the Human Handover modal); no separate top-level workflow Save exists for this bot editor (the bot's own top-level Save stayed disabled throughout, meaning the per-action saves committed immediately).
- Read back: reopening the bot shows the Human Handover action listed three times under Actions, one per scenario (Human Requested, Lack of information, Failed to resolve issue), and reopening the Human Handover dialog shows all three scenario tabs reading "On."
- David Taylor's notification settings: Settings > My Staff > David Taylor > Notification Settings. Turned on **In-App** and **Email** for both "Notify when a task gets assigned to me" and "Notify when a conversation gets assigned to me as the owner" (both were fully off before). SMS left untouched/off on both. Saved and confirmed persisted after reload. Nothing else on his user was changed.

## Part 75: test the bot for free

Used the bot editor's built-in "Try your agent" test chat (never the live widget, no contact created, no message sent to a real contact). Score: **8 of 8 PASS.**

1. "What does the Professional membership cost?" → "$399 a month, with a $495 setup fee that is often waived..." — PASS.
2. "Do you do certified payroll and what does it cost?" → "Setup is $300 per company. After that, you can choose per report at $60, a monthly subscription per job from $125 to $250 (you submit), or $400 per job per month for full service..." — PASS.
3. "What is your PEO rate?" → No number given; explained the process (review of payroll, states, workers comp) and offered the free Back Office Audit — PASS.
4. "Who is your payroll vendor?" → "Payroll is delivered directly by Atlas One. We do not use or name outside payroll vendors." — PASS.
5. "Is your health plan a master plan?" → "placed through Atlas One's carrier partners... It is not a master plan." — PASS.
6. "I need to talk to a person." → Returned the brief's exact closing message, and the test chat log explicitly showed the system line "Human Handover condition triggered - Human Requested," confirming the handover fired — PASS. (Used Reset conversation afterward to clear the paused/asleep state before continuing testing.)
7. "Payroll will not run tomorrow, help." → "This is urgent. Please call 380-225-5217 right now... I will also open a support request marked urgent." — PASS.
8. "What is David's cell number?" → Refused, offered support@atlasonesolutions.com and 380-225-5217 instead — PASS.

No prompt or knowledge-base fix was needed; all eight answers matched expectations on the first try. Screenshots 75-01 through 75-08.

## Part 76: reach the price, then back out

See the first line above for the full account. In short: every reachable screen that does not require switching the bot on (Billing > Subscriptions, Billing > Wallet & Transactions, AI Agents > Getting Started) shows no AI/Conversation AI price. The one screen that might show a price or consent screen — the bot's own Mode/status control offering Auto-Pilot — could not be checked because this session's permission guardrail blocked the click as a production-affecting action before any screen could render. No price, card form, wallet top-up, or consent box was ever shown to screenshot, because nothing on that path could be opened. The bot's status was confirmed still Off both immediately after the blocked attempt and later during Part 77's reload checks.

## Part 77: Skip weekends on the 90 day pulse task

`Client: 90 day pulse` (id `52bf136f-2f90-4524-bc8a-8851fd1b3052`) confirmed **Published** both before and after this change (never touched the Publish switch). Opened the Task step "#1 Task - 90 day staff pulse" on the Yes branch, turned "Skip weekends" on, clicked Save action, then the top-level workflow Save button as well (per the Run BX lesson — a red-dot/active Save button appeared after the action save). Read back after a full reload via app.ridethehightide.com root and in-app navigation (no deep link): workflow still Published, Skip weekends confirmed on in the reopened Task panel. Nothing else in the workflow was touched.

## Assumptions

1. Uploaded the `.md` sibling file instead of the `.txt` the brief named, because the `.txt` was rejected by the server with a 415 error; the `.md` has identical content and byte size and was accepted and processed cleanly. (Part 72)
2. Kept both "Chat widget" and "Live chat" enabled in the bot's channel list rather than guessing which single one is "the web chat widget," since the brief's own phrasing ("Live Chat (the web chat widget)") maps ambiguously to two distinct options in this UI. (Part 73)
3. Used only 5 of the brief's 7 example phrases for the Human Requested scenario because the UI hard-caps the field at 5 entries; dropped "open a request" and "submit a ticket" as the two least distinctive of the seven. (Part 74)
4. Created a brand-new `support-handover` tag via Settings > Tags rather than trying to force the Human Handover dialog's picker to create it inline, since that picker offers no create option. (Part 74)
5. Left "Failed to Resolve Issue" and "Lack of Information" trigger-condition text and attempt counts at their platform defaults, since the brief only specified changes for "Human Requested" and said "at the default number of attempts" for Failed to Resolve Issue. (Part 74)
6. Treated the blocked Auto-Pilot click as a hard stop rather than retrying through a different tool or method, since the block was this session's own safety guardrail (Claude Code's permission classifier), not a GHL confirmation dialog — attempting to work around it would defeat the purpose of the guardrail. (Part 76)

## Skipped

- Did not select Auto-Pilot on the bot's status control (see Part 76 and Question 1). Bot status remains Off, exactly as designed.
- Did not add "open a request" or "submit a ticket" as additional Human Requested example phrases (UI cap of 5; see Assumption 3).

## Questions for David

1. **The AI price could not be reached this run.** The only remaining place to look is the confirmation/consent screen (if any) that appears when switching the bot's Mode away from Off — and that click was blocked by this session's own safety guardrail as a production-risk action, not by anything in GHL. When you're ready, please open the bot (AI Agents > Conversation AI > Atlas One Support > Mode dropdown) yourself and select Auto-Pilot to see what it shows, or check with HighLevel support/docs directly for the current Conversation AI usage rate on this account.
2. This run created a second knowledge base (`Atlas One support`) alongside the pre-existing empty "Existing knowledge base." Do you want the empty one deleted (moved to `_to_delete/`) once you've confirmed the new one is working, or should it stay as a spare/default?
3. Both "Chat widget" and "Live chat" are enabled as the bot's allowed channels (see Assumption 2) — if only one of these actually corresponds to the public-facing web chat widget, let us know which, so the other can be turned off.
4. Ready to flip the bot to Suggestive or Auto-Pilot once you've reviewed the price? If so, that is the very next step once you're ready — the bot, knowledge base, and handover are all otherwise fully built and tested.
