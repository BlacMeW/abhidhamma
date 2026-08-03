import re

with open('paticcasamuppada.html', 'r', encoding='utf-8') as f:
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
                        <i class="fa-solid fa-table-list"></i> ပစ္စယသင်္ဂဟ သရုပ်ခွဲ အကျဉ်းချုပ် မဟာဇယားကြီးများ
                    </h3>
                    <p class="text-xs text-slate-600 dark:text-slate-400">ပဋိစ္စသမုပ္ပါဒ် အင်္ဂါ (၁၂) ပါး၊ ကာလ (၃) ပါး နှင့် ပဋ္ဌာန်း ပစ္စည်း (၂၄) ပါး အုပ်စုများ</p>
                </div>
            </div>

            <!-- Table 1: Paticcasamuppada 12 factors & 3 periods -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-amber-500/30" open>
                <summary class="flex items-center justify-between font-bold text-amber-700 dark:text-amber-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-arrows-spin mr-2"></i>ပဋိစ္စသမုပ္ပါဒ် အင်္ဂါ (၁၂) ပါး နှင့် ကာလ (၃) ပါး ဆက်စပ်မှု</span>
                </summary>
                <div id="paticca-kala-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Paccaya 24 conditions -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-cyan-500/30" open>
                <summary class="flex items-center justify-between font-bold text-cyan-700 dark:text-cyan-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-network-wired mr-2"></i>ပဋ္ဌာန်း ပစ္စည်း (၂၄) ပါး အုပ်စုခွဲ (Paccaya Groups)</span>
                </summary>
                <div id="paccaya-groups-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </div>
    </section>

    <!-- Footer Dedication -->"""
    content = content.replace(html_target, html_replacement)

# Add JS logic right before `});` at the end of DOMContentLoaded
if "renderPaccayaMasterTables();" not in content:
    js_code = """
            function renderPaccayaMasterTables() {
                // 1. Paticca Kala Table
                const container1 = document.getElementById('paticca-kala-matrix');
                if (container1) {
                    const data1 = [
                        { name: 'အတိတ်ကာလ (Past)', anga: 'အဝိဇ္ဇာ၊ သင်္ခါရ', hethu: 'အတိတ် အကြောင်း (၂) ပါး', desc: 'လွန်လေပြီးသော ဘဝများက ပြုလုပ်ခဲ့သော မသိမှု (အဝိဇ္ဇာ) နှင့် ပြုလုပ်အားထုတ်မှု (သင်္ခါရ) ကံတရားများ။', color: 'rose' },
                        { name: 'ပစ္စုပ္ပန်ကာလ (Present)', anga: 'ဝိညာဏ်၊ နာမ်ရုပ်၊ သဠာယတန၊ ဖဿ၊ ဝေဒနာ (အကျိုး ၅ ပါး) + တဏှာ၊ ဥပါဒါန်၊ ဘဝ (အကြောင်း ၃ ပါး)', hethu: 'ပစ္စုပ္ပန် အကျိုး (၅) ပါး၊ ပစ္စုပ္ပန် အကြောင်း (၃) ပါး', desc: 'ယခုဘဝတွင် ခံစားရသော အကျိုးတရား (၅) ပါး နှင့် ယခုဘဝတွင် ထပ်မံပြုလုပ်သော အကြောင်းတရား (၃) ပါး။', color: 'amber' },
                        { name: 'အနာဂတ်ကာလ (Future)', anga: 'ဇာတိ၊ ဇရာ-မရဏ', hethu: 'အနာဂတ် အကျိုး (၂) ပါး', desc: 'ယခုဘဝက ပြုလုပ်သော အကြောင်း (၃) ပါးကြောင့် နောင်ဘဝတွင် ထပ်မံဖြစ်ပေါ်လာမည့် ပဋိသန္ဓေနေခြင်း နှင့် အို-သေခြင်း။', color: 'emerald' }
                    ];
                    let html1 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-amber-50 dark:bg-amber-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">ကာလ (Time)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">ပါဝင်သော အင်္ဂါတရားများ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">အကြောင်း/အကျိုး</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ရှင်းလင်းချက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data1.forEach(d => {
                        html1 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed font-medium">${d.anga}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400">${d.hethu}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html1 += `</tbody></table>`;
                    container1.innerHTML = html1;
                }

                // 2. Paccaya Groups Table
                const container2 = document.getElementById('paccaya-groups-matrix');
                if (container2) {
                    const data2 = [
                        { name: '၁။ သဟဇာတ အုပ်စု', count: '၁၅ မျိုး', desc: 'သဟဇာတ၊ အညမည၊ နိဿယ၊ ဝိပါက၊ သမ္ပယုတ္တ စသော (အတူတကွ ဖြစ်၍ ကျေးဇူးပြုသော ပစ္စည်းများ)', color: 'emerald' },
                        { name: '၂။ အာရမ္မဏ အုပ်စု', count: '၈ မျိုး', desc: 'အာရမ္မဏ၊ အာရမ္မဏာဓိပတိ၊ အာရမ္မဏူပနိဿယ စသော (အာရုံပြု၍ ကျေးဇူးပြုသော ပစ္စည်းများ)', color: 'cyan' },
                        { name: '၃။ အနန္တရ အုပ်စု', count: '၇ မျိုး', desc: 'အနန္တရ၊ သမနန္တရ၊ အနန္တရူပနိဿယ၊ အာသေဝန၊ နတ္ထိ၊ ဝိဂတ စသော (အကြားမရှိ ဆက်တိုက်ဖြစ်၍ ကျေးဇူးပြုသော ပစ္စည်းများ)', color: 'amber' },
                        { name: '၄။ ပကတူပနိဿယ အုပ်စု', count: '၁ မျိုး', desc: 'ပကတူပနိဿယ (အားကြီးသော အကြောင်းအဖြစ် ကျေးဇူးပြုသော ပစ္စည်း)', color: 'rose' },
                        { name: '၅။ ရူပ အုပ်စု', count: '၆ မျိုး', desc: 'ပုရေဇာတ၊ ပစ္ဆာဇာတ၊ အာဟာရ၊ ဣန္ဒြိယ (ရုပ်တရားများနှင့် သက်ဆိုင်သော ပစ္စည်းများ)', color: 'sky' },
                        { name: '၆။ နာနာက္ခဏိကကမ္မ အုပ်စု', count: '၁ မျိုး', desc: 'နာနာက္ခဏိကကမ္မ (အချိန်ကွာခြားပြီးမှ အကျိုးပေးသော ကံပစ္စည်း)', color: 'fuchsia' }
                    ];
                    let html2 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-cyan-50 dark:bg-cyan-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">ပစ္စည်း အုပ်စုကြီး (Paccaya Group)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">ပစ္စည်း အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော ပစ္စည်းများ (သဘောတရား)</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data2.forEach(d => {
                        html2 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html2 += `</tbody></table>`;
                    container2.innerHTML = html2;
                }
            }

            renderPaccayaMasterTables();
"""
    
    js_target = "            const tbody = document.getElementById('synthesis-matrix-tbody');"
    if js_target in content:
        content = content.replace(js_target, js_code + "\n" + js_target)

with open('paticcasamuppada.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated paticcasamuppada.html")
