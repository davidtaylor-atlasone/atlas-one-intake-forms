# Atlas One email HTML: how to build a GHL email that survives Outlook

Written 2026-09-13 (Run AC). The template is the booking wrapper from Run E (September 2026), the one all sixteen
booking and follow up emails already use. Follow this page and a new email will look like the others in Gmail, Apple
Mail, iPhone Mail, Outlook desktop (Word rendering engine), Outlook web and the GHL preview.

## The four rules that matter

1. **Tables, not divs.** Outlook desktop renders with Word. It ignores `max-width`, flexbox, `border-radius` on
   anchors, background images and most CSS on `<div>`. A 600 pixel table with `cellpadding` and inline styles on `<td>`
   renders the same everywhere.
2. **Buttons are a table cell with `bgcolor`, and the anchor carries no inline style.** GHL's editor strips `style`
   from `<a>` when it saves, so a styled anchor becomes a bare blue underlined link. Put the colour on the `<td
   bgcolor>` and the text styling on a `<span>` inside the anchor. The whole cell is the button.
3. **The logo is the raw PNG on storage.googleapis.com, never the images.leadconnectorhq.com copy.** The
   leadconnectorhq copy is served as WebP and Outlook shows a broken image. Fixed width in the `width` attribute and
   the style, `display:block`, `border:0`, real `alt` text.
4. **Type the body through the `</>` source dialog and never through the WYSIWYG** (BUILD-INDEX rule 23). Paste the
   whole document, save, close the dialog with Escape, reload the workflow and re read the body, because an undo can
   silently revert a paste. Type the subject as plain text; the merge picker corrupts subjects.

And the copy rules that apply to everything Atlas One sends (rule 31 and the brand rules): no dashes of any kind in
the copy (write a colon, a comma or a new sentence instead; hyphens inside compound words are fine), no vendor or PEO
brand names, no Atlas One prices in marketing email, every statistic sourced, no colour as the only signal, and the
signature block is text (no image signature, no vCard).

## The wrapper (copy this whole thing)

Replace `BODY` with the message. Replace nothing else. `LOGO_URL` is
`https://storage.googleapis.com/highlevel-backend.appspot.com/location/AzTPxnK2vSUj19jYoDmR/form/Cxqawj85qg4ULUl64nMc/header-image/923a20f4-ffe6-4528-8245-d2f698889c5e.png`.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FAFAF8" style="background:#FAFAF8;padding:32px 0;font-family:'DM Sans',Arial,Helvetica,sans-serif;">
<tr><td align="center" style="padding:0 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="max-width:600px;width:100%;background:#FFFFFF;border:1px solid #DBE4ED;">
  <tr><td style="padding:28px 40px 8px 40px;">
    <img src="LOGO_URL" alt="Atlas One Solutions" width="150" style="display:block;width:150px;height:auto;border:0;">
  </td></tr>
  <tr><td style="padding:16px 40px 8px 40px;color:#23304D;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:16px;line-height:1.6;">
<!-- BODY START -->
BODY
<!-- BODY END -->
  </td></tr>
  <tr><td style="padding:24px 40px 32px 40px;border-top:1px solid #DBE4ED;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
      <td valign="top" style="padding-right:16px;"><img src="LOGO_URL" alt="" width="44" style="display:block;width:44px;height:auto;border:0;"></td>
      <td valign="top" style="color:#23304D;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;">
        <strong style="font-size:15px;">David Taylor</strong><br>
        Founder, Atlas One Solutions<br>
        <a href="tel:13852137177"><span style="color:#23304D;text-decoration:none;">385-213-7177</span></a> &nbsp;&middot;&nbsp;
        <a href="mailto:David@AtlasOneSolutions.com"><span style="color:#788DE3;text-decoration:none;">David@AtlasOneSolutions.com</span></a><br>
        <a href="https://atlasonesolutions.com"><span style="color:#788DE3;text-decoration:none;">AtlasOneSolutions.com</span></a> &nbsp;&middot;&nbsp;
        <a href="https://api.leadconnectorhq.com/widget/groups/book-david"><span style="color:#788DE3;text-decoration:none;">Book time with me</span></a>
      </td></tr></table>
    <p style="margin:20px 0 0 0;color:#788DE3;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:12px;letter-spacing:0.04em;">ONE CALL SOLVES EVERYTHING.</p>
  </td></tr>
</table>
<p style="margin:16px 0 0 0;color:#9AA3B2;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:11px;">Atlas One Solutions LLC &middot; Lehi, Utah</p>
</td></tr></table>
```

Why the pieces are the way they are: `role="presentation"` stops screen readers announcing the layout as a data
table. `bgcolor` on the tables is the Outlook fallback for the CSS `background`. The outer `padding:0 12px` keeps a
gutter on phones. No `border-radius` on the card: Outlook ignores it and the corners would differ between clients,
so it is left square everywhere on purpose. Because the anchors carry no style, most clients underline the signature links; that is accepted (rendered and checked 2026-09-13, `repo:_briefs/assets/run-AC/shots/job8/wrapper_sample.png`). `font-family` is repeated on every text cell because Outlook does not
inherit it from the parent table.

## Body pieces (copy the one you need into BODY)

Paragraph:
```html
<p style="margin:0 0 16px 0;">Text.</p>
```

The button (the whole cell is clickable, the anchor has no style, the colour lives on the cell):
```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:24px 0;"><tr>
  <td bgcolor="#788DE3" style="background:#788DE3;padding:12px 24px;">
    <a href="URL"><span style="color:#FFFFFF;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:16px;font-weight:700;text-decoration:none;display:inline-block;">Button text</span></a>
  </td>
</tr></table>
```
Follow the button with the same link as plain text for people who read with images and colours off:
```html
<p style="margin:0 0 16px 0;font-size:13px;color:#5B6577;">Or open this link: <a href="URL"><span style="color:#788DE3;">URL</span></a></p>
```

Bulleted list:
```html
<ul style="margin:0 0 16px 20px;padding:0;"><li style="margin:0 0 8px 0;">Item</li></ul>
```

A boxed detail (a date, a Zoom line, a number):
```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 16px 0;"><tr>
  <td bgcolor="#DBE4ED" style="background:#DBE4ED;padding:14px 18px;color:#23304D;font-size:15px;line-height:1.5;">
    <strong>Wednesday, September 9, 2026, 4:00 PM</strong><br>Zoom link in the button above.
  </td>
</tr></table>
```

Closing line (the signature block carries name, phone and email, so the body never repeats them):
```html
<p style="margin:0;">Thanks,<br>David</p>
```

## Merge tags that render correctly

`{{contact.first_name}}`, `{{appointment.start_time}}` (full date and time),
`{{appointment.meeting_location}}` (the Zoom link), `{{appointment.title}}`. Type them in the source dialog, never
through the picker in the subject line. Test with a seed contact before publishing.

## Build steps in GHL (the source dialog rules, BUILD-INDEX rule 23)

1. Automation, open the workflow, open the Send Email action.
2. Type the subject as plain text. No merge picker.
3. Click the `</>` source code button in the editor toolbar. Select all, paste the whole wrapper with BODY filled in.
4. Save inside the dialog, then press Escape to close it. Do not click the WYSIWYG canvas afterwards.
5. Save the action. Reload the page. Open the action again and re read the source: confirm the `<td bgcolor>` and
   the `<span>` inside the anchor are still there. If the button reverted to a styled anchor, paste again.
6. Send a test to a seed contact (never a real prospect) and open it in Outlook desktop, Outlook web, Gmail and
   iPhone Mail. Check: logo shows, button is periwinkle with white text, signature links are periwinkle, no dash
   anywhere, the plain text link under the button works.
7. Confirm the workflow is still Published. Do not change triggers or waits.

## The checks before anything ships (rule 31 scan)

Run the same scan the blog set uses: no em dash, no en dash, no spaced hyphen; no vendor or PEO brand names; no
Atlas One prices in marketing email; every statistic has a source line; subject under 60 characters; preheader under
100. One command from the repo:
`grep -nE "—|–| - " body.html` must return nothing.

## Embedding the same look outside GHL

A GHL form or a tool page that sends its own email (the AI Email Assistant, the client portal sign in link) uses the
same wrapper. The portal's template lives in `atlas-one-portal/server/email.ts`; keep it in step with this page.
For a web page that shows an email preview, the wrapper renders as is inside any HTML page: it uses no CSS classes.

## Things that break and why

| Symptom | Cause | Fix |
|---|---|---|
| Button is a plain blue underlined link | Inline style on the `<a>` was stripped by GHL | Colour on `<td bgcolor>`, styling on the `<span>` inside |
| Logo is a broken image in Outlook | The images.leadconnectorhq.com URL serves WebP | Use the storage.googleapis.com PNG |
| Card has no width on phones or is too wide in Outlook | Width only in CSS | `width="600"` attribute plus `max-width` style, outer cell `align="center"` |
| Text is Times New Roman in Outlook | Font family not on that cell | Repeat `font-family` on every text `<td>` |
| Body text vanished after save | Editor undo reverted the paste | Save in the dialog, Escape, reload, re read |
| Subject shows `{{contact.first_name}}` literally | Picker inserted a corrupted tag | Type the subject by hand |
| Dashes appeared | Copy pasted from a doc with smart punctuation | Run the grep scan; write colons and commas |
