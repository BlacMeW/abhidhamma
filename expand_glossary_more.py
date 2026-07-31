import re

additional_terms = """
            { term: 'Asubha (အသုဘ)', meaning: 'မတင့်တယ်ခြင်း၊ စက်ဆုပ်ဖွယ် (ကမ္မဋ္ဌာန်း ၄၀ တွင် ပါဝင်သည်)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Adhipati (အဓိပတိ)', meaning: 'အကြီးအမှူးဖြစ်သော အကြောင်းတရား (ဆန္ဒ၊ ဝီရိယ၊ စိတ္တ၊ ဝီမံသ)' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Anantaram (အနန္တရ)', meaning: 'ခြားနားမှုမရှိဘဲ အကျိုးပေးသော ပစ္စည်း' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Anussati (အနုဿတိ)', meaning: 'အဖန်ဖန် အောက်မေ့ခြင်း (ဗုဒ္ဓါနုဿတိ စသော ကမ္မဋ္ဌာန်းများ)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Brahmavihāra (ဗြဟ္မဝိဟာရ)', meaning: 'မြတ်သော နေထိုင်ခြင်း (မေတ္တာ၊ ကရုဏာ၊ မုဒိတာ၊ ဥပေက္ခာ)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Carita (စရိုက်)', meaning: 'လေ့လာကျက်စားလေ့ရှိသော အမူအကျင့် (ရာဂစရိုက် စသည်)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Gantha (ဂန္ထ)', meaning: 'ခန္ဓာကိုယ်နှင့် အာရုံကို နှောင်ဖွဲ့တတ်သော တရား' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Kasiṇa (ကသိုဏ်း)', meaning: 'အလုံးစုံကို ဖြန့်ကြက်၍ ရှုရသော အာရုံ (ဥပမာ - ပထဝီကသိုဏ်း)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Nīvaraṇa (နီဝရဏ)', meaning: 'ကုသိုလ်တရားတို့ကို တားဆီးပိတ်ပင်တတ်သော တရား' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Paccuppanna (ပစ္စုပ္ပန်)', meaning: 'ယခုဖြစ်ဆဲ အချိန် (ပစ္စုပ္ပန်အာရုံ)' , links: [{ name: 'ပကိဏ္ဏကပိုင်း (Pakiṇṇaka)', url: 'pakinnaka_sangaha.html' }] },
            { term: 'Sahajāta (သဟဇာတ)', meaning: 'အတူတကွ ဖြစ်ပေါ်လာသော ပစ္စည်း' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Yoga (ယောဂ)', meaning: 'ယှဉ်စေတတ်သော၊ ဆက်စပ်ပေးတတ်သော တရား ၄ ပါး' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
"""

with open("glossary.html", "r", encoding="utf-8") as f:
    content = f.read()

# Insert before "];"
end_str = "];"
end_idx = content.rfind(end_str)

if end_idx != -1:
    # Need a comma if not there
    before_bracket = content[:end_idx].strip()
    if not before_bracket.endswith(','):
        new_content = content[:end_idx] + ",\n" + additional_terms + "];" + content[end_idx+2:]
    else:
        new_content = content[:end_idx] + "\n" + additional_terms + "];" + content[end_idx+2:]
        
    with open("glossary.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Glossary additional terms updated.")
else:
    print("Could not find the end array in glossary.html")
