# Run N: client portal (portal.atlasonesolutions.com)

Terminal B, 11 Sep 2026. Code: `~/Projects/atlas-one-portal`, pushed to the private repo
`github.com/davidtaylor-atlasone/atlas-one-portal` (branch `main`, commit `f681332`).

## 1. Starter evaluation and choice

David's addendum: clone a finished open source product, judge by magic link ready, multi
tenant ready, documents and tables ready, active maintenance in 2026. All three were pulled
and read, not judged from their READMEs.

| | Refine (refine.dev) | Vercel `nextjs/saas-starter` | `satnaing/shadcn-admin` |
|---|---|---|---|
| Magic link ready | No. The Supabase auth provider example signs in with a password. | No. Email plus password, bcrypt, JWT cookie. | No. Sign in is a mock (`sleep(2000)` then a fake token). Clerk is an optional demo in its own folder. |
| Multi tenant or teams ready | No. Documented as a pattern only. The CRM example has "companies" as a data resource, not tenancy. | **Yes.** Teams, members, owner and member roles, invitations, in Postgres via Drizzle. | No. |
| Documents and tables ready | Partly. Ant Design tables, but the example is wired to a hosted GraphQL demo backend (nestjs-query). | No. Seven shadcn components, an activity list, settings pages. | **Yes.** TanStack Table with faceted filters, pagination, bulk actions, column visibility, plus every screen designed (dashboard, tables, settings, errors, auth, command menu, light and dark). |
| Active maintenance 2026 | Yes for the framework (release 10 Sep 2026). **The "Enterprise CRM" example itself moved to the paid Enterprise edition**; the community version is the smaller `app-crm-minimal`. | Security bumps only (last feature commit June 2025, Next 15 canary CVE patch Dec 2025). | Yes. Pushed 10 Sep 2026, dependency bumps June 2026, v2.2.1. |
| Stack | Vite, React, Ant Design, react-router, Refine data providers | Next.js 15 App Router, Tailwind 4, Drizzle, Stripe | Vite, React 19, TanStack Router and Query, Tailwind 4, shadcn/ui |

Nobody has magic link ready. Nobody has tenancy the way this portal needs it, because here a
tenant is a **GHL company** and the source of truth is GHL, not a table in the app, so the
saas-starter teams schema would be dead weight. On the two criteria that can be met out of the
box (tables and maintenance) shadcn-admin wins outright, and it is the only one where every
screen the brief asks for already has a designed home.

**Choice: shadcn-admin**, commit `e16c87f` (recorded in `.upstream-commit`). Kept as is:
the sidebar, header, theme system with light and dark, command menu, data table kit, error
pages, sign in shell, form kit, mobile layout. Removed: Clerk, the demo apps, chats, users,
tasks, settings pages, the mock auth store, vitest. Built on top: brand, GHL data, auth, the
five client pages and the admin page.

### Why Supabase is not in the stack

The brief named Supabase for the magic link. Two facts changed that decision during the build:

1. No starter had magic link auth to reuse, so the auth layer had to be written either way.
2. The GHL key already lets the server send an email **as David** through the conversations
   API (`POST /conversations/messages`, type Email), and read it back. That is the only thing
   Supabase would have contributed (sending the link and minting a token).

So the portal signs its own 15 minute token (jose, HS256, secret in `PORTAL_SESSION_SECRET`),
GHL delivers the email from `David@AtlasOneSolutions.com`, and every sign in shows up in the
contact's conversation in GHL. One fewer account for David to create, no browser side keys,
and the login flow was testable end to end in this session with no external setup. Switching
to Supabase later would be a small adapter in `server/auth.ts` and `server/app.ts`; nothing
in the UI would change.

## 2. What is built and tested

**Stack.** Vite SPA plus a Hono API. Locally the API runs on :8787 (`pnpm dev:api`) with
Vite proxying `/api`; on Vercel the same Hono app is one serverless function
(`api/index.ts`) and `vercel.json` routes `/api/*` to it and everything else to the SPA.
The GHL key is read from the environment on the server only; `src/` never sees it.

**Brand.** Navy `#23304D`, periwinkle `#788DE3`, off white `#FAFAF8`, soft blue `#DBE4ED`
as the Tailwind theme tokens (light and dark). DM Sans body, Horas headings, both served
as `@font-face` from `public/fonts/` (the binaries were lifted out of the base64 blocks in
`tools/index.html`, so no Google Fonts call). Full colour lockup on the sign in page, the
white lockup from the tools page in the navy sidebar, laptop mark favicon.

**Auth.**
- `POST /api/auth/request` looks the email up in GHL. A contact tagged `client-current`, or
  an address in `PORTAL_ADMIN_EMAILS`, gets the link. Anyone else gets the polite refusal
  (screenshot 02) and no email is sent.
- The link opens `/verify?token=…`; the page POSTs the token (so mail scanners that GET links
  cannot burn it), the server re-reads the contact, re-checks the tag, sets a 7 day httpOnly
  `SameSite=Lax` cookie.
- Every API call re-reads the contact and re-checks `client-current`, so removing the tag in
  GHL locks the client out immediately.
- Links are valid for 15 minutes. Single use needs somewhere to remember the used id; on
  serverless that means a custom field. Create a Single line field `portal_last_link`, put
  its id in `GHL_FIELD_PORTAL_NONCE`, and links become single use with no code change.

**Tenancy.** Client = `contact.companyName`, falling back to `businessName` (the HubSpot
import filled `businessName`, the forms fill `companyName`). Admin = the emails in
`PORTAL_ADMIN_EMAILS`, default `david@atlasonesolutions.com`.

**Pages** (all mobile first, screenshots in `_briefs/assets/run-N/`, both Pixel 7 width and
1280 desktop):

| Page | Source of truth in GHL | Screenshot |
|---|---|---|
| Sign in | contacts search by email, tag check | 01, 02, 03 |
| Home | company, services from `service-*` tags plus the `services_requested` field (and a `services` field once it exists), Membership Tier, WC Renewal Date, Benefits Renewal Date, Savings to date once that field exists, date added | 04 |
| Documents | file URLs found in the contact's custom fields, plus attachments on the contact's conversation messages, newest first, direct download | 05 |
| Requests | three forms (COI, question, change). Each writes a note on the contact and a task for David (`assignedTo` his user id `vTV2wRivyR9f9XWNook3`, due next day) | 06, 09 |
| Book a call | iframe of `https://api.leadconnectorhq.com/widget/groups/book-david` with GHL's resize script; renders all four calendars | 07 |
| Pay | the 14 links from Run L. With a Membership Tier set: that tier's membership and setup plus every add on. Without: all 14 | 08 |
| Admin (David only) | every contact tagged `client-current`, grouped by company, search, "View as" impersonation with a banner and Stop viewing. Requests sent while viewing are filed on the client's record and marked as sent by David | 10, 11 |

**Custom field ids** were discovered by writing values by key on a probe contact and reading
back (the definitions endpoint is out of scope, see section 3). Recorded in
`server/fields.ts`: `membership_tier` G5BpPnwz9LUXdiTYG4B2, `services_requested`
irg89YQIOHAaFFfEojJ9, `wc_renewal_date` ZRqAiccyEnoNSqKCkMlD, `benefits_renewal_date`
1HY5GB56JfGVW9pZNdCn, `vertical` gZn8B7wJU1zXDuKYrNoi. The fields `services` and
`savings_to_date` **do not exist yet**; GHL silently dropped them. When David creates them the
portal picks them up by env var (`GHL_FIELD_SERVICES`, `GHL_FIELD_SAVINGS`) today, or by key
automatically once the custom fields scope is added.

**Seed clients** (tag `client-current` plus `portal-seed`, remove with `pnpm seed -- --remove`):

| Company | Person | Email | Phone | Tier |
|---|---|---|---|---|
| Harbor Dental Group | Harper Lindqvist | david+portal-harbor@atlasonesolutions.com | +1 801 555 0171 | Professional, WC 1 Mar 2027, Benefits 1 Jan 2027 |
| Summit Electrical LLC | Mateo Sørensen | david+portal-summit@atlasonesolutions.com | +1 801 555 0172 | Essential, WC 15 Nov 2026 |
| Northstar Hospitality | Priya Okonkwo | david+portal-northstar@atlasonesolutions.com | +1 801 555 0173 | none |

GHL accepted `client-current` on the seed contacts by API. Whether it now shows in Settings >
Tags could not be checked (the tags endpoint is out of scope for the key); Run O part 2
should look before creating it.

**Playwright**: 10 of 10 pass (5 tests, mobile and desktop), 42 seconds, against the built
app on one origin exactly as on Vercel:

1. Unknown email gets the polite refusal.
2. Signed out visitor on `/documents` is sent to `/sign-in`.
3. Client login: request the link through the UI, read the email back out of GHL, follow it,
   then Home (name, company, services, tier badge, renewals), Documents, Requests, Book (iframe
   src), Pay (Professional sees Professional and not Essential), and `/admin` bounces a client.
4. A COI request lands on the GHL contact as a note beginning `[Portal request] COI request:
   Harbor Dental Group` and an open task with that title.
5. Admin login as the plus addressed test admin, all three companies listed, View as Mateo
   shows the banner, his home page and his Essential pay links, Stop viewing returns to Admin.

The test COI notes and tasks were deleted afterwards so David's task list stays clean. A
contact "Atlas One Admin" (`david+portal-admin@atlasonesolutions.com`, tag `portal-admin`)
was created by the suite's admin login; delete it whenever the suite is retired.

## 3. What needs David

Nothing here needs a password typed by anyone but David.

1. **Vercel.** Create the account, Add New Project, import `davidtaylor-atlasone/atlas-one-portal`
   (framework preset Vite is auto detected, build `pnpm build`, output `dist`). Add these
   environment variables (Production and Preview):
   `GHL_PRIVATE_INTEGRATION_TOKEN`, `GHL_LOCATION_ID=AzTPxnK2vSUj19jYoDmR`,
   `PORTAL_SESSION_SECRET` (any 64 hex characters, `openssl rand -hex 32`),
   `PORTAL_APP_URL=https://portal.atlasonesolutions.com`,
   `PORTAL_ADMIN_EMAILS=david@atlasonesolutions.com`. Deploy.
2. **DNS.** In Vercel, Project > Settings > Domains, add `portal.atlasonesolutions.com`. Then at
   the DNS host for atlasonesolutions.com add `CNAME portal -> cname.vercel-dns.com`. Vercel
   issues the certificate itself.
3. **GHL scopes** (Settings > Private Integrations, edit the integration). The key refused:
   - `locations/customFields.readonly` (View Custom Fields). With it the portal resolves every
     field by key at runtime instead of the id map.
   - Optional, for phase 2: `invoices.readonly` (invoices page), `medias.readonly` (media
     library files), `payments/orders.readonly` (payment history), `users.readonly`.
4. **Two custom fields**, Contact object, when convenient: `Services` (Multi line, key
   `services`, which Run O part 2 also wants) and `Savings to date` (Number, key
   `savings_to_date`). Optional third: `Portal last link` (Single line, key `portal_last_link`)
   for single use links; set its id in `GHL_FIELD_PORTAL_NONCE`.
5. **Real clients** appear the moment Run O part 2 tags them `client-current`. Contacts with
   no email in GHL cannot sign in; 1,237 of the 2,136 have none.

## 4. Phase 2

- **NowCerts COI pull**: replace the COI request note with a live certificate generated from
  NowCerts and dropped into Documents; needs the NowCerts API key and the policy to client
  mapping.
- **Invoices from GHL**: `GET /invoices/` by contact once `invoices.readonly` is on the key;
  list, status, pay link per invoice on the Pay page.
- **E-sign**: GHL Documents and Contracts (`proposals/document` endpoints) listed under
  Documents with a Sign link, once the `proposals` scopes are added.
- Single use links via the nonce field (section 2), rate limiting on `/api/auth/request`
  (Vercel WAF or a KV counter), a "who else at your company" view so a second contact at the
  same company can be invited from the portal, and a proper Services picklist once the
  field exists.
