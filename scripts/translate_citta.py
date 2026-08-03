import re

def translate_citta(name):
    # Mapping
    meanings = []
    
    if "သောမနဿသဟဂုတ်" in name: meanings.append("ဝမ်းမြောက်ဝမ်းသာ")
    elif "ဒေါမနဿသဟဂုတ်" in name: meanings.append("စိတ်ဆင်းရဲစွာ")
    elif "ဥပေက္ခာသဟဂုတ်" in name: meanings.append("ဝမ်းသာခြင်း/ဝမ်းနည်းခြင်းမရှိဘဲ (လျစ်လျူရှုလျက်)")
    elif "သုခသဟဂုတ်" in name: meanings.append("ကိုယ်ချမ်းသာစွာ")
    elif "ဒုက္ခသဟဂုတ်" in name: meanings.append("ကိုယ်ဆင်းရဲစွာ")
    
    if "ဒိဋ္ဌိဂတသမ္ပယုတ်" in name: meanings.append("မှားယွင်းသောအမြင်(အယူ)နှင့် ယှဉ်၍")
    elif "ဒိဋ္ဌိဂတဝိပ္ပယုတ်" in name: meanings.append("မှားယွင်းသောအမြင်(အယူ)နှင့် မယှဉ်ဘဲ")
    elif "ပဋိဃသမ္ပယုတ်" in name: meanings.append("ဒေါသ(ငြူစူခြင်း)နှင့် ယှဉ်၍")
    elif "ဝိစိကိစ္ဆာသမ္ပယုတ်" in name: meanings.append("ယုံမှားသံသယနှင့် ယှဉ်၍")
    elif "ဥဒ္ဓစ္စသမ္ပယုတ်" in name: meanings.append("ပျံ့လွင့်ခြင်းနှင့် ယှဉ်၍")
    elif "ဉာဏသမ္ပယုတ်" in name: meanings.append("အသိဉာဏ်ပညာနှင့် ယှဉ်၍")
    elif "ဉာဏဝိပ္ပယုတ်" in name: meanings.append("အသိဉာဏ်ပညာနှင့် မယှဉ်ဘဲ")
    
    if "အသင်္ခါရိက" in name: meanings.append("တိုက်တွန်းမှုမပါဘဲ အလိုအလျောက် ဖြစ်သောစိတ်")
    elif "သသင်္ခါရိက" in name: meanings.append("တိုက်တွန်းမှုကြောင့် ဖြစ်သောစိတ်")
    
    if not meanings:
        return None
    
    # Check if "ဖြစ်သောစိတ်" is already at the end, if not add it unless it's just one or two words.
    result = " ".join(meanings)
    if not "ဖြစ်သောစိတ်" in result and len(meanings) > 0:
        if "ယှဉ်၍" in result:
             result += " ဖြစ်သောစိတ်"
        
    return result

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_citta = False

for line in lines:
    if line.strip().startswith("## စိတ် (၈၉ / ၁၂၁)"):
        in_citta = True
    elif line.strip().startswith("## စေတသိက်"):
        in_citta = False
        
    if in_citta and line.strip().startswith("- ") and "ဟဂုတ်" in line:
        # It's a citta name
        match = re.match(r'^(\s*)-\s+(.*)$', line)
        if match:
            indent = match.group(1)
            name = match.group(2).strip()
            
            # Remove any trailing spaces or html
            name_clean = name.split("<")[0].strip()
            
            translation = translate_citta(name_clean)
            if translation:
                new_lines.append(f"{indent}- {name}\n")
                new_lines.append(f"{indent}  - {translation}\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
    
print("Citta translation applied.")
