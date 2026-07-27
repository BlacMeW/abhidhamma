import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/kammatthana_sangaha.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject Nimitta/Bhavana section right before "Jhana attainment level" (line ~131)
insert_point_1 = "        <!-- Jhana attainment level -->"
nimitta_html = """        <!-- Nimitta & Bhavana Progression -->
        <details class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-violet-500/20" open>
            <summary class="flex items-center justify-between font-bold text-violet-700 dark:text-violet-300 text-base">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>ဘာဝနာ (၃) ပါး နှင့် နိမိတ် (၃) ပါး အဆင့်ဆင့် တက်လှမ်းပုံ</span>
            </summary>
            <div class="mt-4 overflow-x-auto pb-4">
                <div class="flex items-start min-w-[700px] justify-between relative">
                    <!-- Connecting Line -->
                    <div class="absolute top-8 left-10 right-10 h-1 bg-slate-200 dark:bg-slate-700 -z-10 rounded-full"></div>
                    
                    <!-- Step 1 -->
                    <div class="flex flex-col items-center text-center w-1/3 px-2">
                        <div class="w-16 h-16 rounded-full bg-slate-100 dark:bg-slate-800 border-4 border-slate-300 dark:border-slate-600 flex items-center justify-center mb-3 shadow-md z-10">
                            <i class="fa-solid fa-eye text-2xl text-slate-500 dark:text-slate-400"></i>
                        </div>
                        <h4 class="font-bold text-slate-800 dark:text-slate-200">၁။ ပရိကမ္မနိမိတ်</h4>
                        <span class="text-[10px] text-slate-500 font-mono mt-0.5">Parikamma-nimitta</span>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 mb-2">မျက်စိဖြင့် တိုက်ရိုက် ကြည့်ရှုနေဆဲဖြစ်သော မူလအာရုံ (ဥပမာ - ကသိုဏ်းဝန်း)။</p>
                        <div class="bg-amber-100 dark:bg-amber-500/20 border border-amber-400/50 rounded-lg p-2 w-full">
                            <span class="font-bold text-amber-800 dark:text-amber-300 text-xs">ပရိကမ္မဘာဝနာ</span>
                            <p class="text-[10px] text-amber-700 dark:text-amber-400 mt-1">အစပိုင်း ကြိုးစားအားထုတ်မှု။ ကမ္မဋ္ဌာန်း ၄၀ လုံး ရနိုင်သည်။</p>
                        </div>
                    </div>
                    
                    <!-- Step 2 -->
                    <div class="flex flex-col items-center text-center w-1/3 px-2">
                        <div class="w-16 h-16 rounded-full bg-sky-100 dark:bg-sky-900 border-4 border-sky-400 dark:border-sky-600 flex items-center justify-center mb-3 shadow-md z-10">
                            <i class="fa-solid fa-brain text-2xl text-sky-600 dark:text-sky-400"></i>
                        </div>
                        <h4 class="font-bold text-sky-700 dark:text-sky-300">၂။ ဥဂ္ဂဟနိမိတ်</h4>
                        <span class="text-[10px] text-slate-500 font-mono mt-0.5">Uggaha-nimitta</span>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 mb-2">မျက်စိမှိတ်ထားသော်လည်း စိတ်ထဲ၌ ထင်ရှားစွာ မြင်နေရသော အာရုံ။</p>
                        <div class="bg-amber-100 dark:bg-amber-500/20 border border-amber-400/50 rounded-lg p-2 w-full">
                            <span class="font-bold text-amber-800 dark:text-amber-300 text-xs">ပရိကမ္မဘာဝနာ</span>
                            <p class="text-[10px] text-amber-700 dark:text-amber-400 mt-1">သမာဓိ အနည်းငယ် ရင့်ကျက်လာသော်လည်း ပရိကမ္မ အဆင့်ပင် ဖြစ်သည်။</p>
                        </div>
                    </div>
                    
                    <!-- Step 3 -->
                    <div class="flex flex-col items-center text-center w-1/3 px-2">
                        <div class="w-16 h-16 rounded-full bg-amber-100 dark:bg-amber-900 border-4 border-amber-400 dark:border-amber-600 flex items-center justify-center mb-3 shadow-md z-10">
                            <i class="fa-solid fa-sun text-2xl text-amber-600 dark:text-amber-400"></i>
                        </div>
                        <h4 class="font-bold text-amber-700 dark:text-amber-300">၃။ ပဋိဘာဂနိမိတ်</h4>
                        <span class="text-[10px] text-slate-500 font-mono mt-0.5">Paṭibhāga-nimitta</span>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 mb-2">ဥဂ္ဂဟနိမိတ်ထက် အဆရာထောင်မက ကြည်လင် တောက်ပလာသော အာရုံစစ်။</p>
                        <div class="bg-emerald-100 dark:bg-emerald-500/20 border border-emerald-400/50 rounded-lg p-2 w-full">
                            <span class="font-bold text-emerald-800 dark:text-emerald-300 text-xs">ဥပစာရ & အပ္ပနာဘာဝနာ</span>
                            <p class="text-[10px] text-emerald-700 dark:text-emerald-400 mt-1">ဈာန်အနီးရောက်ခြင်း နှင့် ဈာန်သို့ ဆိုက်ရောက်ခြင်း။ ကမ္မဋ္ဌာန်း ၂၂ ပါးသာ ဤအဆင့်သို့ ရောက်နိုင်သည်။</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="text-[11px] text-slate-500 dark:text-slate-500 mt-2 border-t border-slate-200 dark:border-slate-800 pt-2 pl-2">
                * ပဋိဘာဂနိမိတ် နှင့် အပ္ပနာဘာဝနာ (ဈာန်) ကို ကသိုဏ်း (၁၀)၊ အသုဘ (၁၀)၊ ကာယဂတာသတိ (၁) နှင့် အာနာပါနဿတိ (၁) စုစုပေါင်း (၂၂) ပါးသော ကမ္မဋ္ဌာန်းများဖြင့်သာ ရရှိနိုင်သည်။ ကျန်ကမ္မဋ္ဌာန်းများမှာ နိမိတ်မထင်၊ ဥပစာရဘာဝနာ အဆင့်၌သာ ရပ်တန့်သည်။
            </div>
        </details>

"""
if "<!-- Nimitta & Bhavana Progression -->" not in content:
    content = content.replace(insert_point_1, nimitta_html + insert_point_1)


# 2. Inject Vipassana Nanas (10) right inside the "7 Visuddhi" section, specifically inside the container.
# First, let's find the 7 Visuddhi HTML.
visuddhi_html_start = """        <!-- 7 Visuddhi -->
        <details class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-violet-500/20" open>
            <summary class="flex items-center justify-between font-bold text-violet-700 dark:text-violet-300 text-base">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>ဝိသုဒ္ဓိ (၇) ပါး — စင်ကြယ်မှု အဆင့်ဆင့်</span>
            </summary>
            <div class="mt-3 pl-5 space-y-1.5 text-xs text-slate-700 dark:text-slate-300 border-l border-slate-200 dark:border-slate-800" id="visuddhi-list"></div>
        </details>"""

# We'll replace it with a more detailed one that contains a container for the 10 Nanas inside Patipada-nanadassana-visuddhi.
# Actually, the visuddhi-list is generated by JS `renderVisuddhi()`.
# Let's add a new section for the 10 Nanas right after Visuddhi.

insert_point_2 = "        <!-- Cross-links -->"
vipassana_nana_html = """        <!-- 10 Vipassana Nanas -->
        <details class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-amber-500/20">
            <summary class="flex items-center justify-between font-bold text-amber-700 dark:text-amber-300 text-base">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>ဝိပဿနာဉာဏ် (၁၀) ပါး — မဂ်ဖိုလ်သို့ တက်လှမ်းရာ ဉာဏ်စဉ်များ</span>
            </summary>
            <div class="mt-4 px-2">
                <p class="text-xs text-slate-600 dark:text-slate-400 mb-5 pl-2 border-l-2 border-amber-400">ဆဋ္ဌမမြောက် ဝိသုဒ္ဓိဖြစ်သော <span class="font-bold text-amber-700 dark:text-amber-300">ပဋိပဒါဉာဏဒဿနဝိသုဒ္ဓိ</span> တွင် အောက်ပါ ဝိပဿနာဉာဏ် (၁၀) ပါး အဆင့်ဆင့် ဖြစ်ပေါ်၍ မဂ်ဖိုလ် (သတ္တမမြောက် ဝိသုဒ္ဓိ) သို့ ကူးပြောင်းသွားသည်။</p>
                <div class="relative pl-6 space-y-6" id="nana-timeline">
                    <!-- Rendered by JS -->
                </div>
            </div>
        </details>

"""
if "<!-- 10 Vipassana Nanas -->" not in content:
    content = content.replace(insert_point_2, vipassana_nana_html + insert_point_2)

# 3. Add JS data and render logic for 10 Nanas
js_insert_point = "        function renderVisuddhi() {"
nana_js = """        const nanaData = [
            { id: 1, pali: 'Sammasana-ñāṇa', name: 'သမသနဉာဏ်', desc: 'ရုပ်နာမ်တို့၏ အနိစ္စ/ဒုက္ခ/အနတ္တ လက္ခဏာ သုံးပါးကို အုပ်စုလိုက် သိမ်းကျုံး၍ ဆင်ခြင်သော ဉာဏ်။', icon: 'fa-layer-group' },
            { id: 2, pali: 'Udayabbaya-ñāṇa', name: 'ဥဒယဗ္ဗယဉာဏ်', desc: 'ရုပ်နာမ်တို့၏ ဖြစ်ပေါ်မှု (ဥဒယ) နှင့် ပျက်စီးမှု (ဝယ) ကို ရှင်းလင်းစွာ ရှုမြင်သော ဉာဏ်။ (ဤအဆင့်တွင် ဩဘာသ စသော ဝိပဿနုပက္ကိလေသ ၁၀ ပါး ဖြစ်ပေါ်တတ်သည်)', icon: 'fa-arrows-up-down' },
            { id: 3, pali: 'Bhaṅga-ñāṇa', name: 'ဘင်္ဂဉာဏ်', desc: 'ဖြစ်ပေါ်မှုကို မမြင်တော့ဘဲ ပျက်စီးမှု (ဘင်္ဂ) သက်သက်ကိုသာ အထပ်ထပ် ရှုမြင်သော ဉာဏ်။', icon: 'fa-bolt-lightning' },
            { id: 4, pali: 'Bhaya-ñāṇa', name: 'ဘယဉာဏ်', desc: 'ထိုသို့ အဆက်မပြတ် ပျက်စီးနေသော ရုပ်နာမ်များကို "ကြောက်မက်ဖွယ် ဘေးကြီး" ဟု ရှုမြင်သော ဉာဏ်။', icon: 'fa-triangle-exclamation' },
            { id: 5, pali: 'Ādīnava-ñāṇa', name: 'အာဒီနဝဉာဏ်', desc: 'ထိုရုပ်နာမ် သင်္ခါရတရားတို့၌ အပြစ်များကို ရှင်းလင်းစွာ မြင်လာသော ဉာဏ်။', icon: 'fa-biohazard' },
            { id: 6, pali: 'Nibbidā-ñāṇa', name: 'နိဗ္ဗိဒါဉာဏ်', desc: 'အပြစ်မြင်သဖြင့် ထိုရုပ်နာမ်တို့အပေါ် ငြီးငွေ့လာသော ဉာဏ်။', icon: 'fa-face-frown' },
            { id: 7, pali: 'Muñcitukamyatā-ñāṇa', name: 'မုဉ္စိတုကမျတာဉာဏ်', desc: 'ထိုရုပ်နာမ် ဆင်းရဲဒုက္ခမှ လွတ်မြောက်လိုသော ဆန္ဒ ပြင်းပြစွာ ဖြစ်ပေါ်လာသော ဉာဏ်။', icon: 'fa-person-running' },
            { id: 8, pali: 'Paṭisaṅkhā-ñāṇa', name: 'ပဋိသင်္ခါဉာဏ်', desc: 'လွတ်မြောက်ရန်အတွက် အနိစ္စ၊ ဒုက္ခ၊ အနတ္တ ကို ပြန်လည်၍ အထူးအားထုတ် ဆင်ခြင်သော ဉာဏ်။', icon: 'fa-magnifying-glass-arrow-right' },
            { id: 9, pali: 'Saṅkhārupekkhā-ñāṇa', name: 'သင်္ခါရုပေက္ခာဉာဏ်', desc: 'ရုပ်နာမ်တို့အပေါ် ကြောက်ခြင်း၊ ငြီးငွေ့ခြင်း စသည် မရှိတော့ဘဲ လျစ်လျူရှုကာ အလယ်အလတ် (ဥပေက္ခာ) တည်ရှိသော အထွတ်အထိပ် ဉာဏ်။', icon: 'fa-scale-balanced' },
            { id: 10, pali: 'Anuloma-ñāṇa', name: 'အနုလောမဉာဏ်', desc: 'မဂ်ဖိုလ် (နိဗ္ဗာန်) သို့ ကူးပြောင်းရန်အတွက် ရှေ့ဉာဏ်၊ နောက်ဉာဏ်တို့နှင့် လျော်ညီစွာ အလွန်လျင်မြန်စွာ ဖြစ်ပေါ်သော ဉာဏ်။', icon: 'fa-forward-step' }
        ];

        function renderNanas() {
            const container = document.getElementById('nana-timeline');
            if (!container) return;
            
            let html = '';
            // Left vertical line
            html += `<div class="absolute left-2 top-4 bottom-4 w-0.5 bg-amber-200 dark:bg-amber-800/50"></div>`;
            
            html += nanaData.map(n => `
                <div class="relative flex gap-4">
                    <div class="absolute -left-6 top-1 w-6 h-6 rounded-full bg-amber-100 dark:bg-amber-900 border-2 border-amber-400 dark:border-amber-600 flex items-center justify-center z-10 text-[9px] font-bold text-amber-700 dark:text-amber-300">
                        ${mm(n.id)}
                    </div>
                    <div class="flex-1 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl p-3 shadow-sm hover:shadow-md transition group">
                        <div class="flex items-center gap-2 mb-1">
                            <i class="fa-solid ${n.icon} text-amber-500 dark:text-amber-600 w-4"></i>
                            <h4 class="font-bold text-amber-800 dark:text-amber-400 text-sm">${n.name}</h4>
                            <span class="text-[10px] text-slate-400 font-mono hidden sm:inline-block">${n.pali}</span>
                        </div>
                        <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed ml-6">${n.desc}</p>
                    </div>
                </div>
            `).join('');
            
            container.innerHTML = html;
        }
        
"""
if "const nanaData =" not in content:
    content = content.replace(js_insert_point, nana_js + js_insert_point)

# 4. Add call to renderNanas() in DOMContentLoaded
init_block = "            renderVisuddhi();"
new_init_block = "            renderVisuddhi();\n            renderNanas();"
if "renderNanas();" not in content:
    content = content.replace(init_block, new_init_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
