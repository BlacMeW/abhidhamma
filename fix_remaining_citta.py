import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

remaining_meanings = {
    "ဉာဏသမ္ပယုတ် ၄": "ဉာဏ်ပညာနှင့် ယှဉ်သော စိတ် ၄ ပါး",
    "ဉာဏဝိပ္ပယုတ် ၄": "ဉာဏ်ပညာနှင့် မယှဉ်သော စိတ် ၄ ပါး",
    "ပဌမဈာန် ကုသိုလ်": "ပဌမဈာန်နှင့် ယှဉ်သော ကုသိုလ်စိတ်",
    "ဒုတိယဈာန် ကုသိုလ်": "ဒုတိယဈာန်နှင့် ယှဉ်သော ကုသိုလ်စိတ်",
    "တတိယဈာန် ကုသိုလ်": "တတိယဈာန်နှင့် ယှဉ်သော ကုသိုလ်စိတ်",
    "စတုတ္ထဈာန် ကုသိုလ်": "စတုတ္ထဈာန်နှင့် ယှဉ်သော ကုသိုလ်စိတ်",
    "ပဉ္စမဈာန် ကုသိုလ်": "ပဉ္စမဈာန်နှင့် ယှဉ်သော ကုသိုလ်စိတ်",
    "ပဌမဈာန် ဝိပါက်": "ပဌမဈာန်နှင့် ယှဉ်သော ဝိပါက်စိတ်",
    "ဒုတိယဈာန် ဝိပါက်": "ဒုတိယဈာန်နှင့် ယှဉ်သော ဝိပါက်စိတ်",
    "တတိယဈာန် ဝိပါက်": "တတိယဈာန်နှင့် ယှဉ်သော ဝိပါက်စိတ်",
    "စတုတ္ထဈာန် ဝိပါက်": "စတုတ္ထဈာန်နှင့် ယှဉ်သော ဝိပါက်စိတ်",
    "ပဉ္စမဈာန် ဝိပါက်": "ပဉ္စမဈာန်နှင့် ယှဉ်သော ဝိပါက်စိတ်",
    "ပဌမဈာန် ကြိယာ": "ပဌမဈာန်နှင့် ယှဉ်သော ကြိယာစိတ်",
    "ဒုတိယဈာန် ကြိယာ": "ဒုတိယဈာန်နှင့် ယှဉ်သော ကြိယာစိတ်",
    "တတိယဈာန် ကြိယာ": "တတိယဈာန်နှင့် ယှဉ်သော ကြိယာစိတ်",
    "စတုတ္ထဈာန် ကြိယာ": "စတုတ္ထဈာန်နှင့် ယှဉ်သော ကြိယာစိတ်",
    "ပဉ္စမဈာန် ကြိယာ": "ပဉ္စမဈာန်နှင့် ယှဉ်သော ကြိယာစိတ်"
}

new_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    match = re.match(r'^(\s*)-\s+(.*)$', line.rstrip())
    if match:
        indent = match.group(1)
        name = match.group(2).strip()
        
        has_child = False
        if i + 1 < len(lines):
            next_match = re.match(r'^(\s*)-\s+(.*)$', lines[i+1].rstrip())
            if next_match and len(next_match.group(1)) > len(indent):
                has_child = True
                
        if name in remaining_meanings and not has_child:
            new_lines.append(line)
            new_lines.append(f"{indent}  - {remaining_meanings[name]}\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)
    i += 1

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Remaining Citta leaf nodes fixed")
