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

## Part B. "Call: not now" workflow

_in progress_
