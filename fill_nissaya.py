import re

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Hardcoded precise nissayas for prominent terms
hardcoded = {
    'Adhikāra': 'အဓိကာရော - အုပ်စိုးခြင်း၊ လွှမ်းမိုးခြင်း၊ အဓိကဖြစ်ခြင်း',
    'Adhimokkha': 'အဓိမောက္ခော - အာရုံကို ဆုံးဖြတ်ခြင်း သဘောတရား',
    'Adosa': 'အဒေါသော - မကြမ်းတမ်းခြင်း၊ မေတ္တာထားခြင်း သဘောတရား',
    'Ahetuka': 'အဟေတုကံ - ဟေတု (လောဘ၊ ဒေါသ စသည့် အမြစ်) မပါဝင်သော (စိတ်)',
    'Ahirika': 'အဟိရိကံ - ဒုစရိုက်ပြုရမည်ကို မရှက်ခြင်း သဘောတရား',
    'Alobha': 'အလောဘော - မလိုချင်ခြင်း၊ မတပ်မက်ခြင်း၊ စွန့်လွှတ်ခြင်း သဘောတရား',
    'Amoha': 'အမောဟော - အမှန်အတိုင်း သိမြင်ခြင်း သဘောတရား',
    'Anattā': 'အနတ္တာ - အစိုးမရခြင်း၊ အတ္တမဟုတ်ခြင်း',
    'Aniccatā': 'အနိစ္စတာ - မမြဲခြင်း သဘော',
    'Anottappa': 'အနောတ္တပ္ပံ - ဒုစရိုက်ပြုရမည်ကို မကြောက်ခြင်း',
    'Arūpa': 'အရူပံ - ရုပ်မရှိသော (နာမ်တရား)',
    'Asaṅkhārika': 'အသင်္ခါရိကံ - တိုက်တွန်းမှု မပါဘဲ မိမိအလိုအလျောက် ထက်မြက်စွာ ဖြစ်ပေါ်သော (စိတ်)',
    'Avijjā': 'အဝိဇ္ဇာ - သစ္စာလေးပါးကို မသိခြင်း (မောဟ)',
    'Bala': 'ဗလံ - ဆန့်ကျင်ဘက်တရားတို့ကို မတုန်လှုပ်စေသော အစွမ်းခွန်အား',
    'Bhava': 'ဘဝေါ - ဖြစ်တည်မှု',
    'Bhavaṅga': 'ဘဝင်္ဂံ - ဘဝ၏ အင်္ဂါ၊ ဘဝကို ဆက်စပ်ပေးသော (စိတ်)',
    'Bhāvanā': 'ဘာဝနာ - ပွားများအားထုတ်ခြင်း',
    'Bojjhaṅga': 'ဗောဇ္ဈင်္ဂံ - သစ္စာလေးပါးကို သိရန် အထောက်အကူပြုသော အင်္ဂါ',
    'Cetanā': 'စေတနာ - တိုက်တွန်းနှိုးဆော်တတ်သော သဘောတရား',
    'Cetasika': 'စေတသိကံ - စိတ်၌ မှီ၍ဖြစ်သော (တရား)',
    'Citta': 'စိတ္တံ - အာရုံကို သိတတ်သော (တရား)',
    'Dosa': 'ဒေါသော - ကြမ်းတမ်းခြင်း၊ စိတ်ဆိုးခြင်း၊ ဖျက်ဆီးလိုခြင်း သဘောတရား',
    'Kusala': 'ကုသလံ - အပြစ်ကင်း၍ ကောင်းမြတ်သော အကျိုးကိုပေးတတ်သော (တရား)',
    'Akusala': 'အကုသလံ - အပြစ်ရှိ၍ ဆင်းရဲသောအကျိုးကို ပေးတတ်သော (တရား)',
    'Lobha': 'လောဘော - လိုချင်တပ်မက်ခြင်း သဘောတရား',
    'Moha': 'မောဟော - အာရုံ၏ သဘောမှန်ကို မသိခြင်း၊ တွေဝေခြင်း',
    'Rūpa': 'ရူပံ - ဖောက်ပြန်တတ်သော သဘောတရား (ရုပ်)',
    'Nibbāna': 'နိဗ္ဗာနံ - တဏှာမှ ထွက်မြောက်ရာ (နိဗ္ဗာန်)'
}

def replacer(match):
    block = match.group(0)
    
    # Extract existing fields
    term_my_m = re.search(r"term_my:\s*'([^']*)'", block)
    pali_eng_m = re.search(r"pali_eng:\s*'([^']*)'", block)
    meaning_m = re.search(r"meaning:\s*'([^']*)'", block)
    nissaya_m = re.search(r"nissaya:\s*'([^']*)'", block)
    
    if term_my_m and meaning_m and nissaya_m:
        nissaya_val = nissaya_m.group(1)
        pali_eng = pali_eng_m.group(1) if pali_eng_m else ''
        term_my = term_my_m.group(1)
        meaning = meaning_m.group(1)
        
        # If nissaya is empty, try to fill it
        if nissaya_val == '':
            if pali_eng in hardcoded:
                new_nissaya = hardcoded[pali_eng]
            else:
                # Generic fallback: "ပါဠိ - အဓိပ္ပာယ်"
                # Strip out bracketed stuff from meaning to make it look more like a nissaya
                short_meaning = re.sub(r'\(.*?\)', '', meaning).strip()
                # Determine ending heuristically
                if term_my.endswith('ာ'):
                    declension = term_my
                elif term_my.endswith('သ') or term_my.endswith('ဟ') or term_my.endswith('ဂ') or term_my.endswith('ရ') or term_my.endswith('က'):
                    declension = term_my + 'ော'
                else:
                    declension = term_my + 'ံ'
                
                new_nissaya = f"{declension} - {short_meaning}"
            
            # replace the empty nissaya
            block = block.replace(f"nissaya: ''", f"nissaya: '{new_nissaya}'")
    
    return block

match = re.search(r'const originalTerms = (\[.*?\]);', content, re.DOTALL)
if match:
    original_array = match.group(1)
    
    # Find all objects and replace them
    new_array = re.sub(r'\{\s*term:.*?(?=\},|\}\s*\])', lambda m: replacer(m), original_array, flags=re.DOTALL)
    
    new_content = content.replace(original_array, new_array)
    with open('glossary.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Auto-filled Nissayas for all terms.")
else:
    print("Array not found.")
