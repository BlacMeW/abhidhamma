import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a sixth table in the HTML section
html_target = "            <!-- Table 2: Rupa Bhumi -->"
if "<!-- Table 6: Rupa Cuti -->" not in content:
    html_new = """            <!-- Table 6: Rupa Cuti (Death Process) -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-indigo-500/30" open>
                <summary class="flex items-center justify-between font-bold text-indigo-700 dark:text-indigo-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-bed mr-2"></i>သေဆုံးချိန် (စုတိအခါ) ၌ ရုပ်များ ချုပ်ငြိမ်းပုံ အဆင့်ဆင့်</span>
                </summary>
                <div id="rupa-cuti-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Rupa Bhumi -->"""
    content = content.replace(html_target, html_new)

# Add the JS logic for the sixth table
js_target = "            renderRupaMasterTables();"
if "const container6 = document.getElementById('rupa-cuti-matrix');" not in content:
    js_new = """                // 6. Rupa Cuti (Death) Table
                const container6 = document.getElementById('rupa-cuti-matrix');
                if (container6) {
                    const data6 = [
                        { name: '၁။ ကမ္မဇရုပ် (ကံကြောင့်ဖြစ်သောရုပ်)', stop: 'စုတိစိတ် (သေမည့်စိတ်) မတိုင်မီ ၁၇-ချက်မြောက်သော စိတ်၏ ဥပါဒ်ခဏ', end: 'စုတိစိတ်၏ ဘင်ခဏ (သေဆုံးသည့်အချိန်) ၌ အကုန်ချုပ်ငြိမ်းသည်', desc: 'သေခါနီးအချိန်တွင် ကံတရားက ရုပ်အသစ်များကို ဆက်လက်မထုတ်လုပ်ပေးတော့ပါ။ ကျန်ရှိနေသော ကမ္မဇရုပ်တို့သည် သေဆုံးသည့်အချိန်၌ အတိအကျ ချုပ်ငြိမ်းသွားသည်။', color: 'indigo' },
                        { name: '၂။ စိတ္တဇရုပ် (စိတ်ကြောင့်ဖြစ်သောရုပ်)', stop: 'စုတိစိတ်၏ ဥပါဒ်ခဏ (သေမည့်စိတ် စတင်ဖြစ်ပေါ်ချိန်)', end: 'စုတိစိတ်၏ ဘင်ခဏ (သေဆုံးသည့်အချိန်) ၌ အကုန်ချုပ်ငြိမ်းသည်', desc: 'စုတိစိတ်သည် နောက်ဆုံးစိတ်ဖြစ်၍ ထိုစိတ်ဖြစ်ပြီးသည်နှင့် စိတ္တဇရုပ်အသစ် ထပ်မဖြစ်တော့ပါ။ ရှိပြီးသား စိတ္တဇရုပ်တို့သည်လည်း ချက်ချင်းချုပ်ငြိမ်းသည်။', color: 'sky' },
                        { name: '၃။ အာဟာရဇရုပ် (အစာကြောင့်ဖြစ်သောရုပ်)', stop: 'အစာအာဟာရ၏ ဩဇာဓာတ် ကုန်ဆုံးသွားချိန်', end: 'ဩဇာဓာတ်ကုန်ဆုံးပြီး နောက်ဆုံးဖြစ်သော အာဟာရဇရုပ်၏ သက်တမ်းကုန်ချိန်', desc: 'သေခါနီးတွင် အစာမစားနိုင်တော့သဖြင့် ခန္ဓာကိုယ်တွင်းရှိ အာဟာရဓာတ်များ ကုန်ဆုံးသွားသည်နှင့် အာဟာရဇရုပ်များလည်း ရပ်တန့်ချုပ်ငြိမ်းသွားသည်။', color: 'emerald' },
                        { name: '၄။ ဥတုဇရုပ် (ဥတုကြောင့်ဖြစ်သောရုပ်)', stop: 'မရပ်တန့်ပါ (အလောင်းကောင်အဖြစ် ဆက်လက်တည်ရှိသည်)', end: 'ရုပ်အလောင်း ဆွေးမြည့်ပျက်စီးပြီး မြေကြီး၊ ပြာ စသည်အဖြစ် ပြောင်းလဲသွားသည်အထိ', desc: 'သေဆုံးပြီးနောက် ကမ္မဇ၊ စိတ္တဇ၊ အာဟာရဇ ရုပ်တို့ မရှိတော့သော်လည်း ဥတုဇရုပ် (အပူ/အအေး) သည် ရုပ်အလောင်းအဖြစ် ဆက်လက်တည်ရှိနေသည်။', color: 'amber' }
                    ];
                    let html6 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-indigo-50 dark:bg-indigo-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-36">ရုပ်အမျိုးအစား</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-64">အသစ်ဖြစ်ပေါ်မှု ရပ်စဲချိန်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-48">အပြီးတိုင် ချုပ်ငြိမ်းချိန်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">ရှင်းလင်းချက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data6.forEach(d => {
                        html6 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200 leading-relaxed font-semibold">${d.stop}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-rose-600 dark:text-rose-400 leading-relaxed font-medium">${d.end}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html6 += `</tbody></table>`;
                    container6.innerHTML = html6;
                }

                """
    
    replace_target = "            }\n\n            renderRupaMasterTables();"
    if replace_target in content:
        content = content.replace(replace_target, js_new + "            }\n\n            renderRupaMasterTables();")
    
    with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Rupa Cuti HTML")
else:
    print("Rupa Cuti HTML already exists")
