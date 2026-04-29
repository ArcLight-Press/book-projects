CH17 = """
<div class="chapter-break">
  <div class="chapter-num">Chapter 17</div>
  <div class="chapter-title">Integrations &amp; the Connected Business</div>
  <div class="chapter-dek">Your POS doesn't operate in a vacuum. It connects to accounting, payroll, inventory management, marketing, delivery, and more. The right integrations save hours per week and eliminate costly data-entry errors.</div>
</div>

<div class="h2">Essential Integration Categories</div>

<div class="h3">1. Accounting (Mission-Critical)</div>
<p>Your POS should sync daily sales data, tax collected, tips, and refunds directly to your accounting software. Manual entry means errors and wasted time.</p>
<table>
  <thead><tr><th>Software</th><th>Cost</th><th>Best Integration With</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>QuickBooks Online</td><td>$30–$200/mo</td><td>Clover, Square, Shopify, Toast, Lightspeed</td><td>Most widely used; excellent POS integrations</td></tr>
    <tr><td>Xero</td><td>$15–$78/mo</td><td>Square, Shopify, Lightspeed, TouchBistro</td><td>Strong international support; clean interface</td></tr>
    <tr><td>FreshBooks</td><td>$19–$60/mo</td><td>Square, Shopify</td><td>Best for service-based businesses</td></tr>
    <tr><td>Wave</td><td>Free</td><td>Square (limited)</td><td>Free option; limited POS integration</td></tr>
  </tbody>
</table>

<div class="h3">2. Payroll</div>
<table>
  <thead><tr><th>Software</th><th>Cost</th><th>Best Integration With</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Gusto</td><td>$40 + $6/person/mo</td><td>Clover, Square, Toast, Shopify</td><td>Full-service payroll, benefits, HR</td></tr>
    <tr><td>ADP Run</td><td>$79 + $4/person/mo</td><td>Clover, Revel</td><td>Enterprise-grade payroll for growing businesses</td></tr>
    <tr><td>Square Payroll</td><td>$35 + $6/person/mo</td><td>Square (built-in)</td><td>Seamless if you're already on Square</td></tr>
    <tr><td>Toast Payroll</td><td>$69 + $9/person/mo</td><td>Toast (built-in)</td><td>Restaurant-specific payroll with tip reporting</td></tr>
    <tr><td>Homebase</td><td>Free–$99/mo</td><td>Clover, Square, Toast</td><td>Scheduling + time tracking + basic payroll</td></tr>
  </tbody>
</table>

<div class="h3">3. Inventory &amp; Supply Chain</div>
<table>
  <thead><tr><th>Software</th><th>Cost</th><th>Function</th></tr></thead>
  <tbody>
    <tr><td>MarketMan</td><td>$239–$429/mo</td><td>Restaurant inventory, food costing, vendor management, waste tracking</td></tr>
    <tr><td>BlueCart</td><td>Varies</td><td>Restaurant ordering and vendor management</td></tr>
    <tr><td>Cin7</td><td>$349+/mo</td><td>Multi-channel inventory sync for retail</td></tr>
    <tr><td>Sortly</td><td>$49–$149/mo</td><td>Visual inventory tracking with photos and QR codes</td></tr>
  </tbody>
</table>

<div class="h3">4. Online Ordering &amp; Delivery</div>
<table>
  <thead><tr><th>Platform</th><th>Commission</th><th>Integrates With</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>DoorDash</td><td>15–30%</td><td>Toast, Clover, Square, SpotOn</td><td>Largest delivery market share in the US</td></tr>
    <tr><td>Uber Eats</td><td>15–30%</td><td>Toast, Clover, Square</td><td>Strong international presence</td></tr>
    <tr><td>Grubhub</td><td>15–30%</td><td>Toast, Clover, SpotOn</td><td>Particularly strong in urban/metro markets</td></tr>
    <tr><td>ChowNow</td><td>Flat monthly fee</td><td>Clover, Square, Toast</td><td>Commission-free ordering; branded website/app</td></tr>
    <tr><td>Toast Online Ordering</td><td>0% commission</td><td>Toast (built-in)</td><td>Zero-commission but Toast-only</td></tr>
    <tr><td>Square Online</td><td>0% commission</td><td>Square (built-in)</td><td>Free basic plan with Square POS sync</td></tr>
  </tbody>
</table>

<div class="h3">5. Marketing &amp; Customer Engagement</div>
<table>
  <thead><tr><th>Tool</th><th>Cost</th><th>Function</th></tr></thead>
  <tbody>
    <tr><td>Mailchimp</td><td>Free–$350+/mo</td><td>Email marketing, automation, customer segmentation</td></tr>
    <tr><td>Klaviyo</td><td>Free–$150+/mo</td><td>Advanced email/SMS marketing; strong e-commerce focus</td></tr>
    <tr><td>Podium</td><td>$289–$449/mo</td><td>Review management, messaging, payments</td></tr>
    <tr><td>Birdeye</td><td>Custom pricing</td><td>Reputation management, surveys, social media</td></tr>
  </tbody>
</table>

<div class="h3">6. Employee Scheduling &amp; Management</div>
<table>
  <thead><tr><th>Tool</th><th>Cost</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td>7shifts</td><td>Free–$34.99/mo per location</td><td>Restaurant scheduling, labor compliance, tip management</td></tr>
    <tr><td>Homebase</td><td>Free–$99/mo</td><td>Small business scheduling, time tracking, hiring</td></tr>
    <tr><td>When I Work</td><td>$2.50/user/mo</td><td>Shift-based scheduling for hourly workers</td></tr>
    <tr><td>Deputy</td><td>$4.50/user/mo</td><td>Enterprise scheduling, compliance, demand forecasting</td></tr>
  </tbody>
</table>

<div class="h2">Integration Compatibility Matrix</div>
<table>
  <thead><tr><th>Integration</th><th>Clover</th><th>Toast</th><th>Square</th><th>Shopify</th><th>Lightspeed</th><th>SpotOn</th></tr></thead>
  <tbody>
    <tr><td>QuickBooks</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Xero</td><td>⚠️</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>⚠️</td></tr>
    <tr><td>Gusto Payroll</td><td>✅</td><td>⚠️</td><td>✅</td><td>✅</td><td>⚠️</td><td>⚠️</td></tr>
    <tr><td>DoorDash</td><td>✅</td><td>✅</td><td>✅</td><td>❌</td><td>⚠️</td><td>✅</td></tr>
    <tr><td>Mailchimp</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>⚠️</td></tr>
    <tr><td>7shifts</td><td>✅</td><td>✅</td><td>✅</td><td>❌</td><td>✅</td><td>✅</td></tr>
    <tr><td>Zapier (any-to-any)</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>⚠️</td></tr>
  </tbody>
</table>
<p style="font-size:8.5pt;">✅ = Native integration | ⚠️ = Available via third-party connector or Zapier | ❌ = Not available</p>

<div class="tip-box">
  <div class="callout-title">💡 The Zapier Bridge</div>
  <p>If your POS and a business tool don't have a native integration, <strong>Zapier</strong> ($19.99–$69/mo) can often bridge the gap. Zapier connects 6,000+ apps and can automate workflows like: "When a sale is made in Clover → Add customer to Mailchimp list" or "When a shift is scheduled in 7shifts → Send confirmation via Slack." Before committing to a POS that lacks a specific integration, check if Zapier can handle it.</p>
</div>
"""
