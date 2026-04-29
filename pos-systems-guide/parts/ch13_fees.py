CH13 = """
<div class="part-divider">
  <div class="part-label">Part III</div>
  <div class="part-title">Knowledge Chapters</div>
  <div class="part-dek">The education core of this guide. Processing fees, cash discount programs, hardware buying, POS security, integrations, and industry-specific advice. These chapters transform you from a buyer into an informed negotiator.</div>
</div>

<div class="chapter-break">
  <div class="chapter-num">Chapter 13</div>
  <div class="chapter-title">Processing Fees Decoded</div>
  <div class="chapter-dek">Flat Rate vs. Interchange Plus — understanding what you really pay. Credit card processing fees are the single largest ongoing cost of running a POS system. This chapter breaks down everything you need to know.</div>
</div>

<div class="h2">How Processing Fees Work</div>
<p>Every time a customer taps, dips, or swipes a card, three parties take a cut of the transaction:</p>

<div class="metrics-row">
  <div class="metric-card"><div class="metric-val">1</div><div class="metric-lbl">Interchange Fee — Card Issuing Bank</div></div>
  <div class="metric-card"><div class="metric-val">2</div><div class="metric-lbl">Network Fee — Visa, MC, Amex</div></div>
  <div class="metric-card"><div class="metric-val">3</div><div class="metric-lbl">Processor Markup — Your POS/Processor</div></div>
</div>

<p>The <strong>interchange fee</strong> is set by the card networks (Visa, Mastercard, etc.) and varies by card type, transaction type, and merchant category code (MCC). You can never negotiate interchange fees — they are fixed and published by the card networks twice per year (April and October).</p>
<p>The <strong>network/assessment fee</strong> is a small percentage charged by the card network itself for using its rails. Typically 0.13–0.15% for Visa/Mastercard. Also non-negotiable.</p>
<p>The <strong>processor markup</strong> is what your payment processor charges on top of interchange and assessments. This is the only negotiable component of your processing costs, and it's where the difference between pricing models matters most.</p>

<div class="h2">The Three Pricing Models</div>

<div class="h3">1. Flat Rate Pricing</div>
<p>You pay one fixed rate for every transaction, regardless of card type. Simple, predictable, but you overpay on low-cost transactions (especially debit cards).</p>
<div class="callout">
  <div class="callout-title">Example: Square at 2.6% + 15¢</div>
  <p>A customer pays with a debit card (actual interchange: ~0.5% + 21¢). You pay 2.6% + 15¢. Square pockets the ~2.1% difference.</p>
  <p>Another customer pays with a premium Amex rewards card (actual interchange: ~2.5% + 10¢). You pay 2.6% + 15¢. Square's margin is only ~0.1%.</p>
  <p><strong>The processor profits most on debit and basic credit cards, and least on premium rewards cards.</strong> If your customer base skews toward debit cards, you're dramatically overpaying with flat-rate pricing.</p>
</div>

<div class="h3">2. Interchange Plus Pricing</div>
<p>You pay the actual interchange rate plus a small, fixed markup. More complex to read on statements, but significantly cheaper at scale.</p>
<div class="callout">
  <div class="callout-title">Example: Helcim at Interchange + 0.3% + 8¢</div>
  <p>Debit card transaction: 0.5% + 21¢ (interchange) + 0.3% + 8¢ (markup) = <strong>0.8% + 29¢</strong></p>
  <p>Premium Amex card: 2.5% + 10¢ (interchange) + 0.3% + 8¢ (markup) = <strong>2.8% + 18¢</strong></p>
  <p>You pay what's fair for each card type. No hidden profit on debit transactions.</p>
</div>

<div class="h3">3. Tiered Pricing (Avoid This)</div>
<p>Transactions are grouped into "qualified," "mid-qualified," and "non-qualified" tiers with different rates. This is the least transparent model and almost always the most expensive. Processors have discretion over which tier a transaction falls into, creating perverse incentives to downgrade transactions to higher-cost tiers.</p>
<div class="danger-box">
  <div class="callout-title">🚨 Red Flag</div>
  <p>If a processor offers you "qualified rate" pricing with no mention of mid-qualified or non-qualified tiers, ask explicitly what those rates are. The "qualified" rate that looks competitive often applies to less than 30% of actual transactions. We recommend avoiding any processor using tiered pricing entirely.</p>
</div>

<div class="h2">Head-to-Head Comparison</div>
<table>
  <thead><tr><th>Factor</th><th>Flat Rate</th><th>Interchange Plus</th><th>Tiered</th></tr></thead>
  <tbody>
    <tr><td>Transparency</td><td>Medium</td><td>High</td><td>Low</td></tr>
    <tr><td>Simplicity</td><td>High</td><td>Moderate</td><td>Low</td></tr>
    <tr><td>Cost at low volume</td><td>Lowest (no monthly fee)</td><td>Slightly higher (monthly fee)</td><td>Varies</td></tr>
    <tr><td>Cost at high volume</td><td>Higher</td><td>Lowest</td><td>Highest</td></tr>
    <tr><td>Debit card savings</td><td>None</td><td>Significant</td><td>Minimal</td></tr>
    <tr><td>Statement clarity</td><td>Very clear</td><td>Detailed but complex</td><td>Confusing</td></tr>
    <tr><td>Processor negotiability</td><td>Limited</td><td>High</td><td>Moderate</td></tr>
  </tbody>
</table>

<div class="h2">Real-World Cost Comparison</div>
<p>What you'd actually pay at different monthly volumes (assumes average $50 ticket, 50% credit / 50% debit card mix):</p>
<table>
  <thead><tr><th>Monthly Volume</th><th>Flat Rate (2.6% + 15¢)</th><th>Interchange Plus (avg 1.93% + 8¢ + $15/mo)</th><th>Annual Savings</th></tr></thead>
  <tbody>
    <tr><td>$5,000</td><td>$145</td><td>$111</td><td>$408/yr</td></tr>
    <tr><td>$10,000</td><td>$290</td><td>$208</td><td>$984/yr</td></tr>
    <tr><td>$25,000</td><td>$725</td><td>$498</td><td>$2,724/yr</td></tr>
    <tr><td>$50,000</td><td>$1,450</td><td>$980</td><td>$5,640/yr</td></tr>
    <tr><td>$100,000</td><td>$2,900</td><td>$1,945</td><td>$11,460/yr</td></tr>
    <tr class="highlight-row"><td>$250,000</td><td>$7,250</td><td>$4,840</td><td>$28,920/yr</td></tr>
  </tbody>
</table>

<div class="tip-box">
  <div class="callout-title">💡 Key Takeaway</div>
  <p>At just $10,000/month in sales (a modest small business), switching from flat-rate to interchange-plus saves nearly <strong>$1,000 per year</strong>. At $50,000/month, savings exceed <strong>$5,600/year</strong>. The break-even point is remarkably low — even businesses processing $3,000–$5,000/month benefit from interchange-plus.</p>
</div>

<div class="h2">Processing Fees by Platform</div>
<table>
  <thead><tr><th>Platform</th><th>Model</th><th>In-Person Rate</th><th>Online Rate</th><th>Keyed Rate</th></tr></thead>
  <tbody>
    <tr><td>Square</td><td>Flat</td><td>2.6% + 15¢</td><td>3.3% + 30¢</td><td>3.5% + 15¢</td></tr>
    <tr><td>Clover (direct)</td><td>Flat</td><td>2.3–2.6% + 10¢</td><td>3.5% + 10¢</td><td>3.5% + 10¢</td></tr>
    <tr><td>Toast</td><td>Flat</td><td>2.49% + 15¢</td><td>—</td><td>3.5% + 15¢</td></tr>
    <tr><td>Shopify</td><td>Flat</td><td>2.4–2.7%</td><td>2.5–2.9% + 30¢</td><td>—</td></tr>
    <tr><td>SpotOn</td><td>Flat</td><td>1.99% + 25¢</td><td>—</td><td>—</td></tr>
    <tr><td>Lightspeed</td><td>Flat</td><td>2.6% + 10¢</td><td>2.9% + 30¢</td><td>—</td></tr>
    <tr><td>Helcim</td><td>IC+</td><td>~1.93% + 8¢</td><td>~2.49% + 25¢</td><td>—</td></tr>
    <tr><td>Payment Depot</td><td>IC+</td><td>IC + 0% + 10¢</td><td>IC + 0% + 15¢</td><td>—</td></tr>
  </tbody>
</table>

<div class="h2">Interchange Fee Ranges by Card Network</div>
<table>
  <thead><tr><th>Card Network</th><th>Debit Range</th><th>Credit Range</th><th>Premium/Rewards</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Visa</td><td>0.05% + 22¢ to 0.80%</td><td>1.51% + 10¢ to 2.40% + 10¢</td><td>Up to 2.40% + 10¢</td><td>Regulated debit capped at 0.05% + 22¢</td></tr>
    <tr><td>Mastercard</td><td>0.05% + 21¢ to 0.80%</td><td>1.48% + 10¢ to 2.10% + 10¢</td><td>Up to 2.10% + 10¢</td><td>Generally slightly lower than Visa</td></tr>
    <tr><td>American Express</td><td>—</td><td>1.35% + 10¢ to 3.15% + 10¢</td><td>Up to 3.15% + 10¢</td><td>Highest rates; mostly premium cards</td></tr>
    <tr><td>Discover</td><td>0.05% + 22¢ to 0.80%</td><td>1.48% + 10¢ to 2.40% + 10¢</td><td>Up to 2.40% + 10¢</td><td>Similar to Visa/MC range</td></tr>
  </tbody>
</table>

<div class="h2">Understanding Your Processing Statement</div>
<p>Processing statements can be confusing, especially on interchange-plus pricing. Here are the key line items to look for:</p>
<table>
  <thead><tr><th>Line Item</th><th>What It Means</th><th>Negotiable?</th></tr></thead>
  <tbody>
    <tr><td>Interchange fees</td><td>The base card-network fee for each transaction type</td><td>No</td></tr>
    <tr><td>Assessment/network fees</td><td>Card network charges (Visa, MC) — typically 0.13–0.15%</td><td>No</td></tr>
    <tr><td>Processor markup</td><td>Your processor's fee on top of interchange</td><td>Yes</td></tr>
    <tr><td>Monthly service fee</td><td>Fixed monthly charge for account maintenance</td><td>Sometimes</td></tr>
    <tr><td>PCI compliance fee</td><td>Monthly fee for PCI DSS compliance tools</td><td>Sometimes</td></tr>
    <tr><td>Batch settlement fee</td><td>Per-batch charge for daily transaction settlement</td><td>Yes</td></tr>
    <tr><td>Chargeback fee</td><td>Fee per chargeback received (typically $15–$35)</td><td>Rarely</td></tr>
    <tr><td>Statement fee</td><td>Fee for generating monthly statements</td><td>Yes — should be $0</td></tr>
    <tr><td>Gateway fee</td><td>For online/e-commerce transactions</td><td>Sometimes</td></tr>
  </tbody>
</table>

<div class="tip-box">
  <div class="callout-title">💰 Our Recommendations by Volume</div>
  <p><strong>Under $5,000/month:</strong> Start with flat-rate (Square). Simplicity is worth the small premium, and you have no monthly fees to worry about.</p>
  <p><strong>$5,000–$20,000/month:</strong> Consider switching to interchange-plus. The savings become meaningful — hundreds to thousands per year.</p>
  <p><strong>$20,000+/month:</strong> Interchange-plus is a no-brainer. You should also be negotiating your markup rate. At high volumes, even 0.05% matters significantly.</p>
  <p><strong>$100,000+/month:</strong> You should be on interchange-plus with a markup under 0.20% + 5¢. At this volume, a skilled negotiator or payment consultant can save you $5,000–$15,000/year.</p>
</div>
"""
