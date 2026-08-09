/*
 * update_seo.js — Site-wide SEO metadata + sitemap generator
 * ----------------------------------------------------------
 * For every page it (re)writes a single SEO block containing:
 *   - keywords / author / publisher / robots
 *   - Open Graph + Twitter Card tags (incl. og:locale my_MM, image dims)
 *   - canonical link
 *   - JSON-LD structured data, typed per page (WebSite / Article /
 *     WebApplication / DefinedTermSet / CollectionPage / WebPage) plus a
 *     BreadcrumbList for every non-home page.
 * It then regenerates sitemap.xml from the actual .html files with tiered
 * priorities and today's <lastmod>.
 *
 * Run:  node scripts/update_seo.js   (or `npm run seo`)
 */

const fs = require('fs');
const path = require('path');

const dir = path.resolve(__dirname, '..');
const BASE = 'https://blacmew.github.io/abhidhamma/';
const SITE_NAME = 'Abhidhammattha Sangaha Visual Guide';
const AUTHOR = 'Maung Wunna Ko (မောင်ဝဏ္ဏကို)';
const DEFAULT_IMG = 'og-image.jpg';
const DEFAULT_TITLE = 'အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide';
const DEFAULT_DESC = 'အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide — ပရိစ္ဆေဒ (၉) ခန်းလုံး၏ ပင်မ Dashboard နှင့် visual guides စုစည်းမှု';

const keywords = 'Abhidhamma, Buddhism, Meditation, Citta, Cetasika, Rupa, Paticcasamuppada, Dhamma, Myanmar, Burmese, အဘិဓမ္မာ, ဗုဒ္ဓဘာသာ, တရားတော်, Abhidhammattha-sangaha, အဘိဓမ္မာသင်္ဂဟကျမ်း, wunna ko, mg wunna ko';

// Files that must never receive SEO tags or appear in the sitemap.
const SKIP = new Set(['google4a5c1bb163d6a397.html', '404.html']);

// ---- Per-page classification -------------------------------------------
// Core doctrinal chapters — highest content value.
const DOCTRINE = new Set([
  'bodhipakkhiya_dhamma', 'citta_cetasikas_visual_guide', 'kilesa_sangaha',
  'missaka_sangaha', 'paccaya_sangaha', 'pakinnaka_sangaha', 'pannatti',
  'paticcasamuppada', 'rupa_sangaha', 'sabba_sangaha', 'vithi_sangaha',
  'vithimutta_sangaha', 'kammatthana_sangaha',
]);
// Practice / meditation guides (read-oriented Articles).
const GUIDE = new Set([
  'satipatthana_guide', 'satipatthana_prompter', 'metta_bhavana_guide',
  'kasina_guide', 'anapana_visualizer',
]);
// Interactive tools (WebApplication).
const WEBAPP = new Set([
  'anapana_counter', 'meditation_timer', 'metta_prompter',
  'kasina_simulator', 'emotion_analyzer',
]);

function classify(base) {
  if (base === 'index') return { schema: 'WebSite', priority: '1.0', changefreq: 'weekly' };
  if (base === 'glossary') return { schema: 'DefinedTermSet', priority: '0.8', changefreq: 'monthly' };
  if (base === 'library') return { schema: 'CollectionPage', priority: '0.7', changefreq: 'monthly' };
  if (base === 'concept_map') return { schema: 'WebPage', priority: '0.8', changefreq: 'monthly' };
  if (DOCTRINE.has(base)) return { schema: 'Article', priority: '0.9', changefreq: 'monthly' };
  if (GUIDE.has(base)) return { schema: 'Article', priority: '0.8', changefreq: 'monthly' };
  if (WEBAPP.has(base)) return { schema: 'WebApplication', priority: '0.7', changefreq: 'monthly' };
  return { schema: 'WebPage', priority: '0.7', changefreq: 'monthly' };
}

// ---- Robust extractors (tolerate attribute-order / self-closing/case) ---
function extractTitle(html) {
  const m = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  return m ? m[1].trim() : null;
}
function extractDescription(html) {
  // Locate the head-level <meta name="description" ...> regardless of
  // attribute order, then pull its content=".." value.
  const tag = html.match(/<meta\b[^>]*\bname=["']description["'][^>]*>/i);
  if (!tag) return null;
  const c = tag[0].match(/\bcontent=["']([\s\S]*?)["']/i);
  return c ? c[1].trim() : null;
}

const publisherNode = {
  '@type': 'Person',
  name: AUTHOR,
};

function buildGraph(schema, { base, title, description, url, imgUrl, today }) {
  const author = { '@type': 'Person', name: AUTHOR };
  const website = {
    '@type': 'WebSite',
    '@id': `${BASE}#website`,
    name: SITE_NAME,
    url: BASE,
    inLanguage: 'my',
    publisher: publisherNode,
  };
  const graph = [];

  if (schema === 'WebSite') {
    graph.push({
      ...website,
      description,
      author,
    });
  } else if (schema === 'Article') {
    graph.push({
      '@type': 'Article',
      headline: title,
      description,
      url,
      inLanguage: 'my',
      image: imgUrl,
      dateModified: today,
      mainEntityOfPage: { '@type': 'WebPage', '@id': url },
      isPartOf: { '@id': `${BASE}#website` },
      author,
      publisher: publisherNode,
    });
  } else if (schema === 'WebApplication') {
    graph.push({
      '@type': 'WebApplication',
      name: title,
      description,
      url,
      inLanguage: 'my',
      applicationCategory: 'EducationApplication',
      operatingSystem: 'Web',
      isPartOf: { '@id': `${BASE}#website` },
      offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
      author,
      publisher: publisherNode,
    });
  } else if (schema === 'DefinedTermSet') {
    graph.push({
      '@type': 'DefinedTermSet',
      name: title,
      description,
      url,
      inLanguage: 'my',
      isPartOf: { '@id': `${BASE}#website` },
      publisher: publisherNode,
    });
  } else if (schema === 'CollectionPage') {
    graph.push({
      '@type': 'CollectionPage',
      name: title,
      description,
      url,
      inLanguage: 'my',
      isPartOf: { '@id': `${BASE}#website` },
      publisher: publisherNode,
    });
  } else {
    graph.push({
      '@type': 'WebPage',
      name: title,
      description,
      url,
      inLanguage: 'my',
      isPartOf: { '@id': `${BASE}#website` },
      author,
      publisher: publisherNode,
    });
  }

  // Breadcrumb for every page except the home dashboard.
  if (base !== 'index') {
    graph.push({
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'ပင်မ (Home)', item: BASE },
        { '@type': 'ListItem', position: 2, name: title, item: url },
      ],
    });
  }

  return { '@context': 'https://schema.org', '@graph': graph };
}

function buildSeoBlock({ base, title, description, url, imgUrl, jsonLd }) {
  return `<!-- SEO & Open Graph Meta Tags -->
    <meta name="keywords" content="${keywords}">
    <meta name="author" content="${AUTHOR}">
    <meta name="publisher" content="${AUTHOR}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description}">
    <meta property="og:type" content="${base === 'index' ? 'website' : 'article'}">
    <meta property="og:url" content="${url}">
    <meta property="og:image" content="${imgUrl}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="${title}">
    <meta property="og:locale" content="my_MM">
    <meta property="og:site_name" content="${SITE_NAME}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:description" content="${description}">
    <meta name="twitter:image" content="${imgUrl}">
    <link rel="canonical" href="${url}">
    <script type="application/ld+json">
${JSON.stringify(jsonLd, null, 2)}
    </script>`;
}

// ---- Main pass ----------------------------------------------------------
const today = new Date().toISOString().split('T')[0];
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && !SKIP.has(f));
const sitemapEntries = [];
let warnings = 0;

for (const file of files) {
  const base = file.replace(/\.html$/, '');
  const fullPath = path.join(dir, file);
  let content = fs.readFileSync(fullPath, 'utf8');

  const title = extractTitle(content) || DEFAULT_TITLE;
  let description = extractDescription(content);
  if (!description) {
    description = DEFAULT_DESC;
    console.warn(`  ⚠  ${file}: no <meta name="description"> — using generic fallback. Add a unique one!`);
    warnings++;
  }

  const url = `${BASE}${base === 'index' ? '' : file}`;
  // Use a page-specific OG image if it exists, else the shared default.
  const perPageImg = `og-${base}.jpg`;
  const imgName = fs.existsSync(path.join(dir, 'assets', perPageImg)) ? perPageImg : DEFAULT_IMG;
  const imgUrl = `${BASE}assets/${imgName}`;

  const { schema, priority, changefreq } = classify(base);
  const jsonLd = buildGraph(schema, { base, title, description, url, imgUrl, today });
  const seoBlock = buildSeoBlock({ base, title, description, url, imgUrl, jsonLd });

  const seoBlockRegex = /<!-- SEO & Open Graph Meta Tags -->[\s\S]*?<\/script>/;
  if (seoBlockRegex.test(content)) {
    content = content.replace(seoBlockRegex, seoBlock);
  } else {
    content = content.replace(/<\/head>/i, `\n    ${seoBlock}\n</head>`);
  }

  fs.writeFileSync(fullPath, content, 'utf8');
  sitemapEntries.push({ url, priority, changefreq });
  console.log(`  ✓ ${file}  [${schema}, p=${priority}]`);
}

// ---- Regenerate sitemap.xml --------------------------------------------
// Sort by priority desc so the most important URLs appear first.
sitemapEntries.sort((a, b) => parseFloat(b.priority) - parseFloat(a.priority));
const sitemap =
  `<?xml version="1.0" encoding="UTF-8"?>\n` +
  `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
  sitemapEntries
    .map(e =>
      `  <url>\n` +
      `    <loc>${e.url}</loc>\n` +
      `    <changefreq>${e.changefreq}</changefreq>\n` +
      `    <priority>${e.priority}</priority>\n` +
      `    <lastmod>${today}</lastmod>\n` +
      `  </url>`)
    .join('\n') +
  `\n</urlset>\n`;

fs.writeFileSync(path.join(dir, 'sitemap.xml'), sitemap, 'utf8');
console.log(`\nsitemap.xml regenerated with ${sitemapEntries.length} URLs.`);
if (warnings) console.log(`${warnings} page(s) still need a unique description.`);
