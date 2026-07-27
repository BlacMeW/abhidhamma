import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_terms = """
            { term: 'Avijjā (အဝိဇ္ဇာ)', meaning: 'သစ္စာလေးပါးကို မသိခြင်း (မောဟ)' },
            { term: 'Taṇhā (တဏှာ)', meaning: 'အာရုံကို တပ်မက်ခြင်း၊ လိုချင်ခြင်း (လောဘ)' },
            { term: 'Upādāna (ဥပါဒါန / ဥပါဒါန်)', meaning: 'အာရုံကို ပြင်းစွာ စွဲလမ်းခြင်း' },
            { term: 'Jāti (ဇာတိ)', meaning: 'ပဋိသန္ဓေတည်နေခြင်း၊ ပထမဆုံး ဖြစ်ပေါ်လာခြင်း' },
            { term: 'Jarā (ဇရာ)', meaning: 'အိုမင်း ရင့်ရော်ခြင်း' },
            { term: 'Maraṇa (မရဏ)', meaning: 'သေဆုံးခြင်း၊ ပျက်စီးခြင်း' },
            { term: 'Nāmarūpa (နာမရူပ / နာမ်ရုပ်)', meaning: 'စိတ်၊ စေတသိက် (နာမ်) နှင့် ဖောက်ပြန်တတ်သော သဘော (ရုပ်)' },
            { term: 'Saḷāyatana (သဠာယတန)', meaning: 'အာယတန ၆ ပါး (စက္ခု၊ သောတ၊ ဃာန၊ ဇိဝှာ၊ ကာယ၊ မန)' },
            { term: 'Phassa (ဖဿ)', meaning: 'အာရုံနှင့် ဒွါရ တွေ့ဆုံထိခိုက်ခြင်း' },
            { term: 'Vedanā (ဝေဒနာ)', meaning: 'အာရုံ၏ အရသာကို ခံစားခြင်း' },
            { term: 'Satipaṭṭhāna (သတိပဋ္ဌာန / သတိပဋ္ဌာန်)', meaning: 'သတိကို စွဲမြဲစွာ တည်ထားခြင်း (ကာယ၊ ဝေဒနာ၊ စိတ္တ၊ ဓမ္မ)' },
            { term: 'Sammappadhāna (သမ္မပ္ပဓာန)', meaning: 'ကောင်းစွာ အားထုတ်ခြင်း (ဝီရိယ ၄ မျိုး)' },
            { term: 'Iddhipāda (ဣဒ္ဓိပါဒ / ဣဒ္ဓိပါဒ်)', meaning: 'ပြီးပြည့်စုံခြင်း၏ အခြေခံ (ဆန္ဒ၊ ဝီရိယ၊ စိတ္တ၊ ဝီမံသ)' },
            { term: 'Bala (ဗလ)', meaning: 'ဆန့်ကျင်ဘက်တရားတို့ကို မတုန်လှုပ်စေသော အစွမ်းခွန်အား (သဒ္ဓါ၊ ဝီရိယ၊ သတိ၊ သမာဓိ၊ ပညာ)' },
            { term: 'Bojjhaṅga (ဗောဇ္ဈင်္ဂ / ဗောဇ္ဈင်)', meaning: 'သစ္စာလေးပါးကို သိရန် အထောက်အကူပြုသော အင်္ဂါ' },
            { term: 'Lobha (လောဘ)', meaning: 'လိုချင်တပ်မက်ခြင်း' },
            { term: 'Dosa (ဒေါသ)', meaning: 'ကြမ်းတမ်းခြင်း၊ အမျက်ထွက်ခြင်း၊ မကျေနပ်ခြင်း' },
            { term: 'Moha (မောဟ)', meaning: 'တွေဝေခြင်း၊ အမှန်ကို မသိခြင်း' },
            { term: 'Māna (မာန)', meaning: 'ထောင်လွှားခြင်း၊ မိမိကိုယ်ကို အထင်ကြီးခြင်း' },
            { term: 'Diṭṭhi (ဒိဋ္ဌိ)', meaning: 'မှားယွင်းစွာ ယူဆခြင်း' },
            { term: 'Vicikicchā (ဝိစိကိစ္ဆာ)', meaning: 'ယုံမှား သံသယဖြစ်ခြင်း' },
            { term: 'Thīna-Middha (ထိန-မိဒ္ဓ)', meaning: 'စိတ်နှင့် စေတသိက်တို့၏ ထိုင်းမှိုင်းခြင်း၊ လေးလံခြင်း' },
            { term: 'Uddhacca (ဥဒ္ဓစ္စ)', meaning: 'စိတ် ပျံ့လွင့်ခြင်း' },
            { term: 'Kukkucca (ကုက္ကုစ္စ)', meaning: 'ပြုခဲ့မိသော အမှား၊ မပြုခဲ့မိသော အကောင်းများအတွက် နောင်တရ ပူပန်ခြင်း' },
            { term: 'Alobha (အလောဘ)', meaning: 'မလိုချင်ခြင်း၊ မတပ်မက်ခြင်း၊ စွန့်လွှတ်ခြင်း' },
            { term: 'Adosa (အဒေါသ)', meaning: 'မကြမ်းတမ်းခြင်း၊ မေတ္တာထားခြင်း' },
            { term: 'Amoha (အမောဟ)', meaning: 'အမှန်အတိုင်း သိမြင်ခြင်း (ပညာ)' },
            { term: 'Saddhā (သဒ္ဓါ)', meaning: 'ယုံကြည်သင့်သည်ကို ယုံကြည်ခြင်း' },
            { term: 'Sati (သတိ)', meaning: 'အာရုံကို မမေ့လျော့ခြင်း' },
            { term: 'Hiri (ဟိရီ)', meaning: 'ဒုစရိုက်ပြုရမည်ကို ရှက်ခြင်း' },
            { term: 'Ottappa (ဩတ္တပ္ပ)', meaning: 'ဒုစရိုက်ပြုရမည်ကို ကြောက်ခြင်း' },
            { term: 'Mahābhūta (မဟာဘူတ)', meaning: 'ကြီးမား ထင်ရှားသော ရုပ်တရား (ပထဝီ၊ အာပေါ၊ တေဇော၊ ဝါယော)' },
            { term: 'Upādārūpa (ဥပါဒါရူပ / ဥပါဒါရုပ်)', meaning: 'မဟာဘုတ် ၄ ပါးကို မှီ၍ ဖြစ်သော ရုပ် (၂၄ ပါး)' },
"""

# find the end of the terms array
match = re.search(r"(\s*)\];\s*// Sort terms alphabetically", content)
if match:
    insert_pos = match.start(0)
    # Check if there is a trailing comma in the last element before adding new ones
    # We will just append a comma to the last line if it doesn't have one?
    # Actually, let's just do a regex replace to insert our terms right before `];`
    
    # Let's ensure the last existing term ends with a comma
    before_insert = content[:insert_pos]
    if not before_insert.strip().endswith(','):
        before_insert += ','
        
    new_content = before_insert + "\n" + new_terms + content[insert_pos:]
    
    with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Glossary updated!")
else:
    print("Could not find insertion point!")

