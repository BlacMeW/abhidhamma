import re

with open('missaka_sangaha.html', 'r', encoding='utf-8') as f:
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
                        <i class="fa-solid fa-table-list"></i> သမုစ္စည်းပိုင်း သရုပ်ခွဲ အကျဉ်းချုပ် မဟာဇယားကြီးများ
                    </h3>
                    <p class="text-xs text-slate-600 dark:text-slate-400">အကုသိုလ်၊ ကုသိုလ်၊ မိဿက နှင့် တရားကိုယ် (ပရမတ္ထ) တူညီမှုများကို ခြုံငုံကြည့်ရှုရန်</p>
                </div>
            </div>

            <!-- Table 1: Akusala/Kusala/Missaka Groups -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-cyan-500/30" open>
                <summary class="flex items-center justify-between font-bold text-cyan-700 dark:text-cyan-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-layer-group mr-2"></i>သမုစ္စည်း (၄) မျိုး ခြုံငုံဇယား (Samuccaya Groups)</span>
                </summary>
                <div id="samuccaya-groups-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Paramattha Mapping -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-emerald-500/30" open>
                <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-fingerprint mr-2"></i>အမည်ကွဲသော်လည်း တရားကိုယ် (ပရမတ္ထ) တူညီသော တရားများ</span>
                </summary>
                <div id="samuccaya-paramattha-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </div>
    </section>

    <!-- Footer Dedication -->"""
    content = content.replace(html_target, html_replacement)

# Add JS logic right before `});` at the end of DOMContentLoaded
if "renderSamuccayaMasterTables();" not in content:
    js_code = """
            function renderSamuccayaMasterTables() {
                // 1. Groups Table
                const container1 = document.getElementById('samuccaya-groups-matrix');
                if (container1) {
                    const data1 = [
                        { name: '၁။ အကုသလ သင်္ဂဟ', count: '၉ မျိုး (တရားကိုယ် ၁၄ ပါး)', desc: 'အာသဝ (၄)၊ ဩဃ (၄)၊ ယောဂ (၄)၊ ဂန္ထ (၄)၊ ဥပါဒါန် (၄)၊ နီဝရဏ (၆)၊ အနုသယ (၇)၊ သံယောဇဉ် (၁၀)၊ ကိလေသာ (၁၀)', type: 'အကုသိုလ် သီးသန့်', color: 'rose' },
                        { name: '၂။ မိဿက သင်္ဂဟ', count: '၇ မျိုး', desc: 'ဟိတ် (၆)၊ ဈာနင်္ဂ (၇)၊ မဂ္ဂင်္ဂ (၁၂)၊ ဣန္ဒြေ (၂၂)၊ ဗလ (၉)၊ အဓိပတိ (၄)၊ အာဟာရ (၄)', type: 'ကုသိုလ်၊ အကုသိုလ်၊ အဗျာကတ ရောနှော', color: 'amber' },
                        { name: '၃။ ဗောဓိပက္ခိယ သင်္ဂဟ', count: '၇ မျိုး (တရားကိုယ် ၁၄ ပါး)', desc: 'သတိပဋ္ဌာန် (၄)၊ သမ္မပ္ပဓာန် (၄)၊ ဣဒ္ဓိပါဒ် (၄)၊ ဣန္ဒြေ (၅)၊ ဗလ (၅)၊ ဗောဇ္ဈင် (၇)၊ မဂ္ဂင် (၈)', type: 'လောကုတ္တရာ မဂ်ဉာဏ်၏ အသင်းအပင်း (ကုသိုလ်)', color: 'emerald' },
                        { name: '၄။ သဗ္ဗ သင်္ဂဟ', count: '၅ မျိုး (ခန္ဓာ၊ အာယတန၊ ဓာတ်၊ သစ္စာ)', desc: 'ခန္ဓာ (၅)၊ ဥပါဒါနက္ခန္ဓာ (၅)၊ အာယတန (၁၂)၊ ဓာတ် (၁၈)၊ အရိယသစ္စာ (၄)', type: 'ပရမတ္ထတရား (၇၂) ပါးလုံး အကျုံးဝင်သည်', color: 'cyan' }
                    ];
                    let html1 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-cyan-50 dark:bg-cyan-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">သမုစ္စည်း အမျိုးအစား</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော အုပ်စုများ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">သဘောသဘာဝ</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data1.forEach(d => {
                        html1 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.desc}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400">${d.type}</td>
                        </tr>`;
                    });
                    html1 += `</tbody></table>`;
                    container1.innerHTML = html1;
                }

                // 2. Paramattha Table
                const container2 = document.getElementById('samuccaya-paramattha-matrix');
                if (container2) {
                    const data2 = [
                        { name: 'လောဘ စေတသိက်', names: 'ကာမာသဝ၊ ဘဝါသဝ၊ ကာမောဃ၊ ဘဝေါဃ၊ ကာမယောဂ၊ ဘဝယောဂ၊ အဘိဇ္ဈာကာယဂန္ထ၊ ကာမုပါဒါန်၊ ကာမရာဂါနုသယ၊ ဘဝရာဂါနုသယ၊ ကာမရာဂသံယောဇဉ်၊ ရူပရာဂသံယောဇဉ်၊ အရူပရာဂသံယောဇဉ်၊ လောဘကိလေသာ', group: 'အကုသလ သင်္ဂဟ (အများဆုံးသော အမည်များဖြင့် ခေါ်ဝေါ်ခံရသည်)', color: 'rose' },
                        { name: 'ပညာ စေတသိက် (အမောဟ)', names: 'အဝိဇ္ဇာ၏ ဆန့်ကျင်ဘက်။ အမောဟဟိတ်၊ ဝီမံသိဒ္ဓိပါဒ်၊ ပညိန္ဒြေ၊ ပညာဗလ၊ ဓမ္မဝိစယသမ္ဗောဇ္ဈင်၊ သမ္မာဒိဋ္ဌိမဂ္ဂင်', group: 'မိဿက နှင့် ဗောဓိပက္ခိယ (ကုသိုလ်ဘက်တွင် အများဆုံးပါဝင်သည်)', color: 'emerald' },
                        { name: 'ဝီရိယ စေတသိက်', names: 'ဝီရိယိန္ဒြေ၊ ဝီရိယဗလ၊ သမ္မာဝါယာမမဂ္ဂင်၊ ဝီရိယသမ္ဗောဇ္ဈင်၊ သမ္မပ္ပဓာန် (၄) ပါးလုံး၊ ဝီရိယိဒ္ဓိပါဒ်', group: 'ဗောဓိပက္ခိယ သင်္ဂဟ (လုံ့လဝီရိယသည် အမည်အမျိုးမျိုးဖြင့် ပါဝင်သည်)', color: 'amber' },
                        { name: 'ဒိဋ္ဌိ စေတသိက်', names: 'ဒိဋ္ဌာသဝ၊ ဒိဋ္ဌောဃ၊ ဒိဋ္ဌိယောဂ၊ ဣဒံသစ္စာဘိနိဝေသကာယဂန္ထ၊ ဒိဋ္ဌုပါဒါန်၊ သီလဗ္ဗတုပါဒါန်၊ အတ္တဝါဒုပါဒါန်၊ ဒိဋ္ဌာနုသယ၊ ဒိဋ္ဌိသံယောဇဉ်၊ သီလဗ္ဗတပရာမာသသံယောဇဉ်၊ ဒိဋ္ဌိကိလေသာ', group: 'အကုသလ သင်္ဂဟ', color: 'rose' }
                    ];
                    let html2 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-emerald-50 dark:bg-emerald-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">တရားကိုယ် (ပရမတ္ထ)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">အမည်အမျိုးမျိုးဖြင့် ခေါ်ဆိုခံရပုံ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">အများဆုံးပါဝင်သော အုပ်စု</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data2.forEach(d => {
                        html2 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.names}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 font-medium">${d.group}</td>
                        </tr>`;
                    });
                    html2 += `</tbody></table>`;
                    container2.innerHTML = html2;
                }
            }

            renderSamuccayaMasterTables();
"""
    # Find DOMContentLoaded block to insert
    js_target = "            const tbody = document.getElementById('missaka-matrix-tbody');"
    if js_target in content:
        content = content.replace(js_target, js_code + "\n" + js_target)
    else:
        # fallback
        content = content.replace("        });\n    </script>\n    <script src=\"accessibility.js\">", js_code + "\n        });\n    </script>\n    <script src=\"accessibility.js\">")

with open('missaka_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated missaka_sangaha.html")
