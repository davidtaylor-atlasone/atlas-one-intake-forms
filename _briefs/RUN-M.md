# Run M

## Part A. /tools index page: PASS

`https://forms.atlasonesolutions.com/tools/` returned the GitHub 404 page because the
directory had three tool subfolders and no `index.html`. Added `tools/index.html`.

### Verified live

| URL | Status | Size |
|---|---|---|
| `https://forms.atlasonesolutions.com/tools/` | **200** | 397,241 b |
| `https://forms.atlasonesolutions.com/tools/retention-cost/` | **200** | 420,307 b |
| `https://forms.atlasonesolutions.com/tools/vendor-consolidation/` | **200** | 407,428 b |
| `https://forms.atlasonesolutions.com/tools/wc-premium-check/` | **200** | 17,833 b |

The size of the index matches the file byte for byte, so the deploy is the file that was
pushed and not a cached 404.

### How it is built

Self contained, **zero CDN calls**. Everything the page needs is already in the repo and was
reused verbatim rather than re-sourced:

- **Fonts.** `tools/retention-cost/index.html` already carries three `@font-face` blocks with
  the font binaries embedded as base64 truetype: **Horas** (weight 400 to 700) and **DM Sans**
  at 400 and 700. All three were copied across unchanged. Horas sets the h1, DM Sans sets
  everything else. This is what makes the page 397 KB, the same order as its sibling tool
  pages, and it is the price of not calling Google Fonts.
- **Logo.** The periwinkle laptop mark is the same `data:image/svg+xml;base64` image already
  embedded in the two branded tool pages, copied across unchanged.
- **Brand colours** as specified: `#23304D` navy, `#788DE3` periwinkle, `#FAFAF8` off white,
  `#DBE4ED` soft blue.
- **Phone width first.** Single column by default, three columns only above 700 px.

### Content

Title **Free business calculators**. Three cards, each one sentence of value, no prices, each
with an **Open the calculator** button on a relative path:

| Path | Card heading |
|---|---|
| `retention-cost/` | What does turnover really cost you? |
| `vendor-consolidation/` | How many vendors are you paying? |
| `wc-premium-check/` | Is your workers comp premium right? |

Footer carries **One Call Solves Everything.** and the 15 minute intro link
`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`.

**No dashes anywhere in the copy.** The only hyphen in visible text is the phone number
385-213-7177. Checked by stripping tags and scanning for hyphen, en dash and em dash.

Commit `174d262`.

## Part B. "Call: not now" workflow: BLOCKED at step one

**The workflow was not created.** Automation > Workflows > **Create workflow will not open its
menu**. The button highlights on click but the dropdown (Start from Scratch, Build Using AI,
Select from Template, Import from a campaign, Company based workflow) never renders.

Tried, all with the same result:

1. Click at several points across the button.
2. Hover first, then click, so a `mouseenter` fires before `mousedown`.
3. Click with no wait, 1 s, 2 s, 3 s, 4 s, 6 s and 8 s before the screenshot.
4. Full page navigation back to the workflows list, twice.
5. The Dashboard round trip prescribed for this run, then straight back to Automation.
6. Window resize to 1440 wide (the captured viewport stayed 1317, so the app never reflowed).
7. Click then **Down then Return**, in case the menu was rendering clipped and only the
   keyboard could reach it.

`find` cannot see the button in the accessibility tree either: the workflows list renders
inside a nested frame and only generic regions are exposed, which is consistent with the menu
being rendered into a portal that is clipped or detached.

**The same menu worked about an hour earlier in this session**, at viewport width 1372, when
the scratch workflow for W-PAY-3 was created. Nothing about the account changed in between.
GHL's "click here to refresh" link was never used, per the run rules.

**I did not use the workarounds that were available**, because each leaves debris in a live
account: cloning a Booking workflow and gutting it, or repurposing the unfinished W-PAY-3
draft. Neither is worth doing without David saying so.

### What did get done

**The `not-now` tag exists.** Created at Settings > Tags on 11 Sep 2026 01:52 PM and confirmed
in the list. Tag count went 25 to 26. That screen's Create button works normally, which is
what makes the workflows page failure look specific rather than account wide.

`not-now` has been added to the tag list in `_briefs/RUN-G-checkpoints.md`.

### Still to do, all of it

Workflow **"Call: not now"**, trigger Contact Tag Added `not-now`, then: send the branded email
(subject `Thanks for the time today, {{contact.first_name}}`, body as specified, no dashes,
text signature, from David@AtlasOneSolutions.com), add tag `hold 6m`, remove tags `booked` and
`sequence active`, update Opportunity stage to Closed Lost with reason "Not now" if one exists,
wait 90 days, create the check in task for David. Then publish and run the live test with the
wait temporarily set to 1 minute.

The email body is already written in the run brief and the branded wrapper technique is
recorded in `RUN-L-payments.md`: clone `P-C-0 Instant reply`, then replace the body by putting
the HTML on the clipboard with `navigator.clipboard.writeText` and pasting into the code pane,
because the editor is a cross origin iframe.
