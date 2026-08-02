import re

with open('vithimutta_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Patisandhi Master Table HTML
patisandhi_target = """                <details class="glass-card rounded-xl p-4 border border-emerald-500/20" open>
                    <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm">
                        <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-xs"></i>စတုယောနိ — ပဋိသန္ဓေ ယူသည့် နည်းလမ်း (၄) မျိုး</span>
                    </summary>
                    <div class="mt-3 pl-2 flex flex-wrap gap-2" id="yoni-chips"></div>
                </details>"""

patisandhi_replacement = patisandhi_target + """
                
                <!-- Master Patisandhi Table -->
                <details class="glass-card rounded-xl p-4 md:p-6 border border-emerald-500/30 mt-4" open>
                    <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base">
                        <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>ဘုံ၊ ပဋိသန္ဓေ၊ ပုဂ္ဂိုလ်၊ သက်တမ်း ဆက်စပ်မှုဇယားကြီး (Master Summary Table)</span>
                    </summary>
                    <div id="patisandhi-master-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
                </details>"""

if patisandhi_target in content:
    content = content.replace(patisandhi_target, patisandhi_replacement)
else:
    print("Error: Could not find patisandhi_target")

# 2. Insert Kamma Master Table HTML
kamma_target = """                <div id="kamma-tetrads" class="space-y-4"></div>"""
kamma_replacement = kamma_target + """
                
                <!-- Master Kamma Table -->
                <details class="glass-card rounded-xl p-4 md:p-6 border border-violet-500/30 mt-4" open>
                    <summary class="flex items-center justify-between font-bold text-violet-700 dark:text-violet-300 text-sm md:text-base">
                        <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>ကမ္မ (၁၆) ပါး အကျဉ်းချုပ်ဇယား (Master Summary Table)</span>
                    </summary>
                    <div id="kamma-master-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
                </details>"""

if kamma_target in content:
    content = content.replace(kamma_target, kamma_replacement)
else:
    print("Error: Could not find kamma_target")

# 3. Insert JavaScript functions
js_code = """
        function renderPatisandhiMasterTable() {
            const container = document.getElementById('patisandhi-master-matrix');
            if (!container) return;
            
            const data = [
                { group: 'အပါယ် (၄) ဘုံ', color: 'rose', rows: [
                    { bhumi: 'ငရဲ, တိရစ္ဆာန်, ပြိတ္တာ, အသုရကာယ်', patisandhi: 'အကုသလဝိပါက် ဥပေက္ခာသန္တီရဏ (၁)', puggala: 'ဒုဂ္ဂတိအဟိတ်ပုဂ္ဂိုလ်', lifespan: 'သက်တမ်းအမြဲမရှိ (ကံကုန်မှသေ)' }
                ]},
                { group: 'ကာမသုဂတိ (၇) ဘုံ', color: 'emerald', rows: [
                    { bhumi: 'လူ့ဘုံ, စတုမဟာရာဇ်ဘုံ (အဟိတ်)', patisandhi: 'ကုသလဝိပါက် ဥပေက္ခာသန္တီရဏ (၁)', puggala: 'သုဂတိအဟိတ်ပုဂ္ဂိုလ် (လူမိုက်/အကန္ဓ)', lifespan: 'သက်တမ်းအမြဲမရှိ (စတုမဟာရာဇ်၌ နှစ် ၅၀၀/လူ့နှစ် ၉ သန်း)' },
                    { bhumi: 'လူ့ဘုံ နှင့် နတ် (၆) ဘုံ', patisandhi: 'မဟာဝိပါက် ဉာဏဝိပ္ပယုတ် (၄)', puggala: 'ဒွိဟိတ်ပုဂ္ဂိုလ်', lifespan: 'လူ(အမြဲမရှိ)၊ နတ်၆ဘုံ(နှစ်၅၀၀ မှ ၁သောင်း၆ထောင်ထိ)' },
                    { bhumi: 'လူ့ဘုံ နှင့် နတ် (၆) ဘုံ', patisandhi: 'မဟာဝိပါက် ဉာဏသမ္ပယုတ် (၄)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ်', lifespan: 'လူ(အမြဲမရှိ)၊ နတ်၆ဘုံ(နှစ်၅၀၀ မှ ၁သောင်း၆ထောင်ထိ)' }
                ]},
                { group: 'ရူပ (၁၅) ဘုံ (အသညသတ်ကြဉ်)', color: 'sky', rows: [
                    { bhumi: 'ပဌမဈာန် (၃) ဘုံ', patisandhi: 'ရူပါဝစရ ပဌမဈာန်ဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: 'ကမ္ဘာ၏ ၃ပုံ၁ပုံ မှ ၁ ကမ္ဘာ အထိ' },
                    { bhumi: 'ဒုတိယဈာန် (၃) ဘုံ', patisandhi: 'ရူပါဝစရ ဒုတိယဈာန်ဝိပါက် (၁) နှင့် တတိယဈာန်ဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: '၂ ကမ္ဘာ မှ ၈ ကမ္ဘာ အထိ' },
                    { bhumi: 'တတိယဈာန် (၃) ဘုံ', patisandhi: 'ရူပါဝစရ စတုတ္ထဈာန်ဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: '၁၆ ကမ္ဘာ မှ ၆၄ ကမ္ဘာ အထိ' },
                    { bhumi: 'စတုတ္ထဈာန် (၆) ဘုံ (အသညသတ်ကြဉ်)', patisandhi: 'ရူပါဝစရ ပဉ္စမဈာန်ဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ (သုဒ္ဓါဝါသ၌ အနာဂါမ်/ရဟန္တာ)', lifespan: 'ကမ္ဘာ ၅၀၀ မှ ၁၆,၀၀၀ အထိ' }
                ]},
                { group: 'အရူပ (၄) ဘုံ', color: 'amber', rows: [
                    { bhumi: 'အာကာသာနဉ္စာယတနဘုံ', patisandhi: 'အာကာသာနဉ္စာယတနဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: 'ကမ္ဘာ ၂ သောင်း' },
                    { bhumi: 'ဝိညာဏဉ္စာယတနဘုံ', patisandhi: 'ဝိညာဏဉ္စာယတနဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: 'ကမ္ဘာ ၄ သောင်း' },
                    { bhumi: 'အာကိဉ္စညာယတနဘုံ', patisandhi: 'အာကိဉ္စညာယတနဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: 'ကမ္ဘာ ၆ သောင်း' },
                    { bhumi: 'နေဝသညာနာသညာယတနဘုံ', patisandhi: 'နေဝသညာနာသညာယတနဝိပါက် (၁)', puggala: 'တိဟိတ်ပုဂ္ဂိုလ် / အရိယာ', lifespan: 'ကမ္ဘာ ၈ သောင်း ၄ ထောင်' }
                ]},
                { group: 'အသညသတ် (၁) ဘုံ', color: 'slate', rows: [
                    { bhumi: 'အသညသတ်ဘုံ', patisandhi: 'ဇီဝိတနဝကကလာပ် (ရုပ်ပဋိသန္ဓေ - ၁)', puggala: 'သုဂတိအဟိတ်ပုဂ္ဂိုလ်', lifespan: 'ကမ္ဘာ ၅၀၀' }
                ]}
            ];

            let html = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead>
                    <tr class="bg-slate-100 dark:bg-slate-800 border-b-2 border-slate-300 dark:border-slate-600">
                        <th class="p-2.5 border-r border-slate-300 dark:border-slate-600 font-bold text-slate-800 dark:text-slate-200">ဘုံအမည်</th>
                        <th class="p-2.5 border-r border-slate-300 dark:border-slate-600 font-bold text-slate-800 dark:text-slate-200">ပဋိသန္ဓေ (၁၉+၁)</th>
                        <th class="p-2.5 border-r border-slate-300 dark:border-slate-600 font-bold text-slate-800 dark:text-slate-200">ပုဂ္ဂိုလ်</th>
                        <th class="p-2.5 font-bold text-slate-800 dark:text-slate-200">သက်တမ်း (အကြမ်းဖျင်း)</th>
                    </tr>
                </thead>
                <tbody>`;

            data.forEach(g => {
                const colorClass = `text-${g.color}-700 dark:text-${g.color}-300`;
                const bgClass = `bg-${g.color}-500/10`;
                html += `<tr class="${bgClass} border-y border-slate-300 dark:border-slate-700">
                    <td colspan="4" class="p-2 font-bold ${colorClass} text-center">${g.group}</td>
                </tr>`;
                
                g.rows.forEach(r => {
                    html += `<tr class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                        <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 font-semibold ${colorClass}">${r.bhumi}</td>
                        <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300">${r.patisandhi}</td>
                        <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300">${r.puggala}</td>
                        <td class="p-2.5 text-slate-600 dark:text-slate-400 font-mono leading-relaxed">${r.lifespan}</td>
                    </tr>`;
                });
            });
            html += `</tbody></table>`;
            container.innerHTML = html;
        }

        function renderKammaMasterTable() {
            const container = document.getElementById('kamma-master-matrix');
            if (!container) return;

            const data = [
                {
                    group: '၁။ ကိစ္စတပ်၍ခေါ်သောကံ ၄-ပါး (Kicca)', color: 'sky',
                    items: [
                        { name: 'ဇနကကံ', desc: 'ပဋိသန္ဓေကျိုး, ပဝတ္တိကျိုးတို့ကို ဖြစ်စေတတ်သောကံ' },
                        { name: 'ဥပတ္ထမ္ဘကကံ', desc: 'ဇနကကံ၏ အကျိုးကို ထောက်ပံ့ကူညီတတ်သောကံ' },
                        { name: 'ဥပပီဠကကံ', desc: 'ဇနကကံ၏ အကျိုးကို နှိပ်စက်တားမြစ်တတ်သောကံ' },
                        { name: 'ဥပဃာတကကံ', desc: 'ဇနကကံ၏ အကျိုးကို အပြီးတိုင် ဖြတ်တောက်ဖျက်ဆီးတတ်သောကံ' }
                    ]
                },
                {
                    group: '၂။ အကျိုးပေးမည့်အလှည့်ကိုစွဲ၍ခေါ်သောကံ ၄-ပါး (Pākadānapariyāya)', color: 'emerald',
                    items: [
                        { name: 'ဂရုကကံ', desc: 'အခြားကံများက တားမြစ်၍မရနိုင်သော အလွန်ကြီးလေးသောကံ (ဥပမာ-ပဉ္စာနန္တရိယကံ၊ မဟဂ္ဂုတ်ကံ)' },
                        { name: 'အာသန္နကံ', desc: 'သေခါနီးကာလ၌ ပြုလုပ်အပ်သော (သို့) အောက်မေ့အပ်သောကံ' },
                        { name: 'အာစိဏ္ဏကံ', desc: 'အမြဲမပြတ် လေ့လာဆည်းပူးထားသောကံ' },
                        { name: 'ကဋတ္တာကံ', desc: 'အထက်ပါ သုံးပါးမှလွတ်သော သာမန်ကံ (အမှတ်တမဲ့ပြုသောကံ)' }
                    ]
                },
                {
                    group: '၃။ အကျိုးပေးမည့်အချိန်ကာလကိုစွဲ၍ခေါ်သောကံ ၄-ပါး (Pākakāla)', color: 'amber',
                    items: [
                        { name: 'ဒိဋ္ဌဓမ္မဝေဒနီယကံ', desc: 'ယခုဘဝ၌ပင် အကျိုးပေးမည့်ကံ (ပထမဇော၏ သတ္တိ)' },
                        { name: 'ဥပပဇ္ဇဝေဒနီယကံ', desc: 'ဒုတိယဘဝ (ဒုတိယအတ္တဘော) ၌ အကျိုးပေးမည့်ကံ (သတ္တမဇော၏ သတ္တိ)' },
                        { name: 'အပရာပရိယဝေဒနီယကံ', desc: 'တတိယဘဝမှစ၍ နိဗ္ဗာန်မဝင်မချင်း အကျိုးပေးမည့်ကံ (အလယ်ဇော ၅-ချက်၏ သတ္တိ)' },
                        { name: 'အဟောသိကံ', desc: 'အကျိုးပေးခွင့် မရတော့ဘဲ ပျက်ပြယ်သွားသောကံ (အချိန်လွန်သွားသောကံ / ရဟန္တာတို့၏ ရှေးကံ)' }
                    ]
                },
                {
                    group: '၄။ အကျိုးပေးရာဌာနကိုစွဲ၍ခေါ်သောကံ ၄-ပါး (Pākaṭṭhāna)', color: 'violet',
                    items: [
                        { name: 'အကုသိုလ်ကံ', desc: 'အပါယ် ၄-ဘုံ၌ အကျိုးပေးတတ်သော မကောင်းမှုကံ (အကုသိုလ်စိတ် ၁၂-ပါး)' },
                        { name: 'ကာမာဝစရကုသိုလ်ကံ', desc: 'ကာမသုဂတိ ၇-ဘုံ၌ အကျိုးပေးတတ်သော ကောင်းမှုကံ (မဟာကုသိုလ်စိတ် ၈-ပါး)' },
                        { name: 'ရူပါဝစရကုသိုလ်ကံ', desc: 'ရူပ ၁၆-ဘုံ၌ အကျိုးပေးတတ်သော ကောင်းမှုကံ (ရူပကုသိုလ်စိတ် ၅-ပါး)' },
                        { name: 'အရူပါဝစရကုသိုလ်ကံ', desc: 'အရူပ ၄-ဘုံ၌ အကျိုးပေးတတ်သော ကောင်းမှုကံ (အရူပကုသိုလ်စိတ် ၄-ပါး)' }
                    ]
                }
            ];

            let html = `<div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">`;
            data.forEach(g => {
                const colorClass = `text-${g.color}-700 dark:text-${g.color}-300`;
                const borderClass = `border-${g.color}-500/30`;
                const bgClass = `bg-${g.color}-500/10`;
                
                html += `<div class="border ${borderClass} rounded-xl overflow-hidden">
                    <div class="${bgClass} p-2 font-bold ${colorClass} text-center border-b ${borderClass}">${g.group}</div>
                    <div class="bg-white dark:bg-slate-900 divide-y divide-slate-200 dark:divide-slate-700">`;
                g.items.forEach(it => {
                    html += `<div class="p-2.5 flex flex-col gap-1 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                        <span class="font-bold text-slate-800 dark:text-slate-200">${it.name}</span>
                        <span class="text-slate-600 dark:text-slate-400">${it.desc}</span>
                    </div>`;
                });
                html += `</div></div>`;
            });
            html += `</div>`;
            container.innerHTML = html;
        }
"""

js_target = """        function jumpToGroup(groupKey) {"""
if js_target in content:
    content = content.replace(js_target, js_code + "\n" + js_target)
else:
    print("Error: Could not find js_target")

# 4. Call render functions in DOMContentLoaded
init_target = """            renderKammaTetrads();"""
init_replacement = init_target + """
            renderPatisandhiMasterTable();
            renderKammaMasterTable();"""
if init_target in content:
    content = content.replace(init_target, init_replacement)
else:
    print("Error: Could not find init_target")

with open('vithimutta_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)

