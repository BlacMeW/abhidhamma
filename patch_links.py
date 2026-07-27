import os
import re

link_str = """                <a href="glossary.html" class="text-xs font-semibold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 px-3.5 py-2 rounded-full transition flex items-center gap-1.5">
                    <i class="fa-solid fa-spell-check"></i> <span class="hidden sm:inline">အဘိဓာန်</span>
                </a>"""

for f in os.listdir('.'):
    if f.endswith('.html') and f != 'glossary.html':
        with open(f, 'r') as file:
            content = file.read()
        
        pattern = r'(\s*<a href="matika\.html")'
        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\n' + link_str + r'\1', content, count=1)
            with open(f, 'w') as file:
                file.write(new_content)
            print(f"Updated {f}")
