# Atlas One — branded intake forms

Static hosting for the two approved branded intake forms. Both POST submissions to the
Atlas One GoHighLevel inbound webhook (location `AzTPxnK2vSUj19jYoDmR`), so leads land in the CRM.

- `peo/` — Quote & Onboarding Intake (PEO / HR / payroll / benefits / WC / insurance)
- `bookkeeping/` — Accounting, Bookkeeping & Payroll service request

Source of truth for these files:
`Atlas_One_Master_Kit/12 GHL Setup doccs/Branded Intake Forms/`

To update: edit the source HTML, copy over `peo/index.html` / `bookkeeping/index.html`, commit, push.
GitHub Pages redeploys automatically.
