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

## Part B. "Call: not now" workflow: BLOCKED, cause found

### Root cause: the Chrome window is hidden, so mouse clicks never reach GHL

Every GHL screen renders inside an **out of process iframe**. The workflows list is
`client-app-automation-workflows.leadconnectorhq.com` inside `app.ridethehightide.com`; the
builder is the same frame; the email editor is another one nested inside that.

The page reports:

```
document.hasFocus()        true
document.visibilityState   "hidden"
document.hidden            true
```

A hidden page still runs script and still accepts **keyboard** events, because those go to
whatever frame holds focus. It does not produce compositor hit test data, and browser side
mouse routing into an out of process iframe depends on that hit test data. So every click
aimed at a GHL screen is swallowed silently. Clicks on the **outer** page still work, which is
why collapsing the left sidebar worked all along and made this look like a GHL bug.

Proved it four ways, all on the workflows list, all no ops:

| Test | Expected | Actual |
|---|---|---|
| Click the row checkbox | ticks | nothing |
| Click a workflow name | opens the builder | nothing |
| Click the Search box and type | filters the list | nothing typed |
| Scroll the list | list scrolls | nothing |

And the outer page is fine: a probe overlay on the parent document recorded clicks at
(615,79), (200,400), (1300,700) exactly as sent, so the coordinates are right and the events
are real. They just stop at the iframe boundary.

**The fix is one click by David: bring the Chrome window to the front.** It is minimised or
fully covered. I cannot do it myself, `osascript` and `open` are off limits for this session.

### What the keyboard route did achieve

Keyboard still reaches the frame, so the escalation ladder was worked to the end:

1. Fresh tab, straight to Automation > Workflows, one click on Create workflow: **failed** (as
   above, no click reaches the frame).
2. Direct builder URL with a fresh UUID: **failed**, "Workflow not found". There is no blank
   builder URL, the id has to exist first.
3. Clone "Booking: no show" from the row menu: **failed**, the row menu is a click too.

Then, driving the frame by keyboard only (focus the iframe from the parent with
`iframe.contentWindow.focus()`, then Tab and Return):

- **The Create workflow menu is not broken.** Tab six times from the top of the frame lands on
  it; Return opens it and all five items render. Down then Return picked **Start from Scratch**.
- That created a real blank workflow: **`ff950be3-829d-4a51-8f9a-825db660796e`**, named
  `New Workflow : 1789164293568`, status Draft, saved.
- The Add trigger panel opens the same way and its search box accepts typing.

**This one empty draft is the only thing left behind.** Nothing was cloned, renamed or
deleted. It becomes "Call: not now" as soon as the window is visible; if David would rather
start clean it is a one line delete from the workflows list.

Building the rest blind, by counting Tab presses through a canvas, five action dropdowns and a
nested cross origin email editor that needs a clipboard paste into a code pane, is not worth
the risk of a wrongly configured live automation. Stopping here.

### What did get done

**The `not-now` tag exists.** Created at Settings > Tags on 11 Sep 2026 01:52 PM and confirmed
in the list. Tag count went 25 to 26, and it is recorded in `_briefs/RUN-G-checkpoints.md`.

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
