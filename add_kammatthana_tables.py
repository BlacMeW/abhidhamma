import re

with open('kammatthana_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert HTML tables right before <!-- Footer Dedication -->
html_target = "    <!-- Footer Dedication -->"
if "sec-summary-tables" not in content:
    html_replacement = """    <!-- Master Summary Tables -->
    <section id="sec-summary-tables" class="max-w-7xl mx-auto px-4 mb-16 relative z-10">
        <div class="glass-card rounded-2xl p-4 md:p-6 border border-indigo-500/30 relative overflow-hidden space-y-6">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3 flex-wrap gap-2 relative z-10">
                <div>
                    <h3 class="font-bold text-indigo-700 dark:text-indigo-300 text-lg flex items-center gap-2">
                        <i class="fa-solid fa-table-list"></i> ကမ္မဋ္ဌာန်းပိုင်း သရုပ်ခွဲ အကျဉ်းချုပ် မဟာဇယားကြီးများ
                    </h3>
                    <p class="text-xs text-slate-600 dark:text-slate-400">စရိုက် နှင့် ကမ္မဋ္ဌာန်းဆက်စပ်မှု၊ ရရှိနိုင်သော ဈာန်/မဂ် အဆင့်ဆင့်များ</p>
                </div>
            </div>

            <!-- Table 1: Carita 6 & Kammatthana 40 -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-rose-500/30" open>
                <summary class="flex items-center justify-between font-bold text-rose-700 dark:text-rose-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-fingerprint mr-2"></i>စရိုက် (၆) ပါး နှင့် သင့်လျော်သော ကမ္မဋ္ဌာန်းများ (Carita & Kammaṭṭhāna)</span>
                </summary>
                <div id="kammatthana-carita-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Jhana & Magga Attainment -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-emerald-500/30" open>
                <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-mountain-sun mr-2"></i>ကမ္မဋ္ဌာန်း (၄၀) မှ ရရှိနိုင်သော ဈာန် နှင့် သမာဓိ အဆင့်ဆင့်</span>
                </summary>
                <div id="kammatthana-jhana-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </div>
    </section>

    <!-- Footer Dedication -->"""
    content = content.replace(html_target, html_replacement)

# Add JS logic right before `});` at the end of DOMContentLoaded
if "renderKammatthanaMasterTables();" not in content:
    js_code = """
            function renderKammatthanaMasterTables() {
                // 1. Carita Table
                const container1 = document.getElementById('kammatthana-carita-matrix');
                if (container1) {
                    const data1 = [
                        { name: '၁။ ရာဂစရိုက်', count: '၁၁ မျိုး', desc: 'အသုဘ (၁၀) ပါး၊ ကာယဂတာသတိ (၁) ပါး', desc2: 'အဆင်းလှခြင်းကို တပ်မက်မှုများသောကြောင့် ရွံစရာအာရုံကို ရှုမှတ်ရသည်။', color: 'rose' },
                        { name: '၂။ ဒေါသစရိုက်', count: '၄ မျိုး', desc: 'အပ္ပမညာ ၄ ပါး (မေတ္တာ၊ ကရုဏာ၊ မုဒိတာ၊ ဥပေက္ခာ) သို့မဟုတ် ဝဏ္ဏကသိုဏ်း ၄ ပါး (အဆင်း ၄ မျိုး)', desc2: 'အမြဲတမ်း စိတ်တိုတတ်သောကြောင့် စိတ်ကြည်လင်အေးချမ်းစေမည့် အာရုံများကို ရှုမှတ်ရသည်။', color: 'amber' },
                        { name: '၃။ မောဟစရိုက် နှင့် ၄။ ဝိတက်စရိုက်', count: '၁ မျိုး', desc: 'အာနာပါနဿတိ (ထွက်သက်ဝင်သက် ရှုမှတ်ခြင်း) တစ်မျိုးတည်းသာ', desc2: 'တွေဝေမှု၊ တွေးတောမှု များသောကြောင့် စိတ်ကို အာရုံတစ်ခုတည်းပေါ်သို့သာ တည်ငြိမ်အောင် ထားရသည်။', color: 'slate' },
                        { name: '၅။ သဒ္ဓါစရိုက်', count: '၆ မျိုး', desc: 'ဗုဒ္ဓါနုဿတိ စသော အနုဿတိ (၆) ပါး', desc2: 'ယုံကြည်မှုလွန်ကဲသောကြောင့် ဘုရား၊ တရား၊ သံဃာ စသည့် ကြည်ညိုဖွယ် ဂုဏ်များကို အာရုံပြုရသည်။', color: 'sky' },
                        { name: '၆။ ဗုဒ္ဓိစရိုက်', count: '၄ မျိုး', desc: 'မရဏာနုဿတိ၊ ဥပသမာနုဿတိ၊ အာဟာရေပဋိကူလသညာ၊ စတုဓာတုဝဝတ္ထာန်', desc2: 'ဉာဏ်ပညာကြီးမားသောကြောင့် ခက်ခဲနက်နဲသော သဘာဝတရားများကို အာရုံပြုရသည်။', color: 'emerald' },
                        { name: 'စရိုက်အားလုံးနှင့် သင့်လျော်သည်', count: '၁၄ မျိုး', desc: 'ပထဝီ၊ အာပေါ စသော ကသိုဏ်းကြီး ၆ ပါး နှင့် အရူပကမ္မဋ္ဌာန်း ၄ ပါး၊ အာကာသကသိုဏ်း၊ အာလောကကသိုဏ်း (ပေါင်း ၁၄ မျိုး)', desc2: 'မည်သည့် စရိုက်ရှိသူမဆို လွတ်လပ်စွာ ရှုမှတ်ပွားများနိုင်သည်။', color: 'cyan' }
                    ];
                    let html1 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-rose-50 dark:bg-rose-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">စရိုက်အမည်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">သင့်လျော်သော ကမ္မဋ္ဌာန်း</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">အမည်များ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">အကြောင်းရင်း</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data1.forEach(d => {
                        html1 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.desc}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc2}</td>
                        </tr>`;
                    });
                    html1 += `</tbody></table>`;
                    container1.innerHTML = html1;
                }

                // 2. Jhana Table
                const container2 = document.getElementById('kammatthana-jhana-matrix');
                if (container2) {
                    const data2 = [
                        { name: 'ဥပစာရသမာဓိ သာရနိုင်သည်', count: '၁၀ မျိုး', desc: 'ဗုဒ္ဓါနုဿတိ အစရှိသော အနုဿတိ ၈ ပါး (ကာယဂတာ၊ အာနာပါန ကြဉ်) + အာဟာရေပဋိကူလသညာ + စတုဓာတုဝဝတ္ထာန်', desc2: 'အာရုံအမျိုးမျိုး ပြောင်းလဲနေသောကြောင့် ဈာန် (အပ္ပနာသမာဓိ) မရနိုင်ဘဲ ဥပစာရသမာဓိ (ဈာန်အနီး) သာ ရနိုင်သည်။', color: 'emerald' },
                        { name: 'ပထမဈာန် သာရနိုင်သည်', count: '၁၁ မျိုး', desc: 'အသုဘ ၁၀ ပါး + ကာယဂတာသတိ ၁ ပါး', desc2: 'ရွံစရာအာရုံဖြစ်သောကြောင့် ဝိတက် (အာရုံသို့ စိတ်ကိုတင်ပေးခြင်း) မပါလျှင် စိတ်က အာရုံကို ယူမည်မဟုတ်သောကြောင့် ဒုတိယဈာန်စသည် မရနိုင်ပါ။', color: 'cyan' },
                        { name: 'ဈာန် (၃) ပါး သာရနိုင်သည် (စတုက္ကနယအရ ဈာန် ၄ ပါး)', count: '၁ မျိုး', desc: 'ကရုဏာ၊ မုဒိတာ အပ္ပမညာ', desc2: 'ဆင်းရဲသူ/ချမ်းသာသူကို အာရုံပြုရသဖြင့် ဥပေက္ခာ (လျစ်လျူရှုမှု) နှင့် တွဲဖက်၍ မရသောကြောင့် စတုတ္ထဈာန်/ပဉ္စမဈာန် မရနိုင်ပါ။ (တချို့ကျမ်းများတွင် မေတ္တာလည်း အပါအဝင်ဟု ဆိုသည်)', color: 'amber' },
                        { name: 'ဈာန် (၄) ပါးလုံး ရနိုင်သည်', count: '၁၈ မျိုး (ကသိုဏ်း ၁၀၊ အာနာပါန ၁၊ ဥပေက္ခာ ၁၊ အရူပ ၄)', desc: 'ကသိုဏ်း ၁၀ ပါး၊ အာနာပါနဿတိ နှင့် ဥပေက္ခာ (ပဉ္စမဈာန်သီးသန့်)၊ အရူပကမ္မဋ္ဌာန်း ၄ ပါး', desc2: 'အာရုံတည်ငြိမ်ပြီး အဆင့်ဆင့် မြင့်တက်သွားနိုင်သောကြောင့် ဈာန်အားလုံး (ပဉ္စမဈာန်အထိ) ရနိုင်သည်။', color: 'rose' }
                    ];
                    let html2 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-emerald-50 dark:bg-emerald-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">ရနိုင်သော အမြင့်ဆုံး သမာဓိ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ကမ္မဋ္ဌာန်းများ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">အကြောင်းရင်း</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data2.forEach(d => {
                        html2 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.desc}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc2}</td>
                        </tr>`;
                    });
                    html2 += `</tbody></table>`;
                    container2.innerHTML = html2;
                }
            }

            renderKammatthanaMasterTables();
"""
    
    js_target = "            const openKey = new URLSearchParams(location.search).get('open');"
    if js_target in content:
        content = content.replace(js_target, js_code + "\n" + js_target)

with open('kammatthana_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated kammatthana_sangaha.html")
