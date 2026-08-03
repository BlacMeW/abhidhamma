import re

with open('vithi_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert HTML tables before <!-- Cross-link -->
html_target = "        <!-- Cross-link -->"
html_replacement = """        <!-- Master Summary Tables -->
        <section id="sec-summary-tables" class="glass-card rounded-2xl p-4 md:p-6 border border-indigo-500/30 relative overflow-hidden space-y-6 mb-8">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3 flex-wrap gap-2 relative z-10">
                <div>
                    <h3 class="font-bold text-indigo-700 dark:text-indigo-300 text-lg flex items-center gap-2">
                        <i class="fa-solid fa-table-list"></i> ၆။ ဝီထိသင်္ဂဟ သရုပ်ခွဲ အကျဉ်းချုပ် ဇယားကြီးများ
                    </h3>
                    <p class="text-xs text-slate-600 dark:text-slate-400">အာရုံသက်တမ်း၊ ပုဂ္ဂိုလ်၊ ဘုံ နှင့် ဇော ဆက်စပ်မှုများကို ခြုံငုံကြည့်ရှုရန်</p>
                </div>
            </div>

            <!-- Table 1: Arammana Lifespan & Vithi -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-cyan-500/30" open>
                <summary class="flex items-center justify-between font-bold text-cyan-700 dark:text-cyan-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-hourglass-half mr-2"></i>ပဉ္စဒွါရဝီထိ အာရုံသက်တမ်း (၁၇ ချက်) နှင့် ဝီထိ (၄) မျိုး ဆက်စပ်ပုံ</span>
                </summary>
                <div id="vithi-arammana-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Puggala, Bhumi, Javana -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-emerald-500/30" open>
                <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-users-viewfinder mr-2"></i>ပုဂ္ဂိုလ် (၈) ယောက် နှင့် ရရှိနိုင်သော ဇောစိတ်များ</span>
                </summary>
                <div id="vithi-puggala-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
            
            <!-- Table 3: Vithi Mutta & Vithi Patta -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-rose-500/30" open>
                <summary class="flex items-center justify-between font-bold text-rose-700 dark:text-rose-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-diagram-project mr-2"></i>ဝီထိမုတ္တ / ဝီထိပတ္တ (ဝီထိတွင် ပါဝင်သောစိတ် / မပါဝင်သောစိတ်) ခွဲခြားမှု</span>
                </summary>
                <div id="vithi-mutta-patta-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </section>

        <!-- Cross-link -->"""

if html_target in content:
    content = content.replace(html_target, html_replacement)
else:
    print("Error: Could not find html_target")

# 2. Add JS logic
js_code = """
        function renderVithiMasterTables() {
            // 1. Arammana Table
            const container1 = document.getElementById('vithi-arammana-matrix');
            if (container1) {
                const data1 = [
                    { name: '၁။ အတိမဟန္တာရုံ', size: 'အလွန်ကြီးမားသော အာရုံ', atita: '၁ ချက်', vithi: '၁၄ ချက် (တဒါရုံ ၂ ကြိမ်ကျသည်)', total: '၁၅ ချက် (အာရုံသက်တမ်း ၁၇ ချက် မကုန်မီ ဘဝင်ပြန်ကျသည်၊ ဝီထိသက်တမ်း ၁၇ ချက်အပြည့်)', end: 'တဒါရမ္မဏဝါရ', color: 'cyan' },
                    { name: '၂။ မဟန္တာရုံ', size: 'ကြီးမားသော အာရုံ', atita: '၂ သို့မဟုတ် ၃ ချက်', vithi: '၁၂ ချက် (တဒါရုံမကျပါ)', total: '၁၄/၁၅ ချက် (အာရုံသက်တမ်း ပြီးဆုံးသွားသည်)', end: 'ဇဝနဝါရ', color: 'sky' },
                    { name: '၃။ ပရိတ္တာရုံ', size: 'သေးငယ်သော အာရုံ', atita: '၄ မှ ၉ ချက်', vithi: 'ဝုဋ္ဌော ၃ ကြိမ် (ဇော မစောပါ)', total: '၇ မှ ၁၂ ချက်', end: 'ဝေါဋ္ဌပ္ပနဝါရ', color: 'indigo' },
                    { name: '၄။ အတိပရိတ္တာရုံ', size: 'အလွန်သေးငယ်သော အာရုံ', atita: '၁၀ မှ ၁၅ ချက်', vithi: 'ဝီထိစိတ် လုံးဝမဖြစ်ပါ (ဘဝင်သာ တုန်လှုပ်သည်)', total: 'ဘဝင်္ဂစလန၊ ဘဝင်္ဂုပစ္ဆေဒ မျှသာ', end: 'မောဃဝါရ', color: 'slate' }
                ];
                let html1 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                    <thead class="bg-cyan-50 dark:bg-cyan-900/40">
                        <tr>
                            <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">အာရုံအမည်</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">အတိတ်ဘဝင် လွန်ခြင်း</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">ဝီထိစိတ် ဖြစ်ခွင့်</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">ဝီထိပြီးဆုံးသည့် ဝါရ</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white dark:bg-slate-900">`;
                data1.forEach(d => {
                    html1 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                        <td class="p-2 border border-slate-300 dark:border-slate-700">
                            <span class="font-bold text-${d.color}-700 dark:text-${d.color}-400 block">${d.name}</span>
                            <span class="text-[10px] text-slate-500">${d.size}</span>
                        </td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.atita}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300">${d.vithi}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-500">${d.end}</td>
                    </tr>`;
                });
                html1 += `</tbody></table>`;
                container1.innerHTML = html1;
            }

            // 2. Puggala Javana Table
            const container2 = document.getElementById('vithi-puggala-matrix');
            if (container2) {
                const data2 = [
                    { name: 'ပုထုဇဉ်', count: '၄ ယောက်', javana: 'အကုသိုလ် (၁၂) ပါး၊ မဟာကုသိုလ် (၈) ပါး၊ မဟဂ္ဂုတ်ကုသိုလ် (၉) ပါး', nojavana: 'ကြိယာဇော (၁၈)၊ မဂ် (၄)၊ ဖိုလ် (၄) တို့ လုံးဝ မစောပါ။ (မဂ်ဉာဏ်မရသေး၍)', color: 'rose' },
                    { name: 'သောတာပန်၊ သကဒါဂါမ်', count: 'သေက္ခ ၂ ယောက်', javana: 'အကုသိုလ် (၇) ပါး (ဒိဋ္ဌိ ၄၊ ဝိစိ ၁ ကြဉ်)၊ မဟာကုသိုလ် (၈) ပါး၊ မဟဂ္ဂုတ်ကုသိုလ် (၉) ပါး၊ မဂ်/ဖိုလ် ဇောများ', nojavana: 'အပါယ်သို့ပို့မည့် အကုသိုလ် ၅ ပါး လုံးဝ မစောတော့ပါ။ ကြိယာဇောများ မစောပါ။', color: 'amber' },
                    { name: 'အနာဂါမ်', count: 'သေက္ခ ၁ ယောက်', javana: 'အကုသိုလ် (၅) ပါး (လောဘဒိဋ္ဌိဝိပ္ပယုတ် ၄၊ ဥဒ္ဓစ္စ ၁)၊ မဟာကုသိုလ် (၈) ပါး၊ မဟဂ္ဂုတ်ကုသိုလ် (၉) ပါး၊ မဂ်/ဖိုလ် ဇောများ', nojavana: 'ဒေါသ (၂) ပါး ထပ်မံကင်းစင်သွားသည်။ ကြိယာဇောများ မစောပါ။', color: 'emerald' },
                    { name: 'ရဟန္တာ', count: 'အသေက္ခ ၁ ယောက်', javana: 'မဟာကြိယာ (၈) ပါး၊ ဟသိတုပ္ပါဒ် (၁) ပါး၊ မဟဂ္ဂုတ်ကြိယာ (၉) ပါး၊ အရဟတ္တဖိုလ် (၁) ပါး', nojavana: 'ကိလေသာ ကင်းစင်သွားပြီဖြစ်၍ အကုသိုလ်ရော ကုသိုလ်ပါ လုံးဝ (လုံးဝ) မစောတော့ပါ။ ကံ မမြောက်တော့ပါ။', color: 'indigo' }
                ];
                let html2 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                    <thead class="bg-emerald-50 dark:bg-emerald-900/40">
                        <tr>
                            <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">ပုဂ္ဂိုလ်</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">အမျိုးအစား</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">ဖြစ်နိုင်သော ဇောစိတ်များ (စောနိုင်သော ဇော)</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">မဖြစ်နိုင်သော ဇောစိတ်များ (ပယ်ပြီး)</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white dark:bg-slate-900">`;
                data2.forEach(d => {
                    html2 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.javana}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-500 leading-relaxed">${d.nojavana}</td>
                    </tr>`;
                });
                html2 += `</tbody></table>`;
                container2.innerHTML = html2;
            }

            // 3. Vithi Mutta & Patta Table
            const container3 = document.getElementById('vithi-mutta-patta-matrix');
            if (container3) {
                const data3 = [
                    { name: 'ဝီထိပတ္တ သက်သက်', count: '၇၀ ပါး', citta: 'အကုသိုလ် (၁၂)၊ ကုသိုလ် (၂၁)၊ ကြိယာ (၁၈)၊ ပဉ္စဒွါရာဝဇ္ဇန်း(၁)၊ ဝိညာဉ်(၁၀)၊ သမ္ပဋိစ္ဆန်း(၂)၊ မနောဒွါရာဝဇ္ဇန်း(၁)၊ ဟသိတုပ္ပါဒ်(၁)၊ မဂ်(၄)', desc: 'ဝီထိလမ်းကြောင်းထဲတွင်သာ ဖြစ်ပေါ်သည်။ ပဋိသန္ဓေ၊ ဘဝင်၊ စုတိ လုံးဝ မဖြစ်ပါ။', color: 'rose' },
                    { name: 'ဝီထိမုတ္တ နှင့် ဝီထိပတ္တ', count: '၁၀ ပါး', citta: 'ဥပေက္ခာသန္တီရဏ (၂) ပါး၊ မဟာဝိပါက် (၈) ပါး', desc: 'ပဋိသန္ဓေ၊ ဘဝင်၊ စုတိ လည်းဖြစ်သလို ဝီထိလမ်းကြောင်းထဲတွင် (တဒါရုံ၊ သန္တီရဏ အနေဖြင့်) လည်း ပါဝင်သည်။ (ရောနှောနေသောစိတ်များ)', color: 'amber' },
                    { name: 'ဝီထိမုတ္တ သက်သက်', count: '၉ ပါး', citta: 'မဟဂ္ဂုတ်ဝိပါက် (၉) ပါး (ရူပဝိပါက် ၅ + အရူပဝိပါက် ၄)', desc: 'ပဋိသန္ဓေ၊ ဘဝင်၊ စုတိ ကိစ္စများတည်းကိုသာ ဆောင်ရွက်ပြီး ဝီထိလမ်းကြောင်းထဲသို့ လုံးဝ မဝင်ပါ။', color: 'emerald' }
                ];
                let html3 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                    <thead class="bg-rose-50 dark:bg-rose-900/40">
                        <tr>
                            <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">အုပ်စုအမည်</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700 w-24 text-center">အရေအတွက်</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th>
                            <th class="p-2 border border-slate-300 dark:border-slate-700">မှတ်ချက်</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white dark:bg-slate-900">`;
                data3.forEach(d => {
                    html3 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.citta}</td>
                        <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                    </tr>`;
                });
                html3 += `</tbody></table>`;
                container3.innerHTML = html3;
            }
        }
"""
js_target = """        function renderAppanaDetailed() {"""
if js_target in content:
    content = content.replace(js_target, js_code + "\n" + js_target)
else:
    print("Error: Could not find js_target")

# 3. Add to Document Ready
init_target = """        window.onload = () => {"""
init_replacement = """        window.onload = () => {
            renderVithiMasterTables();"""
if init_target in content:
    content = content.replace(init_target, init_replacement)
else:
    print("Error: Could not find init_target")

with open('vithi_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)
