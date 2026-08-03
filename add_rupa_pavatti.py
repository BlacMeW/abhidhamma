import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a third table in the HTML section
html_target = "<!-- Table 2: Bhumi -->"
if "<!-- Table 3: Rupa Pavatti -->" not in content:
    html_new = """            <!-- Table 3: Rupa Pavatti -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-amber-500/30" open>
                <summary class="flex items-center justify-between font-bold text-amber-700 dark:text-amber-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-seedling mr-2"></i>ရုပ်တို့၏ ဖြစ်စဉ် (ပဋိသန္ဓေအခါ နှင့် ပဝတ္တိအခါ ရုပ်ဖြစ်ပေါ်ပုံ)</span>
                </summary>
                <div id="rupa-pavatti-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Bhumi -->"""
    content = content.replace(html_target, html_new)

# Add the JS logic for the third table
js_target = "renderRupaMasterTables();"
if "const container3 = document.getElementById('rupa-pavatti-matrix');" not in content:
    js_new = """                // 3. Rupa Pavatti Table
                const container3 = document.getElementById('rupa-pavatti-matrix');
                if (container3) {
                    const data3 = [
                        { name: '၁။ အဏ္ဍဇ, ဇလာဗုဇ (ဂဗ္ဘသေယျက)', time: 'ပဋိသန္ဓေအခါ', details: 'ကမ္မဇကလာပ် (၃) စည်း (ကာယ၊ ဘာဝ၊ ဝတ္ထု)', desc: 'မိခင်ဝမ်းခေါင်း၌ ပဋိသန္ဓေနေစဉ် အစပထမ ကံကြောင့်ဖြစ်သော ရုပ်ကလာပ် ၃ ခုသာ ဖြစ်ပေါ်သည်။', color: 'amber' },
                        { name: '၁။ အဏ္ဍဇ, ဇလာဗုဇ (ဂဗ္ဘသေယျက)', time: 'ပဝတ္တိအခါ (အသက်ရှင်စဉ်)', details: 'ကမ္မဇကလာပ် (ကျန်ရှိသော စက္ခု, သောတ စသည်များ အဆင့်ဆင့် ဆက်လက်ဖြစ်ပေါ်သည်) + စိတ္တဇ၊ ဥတုဇ၊ အာဟာရဇ ရုပ်များ', desc: 'ပထမဘဝင်စိတ်မှစ၍ စိတ္တဇရုပ်၊ ဌီတိရောက်သည်နှင့် ဥတုဇရုပ်၊ အစာအာဟာရ ဖြန့်ကြက်ချိန်မှစ၍ အာဟာရဇရုပ်များ စတင်ဖြစ်ပေါ်သည်။', color: 'amber' },
                        { name: '၂။ သံသေဒဇ, ဩပပါတိက (ဘုံဇင်္ကမာ)', time: 'ပဋိသန္ဓေအခါ', details: 'ကမ္မဇကလာပ် (၇) စည်း (စက္ခု၊ သောတ၊ ဃာန၊ ဇိဝှာ၊ ကာယ၊ ဘာဝ၊ ဝတ္ထု)', desc: 'ကိုယ်ထင်ရှား ချက်ချင်းဖြစ်ပေါ်လာသူများဖြစ်၍ ပဋိသန္ဓေခဏ၌ပင် ကမ္မဇကလာပ် ၇ ခုစလုံး ပြည့်စုံစွာ ဖြစ်ပေါ်သည်။ (အကင်းမဲ့သူများတွင် လျော့နည်းနိုင်သည်)', color: 'emerald' },
                        { name: '၂။ သံသေဒဇ, ဩပပါတိက (ဘုံဇင်္ကမာ)', time: 'ပဝတ္တိအခါ (အသက်ရှင်စဉ်)', details: 'စိတ္တဇ၊ ဥတုဇ၊ အာဟာရဇ ရုပ်များ (စိတ္တဇ၊ ဥတုဇသည် ပဋိသန္ဓေခဏအလွန် ချက်ချင်းဖြစ်သည်)', desc: 'အာဟာရဇရုပ်သည်ကား မိမိတို့ဘုံ၌ သင့်လျော်သော အာဟာရကို စားမျိုပြီးချိန်မှသာ ဖြစ်ပေါ်သည်။', color: 'emerald' },
                        { name: '၃။ ရူပဗြဟ္မာများ', time: 'ပဋိသန္ဓေအခါ', details: 'ကမ္မဇကလာပ် (၄) စည်း (စက္ခု၊ သောတ၊ ဝတ္ထု၊ ဇီဝိတ)', desc: 'ရူပဗြဟ္မာများတွင် ဃာန၊ ဇိဝှာ၊ ကာယ၊ ဘာဝ ရုပ်များ မရှိပါ။', color: 'cyan' },
                        { name: '၃။ ရူပဗြဟ္မာများ', time: 'ပဝတ္တိအခါ (အသက်ရှင်စဉ်)', details: 'စိတ္တဇ၊ ဥတုဇ ရုပ်များ', desc: 'ဗြဟ္မာများတွင် အာဟာရဇရုပ် မရှိပါ။', color: 'cyan' },
                        { name: '၄။ အသညသတ်ဗြဟ္မာ', time: 'ပဋိသန္ဓေအခါ', details: 'ဇီဝိတနဝက ကလာပ် (၁) စည်းသာ', desc: 'စိတ်မရှိ၊ နာမ်တရားမရှိသော ဘုံဖြစ်၍ ဇီဝိတနဝက (အသက်+ရုပ်၈ပါး) ကမ္မဇကလာပ် ၁ ခုသာ ရှိသည်။', color: 'violet' },
                        { name: '၄။ အသညသတ်ဗြဟ္မာ', time: 'ပဝတ္တိအခါ (အသက်ရှင်စဉ်)', details: 'ဥတုဇ ရုပ်များ (စိတ္တဇ၊ အာဟာရဇ မရှိပါ)', desc: 'ကမ္မဇ နှင့် ဥတုဇ ရုပ် ၂ မျိုးသာ အသက်ရှင်စဉ်တောက်လျှောက် ဖြစ်ပေါ်သည်။', color: 'violet' }
                    ];
                    let html3 = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                        <thead class="bg-amber-50 dark:bg-amber-900/40">
                            <tr>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-40">သတ္တဝါ အမျိုးအစား (ပဋိသန္ဓေ)</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-32">အချိန်ကာလ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700 w-56">ဖြစ်ပေါ်သော ရုပ်ကလာပ်များ</th>
                                <th class="p-2 border border-slate-300 dark:border-slate-700">အသေးစိတ် ရှင်းလင်းချက်</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-slate-900">`;
                    data3.forEach(d => {
                        html3 += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 font-medium text-slate-700 dark:text-slate-300">${d.time}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200 leading-relaxed font-semibold">${d.details}</td>
                            <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-600 dark:text-slate-400 leading-relaxed">${d.desc}</td>
                        </tr>`;
                    });
                    html3 += `</tbody></table>`;
                    container3.innerHTML = html3;
                }

                """
    # Replace in file. We need to find the `function renderRupaMasterTables() {` and insert it before it ends.
    replace_target = "            }\n\n            renderRupaMasterTables();"
    if replace_target in content:
        content = content.replace(replace_target, js_new + "            }\n\n            renderRupaMasterTables();")

with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated rupa_sangaha.html with Rupa Pavatti table.")
