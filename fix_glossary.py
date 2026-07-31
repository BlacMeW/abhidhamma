with open("glossary.html", "r", encoding="utf-8") as f:
    content = f.read()

# I will find "if (!groups[letter]) groups[letter] = [,"
# and replace it with "if (!groups[letter]) groups[letter] = [];"
# and also I need to move the additional terms to the correct `const terms = [...];` block.

wrong_insertion = """if (!groups[letter]) groups[letter] = [,

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
];"""

content = content.replace(wrong_insertion, "if (!groups[letter]) groups[letter] = [];")

# now correctly insert into const terms
additional = """
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
            { term: 'Yoga (ယောဂ)', meaning: 'ယှဉ်စေတတ်သော၊ ဆက်စပ်ပေးတတ်သော တရား ၄ ပါး' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] }
"""

terms_end_str = "            { term: 'Ṭhiti (ဌီ)', meaning: 'တည်နေခြင်း ခဏ' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] }"
content = content.replace(terms_end_str, terms_end_str + ",\n" + additional)

with open("glossary.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Syntax fixed")
