CH25 = """
<div class="chapter-break">
  <div class="chapter-num">Chapter 25</div>
  <div class="chapter-title">Glossary of POS &amp; Payment Terms</div>
  <div class="chapter-dek">A comprehensive reference of every term, abbreviation, and concept used in this guide — and in the POS industry at large.</div>
</div>

<table>
  <thead><tr><th style="width:30%;">Term</th><th>Definition</th></tr></thead>
  <tbody>
    <tr><td><strong>ACH (Automated Clearing House)</strong></td><td>Electronic network for financial transactions in the U.S. Used for direct deposits, bank transfers, and some payment processing settlements.</td></tr>
    <tr><td><strong>Acquirer (Acquiring Bank)</strong></td><td>The bank or financial institution that processes card transactions on behalf of the merchant. Receives authorization requests and settles funds to the merchant's account.</td></tr>
    <tr><td><strong>Assessment Fee</strong></td><td>A fee charged by card networks (Visa, Mastercard) on every transaction, separate from interchange fees. Typically 0.13–0.15% of the transaction amount.</td></tr>
    <tr><td><strong>Authorization</strong></td><td>The process of verifying that a cardholder has sufficient funds or credit to complete a transaction. Occurs in real-time at the point of sale.</td></tr>
    <tr><td><strong>AVS (Address Verification Service)</strong></td><td>Fraud prevention tool that verifies the billing address provided by the cardholder matches the address on file with the issuing bank. Used primarily for card-not-present transactions.</td></tr>
    <tr><td><strong>Batch Settlement</strong></td><td>The process of sending a group (batch) of authorized transactions to the acquiring bank for processing and funding. Most merchants batch once daily.</td></tr>
    <tr><td><strong>BOPIS (Buy Online, Pick Up In-Store)</strong></td><td>An omnichannel fulfillment method where customers purchase online and collect their items at a physical store location.</td></tr>
    <tr><td><strong>Card-Not-Present (CNP)</strong></td><td>A transaction where the physical card is not present (online, phone, mail order). CNP transactions carry higher interchange rates due to increased fraud risk.</td></tr>
    <tr><td><strong>Card-Present (CP)</strong></td><td>A transaction where the physical card is presented and read by the terminal (chip, tap, or swipe). Lower fraud risk = lower interchange rates.</td></tr>
    <tr><td><strong>Cash Discount</strong></td><td>A pricing model where the listed price is the card price, and customers who pay with cash receive a discount (typically 3–4%). Legal in all 50 states.</td></tr>
    <tr><td><strong>Chargeback</strong></td><td>A dispute initiated by a cardholder through their issuing bank, resulting in a reversal of funds from the merchant. Chargebacks incur fees ($15–$35 per incident) and can result in account termination if excessive.</td></tr>
    <tr><td><strong>Chip Card (EMV)</strong></td><td>A payment card with an embedded microchip that generates a unique code for each transaction, making it more secure than magnetic stripe cards.</td></tr>
    <tr><td><strong>Cloud POS</strong></td><td>A POS system that stores data and runs software on remote servers accessed via the internet. Enables remote access, automatic updates, and multi-location management.</td></tr>
    <tr><td><strong>CVV/CVC</strong></td><td>Card Verification Value / Card Verification Code. The 3–4 digit security code on a payment card used to verify card-not-present transactions.</td></tr>
    <tr><td><strong>Dual Pricing</strong></td><td>Displaying two prices for every item — a cash price and a card price — allowing customers to choose. The modern evolution of cash discounting.</td></tr>
    <tr><td><strong>Durbin Amendment</strong></td><td>Part of the Dodd-Frank Act (2010) that caps debit card interchange fees for banks with $10+ billion in assets. Regulated debit interchange is capped at 0.05% + 22¢.</td></tr>
    <tr><td><strong>E2EE (End-to-End Encryption)</strong></td><td>Encryption that protects payment data from the moment of capture (card dip/tap) through the entire transaction process until it reaches the processor.</td></tr>
    <tr><td><strong>Effective Rate</strong></td><td>Your true processing cost, calculated as: Total Processing Fees ÷ Total Sales Volume. The single best metric for comparing processing costs across different pricing models.</td></tr>
    <tr><td><strong>EMV</strong></td><td>Europay, Mastercard, Visa — the global standard for chip card technology. EMV chip transactions are more secure than magnetic stripe and shift fraud liability to the party without EMV capability.</td></tr>
    <tr><td><strong>ETF (Early Termination Fee)</strong></td><td>A penalty charged for canceling a POS or processing contract before its term expires. Can range from $250 to $5,000+ depending on the provider and remaining term.</td></tr>
    <tr><td><strong>Flat-Rate Pricing</strong></td><td>A processing pricing model where every transaction is charged the same rate regardless of card type. Simple but typically more expensive at volume than interchange-plus.</td></tr>
    <tr><td><strong>Interchange Fee</strong></td><td>The fee paid to the card-issuing bank on every transaction. Set by card networks (Visa, Mastercard) and varies by card type, transaction type, and merchant category. Non-negotiable.</td></tr>
    <tr><td><strong>Interchange Plus (IC+)</strong></td><td>A transparent pricing model where the merchant pays the actual interchange fee plus a fixed markup from the processor. Generally the most cost-effective model at volume.</td></tr>
    <tr><td><strong>ISO (Independent Sales Organization)</strong></td><td>A third-party company authorized to sell payment processing services on behalf of an acquiring bank or processor. ISOs resell Clover, and their pricing/terms may differ significantly from direct.</td></tr>
    <tr><td><strong>KDS (Kitchen Display System)</strong></td><td>A digital screen in a restaurant kitchen that replaces paper tickets, displaying orders with color-coding, timing, and routing capabilities.</td></tr>
    <tr><td><strong>Loyalty Program</strong></td><td>A customer retention system that rewards repeat purchases with points, discounts, or perks. Built into many POS platforms or available as add-ons.</td></tr>
    <tr><td><strong>MCC (Merchant Category Code)</strong></td><td>A four-digit code assigned to businesses that classifies the type of goods or services provided. MCC affects interchange rates and processing eligibility.</td></tr>
    <tr><td><strong>NFC (Near Field Communication)</strong></td><td>Short-range wireless technology that enables contactless payments. Used by Apple Pay, Google Pay, Samsung Pay, and contactless cards.</td></tr>
    <tr><td><strong>Omnichannel</strong></td><td>A commerce approach that provides customers with a seamless experience across all channels (in-store, online, mobile, social media) with synchronized inventory and customer data.</td></tr>
    <tr><td><strong>P2PE (Point-to-Point Encryption)</strong></td><td>PCI-validated encryption standard where payment data is encrypted at the point of interaction (terminal) and only decrypted within the secure payment processor environment.</td></tr>
    <tr><td><strong>PCI DSS</strong></td><td>Payment Card Industry Data Security Standard — a set of security requirements that all businesses handling card data must comply with. Current version: PCI DSS v4.0.1.</td></tr>
    <tr><td><strong>POS (Point of Sale)</strong></td><td>The location and system where a retail transaction is completed. Modern POS systems include hardware (terminal, reader) and software (inventory, CRM, reporting).</td></tr>
    <tr><td><strong>QSR (Quick-Service Restaurant)</strong></td><td>A restaurant with limited or no table service, emphasizing speed and efficiency. Examples: fast food, fast-casual, counter-service cafes.</td></tr>
    <tr><td><strong>SAQ (Self-Assessment Questionnaire)</strong></td><td>A PCI DSS compliance validation tool for merchants who self-assess their cardholder data security. Required annually for Level 2–4 merchants.</td></tr>
    <tr><td><strong>SKU (Stock Keeping Unit)</strong></td><td>A unique identifier assigned to each distinct product and variant for inventory tracking and management purposes.</td></tr>
    <tr><td><strong>Surcharge</strong></td><td>An additional fee added to a transaction when a customer pays with a credit card. Banned in some states and subject to card network rules (max 3%). Distinct from cash discount.</td></tr>
    <tr><td><strong>Tap to Pay</strong></td><td>Contactless payment method where a customer taps their card, phone, or wearable on an NFC-enabled reader. Faster and more hygienic than chip insertion.</td></tr>
    <tr><td><strong>Tiered Pricing</strong></td><td>A processing pricing model that groups transactions into qualified, mid-qualified, and non-qualified tiers with different rates. The least transparent and typically most expensive model.</td></tr>
    <tr><td><strong>Tokenization</strong></td><td>The process of replacing sensitive card data with a non-sensitive placeholder (token) that can be used for processing without exposing the actual card number.</td></tr>
    <tr><td><strong>Virtual Terminal</strong></td><td>A web-based interface that allows merchants to process card-not-present transactions by manually entering card information. Used for phone and mail orders.</td></tr>
  </tbody>
</table>
"""
