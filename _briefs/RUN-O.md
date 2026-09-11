# Run O: client status review and suppression gate

## Part 1 (terminal B, 11 Sep 2026): DONE

### What was exported

Every contact in location `AzTPxnK2vSUj19jYoDmR`, pulled by API with `POST /contacts/search`
paged 100 at a time using `searchAfter`. **2,136 contacts**, which matches the `total` the API
reports and the figure in the brief.

Written to `_briefs/assets/run-O/contacts-review.xlsx` and copied to OneDrive at:

```
~/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/_BUILD-LOG/2026-09-11-contacts-review.xlsx
```

### Workbook layout

**Sheet 1, Contacts.** One row per contact, sorted by Company then Last name, header frozen,
autofilter on. Columns:

| Column | Source |
|---|---|
| Company | `businessName`, falling back to `companyName` (359 contacts have one, 1,777 do not) |
| First, Last, Email, Phone | contact fields |
| Tags | comma joined |
| Lead Source | `source`, falling back to the HubSpot "original source" custom field the import carried |
| Vertical | custom field `gZn8B7wJU1zXDuKYrNoi` (no contact has it set today, so the column is blank) |
| Membership Tier | any custom field whose value is Essential, Professional, Enterprise or Concierge (none set today) |
| Date added | `dateAdded`, date only |
| **Client status** | fill column, dropdown: Current client, Former client, Prospect, Referral partner, Vendor, Personal, Delete |
| **Brand** | fill column, dropdown: Cornerstone, G&A, Vero, Atlas One, None |
| **Services** | fill column, free text (PEO, Payroll, Benefits, WC, Bookkeeping, Other) |
| **OK to prospect** | fill column, dropdown: Yes, No |
| GHL contact id | so part 2 can write back without matching on email (1,237 contacts have no email) |

The four fill columns are shaded soft blue `#DBE4ED`. Data validation is on each dropdown.

**Pre-fill.** Client status was set to Current client for any contact tagged `client`,
`current-client` or `cirque`, or with a Membership Tier value. **Zero contacts matched.** The
whole location carries only four tag values today (`reply received`, `intake-received`,
`form-a-sent`, `form-b-sent`, on six contacts) and no membership tier has been written yet, so
every Client status cell is blank for David to fill.

**Sheet 2, Companies.** One row per distinct Company (268) with a contact count, plus a final
row for the 1,777 contacts with no company on record. Same four fill columns and dropdowns so
David can mark a whole company at once. Part 2 applies a company row to every contact with
that Company, then lets a filled Contacts row override it.

**Sheet 3, Email domains.** Added because 83 percent of the import has no company name. One
row per email domain (332), contact count, a flag for free mail providers (gmail, yahoo and
so on), and the same four fill columns. Part 2 treats a filled domain row exactly like a
company row: it applies to every contact at that domain unless the Contacts row says
otherwise. Free mail domains should be left blank.

### Facts about the data worth knowing before filling it in

- 2,109 of 2,136 contacts came from a single HubSpot **IMPORT** on 3 Sep 2026.
- 1,237 have no email, 849 have no phone. Contacts with no email cannot use the client portal
  (Run N) until an email is added in GHL.
- The five `companyName` values are `Test 007`, `vfdz`, `abcd` and `HubSpot` twice; the real
  company data lives in `businessName`.
- Three `Seed` test contacts remain (`seed-a@`, `seed-d@`, `david+seedb@`); mark them Delete.
- `GET /locations/{id}/customFields` is out of scope for the Private Integration key (401),
  which is why Vertical and Membership Tier are matched by observed id and value rather than
  by field key. Adding the scope **View Custom Fields** (`locations/customFields.readonly`)
  in Settings > Private Integrations would let part 2 resolve every field by key.

## Part 2 (terminal A, later): NOT STARTED, do not run in terminal B

Input: the filled workbook (David saves it in place in `_BUILD-LOG` or hands the path over).

### 1. Resolve each contact's status

Precedence, highest first: Contacts row, then Companies row for that Company, then Email
domains row for that domain. Blank everywhere means no change. `Delete` rows are listed in the
report for David to confirm before any `DELETE /contacts/{id}` call is made.

### 2. Write back to GHL by API, by contact id

| Client status | Tag to add | Client Status field |
|---|---|---|
| Current client | `client-current` | Current client |
| Former client | `client-former` | Former client |
| Referral partner | `partner` | Referral partner |
| Vendor | `vendor` | Vendor |
| Prospect | none | Prospect |
| Personal | `do-not-prospect` | Personal |
| Delete | none, reported for confirmation | |

`OK to prospect = No` adds `do-not-prospect` regardless of status. Brand writes the existing
`Brand Identity` dropdown when the value is Atlas One or Cornerstone; G&A and Vero need two
options added to that field first (Settings > Custom Fields, GHL will not let the API add
options). Services writes the `Services` custom field (create as Multi line if it does not
exist, folder Client). `Client Status` is a new Dropdown (single) field with the seven values
above, folder Client. Remember GHL lowercases tag names on save.

Tags to create first at Settings > Tags: `client-current`, `client-former`, `partner`,
`vendor`, `do-not-prospect`.

### 3. Suppression gate on the prospecting workflows

Add as the **first action** after the trigger in each of **W2 Warm referral, W3 Trigger
sequence, W3a Renewal calendar, W4 Cold cadence, W7 WSA handoff (Cornerstone)** and
**Tool-Lead Nurture**:

If/Else "Suppress clients and partners": branch **Suppressed** when
`Tag` Is `client-current` **OR** `do-not-prospect` **OR** `partner` (three conditions in one
branch, OR between them; note from Run J that the OR pill is not a toggle, add each condition
with the OR selector). Suppressed branch: **End workflow**. None branch: the existing sequence.
Publish each one after the edit and confirm the Status column reads Published.

W6 Suppression and caps already ends on `dnc` and `not interested`; leave it alone, the new
gate is per workflow so a current client never enters the sequence in the first place.

### 4. Smart lists

- **Current clients**: Tag Is `client-current`.
- **Prospectable**: Tag Is Not `client-current` AND Tag Is Not `do-not-prospect` AND Tag Is
  Not `partner` AND Tag Is Not `dnc` AND Email Is Not Empty. Build the ANDs as one filter
  group; the top level between groups is OR.

### 5. Report

Append a "Part 2" section here with counts per status, the tags applied, the field values
written, the Delete list awaiting confirmation, and screenshots of each gate and both smart
lists under `_briefs/assets/run-O/`.
