CH16 = """
<div class="chapter-break">
  <div class="chapter-num">Chapter 16</div>
  <div class="chapter-title">POS Security &amp; PCI Compliance</div>
  <div class="chapter-dek">A data breach can destroy a small business — the average cost of a breach for companies with fewer than 500 employees is $3.31 million. This chapter covers everything you need to know about protecting your business and staying PCI compliant.</div>
</div>

<div class="h2">What is PCI DSS?</div>
<p>The <strong>Payment Card Industry Data Security Standard (PCI DSS)</strong> is a set of security requirements established by the major card networks (Visa, Mastercard, Amex, Discover) to protect cardholder data. Every business that accepts, processes, stores, or transmits credit card data must comply with PCI DSS — regardless of size.</p>
<p>The current version is <strong>PCI DSS v4.0.1</strong>, which became mandatory on March 31, 2025, replacing v3.2.1. The updated standard introduces more rigorous requirements for authentication, encryption, and continuous monitoring.</p>

<div class="h2">PCI DSS Compliance Levels</div>
<table>
  <thead><tr><th>Level</th><th>Annual Transactions</th><th>Requirements</th><th>Who Falls Here</th></tr></thead>
  <tbody>
    <tr><td>Level 4</td><td>Under 20,000 e-commerce or under 1 million total</td><td>SAQ (Self-Assessment Questionnaire) + quarterly vulnerability scan</td><td>Most small businesses</td></tr>
    <tr><td>Level 3</td><td>20,000–1,000,000 e-commerce</td><td>SAQ + quarterly vulnerability scan</td><td>Growing e-commerce businesses</td></tr>
    <tr><td>Level 2</td><td>1–6 million total</td><td>SAQ + quarterly vulnerability scan by ASV</td><td>Mid-size merchants</td></tr>
    <tr><td>Level 1</td><td>Over 6 million total</td><td>Annual on-site audit by QSA + quarterly ASV scan</td><td>Large enterprises, chains</td></tr>
  </tbody>
</table>

<div class="callout">
  <div class="callout-title">Good News for Small Businesses</div>
  <p>If you use a modern POS platform (Clover, Toast, Square, Shopify, etc.), much of your PCI compliance is handled by your provider. These platforms are themselves PCI-certified, and their hardware uses end-to-end encryption and tokenization. Your primary responsibilities are network security, physical access control, and completing your annual SAQ.</p>
</div>

<div class="h2">The 12 PCI DSS Requirements (Summarized)</div>
<table>
  <thead><tr><th>#</th><th>Requirement</th><th>What It Means for You</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>Install and maintain network security controls</td><td>Use a firewall; don't run POS on public Wi-Fi</td></tr>
    <tr><td>2</td><td>Apply secure configurations to all system components</td><td>Change default passwords; disable unused services</td></tr>
    <tr><td>3</td><td>Protect stored account data</td><td>Don't store full card numbers; use tokenization</td></tr>
    <tr><td>4</td><td>Protect cardholder data with strong cryptography during transmission</td><td>Use TLS 1.2+ for all data transmission</td></tr>
    <tr><td>5</td><td>Protect all systems from malicious software</td><td>Use antivirus; keep systems patched and updated</td></tr>
    <tr><td>6</td><td>Develop and maintain secure systems and software</td><td>Keep POS software updated; apply security patches promptly</td></tr>
    <tr><td>7</td><td>Restrict access by business need-to-know</td><td>Limit POS admin access to managers/owners only</td></tr>
    <tr><td>8</td><td>Identify users and authenticate access</td><td>Unique login per employee; strong passwords or PINs</td></tr>
    <tr><td>9</td><td>Restrict physical access to cardholder data</td><td>Secure POS terminals; monitor for tampering</td></tr>
    <tr><td>10</td><td>Log and monitor all access to system components and cardholder data</td><td>Enable audit logging; review logs regularly</td></tr>
    <tr><td>11</td><td>Test security of systems and networks regularly</td><td>Quarterly vulnerability scans by an Approved Scanning Vendor (ASV)</td></tr>
    <tr><td>12</td><td>Support information security with organizational policies</td><td>Written security policy; employee training; incident response plan</td></tr>
  </tbody>
</table>

<div class="h2">Common POS Security Threats</div>

<div class="h3">1. Skimming and Tampering</div>
<p>Criminals install overlay devices on card readers to capture card data. This affects both chip and magnetic stripe transactions.</p>
<ul>
  <li>Inspect card readers daily for loose parts, unusual overlays, or misaligned components</li>
  <li>Use tamper-evident seals on terminals</li>
  <li>Train staff to recognize signs of tampering</li>
  <li>Consider terminals with anti-skimming technology (most modern terminals include this)</li>
</ul>

<div class="h3">2. Malware and Ransomware</div>
<p>POS malware has been responsible for some of the largest retail data breaches in history (Target, Home Depot, Wendy's).</p>
<ul>
  <li>Keep all systems updated with the latest security patches</li>
  <li>Don't use POS computers for web browsing, email, or other non-POS activities</li>
  <li>Implement endpoint protection software</li>
  <li>Segment your POS network from your general business and guest Wi-Fi networks</li>
</ul>

<div class="h3">3. Employee Theft and Internal Fraud</div>
<p>Internal threats account for a significant portion of POS-related losses.</p>
<ul>
  <li>Use unique employee PINs or logins for every staff member</li>
  <li>Enable transaction logging and review void/refund reports daily</li>
  <li>Set role-based permissions — cashiers shouldn't have admin access</li>
  <li>Monitor for unusual patterns: excessive voids, post-close transactions, or skewed cash counts</li>
</ul>

<div class="h3">4. Network Attacks</div>
<p>Unsecured networks are the most common attack vector for POS breaches.</p>
<ul>
  <li>Never run POS systems on public or guest Wi-Fi networks</li>
  <li>Use WPA3 encryption for wireless POS connections</li>
  <li>Implement a dedicated VLAN (Virtual LAN) for POS devices</li>
  <li>Use a business-grade firewall with intrusion detection/prevention</li>
  <li>Disable remote access unless absolutely necessary; use VPN if needed</li>
</ul>

<div class="h2">Security Features by Platform</div>
<table>
  <thead><tr><th>Feature</th><th>Clover</th><th>Toast</th><th>Square</th><th>Shopify</th><th>Shift4</th></tr></thead>
  <tbody>
    <tr><td>End-to-end encryption</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Tokenization</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>PCI Level 1 certified</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>P2PE validated</td><td>❌</td><td>❌</td><td>❌</td><td>❌</td><td>✅</td></tr>
    <tr><td>Offline mode encryption</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Role-based permissions</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Audit logging</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Two-factor auth (admin)</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
  </tbody>
</table>

<div class="h2">Your Security Checklist</div>
<div class="callout">
  <div class="callout-title">✅ Monthly Security Checklist</div>
  <ol>
    <li>Physically inspect all card readers and terminals for tampering</li>
    <li>Review void and refund reports for unusual patterns</li>
    <li>Verify all POS software is up to date</li>
    <li>Confirm employee access levels are appropriate (deactivate former employees immediately)</li>
    <li>Check that your network firewall is active and properly configured</li>
    <li>Review security logs for unauthorized access attempts</li>
    <li>Verify backup systems are functioning</li>
    <li>Test your incident response procedures (quarterly)</li>
  </ol>
</div>
"""
