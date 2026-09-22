# BRIEF-GHL-JOBS (current run: Run CE, 2026-09-22). Two line contact footer, people.json with Charity Taylor, rep kits, Sending as picker, passphrase removed.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run: make the reasonable call, log it, batch anything left to the end of the report. No sends, no deploy,
no spending. Deleting is a move into `_to_delete/superseded-2026-09-22/`. No dashes in anything a client or
prospect reads. Log as you go to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with
`_BUILD-LOG/RUN-GHL-JOBS-report.md`. Screenshots to `_briefs/assets/run-CE-jobs/` in the intake forms repo.

Written by Cowork (chat A1 GHL Jobs) after auditing the files on disk on 2026-09-22. Decisions behind it are
David's and are recorded in `claude/contact-footer-and-rep-standard-2026-09-22.md` and
`claude/sales-rep-setup-and-signatures-2026-09-22.md`. Do not re ask them.

Paths. Master Kit = `.../2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit`.
A1_Sales = `.../2. Atlas 1 Solutions Marketing/A1_Sales` (beside HR_Docs, not inside it). INTERNAL =
`Master_Kit/_INTERNAL (do not share)`. Repo = `~/Projects/atlas-one-intake-forms`.

## What the audit found (so you do not rediscover it)

1. `INTERNAL/contact.json` exists from Run CD with roles `sales` (David), `support` (company) and `rep: null`.
   `build_command.py` reads it through `load_contact(role)` at line 42, and the only call is line 1372
   (`load_contact("support")` for the Sales Kit hero line). Nothing else reads it yet.
2. Zero pages anywhere carry an `a1-footer` class today. Every footer is hand typed and varies.
3. `build_command.py` takes the Master Kit path as `sys.argv[1]` with no argparse, so `--person` needs a real
   argument parser that keeps the positional path working exactly as today.
4. The Sales Kit inlines each tool's raw HTML as a blob. Those blobs carry David's footer baked in. So a rep kit
   is NOT a rep kit just by changing the hero line: the person line inside every inlined blob must be swapped at
   build time. That is why the `a1-footer-person` class has to land on every piece first (Job 2) before Job 3.
5. COMMAND renders pages two ways, both with `document.write` into a fresh iframe: the Preview pane (around
   line 939) and the Present runner `renderFramePage` (around line 1185, which already injects
   `<style>.brandbar{display:none !important}</style>`). Job 4 must hook BOTH paths.
6. `catalogue.py` line 13 is `INTERNAL_PASSPHRASE = "atlas1"`. The build already does
   `lock_internal = bool(INTERNAL_PASSPHRASE)`, so None removes the gate with no other code change.
7. Source generators that exist: division sheets `INTERNAL/tools/division_sheets_build_2026-09-12.py`; the
   Software and Microsoft 365 one pagers `_BUILD-LOG/software-licenses-src-2026-09-16.tgz`; industry overlays and
   the benefits menu in the prospecting kit build tree (`_BUILD-LOG/prospecting-kit-src-*.tgz`, newest first; if
   `build_benefits.py` is not in any tgz, find it on disk before concluding it is gone). For any other piece,
   search for its generator before editing the HTML by hand. A hand edited HTML with a live generator gets
   overwritten on the next build, so edit the source whenever one exists, then regenerate.

## Job 1: people.json replaces contact.json, with Charity Taylor

Create `INTERNAL/people.json` exactly like this (keep the `_source` note style Run CD used):

```
{
  "_source": "Run CE 2026-09-22. One file for every contact line on every piece. The GoHighLevel user record owns who a deal belongs to; this file is the print copy. Name, title, email and phone must match the GoHighLevel user. Add a rep here and in GoHighLevel in the same sitting.",
  "company": {
    "name": "Atlas One Solutions",
    "support_email": "support@atlasonesolutions.com",
    "phone": "380-225-5217",
    "phone_display": "380-CALL-A1S (380-225-5217)",
    "site": "AtlasOneSolutions.com"
  },
  "people": {
    "david": {
      "slug": "david", "name": "David Taylor", "title": "Founder",
      "email": "david@atlasonesolutions.com",
      "phone": "380-225-5217",
      "phone_display": "380-CALL-A1S (380-225-5217)",
      "booking": "https://api.leadconnectorhq.com/widget/groups/book-david",
      "default": true
    },
    "charity": {
      "slug": "charity", "name": "Charity Taylor", "title": "Business Advisor",
      "email": "charity@atlasonesolutions.com",
      "phone": "801-787-8154",
      "phone_display": "801-787-8154",
      "booking": null,
      "default": false
    }
  }
}
```

Rules for the loader (one function, `load_people()`, in a small shared module `INTERNAL/people.py` that every
generator imports, so there is one reader and not six):
- `sales` resolves to the default person and `support` resolves to the company block, so every Run CD call
  keeps working. Keep `load_contact(role)` as a thin wrapper over it.
- Exactly one person may carry `default: true`; the loader hard fails otherwise.
- A null `booking` means the person line leaves out Book a time entirely. Never fall back to David's booking
  link on someone else's line (that would book David). Charity has no calendar yet.
- Move `contact.json` to `_to_delete/superseded-2026-09-22/` once nothing reads it (grep the Master Kit, the
  repo and the email assistant repo for `contact.json` first and list every hit in the report).

## Job 2: the standard footer, one snippet, every piece

One function in `people.py`, `footer_html(person_slug=None)`, returns:

```
<footer class="a1-footer">
  <div class="a1-footer-person">Name, Title · email · phone · <a href="booking">Book a time</a></div>
  <div class="a1-footer-company">Atlas One Solutions · support@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · AtlasOneSolutions.com</div>
</footer>
```

Emails and booking are real links (mailto, tel, https), on descriptive text, never a bare URL. Styling: brand
colors only (navy text, periwinkle rule above, off white or soft blue ground), DM Sans, small, prints on the
page. The class names are the contract, the styling is not: Job 3 and Job 4 find `a1-footer-person` by name.

Put it on these, replacing whatever contact block each has now (audit list from 2026-09-22, every one has
zero `a1-footer` today):
- Division sheets (six): Payroll HR, Benefits Retirement, Financial Services, Risk Insurance, Technology
  Operations, Business Consulting. Through `division_sheets_build_2026-09-12.py`, HTML and PDF regenerated.
- Industry overlays 01 to 06 in `A1_Sales/Industry Playbooks/`. Through the prospecting kit source. The
  Cornerstone brand toggle on these pages must keep working: when toggled to Cornerstone, the footer is the
  Cornerstone block they carry today, untouched (partner brand material keeps its own number).
- `A1 What we do Overview/Atlas_One_Services_Overview.html` and `Atlas_One_Partner_Client_Program_PPG.html`.
- `AI Services and Assistants/`: AI Task Agent, AI Email Assistant, Background Screening one pagers.
- `Proof & Case Studies/Atlas_One_Proof_Sheet.html`.
- `Atals 1 Membership Pricing/`: Membership Pricing and Membership Brochure.
- `Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html` (through `build_benefits.py`; footer only, no LTD
  row in this run, see Job 7).
- `Total Impact Model/Atlas_One_Total_Impact_Model.html` (through `build_tim.py`).
- `Atlas 1 Bookkeeping/`: Bookkeeping Marketing Sheet V8 and QuickBooks Accountant Access Guide.
- `Client Portal/Atlas_One_Client_Portal.html` and `Atlas_One_Client_Dashboard_GHL.html`.
- `Pricing/Atlas_One_Price_List.html` ONLY if its catalogue audience is prospect or client. If internal, leave it.
- `Atlas 1 Software and Licenses/Atlas_One_Software_and_Licenses_OnePager.html` and
  `Atlas_One_Microsoft_365_OnePager.html`: these go BACK to David on the person line (Run CD swept them to
  support@ on the tool footer rule; they are sales material he hands over and the first is in the 45 and 60
  minute Present playlists). Through `software-licenses-src-2026-09-16.tgz`, PDFs regenerated.
- Every PDF that has one of these as its source is regenerated in the same run from the same source.

Leave these alone, and say so in the report:
- The two Software Marketplace Sheets and `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_AI_Email_Assistant_Help.html`
  (website and help bound, company only, already support@).
- `Dr Gould Dental/` (sent client emails, prospect folder), `Email Templates/`, `Website/.../Email_to_Thomas_*`,
  the BRJ Pricing Page SPEC, the Blog Set (website paste, the CMS carries its own footer), the WSA Audiology
  Partnership Plus folder (partner brand), and the two internal playbooks (not prospect facing).

Public pages on forms.atlasonesolutions.com (the repo copies of what we do, census, self assessment, time
savings, vendor audit, retention cost): these are found by a stranger, not handed over by a person, so they
carry the company line plus a Book a time link to the group booking link, and no person line. That is
Cowork's call on a conflict between two recorded decisions ("both lines always" and "support@ is right for a
public page"); record it in the report so David can overrule it.
- Specifically the Run CD carry over: `tools/what-we-do/index.html` in the repo still has the old contact while
  the Master Kit copy `06 Calculators.../Atlas_One_Everything_We_Handle.html` was changed to support@. Bring the
  repo copy in line with support@ and the company footer, and give the Master Kit copy the same footer so the
  two match again. Regenerate `A1_Sales/Atlas_One_Everything_We_Handle.pdf` from it. Commit and push the repo.

Generators: make each of these read the footer from `people.py` rather than a literal, where the file exists:
`build_command.py`, `build_tim.py`, `build_audit_report.py`, `service_deck.py`, the agreement and packet
generators, the cadence email wrapper. The two decks (`service_deck.py` output and any pptx) keep a one line
contact because a slide has no room for two; use the company line on decks. Office files with no source are
David's per rule 37: list them, do not edit them.

Report a before and after table: file, old contact, new person line, company line present yes or no.

## Job 3: the rep kit generator, proven on Charity

`build_command.py` gains an argument parser: positional Master Kit path (unchanged behaviour) plus
`--person <slug>` defaulting to the default person. Running it with no flag must produce the same two files it
produces today apart from the footer change and the build stamp.

With a non default slug it builds ONLY the rep kit, not COMMAND, into
`A1_Sales/_Rep Kits/<Person Name>/`:
- `Atlas One Sales Kit (<Person Name>).html`, through the existing Sales Kit call with
  `audience={"prospect","client"}`, `zone_filter={"Sales Kit","Tools"}` and `exclude_internal_path=True`
  unchanged, and the forbidden term check on and a hard stop.
- Before each blob is inlined, replace the inner HTML of its `a1-footer-person` element with that person's
  line. A blob that should have a person line and does not is a build failure naming the file, not a silent
  skip (rule 5, never drop a record silently). The company line is never touched.
- The hero line reads "Shared by <Person Name>, Atlas One Solutions. Call <person phone_display>."
- The same run writes that person's own copies of the standalone one pagers and division sheets (HTML and
  PDF) from the Job 2 list into the same folder, generated through their sources with the person slug, never
  by string replacing a finished PDF.

Prove it on the real rep, `charity`, not a demo slug: build her kit, then check it carries her footer
(Charity Taylor, Business Advisor, her email, 801-787-8154, no Book a time link since her booking is null),
zero Internal zone rows, zero Present markup, and grep it for the six forbidden terms and for the word margin
outside CSS. Leave the folder in place. Put a plain text file beside it, `READ ME FIRST.txt`: "Built
2026-09-22. Do not hand this to Charity until her Microsoft 365 mailbox charity@atlasonesolutions.com exists
and her GoHighLevel user is set up, or replies to her email bounce."

## Job 4: Sending as picker in COMMAND

A select in the COMMAND header beside `#themetoggle`, listing every person in `people.json` by name, default
David, remembered in `localStorage` inside try and catch. Whatever COMMAND renders through the Preview iframe
AND through `renderFramePage` gets an injected rule hiding `.a1-footer-person` plus a replacement person line
for the selected person. The company line is never hidden or swapped. The picker lives in the COMMAND build
only; the Sales Kit and any rep kit carry no picker.

## Job 5: remove the Internal passphrase

`catalogue.py`: `INTERNAL_PASSPHRASE = None`, keeping the comment above it and adding one line saying a string
puts the curtain back. Confirm the build prints "(none, curtain removed)", the Internal tab opens with no gate,
and the AI Email Assistant Approval Queue, Activity log and Tasks and Follow ups are each one click away.
Confirm the built Sales Kit still carries no Internal zone.

## Job 6: rebuild and verify

Run `catalogue_check.py`, then rebuild COMMAND and the Sales Kit with the Master Kit path, then Charity's kit.
Headless Chromium at 1440, 1024 and 390:
- every COMMAND zone still scrolls to its last row, all eight Present playlists run end to end;
- the footer renders two lines on ten sampled pieces (at least two division sheets, one overlay in each brand
  position, both software one pagers, the benefits menu, the proof sheet);
- the Sending as picker swaps the person line to Charity and back in Preview and in Present, and the company
  line is identical in every screenshot;
- Charity's kit passes the checks in Job 3.
Commit and push the repo copies touched in Job 2. Deploy nothing.

## Job 7: LTD row on the Employee Benefits Menu. SKIP in this run.

David sells long term disability and every ancillary line (confirmed 2026-09-22). The job to add the LTD row
through `build_benefits.py` stays gated on David supplying the LTD carrier and starting rate. He has not
supplied them as of this brief, so do nothing on it: no invented carrier, no copied STD rate, no empty row.
Say "Job 7 skipped, no LTD carrier or rate supplied" in the report.

## Not in this run

- Charity's GoHighLevel user, the assigned user merge fields in email signatures and the reply to on email
  steps: that is the GoHighLevel browser, the GHL terminal's job.
- Charity's Microsoft 365 mailbox: David buys the licence.
- The Health Quote Census v3 columns: queued as Run CF in `BRIEF-GHL-JOBS-queued-census-v3.md`, next run.

## Report must include

Before and after footer table; every generator changed; every file left alone and why; the `contact.json`
grep hits; Charity kit checks with the grep output; screenshot list; the public page footer call flagged for
David; Office files with no source for David; any question batched at the end.
