import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_section = """### အကုသိုလ် (၁၄)
#### မောစတုက္က (၄)
- မောဟ
  - အဝိဇ္ဇာ
  - အမှန်ကို မသိမှု
- အဟိရိက (မကောင်းမှုပြုရမည်ကို မရှက်မှု)
- အနောတ္တပ္ပ (မကောင်းမှုပြုရမည်ကို မကြောက်မှု)
- ဥဒ္ဓစ္စ (စိတ်ပျံ့လွင့်မှု)
#### လောတိက (၃)
- လောဘ
  - တပ်မက်မှု
  - လိုချင်မှု
- ဒိဋ္ဌိ (မှားယွင်းစွာ ယူဆမှု)
- မာန (ထောင်လွှားမှု)
#### ဒေါစတုက္က (၄)
- ဒေါသ
  - ကြမ်းတမ်းမှု
  - ဖျက်ဆီးလိုမှု
- ဣဿာ (သူတစ်ပါးကြီးပွားချမ်းသာသည်ကို ငြူစူမှု)
- မစ္ဆရိယ
  - မိမိစည်းစိမ်ကို ဝှက်ထားလိုမှု
  - နှမြောမှု
- ကုက္ကုစ္စ
  - ပြုခဲ့
  - မပြုခဲ့သည်ကို နောင်တရမှု
#### ထီသိတ် (၂)
- ထိန (စိတ်၏ လေးလံထိုင်းမှိုင်းမှု)
- မိဒ္ဓ (စေတသိက်တို့၏ လေးလံထိုင်းမှိုင်းမှု)
#### ဝိစိကိစ္ဆာ (၁)
- ဝိစိကိစ္ဆာ
  - ယုံမှားသံသယဖြစ်မှု
  - မဆုံးဖြတ်နိုင်မှု"""

new_section = """### အကုသိုလ် (၁၄)
#### မောစတုက္က (၄)
- မောဟ<br><span style="font-size:0.8em; color:gray">(အမှန်ကို မသိမှု)</span>
- အဟိရိက<br><span style="font-size:0.8em; color:gray">(မကောင်းမှုပြုရမည်ကို မရှက်မှု)</span>
- အနောတ္တပ္ပ<br><span style="font-size:0.8em; color:gray">(မကောင်းမှုပြုရမည်ကို မကြောက်မှု)</span>
- ဥဒ္ဓစ္စ<br><span style="font-size:0.8em; color:gray">(စိတ်ပျံ့လွင့်မှု)</span>
#### လောတိက (၃)
- လောဘ<br><span style="font-size:0.8em; color:gray">(တပ်မက်မှု၊ လိုချင်မှု)</span>
- ဒိဋ္ဌိ<br><span style="font-size:0.8em; color:gray">(မှားယွင်းစွာ ယူဆမှု)</span>
- မာန<br><span style="font-size:0.8em; color:gray">(ထောင်လွှားမှု)</span>
#### ဒေါစတုက္က (၄)
- ဒေါသ<br><span style="font-size:0.8em; color:gray">(ကြမ်းတမ်းမှု၊ ဖျက်ဆီးလိုမှု)</span>
- ဣဿာ<br><span style="font-size:0.8em; color:gray">(သူတစ်ပါးကြီးပွားချမ်းသာသည်ကို ငြူစူမှု)</span>
- မစ္ဆရိယ<br><span style="font-size:0.8em; color:gray">(မိမိစည်းစိမ်ကို ဝှက်ထားလိုမှု၊ နှမြောမှု)</span>
- ကုက္ကုစ္စ<br><span style="font-size:0.8em; color:gray">(ပြုခဲ့၊ မပြုခဲ့သည်ကို နောင်တရမှု)</span>
#### ထီသိတ် (၂)
- ထိန<br><span style="font-size:0.8em; color:gray">(စိတ်၏ လေးလံထိုင်းမှိုင်းမှု)</span>
- မိဒ္ဓ<br><span style="font-size:0.8em; color:gray">(စေတသိက်တို့၏ လေးလံထိုင်းမှိုင်းမှု)</span>
#### ဝိစိကိစ္ဆာ (၁)
- ဝိစိကိစ္ဆာ<br><span style="font-size:0.8em; color:gray">(ယုံမှားသံသယဖြစ်မှု၊ မဆုံးဖြတ်နိုင်မှု)</span>"""

content = content.replace(old_section, new_section)
with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Akusala formatted.")
