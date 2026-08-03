import os
import re

def add_keywords(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_keywords = ", Abhidhammattha-sangaha, အဘိဓမ္မာသင်္ဂဟကျမ်း"
    # Find the keywords meta tag and append if not already there
    if new_keywords not in html:
        # Regex to match the existing keywords content
        # <meta name="keywords" content="Abhidhamma, ... , တရားတော်">
        new_html = re.sub(r'(<meta name="keywords" content="[^"]+)(">)', r'\1' + new_keywords + r'\2', html, flags=re.IGNORECASE)
        
        if new_html != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Updated keywords in {filename}")

if __name__ == "__main__":
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and os.path.isfile(f)]
    for f in html_files:
        add_keywords(f, f)
