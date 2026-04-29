CSS = """
@import url("https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;500&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap");

/* ── Page Setup — KDP 6×9 trim ────────────────────────────── */
@page {
  size: 6in 9in;
  margin: 0.75in 0.625in 0.85in 0.625in;
  @bottom-center {
    content: counter(page);
    font-family: "Roboto Mono", monospace;
    font-size: 8pt;
    color: #999;
    letter-spacing: 0.08em;
  }
}
@page :first { margin-top: 0; margin-bottom: 0; @bottom-center { content: none; } }
@page cover { margin: 0; @bottom-center { content: none; } }
@page frontmatter { @bottom-center { content: none; } }

:root {
  --navy: #1B2A4A;
  --navy-light: #2D4470;
  --navy-dark: #0F1B33;
  --accent: #3B82F6;
  --accent-light: #60A5FA;
  --teal: #0D9488;
  --green: #16A34A;
  --red: #DC2626;
  --amber: #D97706;
  --surface: #FFFFFF;
  --ink: #1A1A2E;
  --dim: #5A6178;
  --faint: #8B90A0;
  --line: #E2E5EB;
  --fill: #F4F6F9;
  --fill-alt: #EEF1F6;
}

/* ── Base Typography ──────────────────────────────────────── */
html, body { margin: 0; padding: 0; }
body {
  font-family: "Satoshi", "Inter", -apple-system, sans-serif;
  font-size: 9pt;
  line-height: 1.50;
  color: var(--ink);
  background: white;
}

h1, h2, h3, h4 { break-after: avoid; margin: 0; font-family: "Satoshi", "Inter", sans-serif; }
p { orphans: 3; widows: 3; margin: 0 0 8pt 0; }
table, .card, figure, tr, .callout, .tip-box, .warn-box { break-inside: avoid; }
p, figcaption, blockquote { text-wrap: pretty; }
h1, h2, h3 { text-wrap: balance; }

/* ── Cover Page ───────────────────────────────────────────── */
.cover-page {
  page: cover;
  width: 6in; height: 9in;
  background: linear-gradient(160deg, var(--navy-dark) 0%, var(--navy) 40%, var(--navy-light) 100%);
  color: white;
  display: flex; flex-direction: column; justify-content: center;
  padding: 1.8in 0.7in 1.2in 0.7in;
  box-sizing: border-box;
  position: relative;
  break-after: page;
}
.cover-badge {
  font-family: "Roboto Mono", monospace;
  font-size: 9pt; letter-spacing: 0.22em; text-transform: uppercase;
  color: rgba(255,255,255,0.6);
  margin-bottom: 18pt;
}
.cover-title {
  font-size: 30pt; font-weight: 700; line-height: 1.08;
  letter-spacing: -0.02em; margin-bottom: 12pt;
}
.cover-subtitle {
  font-size: 11pt; font-weight: 400; line-height: 1.45;
  color: rgba(255,255,255,0.75); max-width: 4.4in;
  margin-bottom: 28pt;
}
.cover-stats {
  display: flex; gap: 24pt; margin-top: 16pt;
}
.cover-stat-num {
  font-size: 24pt; font-weight: 700; color: var(--accent-light);
  line-height: 1.0;
}
.cover-stat-lbl {
  font-family: "Roboto Mono", monospace;
  font-size: 7.5pt; letter-spacing: 0.12em; text-transform: uppercase;
  color: rgba(255,255,255,0.55); margin-top: 4pt;
}
.cover-footer {
  position: absolute; bottom: 36pt; left: 0.7in; right: 0.7in;
  display: flex; justify-content: space-between; align-items: flex-end;
}
.cover-publisher {
  font-family: "Roboto Mono", monospace;
  font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase;
  color: rgba(255,255,255,0.5);
}
.cover-edition {
  font-family: "Roboto Mono", monospace;
  font-size: 8pt; letter-spacing: 0.1em;
  color: rgba(255,255,255,0.4);
}

/* ── Front Matter ─────────────────────────────────────────── */
.frontmatter { page: frontmatter; }
.fm-title {
  font-size: 22pt; font-weight: 700; color: var(--navy);
  margin-bottom: 18pt; letter-spacing: -0.01em;
}

/* ── Table of Contents ────────────────────────────────────── */
.toc-part {
  font-family: "Roboto Mono", monospace;
  font-size: 8pt; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--accent); margin: 20pt 0 8pt 0; font-weight: 500;
}
.toc-part:first-of-type { margin-top: 0; }
.toc-entry {
  display: flex; justify-content: space-between; align-items: baseline;
  padding: 3.5pt 0; border-bottom: 0.5pt solid var(--line);
  font-size: 9.5pt;
}
.toc-entry:last-child { border-bottom: none; }
.toc-num { font-weight: 600; color: var(--navy); min-width: 24pt; }
.toc-title { flex: 1; color: var(--ink); }
.toc-page {
  font-family: "Roboto Mono", monospace;
  font-size: 8pt; color: var(--faint); min-width: 20pt; text-align: right;
}

/* ── Chapter Headers ──────────────────────────────────────── */
.chapter-break {
  break-before: page;
  background: var(--navy);
  color: white;
  margin: -0.75in -0.625in 0 -0.625in;
  padding: 1.3in 0.625in 0.6in 0.625in;
  margin-bottom: 22pt;
}
.chapter-num {
  font-family: "Roboto Mono", monospace;
  font-size: 9pt; letter-spacing: 0.22em; text-transform: uppercase;
  color: rgba(255,255,255,0.5); margin-bottom: 10pt;
}
.chapter-title {
  font-size: 22pt; font-weight: 700; line-height: 1.12;
  letter-spacing: -0.015em; margin-bottom: 8pt;
}
.chapter-dek {
  font-size: 10pt; font-weight: 400; line-height: 1.45;
  color: rgba(255,255,255,0.7); max-width: 4.5in;
}

/* ── Section headings ─────────────────────────────────────── */
.h2 {
  font-size: 14pt; font-weight: 700; color: var(--navy);
  margin: 22pt 0 10pt 0; letter-spacing: -0.01em;
  padding-bottom: 4pt; border-bottom: 1.5pt solid var(--navy);
}
.h3 {
  font-size: 11pt; font-weight: 600; color: var(--navy-light);
  margin: 14pt 0 6pt 0;
}
.h4 {
  font-size: 10pt; font-weight: 600; color: var(--ink);
  margin: 12pt 0 5pt 0;
}

/* first h2 after chapter header needs less top margin */
.chapter-break + .h2, .chapter-break + * > .h2:first-child { margin-top: 0; }

/* ── Metric Cards ─────────────────────────────────────────── */
.metrics-row {
  display: flex; gap: 10pt; margin: 14pt 0 18pt 0;
}
.metric-card {
  flex: 1; min-width: 0;
  background: var(--fill);
  padding: 12pt 14pt;
  text-align: center;
}
.metric-val {
  font-size: 16pt; font-weight: 700; color: var(--navy);
  line-height: 1.1;
}
.metric-lbl {
  font-family: "Roboto Mono", monospace;
  font-size: 7pt; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--dim); margin-top: 3pt;
}

/* ── Tables ───────────────────────────────────────────────── */
table {
  width: 100%; border-collapse: collapse;
  font-size: 8pt; margin: 8pt 0 12pt 0;
}
thead th {
  background: var(--navy);
  color: white;
  font-family: "Roboto Mono", monospace;
  font-size: 6.5pt; letter-spacing: 0.1em; text-transform: uppercase;
  font-weight: 500;
  padding: 5pt 5pt;
  text-align: left;
}
tbody td {
  padding: 4pt 5pt;
  border-bottom: 0.5pt solid var(--line);
  vertical-align: top;
}
tbody tr:nth-child(even) { background: var(--fill); }
tbody tr:last-child td { border-bottom: none; }
td.num, th.num { text-align: right; font-feature-settings: "tnum" 1, "lnum" 1; }

/* ── Callout Boxes ────────────────────────────────────────── */
.callout {
  background: var(--fill);
  padding: 12pt 14pt;
  margin: 12pt 0;
  font-size: 9.5pt;
}
.callout-title {
  font-weight: 600; font-size: 9.5pt;
  color: var(--navy); margin-bottom: 4pt;
}
.tip-box {
  background: #F0FDF4;
  padding: 10pt 14pt;
  margin: 12pt 0;
  font-size: 9.5pt;
}
.tip-box .callout-title { color: var(--green); }
.warn-box {
  background: #FFFBEB;
  padding: 10pt 14pt;
  margin: 12pt 0;
  font-size: 9.5pt;
}
.warn-box .callout-title { color: var(--amber); }
.danger-box {
  background: #FEF2F2;
  padding: 10pt 14pt;
  margin: 12pt 0;
  font-size: 9.5pt;
}
.danger-box .callout-title { color: var(--red); }

/* ── Pros / Cons ──────────────────────────────────────────── */
.pros-cons { display: flex; gap: 12pt; margin: 12pt 0; }
.pros, .cons { flex: 1; min-width: 0; padding: 10pt 12pt; font-size: 9pt; }
.pros { background: #F0FDF4; }
.cons { background: #FEF2F2; }
.pros-title { font-weight: 600; color: var(--green); margin-bottom: 6pt; font-size: 9.5pt; }
.cons-title { font-weight: 600; color: var(--red); margin-bottom: 6pt; font-size: 9.5pt; }
.pros li, .cons li { margin-bottom: 3pt; }

/* ── Verdict ──────────────────────────────────────────────── */
.verdict {
  background: var(--navy);
  color: white;
  padding: 14pt 16pt;
  margin: 16pt 0;
}
.verdict-title {
  font-size: 11pt; font-weight: 700; margin-bottom: 6pt;
}
.verdict p { color: rgba(255,255,255,0.85); font-size: 9.5pt; margin-bottom: 6pt; }
.verdict strong { color: white; }

/* ── Lists ────────────────────────────────────────────────── */
ul, ol { margin: 6pt 0 10pt 0; padding-left: 18pt; }
li { margin-bottom: 3pt; font-size: 9.5pt; }

/* ── Checklist ────────────────────────────────────────────── */
.checklist { list-style: none; padding-left: 0; }
.checklist li { padding-left: 16pt; position: relative; margin-bottom: 4pt; }
.checklist li::before { content: "✓"; position: absolute; left: 0; color: var(--green); font-weight: 700; }

/* ── Two-col layout ───────────────────────────────────────── */
.two-col { display: flex; gap: 16pt; margin: 10pt 0; }
.two-col > div { flex: 1; min-width: 0; }

/* ── Pull quote ───────────────────────────────────────────── */
.pull-quote {
  font-size: 13pt; font-weight: 500; color: var(--navy);
  line-height: 1.4; margin: 20pt 24pt;
  font-style: italic;
}

/* ── Divider ──────────────────────────────────────────────── */
hr { border: none; border-top: 1pt solid var(--line); margin: 16pt 0; }

/* ── Footer labels ────────────────────────────────────────── */
.page-footer-label {
  font-family: "Roboto Mono", monospace;
  font-size: 7pt; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--faint);
}

/* ── Part Divider ─────────────────────────────────────────── */
.part-divider {
  break-before: page;
  background: var(--fill);
  margin: -0.75in -0.625in 0 -0.625in;
  padding: 2.2in 0.625in 0.5in 0.625in;
  margin-bottom: 0;
  height: calc(9in - 2.2in - 0.5in);
  box-sizing: border-box;
}
.part-label {
  font-family: "Roboto Mono", monospace;
  font-size: 10pt; letter-spacing: 0.22em; text-transform: uppercase;
  color: var(--accent); margin-bottom: 12pt; font-weight: 500;
}
.part-title {
  font-size: 24pt; font-weight: 700; color: var(--navy);
  line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 12pt;
}
.part-dek {
  font-size: 10pt; color: var(--dim); line-height: 1.5;
  max-width: 4.2in;
}

/* ── Back matter ──────────────────────────────────────────── */
.back-page {
  break-before: page;
  background: var(--navy);
  color: white;
  margin: -0.75in -0.625in -0.85in -0.625in;
  padding: 2in 0.625in;
  min-height: calc(9in - 0.75in - 0.85in);
  box-sizing: border-box;
}

/* ── Numbered steps ───────────────────────────────────────── */
.steps { counter-reset: step; list-style: none; padding-left: 0; }
.steps li {
  counter-increment: step; padding-left: 28pt; position: relative;
  margin-bottom: 8pt; font-size: 9.5pt;
}
.steps li::before {
  content: counter(step);
  position: absolute; left: 0; top: 0;
  width: 18pt; height: 18pt; line-height: 18pt;
  text-align: center; background: var(--navy); color: white;
  font-size: 8pt; font-weight: 700;
  font-family: "Roboto Mono", monospace;
}

/* ── Comparison highlight ─────────────────────────────────── */
.highlight-row td { background: #EFF6FF !important; font-weight: 500; }

/* ── Inline badge ─────────────────────────────────────────── */
.badge {
  display: inline-block; padding: 1pt 6pt;
  font-family: "Roboto Mono", monospace;
  font-size: 7pt; letter-spacing: 0.08em; text-transform: uppercase;
  font-weight: 500;
}
.badge-green { background: #DCFCE7; color: #166534; }
.badge-red { background: #FEE2E2; color: #991B1B; }
.badge-blue { background: #DBEAFE; color: #1E40AF; }
.badge-amber { background: #FEF3C7; color: #92400E; }
"""
