import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a fourth table in the HTML section
html_target = "            <!-- Table 3: Rupa Pavatti -->"
if "<!-- Table 4: Rupa Samutthana -->" not in content:
    html_new = """            <!-- Table 4: Rupa Samutthana (Causes) -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-fuchsia-500/30" open>
                <summary class="flex items-center justify-between font-bold text-fuchsia-700 dark:text-fuchsia-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-wand-magic-sparkles mr-2"></i>ရုပ်ဖြစ်ကြောင်း (၄) ပါး နှင့် ၎င်းတို့ဖြစ်စေသော ရုပ်များ (Rūpa Samuṭṭhāna)</span>
                </summary>
                <div id="rupa-samutthana-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 3: Rupa Pavatti -->"""
    content = content.replace(html_target, html_new)

# Add the JS logic for the fourth table
js_target = "            renderRupaMasterTables();"
if "const container4 = document.getElementById('rupa-samutthana-matrix');" not in content:
    js_new = """                // 4. Rupa Samutthana Table
                const container4 = document.getElementById('rupa-samutthana-matrix');
                if (container4) {
                    const data4 = [
                        { name: '၁။ ကံ (Kamma)', count: '၁၈ ပါး', details: 'အဝိနိဗ္ဘောဂရုပ် (၈)၊ အာကာသဓာတ် (၁)၊ ပသာဒရုပ် (၅)၊ ဘာဝရုပ် (၂)၊ ဟဒယဝတ္ထု (၁)၊ ဇီဝိတရုပ် (၁)', desc: 'ကံကြောင့်သာဖြစ်သော (ကမ္မဇသီးသန့်) ရုပ်များမှာ ပသာဒ ၅၊ ဘာဝ ၂၊ ဟဒယ ၁၊ ဇီဝိတ ၁ ပေါင်း ၉ ပါး ဖြစ်သည်။', color: 'rose' },
                        { name: '၂။ စိတ် (Citta)', count: '၁၅ ပါး', details: 'အဝိနိဗ္ဘောဂရုပ် (၈)၊ အာကာသဓာတ် (၁)၊ သဒ္ဒရုပ် (၁)၊ ဝိညတ္တိရုပ် (၂)၊ ဝိကာရရုပ် (၃)', desc: 'စိတ်ကြောင့်သာဖြစ်သော (စိတ္တဇသီးသန့်) ရုပ်များမှာ ကာယဝိညတ်၊ ဝစီဝိညတ် ၂ ပါး ဖြစ်သည်။', color: 'sky' },
                        { name: '၃။ ဥတု (Utu)', count: '၁၃ ပါး', details: 'အဝိနိဗ္ဘောဂရုပ် (၈)၊ အာကာသဓာတ် (၁)၊ သဒ္ဒရုပ် (၁)၊ ဝိကာရရုပ် (၃)', desc: 'ဥတုကြောင့်သာဖြစ်သော (ဥတုဇသီးသန့်) ရုပ် မရှိပါ။ (စိတ္တဇနှင့် ဆင်တူသော်လည်း ဝိညတ် ၂ ပါး မပါဝင်ပါ)', color: 'amber' },
                        { name: '၄။ အာဟာရ (Āhāra)', count: '၁၂ ပါး', details: 'အဝိနိဗ္ဘောဂရုပ် (၈)၊ အာကာသဓာတ် (၁)၊ ဝိကာရရုပ် (၃)', desc: 'အာဟာရကြောင့်သာဖြစ်သော (အာဟာရဇသီးသန့်) ရုပ် မရှိပါ။', color: 'emerald' },
                        { name: 'အကြောင်း (၄) ပါးလုံးကြောင့်ဖြစ်သည်', count: '၉ ပါး', details: 'အဝိနိဗ္ဘောဂရုပ် (၈) ပါး နှင့် အာကာသဓာတ် (၁) ပါး', desc: 'ဤ ၉ ပါးသည် ကံ၊ စိတ်၊ ဥတု၊ အာဟာရ (၄) မျိုးလုံးမှ ဖြစ်ပေါ်နိုင်သည်။ (စတုသမုဋ္ဌာနိကရုပ်)', color: 'violet' }
                    ];
                    let html4 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-fuchsia-50 dark:bg-fuchsia-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">အကြောင်းတရား</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">ရုပ်အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-64">ဖြစ်ပေါ်စေသော ရုပ်တို့၏ အမည်များ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">မှတ်ချက် (အသေးစိတ်)</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data4.forEach(d => {
                        html4 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200 leading-relaxed">${d.details}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html4 += `</tbody></table>`;
                    container4.innerHTML = html4;
                }

                """
    
    replace_target = "            }\n\n            renderRupaMasterTables();"
    if replace_target in content:
        content = content.replace(replace_target, js_new + "            }\n\n            renderRupaMasterTables();")
    
    with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Rupa Samutthana HTML")
else:
    print("Rupa Samutthana HTML already exists")
