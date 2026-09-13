#!/usr/bin/env python3
"""Run AC job 9: Census v2 patch. Relationship column, full address (ZIP only under 10 employees), tobacco removed from
the UI (key kept empty in the payload), optional masked SSN (local CSV only, never in the payload), spouse and dependent
rows under each employee, "multiple plan options" question, dash pass. Payload: existing keys unchanged, new keys added.
usage: census_v2_patch.py <in.html> <out.html>"""
import sys, io, re
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8', newline='').read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:70], s.count(old)); s = s.replace(old, new)
def opt(old, new):  # dash pass: the kit copy already had most of these fixed in Run W, the repo copy did not
    global s
    s = s.replace(old, new)

# ---- dash pass in visible copy ----
opt('<title>Health Insurance Quote — Census &amp; RFP Intake | Atlas One Solutions</title>', '<title>Health Insurance Quote: Census and RFP Intake | Atlas One Solutions</title>')
opt('<h2>Health Insurance Quote — Census &amp; RFP Intake</h2>', '<h2>Health Insurance Quote: Census and RFP Intake</h2>')
opt('Faster and simpler than a spreadsheet — everything stays', 'Faster and simpler than a spreadsheet. Everything stays')
opt('(rates, bill, claims) — optional and can come later.', '(rates, bill, claims), optional and can come later.')
opt('placeholder="e.g., Metal fabrication — SIC 3441"', 'placeholder="e.g., Metal fabrication, SIC 3441"')
opt("leave them blank — you can provide", "leave them blank. You can provide")
opt('<option>Yes — can provide</option>', '<option>Yes, can provide</option>')
opt('Last step — how should David reach you', 'Last step: how should David reach you')
opt('not stored on this page — it stays in your browser', 'not stored on this page. It stays in your browser')
opt("'That CSV looked empty — nothing to import.'", "'That CSV looked empty, nothing to import.'")
opt("'Sorry — we could not read that CSV. Try the blank template.'", "'Sorry, we could not read that CSV. Try the blank template.'")
opt("lines.push(['Atlas One Solutions — Health Quote Census & RFP Intake']);", "lines.push(['Atlas One Solutions: Health Quote Census and RFP Intake']);")
opt("['Current carrier — Medical'", "['Current carrier, Medical'"); opt("['Current carrier — Dental'", "['Current carrier, Dental'"); opt("['Current carrier — Vision'", "['Current carrier, Vision'")
opt("var subject = 'Health quote census — ' + company;", "var subject = 'Health quote census: ' + company;")
opt("(d.company.eligible || '—')", "(d.company.eligible || 'not given')"); opt("(d.company.effectiveDate || '—')", "(d.company.effectiveDate || 'not given')"); opt("(d.coverage.join(', ') || '—')", "(d.coverage.join(', ') || 'not given')")
opt("button — please find the CSV attached", "button. Please find the CSV attached")
opt("toast('Saved. Keep this file — reopen it here", "toast('Saved. Keep this file and reopen it here")
opt('<span class="summary-empty">—</span>', '<span class="summary-empty">not given</span>')
opt("var label = o === '' ? '—' : o;", "var label = o === '' ? 'Select' : o;")

# ---- step 3: multiple plan options question ----
rep('''    <div class="section-label">Plan preferences</div>
    <div class="grid">''', '''    <div class="section-label">Plan preferences</div>
    <div class="grid">
      <div class="field">
        <label>Do you want more than one plan option offered to employees? <span class="opt">(optional)</span></label>
        <select name="multiPlan">
          <option value="">Not sure yet</option>
          <option value="one">One plan for everyone</option>
          <option value="two">Two options (for example a low deductible and an HSA plan)</option>
          <option value="three">Three or more options</option>
        </select>
        <div class="hint">Under 500 enrolled, every option comes from the same carrier. More than one option usually needs a larger group and steady participation.</div>
      </div>''')

# ---- step 4: table header, toolbar note, CSV note ----
rep('''            <th>First name</th>
            <th>Last / ID</th>
            <th>DOB or Age</th>
            <th>Gender</th>
            <th>Home ZIP</th>
            <th>Coverage tier</th>
            <th>Tobacco</th>
            <th>Dep.</th>
            <th></th>''', '''            <th>First name</th>
            <th>Last / ID</th>
            <th>Relationship</th>
            <th>DOB or Age</th>
            <th>Gender</th>
            <th class="addr-col">Home street</th>
            <th class="addr-col">City</th>
            <th class="addr-col">State</th>
            <th>Home ZIP</th>
            <th>Coverage tier</th>
            <th>SSN <span class="opt">(optional)</span></th>
            <th></th>''')
rep('''<p class="card-sub">Add a row per employee, or upload a CSV and we'll fill the table for you.</p>''',
    '''<p class="card-sub">Add a row per employee, then use "+ spouse" or "+ child" on the employee's row for anyone covered with them. Or upload a CSV and we fill the table for you.</p>
    <div class="note-box" id="addrNote" style="margin-bottom:12px;"><strong>Address:</strong> for groups under 10 employees the carrier only needs the home ZIP. At 10 or more the full home address is asked for; the street, city and state columns appear when the eligible employee count on the Company step is 10 or higher.</div>''')
rep('''<strong>CSV format:</strong> columns are <em>First, Last/ID, DOB or Age, Gender, ZIP, Tier, Tobacco, Dependents</em>. Tier accepts EE, EE+Spouse, EE+Child(ren), Family, or Waiving. Use the blank template above for a guaranteed match.''',
    '''<strong>CSV format:</strong> columns are <em>First, Last/ID, Relationship, DOB or Age, Gender, Street, City, State, ZIP, Tier, SSN</em>. Relationship is Employee, Spouse, Child or Domestic partner; a spouse or child row belongs to the employee row above it. Tier accepts EE, EE+Spouse, EE+Child(ren), Family, or Waiving. The older eight column template (with Tobacco and Dependents) still imports. <strong>SSN is optional</strong>: it is masked on screen, saved only into the CSV you download, and never sent anywhere by this page.''')

# ---- JS: headers, tiers, relationships ----
rep("var CENSUS_HEADERS = ['First','Last/ID','DOB or Age','Gender','ZIP','Tier','Tobacco','Dependents'];",
    "var CENSUS_HEADERS = ['First','Last/ID','Relationship','DOB or Age','Gender','Street','City','State','ZIP','Tier','SSN'];\n  var RELS = ['Employee','Spouse','Domestic partner','Child'];")

# ---- makeRow rewrite ----
old_make = s[s.find('  function makeRow(data){'):s.find('  function genderOptions(sel){')]
new_make = r'''  function relOptions(selected){
    return RELS.map(function(r){ return '<option'+(r===selected?' selected':'')+'>'+r+'</option>'; }).join('');
  }
  function maskSSN(v){
    var d = String(v||'').replace(/\D/g,'').slice(0,9);
    if(d.length <= 4) return d;
    return d.slice(0,3).replace(/\d/g,'*') + '-' + d.slice(3,5).replace(/\d/g,'*') + '-' + d.slice(5);
  }
  function makeRow(data){
    data = data || {};
    var rel = data.relationship || 'Employee';
    var isDep = rel !== 'Employee';
    var tr = document.createElement('tr');
    tr.className = isDep ? 'dep-row' : 'emp-row';
    tr.setAttribute('data-ssn', String(data.ssn||'').replace(/\D/g,'').slice(0,9));
    tr.innerHTML =
      '<td><input type="text" class="c-first" value="'+esc(data.first)+'" placeholder="'+(isDep?'First name':'Optional')+'"></td>' +
      '<td><input type="text" class="c-last" value="'+esc(data.last)+'" placeholder="Last or ID"></td>' +
      '<td><select class="c-rel cell-mid">'+relOptions(rel)+'</select></td>' +
      '<td><input type="text" class="c-dob cell-mid" value="'+esc(data.dob)+'" placeholder="MM/DD/YYYY or age"></td>' +
      '<td><select class="c-gender cell-mid">'+genderOptions(data.gender)+'</select></td>' +
      '<td class="addr-col"><input type="text" class="c-street" value="'+esc(data.street)+'" placeholder="Street"'+(isDep?' disabled':'')+'></td>' +
      '<td class="addr-col"><input type="text" class="c-city cell-mid" value="'+esc(data.city)+'" placeholder="City"'+(isDep?' disabled':'')+'></td>' +
      '<td class="addr-col"><input type="text" class="c-state cell-narrow" value="'+esc(data.state)+'" placeholder="UT" maxlength="2" style="text-transform:uppercase"'+(isDep?' disabled':'')+'></td>' +
      '<td><input type="text" class="c-zip cell-narrow" value="'+esc(data.zip)+'" placeholder="ZIP" inputmode="numeric" maxlength="10"'+(isDep?' disabled':'')+'></td>' +
      '<td><select class="c-tier"'+(isDep?' disabled':'')+'>'+tierOptions(data.tier)+'</select></td>' +
      '<td><input type="text" class="c-ssn cell-mid" value="'+esc(maskSSN(data.ssn))+'" placeholder="Optional" inputmode="numeric" autocomplete="off" maxlength="11"></td>' +
      '<td class="row-acts">'+(isDep?'':'<button type="button" class="row-add" data-rel="Spouse" title="Add spouse or partner">+ spouse</button><button type="button" class="row-add" data-rel="Child" title="Add child">+ child</button>')+'<button type="button" class="row-x" title="Remove">&times;</button></td>';
    tr.querySelector('.row-x').addEventListener('click', function(){
      if(!isDep){ // remove the dependants that belong to this employee too
        var nx = tr.nextSibling;
        while(nx && nx.classList && nx.classList.contains('dep-row')){ var gone = nx; nx = nx.nextSibling; gone.parentNode.removeChild(gone); }
      }
      tr.parentNode.removeChild(tr);
      updateCount();
    });
    Array.prototype.forEach.call(tr.querySelectorAll('.row-add'), function(btn){
      btn.addEventListener('click', function(){
        var dep = makeRow({relationship: btn.getAttribute('data-rel')});
        var after = tr; while(after.nextSibling && after.nextSibling.classList && after.nextSibling.classList.contains('dep-row')) after = after.nextSibling;
        after.parentNode.insertBefore(dep, after.nextSibling);
        updateCount();
        dep.querySelector('.c-first').focus();
      });
    });
    var ssnEl = tr.querySelector('.c-ssn');
    ssnEl.addEventListener('focus', function(){ ssnEl.value = tr.getAttribute('data-ssn') || ''; });
    ssnEl.addEventListener('input', function(){ tr.setAttribute('data-ssn', ssnEl.value.replace(/\D/g,'').slice(0,9)); });
    ssnEl.addEventListener('blur', function(){ ssnEl.value = maskSSN(tr.getAttribute('data-ssn')); });
    tr.querySelector('.c-rel').addEventListener('change', function(e){
      // relationship changed by hand: rebuild the row so the right cells are enabled
      var d = rowData(tr); d.relationship = e.target.value; var fresh = makeRow(d); tr.parentNode.replaceChild(fresh, tr); updateCount();
    });
    return tr;
  }
  function rowData(tr){
    var rel = val(tr,'.c-rel'), dep = rel !== 'Employee';
    return { first: val(tr,'.c-first'), last: val(tr,'.c-last'), relationship: rel, dob: val(tr,'.c-dob'), gender: val(tr,'.c-gender'),
      street: dep ? '' : val(tr,'.c-street'), city: dep ? '' : val(tr,'.c-city'), state: dep ? '' : val(tr,'.c-state').toUpperCase(), zip: dep ? '' : val(tr,'.c-zip'), tier: dep ? '' : val(tr,'.c-tier'), ssn: tr.getAttribute('data-ssn') || '' };
  }
  function rowBlank(d){ return !(d.first || d.last || d.dob || d.ssn); }
  function applyAddressMode(){
    var n = parseInt(getField('eligible'), 10) || 0;
    var big = n >= 10 || (form.querySelector('input[name="groupSize"]:checked') || {}).value === 'large';
    document.body.classList.toggle('show-addr', big);
    var note = document.getElementById('addrNote');
    if(note) note.innerHTML = big ? '<strong>Address:</strong> this group has 10 or more eligible employees, so the carrier asks for each employee\'s full home address. Dependants use the employee\'s address.' : '<strong>Address:</strong> for groups under 10 employees the carrier only needs the home ZIP. The street, city and state columns appear when the eligible employee count on the Company step is 10 or higher.';
  }
'''
s = s.replace(old_make, new_make)

# count only employees (dependants listed separately)
rep("  function countEmployees(){ return censusBody.getElementsByTagName('tr').length; }",
    "  function countEmployees(){ return censusBody.querySelectorAll('tr.emp-row').length; }\n  function countDependants(){ return censusBody.querySelectorAll('tr.dep-row').length; }")
rep("    empCountEl.textContent = n;", "    empCountEl.textContent = n; var dc = document.getElementById('depCount'); if(dc) dc.textContent = countDependants() ? ', plus ' + countDependants() + ' spouse' + (countDependants()===1?'':'s') + ' and dependants' : '';")
rep('<div class="census-counter"><span id="empCount">0</span> employees entered</div>', '<div class="census-counter"><span id="empCount">0</span> employees entered<span id="depCount"></span></div>')

# ---- CSV import: header based ----
old_imp = s[s.find("        // Detect + skip header row if first cell looks like a header"):s.find("        if(added > 0){")]
new_imp = r'''        // Header based import. Old eight column files (First, Last/ID, DOB or Age, Gender, ZIP, Tier, Tobacco, Dependents)
        // and the v2 eleven column template both work; unknown layouts fall back to the v2 order.
        var hdrText = rows[0].join(',').toLowerCase();
        var looksHeader = /first|name|last|id|dob|age|gender|zip|tier|coverage|tobacco|dep|relationship|street|city|state|ssn/.test(hdrText);
        var startIdx = looksHeader ? 1 : 0;
        var hdr = looksHeader ? rows[0].map(function(h){ return (h||'').toLowerCase().replace(/[^a-z]/g,''); }) : [];
        function col(cols, names, fallbackIdx){
          for(var k=0;k<names.length;k++){ var j = hdr.indexOf(names[k]); if(j >= 0) return (cols[j]||'').trim(); }
          return hdr.length ? '' : ((cols[fallbackIdx]||'').trim());
        }
        var oldLayout = hdr.length && hdr.indexOf('tobacco') >= 0 && hdr.indexOf('relationship') < 0;
        var added = 0;
        for(var r = startIdx; r < rows.length; r++){
          var cols = rows[r];
          var rec = {
            first:   col(cols, ['first','firstname'], 0),
            last:    col(cols, ['lastid','last','lastname','id','employeeid'], 1),
            relationship: normRel(col(cols, ['relationship','rel','relation'], 2)),
            dob:     col(cols, ['doborage','dob','dateofbirth','age','birthdate'], 3),
            gender:  normGender(col(cols, ['gender','sex'], 4)),
            street:  col(cols, ['street','address','homestreet','address1'], 5),
            city:    col(cols, ['city'], 6),
            state:   col(cols, ['state','st'], 7),
            zip:     col(cols, ['zip','homezip','zipcode','postal'], 8),
            tier:    normTier(col(cols, ['tier','coveragetier','coverage'], 9)),
            ssn:     col(cols, ['ssn','socialsecurity'], 10)
          };
          if(oldLayout){ rec.dob = col(cols,['doborage','dob','age'],2); rec.gender = normGender(col(cols,['gender'],3)); rec.zip = col(cols,['zip'],4); rec.tier = normTier(col(cols,['tier'],5)); rec.relationship = 'Employee'; }
          addRow(rec);
          added++;
        }
'''
s = s.replace(old_imp, new_imp)
rep("  function normGender(v){", "  function normRel(v){\n    var t = (v||'').toLowerCase();\n    if(!t || t.indexOf('emp') === 0 || t === 'ee' || t === 'self' || t === 'subscriber') return 'Employee';\n    if(t.indexOf('sp') === 0 || t.indexOf('wife') === 0 || t.indexOf('husband') === 0) return 'Spouse';\n    if(t.indexOf('partner') > -1 || t.indexOf('domestic') > -1) return 'Domestic partner';\n    if(t.indexOf('ch') === 0 || t.indexOf('son') === 0 || t.indexOf('daughter') === 0 || t.indexOf('dep') === 0 || t.indexOf('kid') === 0) return 'Child';\n    return 'Employee';\n  }\n  function normGender(v){")

rep("setStatus('Imported ' + added + ' employee' + (added===1?'':'s') + ' from ' + file.name + '.', 'ok');", "setStatus('Imported ' + added + ' row' + (added===1?'':'s') + ' (employees and dependants) from ' + file.name + '.', 'ok');")

# ---- template ----
rep("""      ['Jane','Doe','04/12/1985','Female','84101','EE+Spouse','N','1'],
      ['','ID-2049','39','Male','84604','Family','N','3']""",
    """      ['Jane','Doe','Employee','04/12/1985','Female','123 Main St','Salt Lake City','UT','84101','EE+Spouse',''],
      ['Tom','Doe','Spouse','09/02/1984','Male','','','','','',''],
      ['','ID-2049','Employee','39','Male','','','','84604','Family',''],
      ['Ava','ID-2049','Child','7','Female','','','','','','']""")

# ---- gather rows: payload keeps old keys, adds new ones; SSN never in the payload ----
old_get = s[s.find("  function getCensusRows(){"):s.find("  function val(scope, sel){")]
new_get = r'''  function getCensusRows(){
    // Backward compatible with the v1 payload: first, last, dob, gender, zip, tier, tobacco (always empty now), dep
    // (count of dependant rows under the employee). New keys: relationship, street, city, state, employeeIndex.
    // The SSN is never part of this object; it goes only into the CSV the visitor downloads.
    var rows = [];
    var empIdx = -1, lastEmp = null;
    Array.prototype.forEach.call(censusBody.getElementsByTagName('tr'), function(tr){
      var d = rowData(tr);
      if(rowBlank(d)) return;   // untouched seed rows are not part of the census
      var isEmp = d.relationship === 'Employee';
      if(isEmp){ empIdx++; }
      var rec = {
        first: d.first, last: d.last, dob: d.dob, gender: d.gender,
        zip: isEmp ? d.zip : (lastEmp ? lastEmp.zip : ''),
        tier: isEmp ? d.tier : (lastEmp ? lastEmp.tier : ''),
        tobacco: '', dep: '0',
        relationship: d.relationship, street: isEmp ? d.street : (lastEmp ? lastEmp.street : ''),
        city: isEmp ? d.city : (lastEmp ? lastEmp.city : ''), state: isEmp ? d.state : (lastEmp ? lastEmp.state : ''),
        employeeIndex: empIdx
      };
      if(isEmp){ lastEmp = rec; } else if(lastEmp){ lastEmp.dep = String(parseInt(lastEmp.dep,10) + 1); }
      rows.push(rec);
    });
    return rows;
  }
  function getCensusRowsWithSSN(){
    var out = [];
    Array.prototype.forEach.call(censusBody.getElementsByTagName('tr'), function(tr){ var d = rowData(tr); if(!rowBlank(d)) out.push(d); });
    return out;
  }
'''
s = s.replace(old_get, new_get)
rep("""      plan: {
        medDeductible: getField('medDeductible'),
        dentalDeductible: getField('dentalDeductible')
      },""", """      plan: {
        medDeductible: getField('medDeductible'),
        dentalDeductible: getField('dentalDeductible'),
        multiPlan: getField('multiPlan')
      },
      censusVersion: 2,""")

# ---- review ----
rep("""      row('Medical deductible', d.plan.medDeductible),
      row('Dental deductible', d.plan.dentalDeductible)""", """      row('Medical deductible', d.plan.medDeductible),
      row('Dental deductible', d.plan.dentalDeductible),
      row('Plan options wanted', {one:'One plan for everyone', two:'Two options', three:'Three or more options'}[d.plan.multiPlan] || '')""")
old_rev = s[s.find("    if(d.census.length){\n      censusInner"):s.find("    html += section('Employee census', censusInner);")]
new_rev = r'''    if(d.census.length){
      var emps = d.census.filter(function(e){ return e.relationship === 'Employee'; }).length;
      censusInner += '<div class="summary-row"><div class="k">Employees entered</div><div class="v"><strong>'+emps+'</strong>' + (d.census.length - emps ? ' plus ' + (d.census.length - emps) + ' spouses and dependants' : '') + '</div></div>';
      censusInner += '<div class="table-scroll" style="margin-top:10px;"><table class="census"><thead><tr>' +
        '<th>First</th><th>Last/ID</th><th>Relationship</th><th>DOB/Age</th><th>Gender</th><th>Address</th><th>ZIP</th><th>Tier</th></tr></thead><tbody>';
      d.census.forEach(function(e){
        var addr = [e.street, e.city, e.state].filter(Boolean).join(', ');
        censusInner += '<tr'+(e.relationship !== 'Employee' ? ' class="dep-row"' : '')+'>' +
          '<td>'+esc(e.first||'')+'</td>'+
          '<td>'+esc(e.last||'')+'</td>'+
          '<td>'+esc(e.relationship||'')+'</td>'+
          '<td>'+esc(e.dob||'')+'</td>'+
          '<td>'+esc(e.gender||'')+'</td>'+
          '<td>'+esc(addr)+'</td>'+
          '<td>'+esc(e.zip||'')+'</td>'+
          '<td>'+esc(e.tier||'')+'</td>'+
        '</tr>';
      });
      censusInner += '</tbody></table></div><div class="hint" style="margin-top:8px;">Social Security numbers are never shown here or sent anywhere. They are written only into the CSV you download.</div>';
    } else {
      censusInner = row('Employees entered', '');
    }
'''
s = s.replace(old_rev, new_rev)

# ---- CSV download: SSN included (local only) ----
rep("""    lines.push(['Medical deductible', d.plan.medDeductible]);
    lines.push(['Dental deductible', d.plan.dentalDeductible]);""", """    lines.push(['Medical deductible', d.plan.medDeductible]);
    lines.push(['Dental deductible', d.plan.dentalDeductible]);
    lines.push(['Plan options wanted', d.plan.multiPlan]);""")
rep("""    lines.push(['EMPLOYEE CENSUS ('+d.census.length+')']);
    lines.push(CENSUS_HEADERS);
    d.census.forEach(function(e){
      lines.push([e.first, e.last, e.dob, e.gender, e.zip, e.tier, e.tobacco, e.dep]);
    });""", """    var full = getCensusRowsWithSSN();
    lines.push(['EMPLOYEE CENSUS ('+full.length+' rows, employees and dependants)']);
    lines.push(CENSUS_HEADERS);
    full.forEach(function(e){
      lines.push([e.first, e.last, e.relationship, e.dob, e.gender, e.street, e.city, e.state, e.zip, e.tier, e.ssn]);
    });""")
rep("'Employees on census: ' + d.census.length + '\\n\\n' +", "'Employees on census: ' + d.census.filter(function(e){ return e.relationship === 'Employee'; }).length + '\\n\\n' +")

# ---- wire address mode ----
rep("  addRow(); addRow(); addRow();\n  showStep(1);", "  addRow(); addRow(); addRow();\n  var elig = form.querySelector('[name=\"eligible\"]'); if(elig){ elig.addEventListener('input', applyAddressMode); elig.addEventListener('change', applyAddressMode); }\n  Array.prototype.forEach.call(form.querySelectorAll('input[name=\"groupSize\"]'), function(r){ r.addEventListener('change', applyAddressMode); });\n  applyAddressMode();\n  showStep(1);")

# ---- CSS ----
rep(".cell-narrow{width:70px;}", ".cell-narrow{width:70px;}\n.addr-col{display:none;}\nbody.show-addr .addr-col{display:table-cell;}\ntr.dep-row td{background:#F3F5FA;}\ntr.dep-row td:first-child{padding-left:22px;position:relative;}\ntr.dep-row td:first-child::before{content:\"\\21B3\";position:absolute;left:8px;color:#5C6780;font-size:12px;top:50%;transform:translateY(-50%);}\n.row-acts{white-space:nowrap;}\n.row-add{background:#fff;border:1.5px solid #C8D2E4;color:#23304D;border-radius:8px;height:30px;padding:0 8px;font-size:11.5px;font-weight:600;cursor:pointer;margin-right:4px;font-family:inherit;}\n.row-add:hover{border-color:#788DE3;color:#788DE3;}")

io.open(dst, 'w', encoding='utf-8', newline='').write(s)
print('written', dst, len(s), 'em dashes left:', s.count('—'))
