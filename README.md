# Atlas One — branded intake forms

Static hosting for the two approved branded intake forms. Both POST submissions to the
Atlas One GoHighLevel inbound webhook (location `AzTPxnK2vSUj19jYoDmR`), so leads land in the CRM.

- `peo/` — Quote & Onboarding Intake (PEO / HR / payroll / benefits / WC / insurance)
- `bookkeeping/` — Accounting, Bookkeeping & Payroll service request
- `email-assistant/` — AI Email Assistant setup intake, for a client who has already signed
- `help/` — AI Email Assistant client help page, every question with a search box

Source of truth for these files:
`Atlas_One_Master_Kit/12 GHL Setup doccs/Branded Intake Forms/`

To update: edit the source HTML, copy over `peo/index.html` / `bookkeeping/index.html` /
`email-assistant/index.html`, commit, push. GitHub Pages redeploys automatically.

`help/index.html` is the exception: **do not edit it, and do not copy it by hand.** It is
generated from `docs/client/FAQ-and-troubleshooting.md` in the `atlas-one-ai-email-assistant`
repo. Run `./.venv/bin/python tools/faq_html.py --yes` there with this repo checked out
beside it and it writes this copy in the same run; `tests/test_clientfaq.py` in that repo
fails if the two are not byte for byte identical. Then commit and push here to publish it.

`email-assistant/` and `help/` are deliberately NOT linked from the root `index.html`, the
same way `census/` is not. That page is the public list a prospect picks from, and neither
of these is for a prospect: the setup intake goes to a client who has already signed, and
the help page is linked from inside the assistant's own queue.
