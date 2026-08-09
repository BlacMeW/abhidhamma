const fs = require('fs');
const path = require('path');

const dir = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const keywords = "Abhidhamma, Buddhism, Meditation, Citta, Cetasika, Rupa, Paticcasamuppada, Dhamma, Myanmar, Burmese, အဘိဓမ္မာ, ဗုဒ္ဓဘာသာ, တရားတော်, Abhidhammattha-sangaha, အဘိဓမ္မာသင်္ဂဟကျမ်း, wunna ko, mg wunna ko";

for (const file of files) {
    if (file === 'google4a5c1bb163d6a397.html' || file === '404.html') continue;
    let content = fs.readFileSync(path.join(dir, file), 'utf8');

    // Extract title
    const titleMatch = content.match(/<title>(.*?)<\/title>/);
    let title = titleMatch ? titleMatch[1] : 'အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide';

    // Extract description
    const descMatch = content.match(/<meta name="description" content="(.*?)">/);
    let description = descMatch ? descMatch[1] : 'အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide — ပရိစ္ဆေဒ (၉) ခန်းလုံး၏ ပင်မ Dashboard နှင့် visual guides စုစည်းမှု';

    const url = `https://blacmew.github.io/abhidhamma/${file === 'index.html' ? '' : file}`;
    const imgName = file === 'index.html' ? 'og-image.jpg' : `og-${file.replace('.html', '.jpg')}`;
    const imgUrl = `https://blacmew.github.io/abhidhamma/assets/${imgName}`;

    // Regex to find SEO block
    const seoBlockRegex = /<!-- SEO & Open Graph Meta Tags -->[\s\S]*?<\/script>/;
    
    const newSeoBlock = `<!-- SEO & Open Graph Meta Tags -->
    <meta name="keywords" content="${keywords}">
    <meta name="author" content="Maung Wunna Ko (မောင်ဝဏ္ဏကို)">
    <meta name="publisher" content="Maung Wunna Ko (မောင်ဝဏ္ဏကို)">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="${url}">
    <meta property="og:image" content="${imgUrl}">
    <meta property="og:site_name" content="Abhidhammattha Sangaha Visual Guide">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:description" content="${description}">
    <meta name="twitter:image" content="${imgUrl}">
    <link rel="canonical" href="${url}">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "${title}",
      "description": "${description}",
      "url": "${url}",
      "author": {
        "@type": "Person",
        "name": "Maung Wunna Ko (မောင်ဝဏ္ဏကို)"
      },
      "publisher": {
        "@type": "Person",
        "name": "Maung Wunna Ko (မောင်ဝဏ္ဏကို)"
      }
    }
    </script>`;

    if (seoBlockRegex.test(content)) {
        content = content.replace(seoBlockRegex, newSeoBlock);
    } else {
        // If not found, insert before </head>
        content = content.replace('</head>', `\n    ${newSeoBlock}\n</head>`);
    }

    fs.writeFileSync(path.join(dir, file), content, 'utf8');
    console.log(`Updated ${file}`);
}

// Update sitemap.xml with lastmod
const sitemapPath = path.join(dir, 'sitemap.xml');
if (fs.existsSync(sitemapPath)) {
    let sitemapContent = fs.readFileSync(sitemapPath, 'utf8');
    const today = new Date().toISOString().split('T')[0];
    
    // Replace <priority>...</priority> with <priority>...</priority>\n    <lastmod>${today}</lastmod> if it doesn't have lastmod
    // First, let's just make sure lastmod is there.
    
    // Instead of complex regex, let's parse and reconstruct minimally or use regex.
    // Each <url> block:
    const urls = sitemapContent.match(/<url>[\s\S]*?<\/url>/g);
    if (urls) {
        let updatedSitemap = sitemapContent;
        urls.forEach(u => {
            if (!u.includes('<lastmod>')) {
                const newU = u.replace(/(<\/priority>)/, `$1\n    <lastmod>${today}</lastmod>`);
                updatedSitemap = updatedSitemap.replace(u, newU);
            } else {
                const newU = u.replace(/<lastmod>.*?<\/lastmod>/, `<lastmod>${today}</lastmod>`);
                updatedSitemap = updatedSitemap.replace(u, newU);
            }
        });
        fs.writeFileSync(sitemapPath, updatedSitemap, 'utf8');
        console.log('Updated sitemap.xml');
    }
}
