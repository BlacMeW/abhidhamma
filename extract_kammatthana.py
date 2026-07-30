import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/kammatthana_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const kammatthanaData = \[.*?\];', content, flags=re.DOTALL)
if m:
    with open('kammatthana_data.txt', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
    print("Extracted to kammatthana_data.txt")
else:
    print("Not found")
