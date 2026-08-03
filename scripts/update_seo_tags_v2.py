import os
import re

BASE_URL = "https://blacmew.github.io/abhidhamma"
OG_IMAGE = f"{BASE_URL}/assets/og-image.jpg"
DEFAULT_TITLE = "Abhidhammattha Sangaha Visual Guide"
DEFAULT_DESC = "အဘိဓမ္မတ္ထသင်္ဂဟ Visual Guide — ဗုဒ္ဓဘာသာ အဘိဓမ္မာ တရားတော်များ လေ့လာရန်"
AUTHOR = "Maung Wunna Ko (မောင်ဝဏ္ဏကို)"

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

    title = extract_tag_content(html, "title") or DEFAULT_TITLE
    desc = extract_tag_content(html, "meta") or DEFAULT_DESC
    
    title_escaped = title.replace('"', '&quot;')
    desc_escaped = desc.replace('"', '&quot;')
    
    page_url = f"{BASE_URL}/{filename}" if filename != "index.html" else f"{BASE_URL}/"

    seo_block = f"""<!-- SEO & Open Graph Meta Tags -->
    <meta name="keywords" content="Abhidhamma, Buddhism, Meditation, Citta, Cetasika, Rupa, Paticcasamuppada, Dhamma, Myanmar, Burmese, အဘိဓမ္မာ, ဗုဒ္ဓဘာသာ, တရားတော်, Abhidhammattha-sangaha, အဘိဓမ္မာသင်္ဂဟကျမ်း">
    <meta name="author" content="{AUTHOR}">
    <meta name="publisher" content="{AUTHOR}">
    <meta name="robots" content="index, follow">
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
      "url": "{page_url}",
      "author": {{
        "@type": "Person",
        "name": "{AUTHOR}"
      }},
      "publisher": {{
        "@type": "Person",
        "name": "{AUTHOR}"
      }}
    }}
    </script>
</head>"""

    # First, strip out ALL instances of the SEO block (including </head> if they were stacked)
    # We remove anything from <!-- SEO & Open Graph Meta Tags --> up to the next </head>
    # Actually, it's safer to remove <!-- SEO ... to </script>\n (or similar) to preserve </head>
    cleaned_html = re.sub(r'<!-- SEO & Open Graph Meta Tags -->.*?</script>\s*', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # We might have removed </head> if we matched it in a previous bug, so let's make sure it's removed and we add exactly one
    cleaned_html = re.sub(r'</head>\s*', '', cleaned_html, flags=re.IGNORECASE)
    
    # Now inject exactly one seo_block (which ends with </head>)
    new_html = cleaned_html + "\n" + seo_block
    # But wait! We need to inject it where </head> was, which is before <body>.
    # If we removed </head>, let's just find <body> and insert the seo_block before it.
    
    # Actually, a better approach:
    # 1. Strip the blocks.
    html_no_blocks = re.sub(r'<!-- SEO & Open Graph Meta Tags -->.*?</script>\s*', '', html, flags=re.IGNORECASE | re.DOTALL)
    # 2. Make sure </head> exists. If the previous bug left multiple </head>s, clean them up.
    # Let's just find </head> and replace it with seo_block (which contains </head>).
    # Since html_no_blocks still has </head>, we can do:
    new_html = re.sub(r'</head>', seo_block, html_no_blocks, count=1, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Cleaned and updated SEO tags in {filename}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
    for f in html_files:
        process_file(f, f)
