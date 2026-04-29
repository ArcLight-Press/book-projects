CH20 = """
<div class="chapter-break">
  <div class="chapter-num">Chapter 20</div>
  <div class="chapter-title">Migration &amp; Implementation</div>
  <div class="chapter-dek">Switching POS systems doesn't have to be painful. With proper planning, you can migrate your menu, inventory, customer data, and payment processing with minimal disruption to daily operations.</div>
</div>

<div class="h2">The 30-Day Migration Timeline</div>
<p>A well-planned POS migration takes approximately 30 days from decision to go-live. Rushing this process leads to mistakes, frustrated staff, and unhappy customers.</p>

<table>
  <thead><tr><th>Week</th><th>Phase</th><th>Key Tasks</th></tr></thead>
  <tbody>
    <tr><td>Week 1</td><td>Planning &amp; Setup</td><td>Order hardware; create account; export data from old system; review contract terms</td></tr>
    <tr><td>Week 2</td><td>Configuration</td><td>Import menu/inventory; set up categories; configure tax rates; set up employees; connect peripherals</td></tr>
    <tr><td>Week 3</td><td>Testing &amp; Training</td><td>Run test transactions; train managers; train staff; test all peripherals; test integrations</td></tr>
    <tr><td>Week 4</td><td>Parallel Run &amp; Go-Live</td><td>Run both systems simultaneously for 2–3 days; go-live on new system; decommission old system</td></tr>
  </tbody>
</table>

<div class="h2">Data Migration Checklist</div>
<div class="callout">
  <div class="callout-title">📋 What to Transfer</div>
  <table style="margin:6pt 0;">
    <thead><tr><th>Data Category</th><th>Export Format</th><th>Priority</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td>Menu / product catalog</td><td>CSV</td><td>Critical</td><td>Most POS systems support CSV import for items, categories, modifiers, and prices</td></tr>
      <tr><td>Inventory counts</td><td>CSV</td><td>Critical</td><td>Do a fresh count on migration day for accuracy</td></tr>
      <tr><td>Customer database</td><td>CSV</td><td>High</td><td>Names, emails, phone numbers, loyalty points (if applicable)</td></tr>
      <tr><td>Employee information</td><td>Manual or CSV</td><td>High</td><td>Roles, permissions, PINs, pay rates</td></tr>
      <tr><td>Gift card balances</td><td>CSV</td><td>High</td><td>Outstanding balances represent a liability — must be honored</td></tr>
      <tr><td>Historical sales data</td><td>PDF/CSV export</td><td>Medium</td><td>Export and archive from old system; rarely importable to new</td></tr>
      <tr><td>Tax settings</td><td>Manual setup</td><td>Critical</td><td>Verify tax rates; test tax calculations before go-live</td></tr>
      <tr><td>Vendor/supplier info</td><td>CSV</td><td>Medium</td><td>If using inventory management features</td></tr>
    </tbody>
  </table>
</div>

<div class="h2">Staff Training Best Practices</div>
<ol>
  <li><strong>Train managers first</strong> — They become your internal experts and can answer staff questions on-the-go.</li>
  <li><strong>Use the vendor's training resources</strong> — Most platforms offer free training videos, webinars, and documentation.</li>
  <li><strong>Hands-on practice</strong> — Let staff process test transactions in training mode. Lecture-style training doesn't work for POS systems.</li>
  <li><strong>Create a cheat sheet</strong> — A one-page quick reference for the 10 most common tasks (ring up sale, split bill, process return, etc.).</li>
  <li><strong>Schedule training during off-hours</strong> — Don't try to train during service. Schedule dedicated 1–2 hour sessions before or after shifts.</li>
  <li><strong>Designate "super users"</strong> — 1–2 tech-savvy staff members per shift who can troubleshoot basic issues.</li>
</ol>

<div class="h2">Go-Live Day Checklist</div>
<div class="callout">
  <div class="callout-title">✅ Day-of Launch Checklist</div>
  <ul>
    <li>☐ All hardware powered on and connected to network</li>
    <li>☐ Card reader processing test transactions successfully</li>
    <li>☐ Receipt printer printing correctly (check formatting)</li>
    <li>☐ Cash drawer opening on cash transactions</li>
    <li>☐ Kitchen printer/KDS receiving orders</li>
    <li>☐ All menu items / products visible and priced correctly</li>
    <li>☐ Tax calculations verified on test transactions</li>
    <li>☐ All employee accounts active with correct permissions</li>
    <li>☐ Backup internet connection ready (cellular hotspot)</li>
    <li>☐ Old POS system accessible (but not primary) for reference</li>
    <li>☐ Vendor support contact information printed and posted by the terminal</li>
    <li>☐ Manager or super-user available on-site for the first full day</li>
  </ul>
</div>

<div class="h2">Common Migration Pitfalls</div>
<div class="danger-box">
  <div class="callout-title">🚨 Mistakes to Avoid</div>
  <ul>
    <li><strong>Rushing the timeline</strong> — A 1-week migration almost always results in errors. Budget 3–4 weeks minimum.</li>
    <li><strong>Not testing before go-live</strong> — Run at least 50 test transactions covering every scenario: cash, card, split, void, refund, discount.</li>
    <li><strong>Forgetting gift cards</strong> — Outstanding gift card balances are a legal liability. Ensure all balances transfer or have a manual lookup process.</li>
    <li><strong>Canceling old service too early</strong> — Keep your old system accessible (even if deactivated) for at least 30 days after go-live for historical data reference and reporting.</li>
    <li><strong>Ignoring tax setup</strong> — Incorrect tax rates on day one create accounting headaches. Verify rates and test calculations thoroughly.</li>
    <li><strong>Undertraining staff</strong> — If cashiers can't process a basic sale confidently, you're not ready to go-live.</li>
    <li><strong>No fallback plan</strong> — Have a plan for what happens if the new system fails on day one. Keep a manual credit card imprinter or phone-based backup.</li>
  </ul>
</div>

<div class="h2">Post-Migration: The First 30 Days</div>
<ul>
  <li><strong>Week 1:</strong> Monitor every shift closely. Collect staff feedback daily. Fix issues immediately.</li>
  <li><strong>Week 2:</strong> Review sales reports against old system benchmarks. Verify processing fees match your contract.</li>
  <li><strong>Week 3:</strong> Fine-tune configurations based on real-world usage. Set up integrations (accounting, payroll, etc.).</li>
  <li><strong>Week 4:</strong> Conduct a formal review: What's working? What needs adjustment? Update staff cheat sheets. Officially decommission old system.</li>
</ul>
"""
