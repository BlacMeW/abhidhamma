import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/sabba_sangaha.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update intro text
content = content.replace("ခွဲခြားနည်း (၄) မျိုး", "ခွဲခြားနည်း (၅) မျိုး")

# 2. Replace the Khandha link-out with the new sections
old_khandha_link = """        <!-- Khandha link-out -->
        <a href="citta_cetasikas_visual_guide.html#citta89" class="block glass-card rounded-2xl p-4 max-w-3xl mx-auto border border-indigo-400 dark:border-indigo-500/30 hover:border-indigo-400 transition flex items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-indigo-500/20 text-indigo-700 dark:text-indigo-300 flex items-center justify-center text-lg flex-shrink-0"><i class="fa-solid fa-layer-group"></i></div>
                <div class="text-left">
                    <span class="font-semibold text-indigo-700 dark:text-indigo-300 text-sm block">ခန္ဓာ (၅) ပါး — ရုပ်/ဝေဒနာ/သညာ/သင်္ခါရ/ဝိညာဏ</span>
                    <span class="text-slate-600 dark:text-slate-400 text-[11px]">Citta & Cetasika Guide ၏ Khandha card တွင် အသေးစိတ် ဖော်ပြထားပြီး ဖြစ်သည်</span>
                </div>
            </div>
            <i class="fa-solid fa-arrow-right text-indigo-700 dark:text-indigo-400 flex-shrink-0"></i>
        </a>"""

new_khandha_sections = """        <!-- Khandha and Upadanakkhandha verification bar -->
        <div class="glass-card rounded-2xl p-4 max-w-3xl mx-auto flex flex-wrap items-center justify-center gap-3 text-xs md:text-sm border border-slate-200 dark:border-slate-700">
            <button onclick="jumpToGroup('khandha')" class="px-3 py-1.5 rounded-lg bg-indigo-100 dark:bg-indigo-500/15 text-indigo-700 dark:text-indigo-300 border border-indigo-400 dark:border-indigo-500/30 hover:bg-indigo-500/25 hover:border-indigo-400 transition">ခန္ဓာ (၅) ပါး</button>
            <span class="text-slate-600">vs</span>
            <button onclick="jumpToGroup('upadanakkhandha')" class="px-3 py-1.5 rounded-lg bg-rose-100 dark:bg-rose-500/15 text-rose-700 dark:text-rose-300 border border-rose-400 dark:border-rose-500/30 hover:bg-rose-500/25 hover:border-rose-400 transition">ဥပါဒါနက္ခန္ဓာ (၅) ပါး</button>
        </div>

        <!-- Khandha explanation -->
        <div class="max-w-3xl mx-auto text-xs text-slate-600 dark:text-slate-400 px-4 mt-2">
            * <b>ခန္ဓာ (၅) ပါး</b> သည် လောကီ/လောကုတ္တရာ တရားအားလုံး (နိဗ္ဗာန်မှလွဲ၍) ကို ခြုံငုံသည်။ <br>
            * <b>ဥပါဒါနက္ခန္ဓာ (၅) ပါး</b> သည် တဏှာဒိဋ္ဌိတို့ဖြင့် အာရုံပြု၍ စွဲလမ်းစရာ (ဥပါဒါန်၏ အာရုံ) ဖြစ်သော "လောကီတရား" သက်သက်ကိုသာ ခြုံငုံသည်။ (လောကုတ္တရာစိတ် ၈ ပါး နှင့် စေတသိက် ၃၆ ပါးတို့သည် ဥပါဒါနက္ခန္ဓာတွင် မပါဝင်ပါ။)
        </div>

        <!-- Khandha groups -->
        <div id="khandha-groups" class="space-y-4 mt-4"></div>"""

if "ခန္ဓာ (၅) ပါး" in content and "ဥပါဒါနက္ခန္ဓာ (၅) ပါး" not in content:
    content = content.replace(old_khandha_link, new_khandha_sections)

# 3. Add to sbData
data_insert = """            // Khandha (5) — indigo
            { id: 101, key: 'rupakkhandha', pali: 'Rūpakkhandha', name: 'ရူပက္ခန္ဓာ', group: 'khandha', icon: 'fa-cubes',
              desc: 'ရုပ်တရား (၂၈) ပါး အစုအဝေး။',
              example: 'အတိတ်/အနာဂတ်/ပစ္စုပ္ပန် စသည့် ရုပ်အားလုံးကို တစ်ပေါင်းတည်းပြု၍ ရူပက္ခန္ဓာဟု ခေါ်သည်။' },
            { id: 102, key: 'vedanakkhandha', pali: 'Vedanākkhandha', name: 'ဝေဒနာက္ခန္ဓာ', group: 'khandha', icon: 'fa-heart',
              desc: 'ဝေဒနာစေတသိက် တစ်ပါးတည်း အစုအဝေး။',
              example: 'စိတ် ၈၉ ပါးလုံး၌ ယှဉ်သော ဝေဒနာအားလုံး ပါဝင်သည်။' },
            { id: 103, key: 'sannakkhandha', pali: 'Saññākkhandha', name: 'သညာက္ခန္ဓာ', group: 'khandha', icon: 'fa-tag',
              desc: 'သညာစေတသိက် တစ်ပါးတည်း အစုအဝေး။',
              example: 'စိတ် ၈၉ ပါးလုံး၌ ယှဉ်သော မှတ်သားမှုသညာအားလုံး ပါဝင်သည်။' },
            { id: 104, key: 'sankharakkhandha', pali: 'Saṅkhārakkhandha', name: 'သင်္ခါရက္ခန္ဓာ', group: 'khandha', icon: 'fa-gears',
              desc: 'ဝေဒနာ၊ သညာ မှလွဲ၍ ကျန်သော စေတသိက် (၅၀) အစုအဝေး။',
              example: 'စိတ်ကို ပြုပြင်ပေးသော စေတနာ အစရှိသည့် တရားများ အားလုံး ပါဝင်သည်။' },
            { id: 105, key: 'vinnanakkhandha', pali: 'Viññāṇakkhandha', name: 'ဝိညာဏက္ခန္ဓာ', group: 'khandha', icon: 'fa-brain',
              desc: 'စိတ် (၈၉) ပါး အစုအဝေး။',
              example: 'လောကီရော လောကုတ္တရာပါ စိတ်အားလုံး ပါဝင်သည်။' },

            // Upadanakkhandha (5) — rose
            { id: 106, key: 'rupupadanakkhandha', pali: 'Rūpupādānakkhandha', name: 'ရူပုပါဒါနက္ခန္ဓာ', group: 'upadanakkhandha', icon: 'fa-cubes',
              desc: 'ဥပါဒါန်၏ အာရုံဖြစ်သော ရုပ်တရား (၂၈) ပါး အစုအဝေး။',
              example: 'ရုပ်အားလုံးသည် လောကီချည်းဖြစ်၍ ရူပက္ခန္ဓာနှင့် အတူတူပင်ဖြစ်သည်။' },
            { id: 107, key: 'vedanupadanakkhandha', pali: 'Vedanupādānakkhandha', name: 'ဝေဒနုပါဒါနက္ခန္ဓာ', group: 'upadanakkhandha', icon: 'fa-heart',
              desc: 'ဥပါဒါန်၏ အာရုံဖြစ်သော လောကီဝေဒနာ အစုအဝေး။',
              example: 'လောကီစိတ် (၈၁) ပါး၌ ယှဉ်သော ဝေဒနာကိုသာ ယူသည်။' },
            { id: 108, key: 'sannupadanakkhandha', pali: 'Saññupādānakkhandha', name: 'သညုပါဒါနက္ခန္ဓာ', group: 'upadanakkhandha', icon: 'fa-tag',
              desc: 'ဥပါဒါန်၏ အာရုံဖြစ်သော လောကီသညာ အစုအဝေး။',
              example: 'လောကီစိတ် (၈၁) ပါး၌ ယှဉ်သော သညာကိုသာ ယူသည်။' },
            { id: 109, key: 'sankharupadanakkhandha', pali: 'Saṅkhārupādānakkhandha', name: 'သင်္ခါရုပါဒါနက္ခန္ဓာ', group: 'upadanakkhandha', icon: 'fa-gears',
              desc: 'ဥပါဒါန်၏ အာရုံဖြစ်သော လောကီစေတသိက် (၅၀) အစုအဝေး။',
              example: 'လောကီစိတ်၌ ယှဉ်သော စေတသိက်များကိုသာ ယူသည်။' },
            { id: 110, key: 'vinnanupadanakkhandha', pali: 'Viññāṇupādānakkhandha', name: 'ဝိညာဏုပါဒါနက္ခန္ဓာ', group: 'upadanakkhandha', icon: 'fa-brain',
              desc: 'ဥပါဒါန်၏ အာရုံဖြစ်သော လောကီစိတ် (၈၁) ပါး အစုအဝေး။',
              example: 'လောကုတ္တရာစိတ် (၈) ပါးသည် ဥပါဒါန်၏ အာရုံ မဖြစ်နိုင်သဖြင့် ဤအစုတွင် မပါဝင်ပါ။' },

            // Ayatana internal (6) — sky"""

if "rupakkhandha" not in content:
    content = content.replace("            // Ayatana internal (6) — sky", data_insert)

# 4. Update groupInfo
group_info_insert = """            'khandha':          { label: 'ခန္ဓာ', sub: 'အစုအဝေး (၅)', color: 'text-indigo-700 dark:text-indigo-300', border: 'border-indigo-500', bg: 'bg-indigo-500/10' },
            'upadanakkhandha':  { label: 'ဥပါဒါနက္ခန္ဓာ', sub: 'စွဲလမ်းဖွယ် အစုအဝေး (၅)', color: 'text-rose-700 dark:text-rose-300', border: 'border-rose-500', bg: 'bg-rose-500/10' },
            'ayatana-internal':"""
if "'khandha':" not in content:
    content = content.replace("            'ayatana-internal':", group_info_insert)

# 5. Update renderSection calls
dom_ready_old = """        document.addEventListener('DOMContentLoaded', () => {
            renderSection('ayatana-groups', ['ayatana-internal', 'ayatana-external']);"""
dom_ready_new = """        document.addEventListener('DOMContentLoaded', () => {
            renderSection('khandha-groups', ['khandha', 'upadanakkhandha']);
            renderSection('ayatana-groups', ['ayatana-internal', 'ayatana-external']);"""
if "renderSection('khandha-groups'" not in content:
    content = content.replace(dom_ready_old, dom_ready_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated sabba_sangaha successfully!")
