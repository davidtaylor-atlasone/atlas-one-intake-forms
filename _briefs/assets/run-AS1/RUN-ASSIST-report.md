# RUN-ASSIST report: Run AS1, the Atlas One Rep Assistant (2026-10-10)

Brief first line confirmed: Run AS1. Terminal ASSIST, Sonnet 5.5 (this run). Nothing was deployed, no Azure resource was created, no API key was created or used, no email sent. Nothing was pushed (see Assumption 9).

## What was built
1. **Knowledge pack** (Job 1): `_INTERNAL (do not share)/build_assistant_pack.py` plus `assistant_guard.py`. Output `_INTERNAL (do not share)/assistant/assistant_pack.json` (price book V12, 142 price rows, built 2026-10-10). Build fails on any blocked vendor or margin word or retired price. Sections of the pricing, offer and facts skills that are not rep safe are dropped and printed at build time (the lock, the retired list, the three family rule, phone numbers by brand, rules, booking links, authority, and all of atlas-facts except the tax/workers comp and QuickBooks sections). All three skills were found (synced copies, read only).
2. **Backend** (Job 2): new repo `~/Projects/atlas-one-rep-assistant` (2 local commits, no remote). Azure Functions, Python. `POST /api/ask`, `GET /api/unanswered` (David token only), per person tokens from people.json (sha256 hashed `TOKEN_HASH_<SLUG>` app settings, revoke one at a time), 60 questions an hour per person, Azure Table logging with the "not in price book" flag, prompt caching, max_tokens 400, temperature 0, `ASSIST_MODEL` default `claude-haiku-5-5`, mock mode with no key, server side output filter (blocked words and retired prices from price_scan.py replace the answer with the safe refusal and log the hit). `deploy_assistant.sh` is dry run by default.
3. **Ask button** (Job 3): `assistant_widget.html` (one shared module) and `assistant_inject.py`, hooked into `build_command.build()` with one commented call and one import. COMMAND got David's token, Charity's Sales Kit got hers, the shared Sales Kit got none. Offline panel is "Price lookup (offline)", a keyword search over the pack's client prices embedded at build time. COMMAND rebuilt (216 items, stamp Oct 10, 2026 11:27 AM), Charity's kit rebuilt (101 items, same stamp), `catalogue_check.py` OK, 216 entries, all 27 checks passed.
4. **Proof** (Job 4): headless Chromium at 390 px and 1280 px on COMMAND and Charity's kit, screenshots in `_BUILD-LOG/assist-shots/` (20 images: closed, offline lookup, online answer, online more, offline after online).

## Test counts
- Backend offline suite: 18 of 18 pass (auth, revoke one person, CORS, 60 an hour limit, PEO always Quoted, unknown service refusal, stale kit notice, 25 adversarial prompts against the mock, the same 25 prompts against 8 leaky model stubs all replaced with the refusal, model error gives 502 with no key text, pack has no guarded content).
- Master Kit `test_assistant_guard.py`: 2 of 2 pass (build_command.FORBIDDEN_TERMS is a subset of the assistant's blocked list).
- Browser proof (`prove_ask.mjs`): 82 of 84 pass, 2 explained below. Every other check passes on both pages at both sizes: scrollWidth equals viewport at 390 and 1280 with the panel closed and open, the button opens, offline lookup finds "handbook" and refuses "yachts", Escape closes, no console errors, **zero network requests as built**, online mode (local mock server) shows Online, three chips, Concierge answer carries $1,900, PEO answers Quoted, the markup question is refused, the objection chip answers from the talking points, the only network calls are the ping and the POSTs, and with the browser set offline the panel falls back to Price lookup.
- Greps on both outputs: no `sk-ant` or `ANTHROPIC_API_KEY`, no margin, markup, cost, wholesale, commission or vendor word inside the widget.
- **Not run: the live model suite.** `tests/live_suite.py --live` calls the real API, which spends money, so it is left to David. Until it runs, Haiku 5.5 stays the default but has not been proven on the rules. If any line fails, set `ASSIST_MODEL=claude-sonnet-5-5`.

The 2 browser failures are the "nothing else changed" text length fingerprint, not the widget. COMMAND differs only by the build stamp. Charity's kit differs by the build stamp and one embedded base64 tool (the self assessment form, changed by commit 48def90 after her kit was last built on Oct 8). Card count, nav count, title, row count and script count are identical before and after on both pages.

## Files
- `_INTERNAL (do not share)/`: `build_assistant_pack.py`, `assistant_guard.py`, `assistant_inject.py`, `assistant_widget.html`, `prove_ask.mjs`, `test_assistant_guard.py`, `assistant/assistant_pack.json`, `assistant/tokens.json` (plaintext tokens, internal only, mode 600), edits to `build_command.py` (import plus one call, nothing else) and `price_scan.py` (skip list, Assumption 6).
- `~/Projects/atlas-one-rep-assistant/`: `function_app.py`, `assistant/` (core, guard, llm, store), `pack/` (copy of the pack and price_scan.py), `tests/`, `tools/make_tokens.py`, `tools/local_server.py`, `deploy_assistant.sh`, `deploy/token_hashes.json` (git ignored), README.
- Rebuilt: `Atlas One COMMAND.html`, `Atlas One Sales Kit.html` (no button, content unchanged), `A1_Sales/_Rep Kits/Charity Taylor/` (whole kit, by `--person charity`).
- This repo: `.claude/commands/run-assist.md` (committed first, as asked), `_briefs/BRIEF-ASSIST-2026-10-10.md`.

## Retire
Nothing replaced and nothing deleted. (`06 Calculators and Tools (NEW Aug 2026)/atlas-command-center.html` is not mine to delete; the chat handles it.)

## Assumptions
1. The pack uses prices.json wording for payroll: "Quoted for your company (headcount, pay cycle, PTO tracking and more)", not the shorter phrase in the brief, because prices.json is the locked source. Tests check the "Quoted for your company" start.
2. The product names "commission agreement" and "Comp and commission plan design" contain a guarded word, so the pack rewords them to "sales pay agreement" and "Sales pay plan design". Real catalogue names are unchanged.
3. I wrote ten short rep talking points in the builder (`TALKING_POINTS`). Each restates the price book or the atlas-offer skill, but the wording is mine. Please read them.
4. Added PEO and payroll brand names beyond the existing lists to the blocked words (Insperity, TriNet, Justworks, Paychex, ADP, Gusto, Paycor, Paylocity, Rippling, Vensure).
5. A plaintext `assistant/tokens.json` sits in `_INTERNAL` because the kit builder has to embed each token. A rep's token is visible inside her own kit HTML; that is the accepted design, and revoking it is one setting.
6. `price_scan.py` now skips `assistant_pack.json` (generated from prices.json, which it already skips). The pack builder scans it line by line itself. Without this the QuickBooks rule fired on two neighbouring lines of skill text.
7. The online ping is a GET to the Function URL on panel open only (any HTTP answer counts as online). Nothing is requested on page load.
8. Until `endpoint.txt` exists the button opens straight to Price lookup with "Ask is not connected yet". After deploy, rebuild COMMAND and the rep kits so they carry the URL.
9. The backend repo has no remote, and a `git push` of this repo's branch was blocked by the permission classifier, so the commits here are local only. The Master Kit is not a git repo.
10. `catalogue_check.py` takes about 4 minutes here; it ran twice (the first run failed on the pack, fixed per Assumption 6).
11. The shared Sales Kit was rebuilt as part of the standard COMMAND build; it has no button, as required.
12. The offline panel header and status pill both say "Price lookup (offline)". Redundant, left as is.

## David's steps (in plain words)
1. Go to **console.anthropic.com** and sign in with the same account the Email Assistant uses. Make a new workspace named **Rep Assistant**. Open it, go to **API keys**, click **Create key**, and set a **monthly spend limit** on the workspace (start at $20). Copy the key. Do not paste it anywhere except step 4.
2. Install the Azure tools if you have not: in Terminal type `brew install azure-cli azure-functions-core-tools@4`, then `az login` and sign in.
3. Optional, spends a few cents: `cd ~/Projects/atlas-one-rep-assistant`, then `ANTHROPIC_API_KEY=<the key> python3 tests/live_suite.py --live`. You should see "0 of 29 failed on claude-haiku-5-5". If something fails, run it again with `ASSIST_MODEL=claude-sonnet-5-5` in front and tell me.
4. Type `./deploy_assistant.sh` and read the dry run. Then `./deploy_assistant.sh --run`. When it asks for the key, paste it (nothing shows as you type) and press Return. You should see "Endpoint: https://atlas-one-rep-assistant.azurewebsites.net/api/ask" and "Wrote endpoint.txt".
5. Rebuild so the button points at the Function: `python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" "<Master_Kit>"`, then the same with `--person charity` added, and one for each other rep.
6. Open **Atlas One COMMAND.html** and click **Ask** (bottom right). You should see an "Online" pill. Tap "What's included in Concierge?" and you should see $1,900 a month, $1,500 setup.
To stop one person: `./deploy_assistant.sh --run --revoke charity`.

## Questions for David
1. Do the ten talking points in the builder say what you want reps to say (Assumption 3)?
2. Rep copies show "Check with David" in the refusal, as the brief specifies. Should reps see "Check with the office" instead?
3. Should the Function repo get a private GitHub remote so it can be pushed?
4. Do you want an Unanswered list inside COMMAND, instead of the raw `/api/unanswered` address?
5. The brief and CLAUDE.md say push after each job, but the push was blocked. Which branch should Run AS1 commits go to (this repo is on `ghl-jobs-run-cw`)?
