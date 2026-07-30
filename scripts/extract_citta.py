import re

file_path = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/citta_cetasikas_visual_guide.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'let cittaData = \[\];\s*\(function buildCittaData\(\) \{.*?\n        \}\)\(\);', content, flags=re.DOTALL)
if m:
    with open('build_citta.js', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
    print("Extracted to build_citta.js")
else:
    print("Not found")
