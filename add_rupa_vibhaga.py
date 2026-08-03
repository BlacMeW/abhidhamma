import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a fifth table in the HTML section (at the very top of the tables)
html_target = "            <!-- Table 1: Kalapa -->"
if "<!-- Table 5: Rupa Vibhaga -->" not in content:
    html_new = """            <!-- Table 5: Rupa Vibhaga -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-sky-500/30" open>
                <summary class="flex items-center justify-between font-bold text-sky-700 dark:text-sky-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-shapes mr-2"></i>ရုပ်တို့၏ အပြား (Rūpa Vibhāga) - ရုပ် (၂၈) ပါးကို အမျိုးအစားခွဲခြားခြင်း</span>
                </summary>
                <div id="rupa-vibhaga-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 1: Kalapa -->"""
    content = content.replace(html_target, html_new)

# Add the JS logic for the fifth table
js_target = "            renderRupaMasterTables();"
if "const container5 = document.getElementById('rupa-vibhaga-matrix');" not in content:
    js_new = """                // 5. Rupa Vibhaga Table
                const container5 = document.getElementById('rupa-vibhaga-matrix');
                if (container5) {
                    const data5 = [
                        { name: 'အဇ္ဈတ္တိကရုပ် (အတွင်းရုပ်)', count: '၅ ပါး', details: 'ပသာဒရုပ် (၅) ပါး (စက္ခု၊ သောတ၊ ဃာန၊ ဇိဝှာ၊ ကာယ)', desc: 'မိမိသန္တာန်၌ အတွင်းအကျဆုံးဖြစ်၍ အကျိုးများသော ရုပ်များ (ကျန် ၂၃ ပါးမှာ ဗာဟိရ - ပြင်ပရုပ် များဖြစ်သည်။)', color: 'sky' },
                        { name: 'ဝတ္ထုရုပ် (မှီရာရုပ်)', count: '၆ ပါး', details: 'ပသာဒရုပ် (၅) ပါး နှင့် ဟဒယဝတ္ထုရုပ် (၁) ပါး', desc: 'စိတ်၊ စေတသိက်တို့ ဖြစ်ပေါ်ရန် မှီခိုရာ နေရာဌာနဖြစ်သော ရုပ်များဖြစ်သည်။', color: 'emerald' },
                        { name: 'ဒွါရရုပ် (တံခါးရုပ်)', count: '၇ ပါး', details: 'ပသာဒရုပ် (၅) ပါး နှင့် ဝိညတ္တိရုပ် (၂) ပါး (ကာယဝိညတ်၊ ဝစီဝိညတ်)', desc: 'စိတ်များ ထွက်ဝင်ရာ၊ အာရုံများ ဝင်ရောက်ရာ တံခါးပေါက်သဖွယ်ဖြစ်သော ရုပ်များဖြစ်သည်။', color: 'amber' },
                        { name: 'ဣန္ဒြိယရုပ် (အစိုးရသောရုပ်)', count: '၈ ပါး', details: 'ပသာဒရုပ် (၅) ပါး၊ ဘာဝရုပ် (၂) ပါး၊ ဇီဝိတရုပ် (၁) ပါး', desc: 'မိမိတို့၏ သက်ဆိုင်ရာ ကိစ္စများတွင် လွှမ်းမိုးအုပ်ချုပ်နိုင်စွမ်းရှိသော ရုပ်များဖြစ်သည်။', color: 'violet' },
                        { name: 'ဩဠာရိကရုပ် (အကြမ်းစားရုပ်)', count: '၁၂ ပါး', details: 'ပသာဒရုပ် (၅) ပါး နှင့် ဂေါစရရုပ် (၇) ပါး (ရူပ၊ သဒ္ဒ၊ ဂန္ဓ၊ ရသ၊ ပထဝီ၊ တေဇော၊ ဝါယော)', desc: 'ထင်ရှားလွယ်၊ တွေ့ထိလွယ်၊ တိုက်ခိုက်လွယ်သော အကြမ်းစားရုပ်များ (ကျန် ၁၆ ပါးမှာ သုခုမ - အနုစားရုပ် များဖြစ်သည်။)', color: 'rose' },
                        { name: 'ကမ္မဇရုပ် (ကံကြောင့်ဖြစ်သောရုပ်)', count: '၁၈ ပါး', details: 'ပသာဒ (၅)၊ ဘာဝ (၂)၊ ဟဒယ (၁)၊ ဇီဝိတ (၁) - ဤ ၉ ပါးမှာ ကမ္မဇသီးသန့် + အဝိနိဗ္ဘောဂ (၈)၊ အာကာသ (၁)', desc: 'အတိတ်ကံကြောင့် ဖြစ်ပေါ်လာသော ရုပ်များဖြစ်သည်။', color: 'indigo' },
                        { name: 'နိပ္ဖန္နရုပ် (အစစ်အမှန်ရုပ်)', count: '၁၈ ပါး', details: 'မဟာဘုတ် (၄)၊ ပသာဒ (၅)၊ ဂေါစရ (၄ - ဖောဋ္ဌဗ္ဗကို မဟာဘုတ်တွင်ရေတွက်)၊ ဘာဝ (၂)၊ ဟဒယ (၁)၊ ဇီဝိတ (၁)၊ အာဟာရ (၁)', desc: 'ကံ၊ စိတ်၊ ဥတု၊ အာဟာရ တို့ကြောင့် အမှန်တကယ် ဖြစ်ပေါ်လာသော ရုပ်အစစ်များ (ကျန် ၁၀ ပါးမှာ အနိပ္ဖန္န - မစစ်မှန်သောရုပ် များဖြစ်သည်။)', color: 'cyan' }
                    ];
                    let html5 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-sky-50 dark:bg-sky-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">အမျိုးအစား (Vibhāga)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-24">ရုပ်အရေအတွက်</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-64">ပါဝင်သော ရုပ်တို့၏ အမည်များ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">အဓိပ္ပာယ် ရှင်းလင်းချက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data5.forEach(d => {
                        html5 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400 text-sm">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium">${d.count}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200 leading-relaxed font-semibold">${d.details}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html5 += `</tbody></table>`;
                    container5.innerHTML = html5;
                }

                """
    
    replace_target = "            }\n\n            renderRupaMasterTables();"
    if replace_target in content:
        content = content.replace(replace_target, js_new + "            }\n\n            renderRupaMasterTables();")
    
    with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Rupa Vibhaga HTML")
else:
    print("Rupa Vibhaga HTML already exists")
