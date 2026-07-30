import re
with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/paccaya_sangaha.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'(const paccayaData = \[.*?\];)', text, flags=re.DOTALL)
with open('paccaya_data.js', 'w', encoding='utf-8') as f:
    for m in matches:
        f.write(m.group(1) + '\n\n')
