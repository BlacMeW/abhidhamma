import re

with open('missaka_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

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
"""

if "function renderSamuccayaMasterTables" not in content:
    target = "            renderMatrix();\n        });"
    if target in content:
        content = content.replace(target, "            renderMatrix();\n" + js_code + "\n            renderSamuccayaMasterTables();\n        });")
        with open('missaka_sangaha.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed missing JS function in missaka_sangaha.html")
    else:
        print("Target not found")
else:
    print("JS function already exists")
