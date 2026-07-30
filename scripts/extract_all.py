import re
with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/pakinnaka_sangaha.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'(const \w+Data = \[.*?\];)', text, flags=re.DOTALL)
with open('pakinnaka_data.js', 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(m.group(1) + '\n\n')

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/pakinnaka_sangaha.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(const dvaradata = \[.*?\];)', text, flags=re.DOTALL)
if m:
    with open('pakinnaka_data.js', 'a', encoding='utf-8') as f:
        f.write(m.group(1) + '\n\n')
