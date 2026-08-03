import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

vithi_meanings = {
    "အတီတဘဝင်": "လွန်လေပြီးသော ဘဝင်",
    "ဘဝင်္ဂစလန": "လှုပ်ရှားသော ဘဝင်",
    "ဘဝင်္ဂုပစ္ဆေဒ": "ပြတ်စဲသော ဘဝင်",
    "ပဉ္စဒွါရာဝဇ္ဇန်း": "အာရုံ ၅ ပါးကို ဆင်ခြင်သောစိတ်",
    "စက္ခုဝိညာဉ်": "မြင်သိစိတ်",
    "သမ္ပဋိစ္ဆိုင်း": "အာရုံကို လက်ခံသောစိတ်",
    "သန္တီရဏ": "အာရုံကို စူးစမ်းသောစိတ်",
    "ဝုဋ္ဌော": "အာရုံကို ဆုံးဖြတ်သောစိတ်",
    "ဇော ၇ ကြိမ်": "အာရုံကို ခံစား/အားထုတ်သောစိတ် ၇ ကြိမ်",
    "တဒါရုံ ၂ ကြိမ်": "ဇော၏အာရုံကို ဆက်လက်ခံစားသောစိတ် ၂ ကြိမ်",
    "မနောဒွါရာဝဇ္ဇန်း": "ဓမ္မာရုံကို ဆင်ခြင်သောစိတ်",
    "ပရိကံ": "ပြင်ဆင်မှု",
    "ဥပစာ": "အနီးအပါး",
    "အနုလုံ": "လျော်ညီမှု",
    "ဂေါတြဘူ": "အနွယ်ကို ဖြတ်ခြင်း/ကူးပြောင်းခြင်း",
    "ဇော ၁ ကြိမ်": "အာရုံကို ခံစား/အားထုတ်သောစိတ် ၁ ကြိမ်"
}

new_lines = []
in_vithi = False
i = 0

while i < len(lines):
    line = lines[i]
    if line.strip().startswith("## ဝီထိ (ဖြစ်စဉ်)"):
        in_vithi = True
    elif line.strip().startswith("## ဝီထိမုတ္တ"):
        in_vithi = False
        
    if in_vithi:
        match = re.match(r'^(\s*)-\s+(.*)$', line.rstrip())
        if match:
            indent = match.group(1)
            name = match.group(2).strip()
            
            # Check if this line already has a child with meaning below it
            has_child = False
            if i + 1 < len(lines):
                next_match = re.match(r'^(\s*)-\s+(.*)$', lines[i+1].rstrip())
                if next_match and len(next_match.group(1)) > len(indent):
                    has_child = True
                    
            if name in vithi_meanings and not has_child:
                new_lines.append(line)
                new_lines.append(f"{indent}  - {vithi_meanings[name]}\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)
    i += 1

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Vithi completely fixed")
