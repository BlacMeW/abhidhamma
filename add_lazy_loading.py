import os
import re

def add_lazy_loading(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all <img ...> tags
    # Add loading="lazy" if it doesn't already exist
    def replacer(match):
        img_tag = match.group(0)
        if 'loading=' not in img_tag:
            # Insert loading="lazy" before the closing bracket
            return img_tag[:-1] + ' loading="lazy">'
        return img_tag

    new_html = re.sub(r'<img\s+[^>]+>', replacer, html, flags=re.IGNORECASE)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Added lazy loading to images in {filename}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
    for f in html_files:
        add_lazy_loading(f, f)
