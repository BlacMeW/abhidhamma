import re
import json

dict_map = {
    'h-lobha': {'pali': 'Lobha', 'nissaya': 'လောဘော - လိုချင်တပ်မက်ခြင်း သဘောတရား'},
    'h-dosa': {'pali': 'Dosa', 'nissaya': 'ဒေါသော - ကြမ်းတမ်းခြင်း၊ စိတ်ဆိုးခြင်း သဘောတရား'},
    'h-moha': {'pali': 'Moha', 'nissaya': 'မောဟော - အာရုံ၏ သဘောမှန်ကို ဖုံးကွယ်ထားခြင်း သဘောတရား'},
    'h-alobha': {'pali': 'Alobha', 'nissaya': 'အလောဘော - အာရုံ၌ မတွယ်တာဘဲ စွန့်လွှတ်ခြင်း သဘောတရား'},
    'h-adosa': {'pali': 'Adosa', 'nissaya': 'အဒေါသော - အာရုံ၌ မကြမ်းတမ်းဘဲ မေတ္တာထားခြင်း သဘောတရား'},
    'h-amoha': {'pali': 'Amoha', 'nissaya': 'အမောဟော - အာရုံ၏ သဘောမှန်ကို ခွဲခြားသိမြင်ခြင်း သဘောတရား'},
    
    'j-vitakka': {'pali': 'Vitakka', 'nissaya': 'ဝိတက္ကော - အာရုံပေါ်သို့ စိတ်ကို တင်ပေးခြင်း (ကြံစည်ခြင်း) သဘော'},
    'j-vicara': {'pali': 'Vicāra', 'nissaya': 'ဝိစာရော - အာရုံကို ထပ်ခါထပ်ခါ သုံးသပ်ခြင်း သဘော'},
    'j-piti': {'pali': 'Pīti', 'nissaya': 'ပီတိ - အာရုံကို နှစ်သက်ခြင်း သဘော'},
    'j-ekaggata': {'pali': 'Ekaggatā', 'nissaya': 'ဧကဂ္ဂတာ - အာရုံတစ်ခုတည်း၌ စူးစိုက်တည်ငြိမ်ခြင်း သဘော'},
    'j-somanassa': {'pali': 'Somanassa', 'nissaya': 'သောမနဿံ - စိတ်ချမ်းသာခြင်း ဝေဒနာ'},
    'j-domanassa': {'pali': 'Domanassa', 'nissaya': 'ဒေါမနဿံ - စိတ်ဆင်းရဲခြင်း ဝေဒနာ'},
    'j-upekkha': {'pali': 'Upekkhā', 'nissaya': 'ဥပေက္ခာ - အလယ်အလတ်ဖြစ်သော ခံစားမှု ဝေဒနာ'},
    
    'm-sammaditthi': {'pali': 'Sammā-diṭṭhi', 'nissaya': 'သမ္မာဒိဋ္ဌိ - မှန်ကန်သော အမြင် (ပညာ)'},
    'm-sammavitakka': {'pali': 'Sammā-saṅkappa', 'nissaya': 'သမ္မာသင်္ကပ္ပေါ - မှန်ကန်သော ကြံစည်မှု'},
    'm-sammavaca': {'pali': 'Sammā-vācā', 'nissaya': 'သမ္မာဝါစာ - မှန်ကန်သော စကား'},
    'm-sammakammanta': {'pali': 'Sammā-kammanta', 'nissaya': 'သမ္မာကမ္မန္တော - မှန်ကန်သော အလုပ်'},
    'm-sammaajiva': {'pali': 'Sammā-ājīva', 'nissaya': 'သမ္မာအာဇီဝေါ - မှန်ကန်သော အသက်မွေးဝမ်းကျောင်း'},
    'm-sammavayama': {'pali': 'Sammā-vāyāma', 'nissaya': 'သမ္မာဝါယာမော - မှန်ကန်သော အားထုတ်မှု'},
    'm-sammasati': {'pali': 'Sammā-sati', 'nissaya': 'သမ္မာသတိ - မှန်ကန်သော အောက်မေ့မှု'},
    'm-sammasamadhi': {'pali': 'Sammā-samādhi', 'nissaya': 'သမ္မာသမာဓိ - မှန်ကန်သော တည်ကြည်မှု'},
    'm-micchaditthi': {'pali': 'Micchā-diṭṭhi', 'nissaya': 'မိစ္ဆာဒိဋ္ဌိ - မှားယွင်းသော အမြင်'},
    'm-micchasankappa': {'pali': 'Micchā-saṅkappa', 'nissaya': 'မိစ္ဆာသင်္ကပ္ပေါ - မှားယွင်းသော ကြံစည်မှု'},
    'm-micchavayama': {'pali': 'Micchā-vāyāma', 'nissaya': 'မိစ္ဆာဝါယာမော - မှားယွင်းသော အားထုတ်မှု'},
    'm-micchasamadhi': {'pali': 'Micchā-samādhi', 'nissaya': 'မိစ္ဆာသမာဓိ - မှားယွင်းသော တည်ကြည်မှု'},
    
    'i-cakkhu': {'pali': 'Cakkhundriya', 'nissaya': 'စက္ခုန္ဒြိယံ - မြင်ခြင်း၌ အစိုးရသော (မျက်စိအကြည်ရုပ်)'},
    'i-sota': {'pali': 'Sotindriya', 'nissaya': 'သောတိန္ဒြိယံ - ကြားခြင်း၌ အစိုးရသော (နားအကြည်ရုပ်)'},
    'i-ghana': {'pali': 'Ghānindriya', 'nissaya': 'ဃာနိန္ဒြိယံ - နံခြင်း၌ အစိုးရသော (နှာခေါင်းအကြည်ရုပ်)'},
    'i-jivha': {'pali': 'Jivhindriya', 'nissaya': 'ဇိဝှိန္ဒြိယံ - အရသာသိခြင်း၌ အစိုးရသော (လျှာအကြည်ရုပ်)'},
    'i-kaya': {'pali': 'Kāyindriya', 'nissaya': 'ကာယိန္ဒြိယံ - ထိတွေ့ခြင်း၌ အစိုးရသော (ကိုယ်အကြည်ရုပ်)'},
    'i-itthi': {'pali': 'Itthindriya', 'nissaya': 'ဣတ္ထိန္ဒြိယံ - မိန်းမဟန် အသွင်အပြင်၌ အစိုးရသော (ဘာဝရုပ်)'},
    'i-purisa': {'pali': 'Purisindriya', 'nissaya': 'ပုရိသိန္ဒြိယံ - ယောက်ျားဟန် အသွင်အပြင်၌ အစိုးရသော (ဘာဝရုပ်)'},
    'i-jivita': {'pali': 'Jīvitindriya', 'nissaya': 'ဇီဝိတိန္ဒြိယံ - အသက်ရှင်ခြင်း၌ အစိုးရသော (ရုပ်/နာမ် ဇီဝိတ)'},
    'i-mano': {'pali': 'Manindriya', 'nissaya': 'မနိန္ဒြိယံ - အာရုံကို သိခြင်း၌ အစိုးရသော (စိတ် ၈၉ ပါး)'},
    'i-sukha': {'pali': 'Sukhindriya', 'nissaya': 'သုခိန္ဒြိယံ - ကိုယ်ချမ်းသာခြင်း၌ အစိုးရသော (ဝေဒနာ)'},
    'i-dukkha': {'pali': 'Dukkhindriya', 'nissaya': 'ဒုက္ခိန္ဒြိယံ - ကိုယ်ဆင်းရဲခြင်း၌ အစိုးရသော (ဝေဒနာ)'},
    'i-somanassa': {'pali': 'Somanassindriya', 'nissaya': 'သောမနဿိန္ဒြိယံ - စိတ်ချမ်းသာခြင်း၌ အစိုးရသော (ဝေဒနာ)'},
    'i-domanassa': {'pali': 'Domanassindriya', 'nissaya': 'ဒေါမနဿိန္ဒြိယံ - စိတ်ဆင်းရဲခြင်း၌ အစိုးရသော (ဝေဒနာ)'},
    'i-upekkha': {'pali': 'Upekkhindriya', 'nissaya': 'ဥပေက္ခိန္ဒြိယံ - အလယ်အလတ်ဖြစ်ခြင်း၌ အစိုးရသော (ဝေဒနာ)'},
    'i-saddha': {'pali': 'Saddhindriya', 'nissaya': 'သဒ္ဓိန္ဒြိယံ - ယုံကြည်ခြင်း၌ အစိုးရသော (သဒ္ဓါစေတသိက်)'},
    'i-viriya': {'pali': 'Vīriyindriya', 'nissaya': 'ဝီရိယိန္ဒြိယံ - အားထုတ်ခြင်း၌ အစိုးရသော (ဝီရိယစေတသိက်)'},
    'i-sati': {'pali': 'Satindriya', 'nissaya': 'သတိန္ဒြိယံ - အောက်မေ့ခြင်း၌ အစိုးရသော (သတိစေတသိက်)'},
    'i-samadhi': {'pali': 'Samādhindriya', 'nissaya': 'သမာဓိန္ဒြိယံ - တည်ကြည်ခြင်း၌ အစိုးရသော (ဧကဂ္ဂတာစေတသိက်)'},
    'i-panna': {'pali': 'Paññindriya', 'nissaya': 'ပညိန္ဒြိယံ - သိမြင်ခြင်း၌ အစိုးရသော (ပညာစေတသိက်)'},
    'i-anannata': {'pali': 'Anaññātaññassāmītindriya', 'nissaya': 'အနညတညဿာမီတိန္ဒြိယံ - မသိသေးသည်ကို သိအောင်လုပ်ခြင်း၌ အစိုးရသော တရား'},
    'i-annita': {'pali': 'Aññindriya', 'nissaya': 'အညိန္ဒြိယံ - သိပြီးသည်ကို ပို၍သိခြင်း၌ အစိုးရသော တရား'},
    'i-annatavi': {'pali': 'Aññātāvindriya', 'nissaya': 'အညာတာဝိန္ဒြိယံ - အကုန်အစင် သိပြီးသူ၏ အဖြစ်၌ အစိုးရသော တရား'},
    
    'b-saddha': {'pali': 'Saddhābala', 'nissaya': 'သဒ္ဓါဗလံ - မယုံကြည်မှုကို တွန်းလှန်နိုင်သော ယုံကြည်ခြင်း ခွန်အား'},
    'b-viriya': {'pali': 'Vīriyabala', 'nissaya': 'ဝီရိယဗလံ - ပျင်းရိမှုကို တွန်းလှန်နိုင်သော အားထုတ်ခြင်း ခွန်အား'},
    'b-sati': {'pali': 'Satibala', 'nissaya': 'သတိဗလံ - မေ့လျော့မှုကို တွန်းလှန်နိုင်သော အောက်မေ့ခြင်း ခွန်အား'},
    'b-samadhi': {'pali': 'Samādhibala', 'nissaya': 'သမာဓိဗလံ - ပျံ့လွင့်မှုကို တွန်းလှန်နိုင်သော တည်ကြည်ခြင်း ခွန်အား'},
    'b-panna': {'pali': 'Paññābala', 'nissaya': 'ပညာဗလံ - မသိမှုကို တွန်းလှန်နိုင်သော သိမြင်ခြင်း ခွန်အား'},
    'b-hiri': {'pali': 'Hirībala', 'nissaya': 'ဟိရီဗလံ - မရှက်မှုကို တွန်းလှန်နိုင်သော ရှက်ခြင်း ခွန်အား'},
    'b-ottappa': {'pali': 'Ottappabala', 'nissaya': 'ဩတ္တပ္ပဗလံ - မကြောက်မှုကို တွန်းလှန်နိုင်သော ကြောက်ခြင်း ခွန်အား'},
    'b-ahiri': {'pali': 'Ahirikabala', 'nissaya': 'အဟိရိကဗလံ - ရှက်ခြင်းကို တွန်းလှန်နိုင်သော မရှက်ခြင်း ခွန်အား (အကုသိုလ်)'},
    'b-anottappa': {'pali': 'Anottappabala', 'nissaya': 'အနောတ္တပ္ပဗလံ - ကြောက်ခြင်းကို တွန်းလှန်နိုင်သော မကြောက်ခြင်း ခွန်အား (အကုသိုလ်)'},
    
    'a-chanda': {'pali': 'Chandādhipati', 'nissaya': 'ဆန္ဒာဓိပတိ - ပြင်းပြသော ဆန္ဒဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း'},
    'a-viriya': {'pali': 'Vīriyādhipati', 'nissaya': 'ဝီရိယာဓိပတိ - ပြင်းပြသော အားထုတ်မှုဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း'},
    'a-citta': {'pali': 'Cittādhipati', 'nissaya': 'စိတ္တာဓိပတိ - ပြင်းပြသော စိတ်စွမ်းအင်ဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း'},
    'a-vimamsa': {'pali': 'Vīmaṃsādhipati', 'nissaya': 'ဝီမံသာဓိပတိ - ပြင်းပြသော စူးစမ်းဆင်ခြင်မှု (ပညာ) ဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း'},
    
    'ah-kabalikara': {'pali': 'Kabaḷīkārāhāra', 'nissaya': 'ကဗဠီကာရာဟာရော - ခန္ဓာကိုယ်ကို ထောက်ပံ့သော ရုပ်အစာ (ဩဇာရုပ်)'},
    'ah-phassa': {'pali': 'Phassāhāra', 'nissaya': 'ဖဿာဟာရော - ဝေဒနာသုံးပါးကို ဖြစ်စေသော ထိတွေ့မှု အစာ'},
    'ah-manosancetana': {'pali': 'Manosañcetanāhāra', 'nissaya': 'မနောသဉ္စေတနာဟာရော - ဘဝသစ်ကို ဖြစ်စေသော ကံတရား အစာ (စေတနာ)'},
    'ah-vinnana': {'pali': 'Viññāṇāhāra', 'nissaya': 'ဝိညာဏာဟာရော - နာမ်ရုပ်ကို ဖြစ်စေသော စိတ်အစာ'}
}

with open('missaka_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    block = match.group(0)
    # Extract the key
    key_match = re.search(r"key:\s*'([^']+)'", block)
    if key_match:
        key = key_match.group(1)
        if key in dict_map:
            pali = dict_map[key]['pali']
            nissaya = dict_map[key]['nissaya']
            # Insert pali and nissaya fields after name: '...'
            block = re.sub(
                r"(name:\s*'[^']+',)", 
                f"\\1 pali: '{pali}', nissaya: '{nissaya}',", 
                block
            )
    return block

match = re.search(r'const msData = \[(.*?)\];', content, re.DOTALL)
if match:
    original_array = match.group(1)
    new_array = re.sub(r'\{\s*id:.*?\}', lambda m: replacer(m), original_array, flags=re.DOTALL)
    new_content = content.replace(original_array, new_array)
    with open('missaka_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Data injected successfully.")
else:
    print("Array not found.")

