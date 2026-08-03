import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert HTML tables right before <!-- Footer Dedication -->
html_target = "    <!-- Footer Dedication -->"
if "sec-summary-tables" not in content:
    html_replacement = """    <!-- Master Summary Tables -->
    <section id="sec-summary-tables" class="max-w-7xl mx-auto px-4 mb-16 relative z-10">
        <div class="glass-card rounded-2xl p-4 md:p-6 border border-indigo-500/30 relative overflow-hidden space-y-6">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3 flex-wrap gap-2 relative z-10">
                <div>
                    <h3 class="font-bold text-indigo-700 dark:text-indigo-300 text-lg flex items-center gap-2">
                        <i class="fa-solid fa-table-list"></i> ရုပ်သင်္ဂဟ သရုပ်ခွဲ အကျဉ်းချုပ် မဟာဇယားကြီးများ
                    </h3>
                    <p class="text-xs text-slate-600 dark:text-slate-400">ရုပ်ကလာပ်များ ဖွဲ့စည်းပုံ နှင့် ဘုံအလိုက်ရနိုင်သော ရုပ်တရားများ</p>
                </div>
            </div>

            <!-- Table 1: Rupa Kalapa -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-cyan-500/30" open>
                <summary class="flex items-center justify-between font-bold text-cyan-700 dark:text-cyan-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-layer-group mr-2"></i>ရုပ်ကလာပ် (၂၁) ပါး ဖွဲ့စည်းပုံ (Rūpa Kalāpa)</span>
                </summary>
                <div id="rupa-kalapa-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Rupa Bhumi -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-emerald-500/30" open>
                <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-earth-asia mr-2"></i>ဘုံအလိုက် ရနိုင်သော ရုပ်တရားများ (Rūpa in Realms)</span>
                </summary>
                <div id="rupa-bhumi-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </div>
    </section>

    <!-- Footer Dedication -->"""
    content = content.replace(html_target, html_replacement)

# 2. Add JS logic right before `});` at the end of DOMContentLoaded
if "renderRupaMasterTables();" not in content:
    js_code = """
            function renderRupaMasterTables() {
                // 1. Kalapa Table
                const container1 = document.getElementById('rupa-kalapa-matrix');
                if (container1) {
                    const data1 = [
                        { name: 'ကမ္မဇကလာပ် (၉) ပါး', cause: 'ကံ (Kamma)', desc: 'စက္ခု၊ သောတ၊ ဃာန၊ ဇိဝှာ၊ ကာယ၊ ဣတ္ထိဘာဝ၊ ပုမ္ဘာဝ၊ ဝတ္ထု၊ ဇီဝိတ', total: 'ဒသက (၁၀) မျိုး ၈ ခု၊ နဝက (၉) မျိုး ၁ ခု', color: 'rose' },
                        { name: 'စိတ္တဇကလာပ် (၆) ပါး', cause: 'စိတ် (Citta)', desc: 'သုဒ္ဓဋ္ဌက၊ ကာယဝိညတ္တိနဝက၊ ဝစီဝိညတ္တိဒသက (သဒ္ဒါပါ)၊ လဟုတာဒိဧကာဒသက (လဟုတာဒိ ၃ ပါးပါ)၊ ကာယဝိညတ္တိလဟုတာဒိဒွါဒသက (၂ မျိုးပေါင်း)၊ ဝစီဝိညတ္တိသဒ္ဒလဟုတာဒိတေရသက (၃ မျိုးပေါင်း)', total: '၈, ၉, ၁၀, ၁၁, ၁၂, ၁၃ ခုစီပါဝင်', color: 'sky' },
                        { name: 'ဥတုဇကလာပ် (၄) ပါး', cause: 'ဥတု (Utu)', desc: 'သုဒ္ဓဋ္ဌက (အခြေခံ ၈ ပါး)၊ သဒ္ဒနဝက (အသံပါ ၉ ပါး)၊ လဟုတာဒိဧကာဒသက (လဟုတာဒိပါ ၁၁ ပါး)၊ သဒ္ဒလဟုတာဒိဒွါဒသက (အသံ+လဟုတာဒိ ၁၂ ပါး)', total: '၈, ၉, ၁၁, ၁၂ ခုစီပါဝင်', color: 'amber' },
                        { name: 'အာဟာရဇကလာပ် (၂) ပါး', cause: 'အာဟာရ (Āhāra)', desc: 'သုဒ္ဓဋ္ဌက (အခြေခံ ၈ ပါး)၊ လဟုတာဒိဧကာဒသက (လဟုတာဒိ ၃ ပါး ထပ်ပေါင်း ၁၁ ပါး)', total: '၈, ၁၁ ခုစီပါဝင်', color: 'emerald' }
                    ];
                    let html1 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-cyan-50 dark:bg-cyan-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">ကလာပ်အမည်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">အကြောင်းရင်း</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော ကလာပ်များ (အသေးစိတ်)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">ရုပ်အရေအတွက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data1.forEach(d => {
                        html1 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.cause}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.desc}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400">${d.total}</td>
                        </tr>`;
                    });
                    html1 += `</tbody></table>
                    <p class="mt-2 text-[11px] text-slate-500 italic">မှတ်ချက်။ ။ အဝိနိဗ္ဘောဂရုပ် (၈) ပါးသည် မည်သည့်ကလာပ်တွင်မဆို မပါမဖြစ် အခြေခံအဖြစ် အမြဲပါဝင်သည်။ လက္ခဏာရုပ် (၄) ပါးသည် ရုပ်အစစ်မဟုတ်သောကြောင့် ကလာပ်ဖွဲ့ရာတွင် မပါဝင်ပါ။</p>`;
                    container1.innerHTML = html1;
                }

                // 2. Bhumi Table
                const container2 = document.getElementById('rupa-bhumi-matrix');
                if (container2) {
                    const data2 = [
                        { name: 'ကာမဘုံ (၁၁ ဘုံ)', rupa: 'ရုပ် (၂၈) ပါးလုံး ရနိုင်သည်', kamma: '၉ ပါးလုံး', citta: '၆ ပါးလုံး', utu: '၄ ပါးလုံး', ahara: '၂ ပါးလုံး', note: 'ကာမဘုံသားတို့သည် ရုပ်ကြမ်းများကို အပြည့်အစုံ ရရှိကြသည်။ (ပဋိသန္ဓေအခါတွင် ရုပ် ၃ မျိုး ၃၀-ပါး ချက်ချင်းရသည်)', color: 'amber' },
                        { name: 'ရူပဘုံ (၁၅ ဘုံ)', rupa: 'ရုပ် (၂၃) ပါးသာ ရသည်', kamma: '၄ ပါး (စက္ခု၊ သောတ၊ ဝတ္ထု၊ ဇီဝိတ)', citta: '၆ ပါးလုံး', utu: '၄ ပါးလုံး', ahara: 'မရှိပါ (ပီတိကိုသာ စားသုံးသည်)', note: 'ဃာန၊ ဇိဝှာ၊ ကာယ ပသာဒ ၃-ပါး နှင့် ဘာဝရုပ် ၂-ပါး မရှိပါ။ (ပဋိသန္ဓေအခါတွင် ရုပ် ၄ မျိုး ၃၉-ပါး ရသည်)', color: 'sky' },
                        { name: 'အသညသတ်ဘုံ (၁ ဘုံ)', rupa: 'ရုပ် (၁၇) ပါးသာ ရသည်', kamma: '၁ ပါး (ဇီဝိတနဝက တစ်ခုတည်းသာ)', citta: 'မရှိပါ (စိတ်မရှိ၍)', utu: '၄ ပါးလုံး', ahara: 'မရှိပါ', note: 'နာမ်တရား(စိတ်) လုံးဝမရှိသော ရုပ်သီးသန့်ဘုံ ဖြစ်သည်။ သဒ္ဒ(အသံ)၊ ဝိညတ်၊ လဟုတာဒိ လည်းမရှိပါ။ (ဇီဝိတနဝကကလာပ်ဖြင့် ပဋိသန္ဓေနေသည်)', color: 'emerald' },
                        { name: 'အရူပဘုံ (၄ ဘုံ)', rupa: 'ရုပ် လုံးဝ မရှိပါ (၀)', kamma: '-', citta: '-', utu: '-', ahara: '-', note: 'ရုပ်တရားကို ရွံမုန်းပြီး နာမ်သီးသန့်ဖြင့်သာ တည်ရှိသော ဘုံဖြစ်သည်။', color: 'slate' }
                    ];
                    let html2 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-emerald-50 dark:bg-emerald-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">ဘုံအမည်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">ရနိုင်သော ရုပ်အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 text-center">ကမ္မဇ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 text-center">စိတ္တဇ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 text-center">ဥတုဇ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 text-center">အာဟာရဇ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">မှတ်ချက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data2.forEach(d => {
                        html2 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.rupa}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-center">${d.kamma}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-center">${d.citta}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-center">${d.utu}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-center">${d.ahara}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.note}</td>
                        </tr>`;
                    });
                    html2 += `</tbody></table>`;
                    container2.innerHTML = html2;
                }
            }

            renderRupaMasterTables();
"""
    
    js_target = "            const tbody = document.getElementById('rupa-matrix-tbody');"
    content = content.replace(js_target, js_code + "\n" + js_target)

with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated rupa_sangaha.html")
