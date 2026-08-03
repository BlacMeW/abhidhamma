import os
import re
import json

BASE_URL = "https://monledhamma.org/citta_cetasikas_visual_guide"
OG_IMAGE = f"{BASE_URL}/assets/og-image.jpg"
DEFAULT_TITLE = "Abhidhammattha Sangaha Visual Guide"
DEFAULT_DESC = "အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide — ဗုဒ္ဓဘာသာ အဘိဓမ္မာ တရားတော်များ လေ့လာရန်"

def extract_tag_content(html, tag_name, attr="content"):
    if tag_name == "title":
        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    elif tag_name == "meta":
        match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def process_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has og:title
    if "og:title" in html or "twitter:card" in html:
        print(f"Skipping {filename}, already has SEO tags.")
        return False

    title = extract_tag_content(html, "title") or DEFAULT_TITLE
    desc = extract_tag_content(html, "meta") or DEFAULT_DESC
    
    # Escape quotes for JSON-LD and meta tags
    title_escaped = title.replace('"', '&quot;')
    desc_escaped = desc.replace('"', '&quot;')
    
    page_url = f"{BASE_URL}/{filename}" if filename != "index.html" else f"{BASE_URL}/"

    seo_block = f"""
    <!-- SEO & Open Graph Meta Tags -->
    <meta name="keywords" content="Abhidhamma, Buddhism, Meditation, Citta, Cetasika, Rupa, Paticcasamuppada, Dhamma, Myanmar, Burmese, အဘိဓမ္မာ, ဗုဒ္ဓဘာသာ, တရားတော်">
    <meta property="og:title" content="{title_escaped}">
    <meta property="og:description" content="{desc_escaped}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_url}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:site_name" content="Abhidhammattha Sangaha Visual Guide">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_escaped}">
    <meta name="twitter:description" content="{desc_escaped}">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <link rel="canonical" href="{page_url}">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{title_escaped}",
      "description": "{desc_escaped}",
      "url": "{page_url}"
    }}
    </script>
</head>"""

    # Inject right before </head>
    new_html = re.sub(r'</head>', seo_block, html, flags=re.IGNORECASE)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Injected SEO tags into {filename}")
        return True
    return False

def generate_sitemap(html_files):
    sitemap_path = "sitemap.xml"
    urls = []
    
    # Push index.html to top
    if "index.html" in html_files:
        html_files.remove("index.html")
        html_files.insert(0, "index.html")

    for f in html_files:
        url = f"{BASE_URL}/{f}" if f != "index.html" else f"{BASE_URL}/"
        priority = "1.0" if f == "index.html" else "0.8"
        urls.append(f"""  <url>
    <loc>{url}</loc>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")
        
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"Generated {sitemap_path}")

def generate_robots():
    robots_path = "robots.txt"
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"Generated {robots_path}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
    
    for f in html_files:
        process_file(f, f)
        
    generate_sitemap(html_files)
    generate_robots()
