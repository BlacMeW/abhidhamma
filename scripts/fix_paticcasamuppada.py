import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

paticca_meanings = {
    "အဝိဇ္ဇာ": "အမှန်တရားကို မသိခြင်း",
    "သင်္ခါရ": "ပြုပြင်စီမံမှု (ကံတရားများ)",
    "ဝိညာဏ်": "သိမှု (ပဋိသန္ဓေစိတ်)",
    "နာမ်ရုပ်": "စိတ်နှင့် ရုပ် (ခန္ဓာ)",
    "သဠာယတန": "အာရုံခံ အကြည်ဓာတ် ခြောက်ပါး",
    "ဖဿ": "အာရုံနှင့် တွေ့ထိမှု",
    "ဝေဒနာ": "ခံစားမှု",
    "တဏှာ": "တပ်မက်မှု",
    "ဥပါဒါန်": "ပြင်းပြစွာ စွဲလမ်းမှု",
    "ဘဝ": "ဖြစ်တည်မှု (ကမ္မဘဝ၊ ဥပပတ္တိဘဝ)",
    "ဇာတိ": "ပဋိသန္ဓေနေခြင်း (မွေးဖွားခြင်း)",
    "ဇရာ-မရဏ": "အိုခြင်းနှင့် သေခြင်း"
}

new_lines = []
in_paticca = False
i = 0

while i < len(lines):
    line = lines[i]
    if line.strip().startswith("### ပဋိစ္စသမုပ္ပါဒ်"):
        in_paticca = True
    elif line.strip().startswith("### ပဋ္ဌာန်း"):
        in_paticca = False
        
    if in_paticca:
        match = re.match(r'^(\s*)-\s+(.*)$', line.rstrip())
        if match:
            indent = match.group(1)
            name = match.group(2).strip()
            
            has_child = False
            if i + 1 < len(lines):
                next_match = re.match(r'^(\s*)-\s+(.*)$', lines[i+1].rstrip())
                if next_match and len(next_match.group(1)) > len(indent):
                    has_child = True
                    
            if name in paticca_meanings and not has_child:
                new_lines.append(line)
                new_lines.append(f"{indent}  - {paticca_meanings[name]}\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)
    i += 1

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Paticcasamuppada fixed")
