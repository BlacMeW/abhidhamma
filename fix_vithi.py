import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

vithi_replacements = {
    "    - အတီတဘဝင်": "    - အတီတဘဝင်\n      - လွန်လေပြီးသော ဘဝင်",
    "    - ဘဝင်္ဂစလန": "    - ဘဝင်္ဂစလန\n      - လှုပ်ရှားသော ဘဝင်",
    "    - ဘဝင်္ဂုပစ္ဆေဒ": "    - ဘဝင်္ဂုပစ္ဆေဒ\n      - ပြတ်စဲသော ဘဝင်",
    "    - ပဉ္စဒွါရာဝဇ္ဇန်း": "    - ပဉ္စဒွါရာဝဇ္ဇန်း\n      - အာရုံ ၅ ပါးကို ဆင်ခြင်သောစိတ်",
    "    - စက္ခုဝိညာဉ်": "    - စက္ခုဝိညာဉ်\n      - မြင်သိစိတ်",
    "    - သမ္ပဋိစ္ဆိုင်း": "    - သမ္ပဋိစ္ဆိုင်း\n      - အာရုံကို လက်ခံသောစိတ်",
    "    - သန္တီရဏ": "    - သန္တီရဏ\n      - အာရုံကို စူးစမ်းသောစိတ်",
    "    - ဝုဋ္ဌော": "    - ဝုဋ္ဌော\n      - အာရုံကို ဆုံးဖြတ်သောစိတ်",
    "    - ဇော ၇ ကြိမ်": "    - ဇော ၇ ကြိမ်\n      - အာရုံကို ခံစား/အားထုတ်သောစိတ် ၇ ကြိမ်",
    "    - တဒါရုံ ၂ ကြိမ်": "    - တဒါရုံ ၂ ကြိမ်\n      - ဇော၏အာရုံကို ဆက်လက်ခံစားသောစိတ် ၂ ကြိမ်",
    "    - မနောဒွါရာဝဇ္ဇန်း": "    - မနောဒွါရာဝဇ္ဇန်း\n      - ဓမ္မာရုံကို ဆင်ခြင်သောစိတ်",
    "    - ပရိကံ": "    - ပရိကံ\n      - ပြင်ဆင်မှု",
    "    - ဥပစာ": "    - ဥပစာ\n      - အနီးအပါး",
    "    - အနုလုံ": "    - အနုလုံ\n      - လျော်ညီမှု",
    "    - ဂေါတြဘူ": "    - ဂေါတြဘူ\n      - အနွယ်ကို ဖြတ်ခြင်း/ကူးပြောင်းခြင်း"
}

# The problem is that there might be trailing spaces or slight indentation differences.
# We will iterate line by line to do replacements.

lines = content.split('\n')
new_lines = []
in_vithi = False

for line in lines:
    if line.strip().startswith("## ဝီထိ"):
        in_vithi = True
    elif line.strip().startswith("## ဝီထိမုတ္တ"):
        in_vithi = False
        
    if in_vithi:
        matched = False
        for k, v in vithi_replacements.items():
            # Check if line matches exactly except for trailing spaces
            if line.rstrip() == k:
                new_lines.append(v)
                matched = True
                break
        if not matched:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Vithi fixed")
