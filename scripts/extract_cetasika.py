import re

file_path = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/citta_cetasikas_visual_guide.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const cetasikaData = \[.*?\n        \];', content, flags=re.DOTALL)
if m:
    with open('build_cetasika.js', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
    print("Extracted to build_cetasika.js")
else:
    print("Not found")
