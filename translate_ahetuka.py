import re

meanings_dict = {
    "စက္ခုဝိညာဉ်": "အဆင်းကို မြင်သိစိတ်",
    "သောတဝိညာဉ်": "အသံကို ကြားသိစိတ်",
    "ဃာနဝိညာဉ်": "အနံ့ကို နံသိစိတ်",
    "ဇိဝှာဝိညာဉ်": "အရသာကို သိသောစိတ်",
    "ကာယဝိညာဉ်": "အတွေ့အထိကို သိသောစိတ်",
    "သမ္ပဋိစ္ဆိုင်း": "အာရုံကို လက်ခံသောစိတ်",
    "သန္တီရဏ": "အာရုံကို စူးစမ်းဆင်ခြင်သောစိတ်",
    "ပဉ္စဒွါရာဝဇ္ဇန်း": "အာရုံ ၅ ပါးကို ဆင်ခြင်သောစိတ်",
    "မနောဒွါရာဝဇ္ဇန်း": "ဓမ္မာရုံကို ဆင်ခြင်သောစိတ်",
    "ဟသိတုပ္ပါဒ်": "ဘုရား ရဟန္တာတို့၏ ပြုံးရယ်သောစိတ်"
}

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_citta = False

for line in lines:
    if line.strip().startswith("## စိတ် (၈၉ / ၁၂၁)"):
        in_citta = True
    elif line.strip().startswith("## စေတသိက်"):
        in_citta = False
        
    match = re.match(r'^(\s*)-\s+(.*)$', line)
    
    if in_citta and match:
        indent = match.group(1)
        name = match.group(2).strip()
        
        # Don't translate headers
        if "(" in name and not "သန္တီရဏ" in name: 
            new_lines.append(line)
            continue
            
        found = False
        for k, v in meanings_dict.items():
            if k in name and "သန္တီရဏ" not in k: # exact match or subset
                new_lines.append(line)
                new_lines.append(f"{indent}  - {v}\n")
                found = True
                break
            elif k == "သန္တီရဏ" and "သန္တီရဏ" in name:
                # Add meaning to existing child node if it has one (like ဥပေက္ခာသဟဂုတ်)
                # We'll just leave it or append it to the next line.
                # Actually, our previous script put a child node with partial translation for it.
                # Let's just fix it by string replacement below.
                pass
                
        if not found:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
