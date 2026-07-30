import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/paticcasamuppada.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const nidanaData = \[.*?\];', content, flags=re.DOTALL)
if m:
    with open('nidana_data.txt', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
    print("Extracted to nidana_data.txt")
else:
    print("Not found")
