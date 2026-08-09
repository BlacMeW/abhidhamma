/*
 * defer_fontawesome.js — make the Font Awesome CDN stylesheet non-render-blocking.
 * Replaces the blocking <link rel="stylesheet"> with the media="print" swap trick
 * plus a <noscript> fallback. Idempotent: skips files already converted.
 *
 * Run:  node scripts/defer_fontawesome.js
 */
const fs = require('fs');
const path = require('path');

const dir = path.resolve(__dirname, '..');
const FA = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
// Matches the FA <link> in either attribute order, self-closing or not.
const linkRe = new RegExp(`<link\\b[^>]*${FA.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\$&')}[^>]*>`, 'i');

const deferred =
  `<link rel="stylesheet" href="${FA}" media="print" onload="this.media='all'">` +
  `<noscript><link rel="stylesheet" href="${FA}"></noscript>`;

let changed = 0;
for (const file of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
  const full = path.join(dir, file);
  let html = fs.readFileSync(full, 'utf8');
  if (!html.includes('font-awesome')) continue;
  if (html.includes("this.media='all'")) { continue; } // already deferred
  const m = html.match(linkRe);
  if (!m) continue;
  html = html.replace(m[0], deferred);
  fs.writeFileSync(full, html, 'utf8');
  console.log(`  ✓ deferred FA in ${file}`);
  changed++;
}
console.log(`\nFont Awesome deferred in ${changed} file(s).`);
