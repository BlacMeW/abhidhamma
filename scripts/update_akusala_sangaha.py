import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/kilesa_sangaha.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text
content = content.replace("အမျိုးအစား (၈) မျိုး", "အမျိုးအစား (၉) မျိုး")
content = content.replace("ရှုထောင့် (၈) မျိုး", "ရှုထောင့် (၉) မျိုး")
content = content.replace("နည်းလမ်း (၈) မျိုး", "နည်းလမ်း (၉) မျိုး")
content = content.replace("ဆောင်ရွက်ပုံ (၈) မျိုး", "ဆောင်ရွက်ပုံ (၉) မျိုး")
content = content.replace("(၄၃) ပါး", "(၅၃) ပါး")

# 2. Update Total verification bar
old_bar = """            <button onclick="jumpToGroup('samyojana')" class="px-2.5 py-1.5 rounded-lg bg-violet-100 dark:bg-violet-500/15 text-violet-700 dark:text-violet-300 border border-violet-400 dark:border-violet-500/30 hover:bg-violet-500/25 hover:border-violet-400 transition">သံယောဇဉ် (၁၀)</button>
            <span class="text-slate-600">=</span>
            <button onclick="jumpToGroup('asava')" class="px-2.5 py-1.5 rounded-lg bg-slate-500/20 text-slate-800 dark:text-slate-200 border border-slate-500/40 font-bold hover:bg-slate-500/30 hover:border-slate-400 transition">(၅၃) ပါး</button>"""

new_bar = """            <button onclick="jumpToGroup('samyojana')" class="px-2.5 py-1.5 rounded-lg bg-violet-100 dark:bg-violet-500/15 text-violet-700 dark:text-violet-300 border border-violet-400 dark:border-violet-500/30 hover:bg-violet-500/25 hover:border-violet-400 transition">သံယောဇဉ် (၁၀)</button>
            <span class="text-slate-600">+</span>
            <button onclick="jumpToGroup('kilesa')" class="px-2.5 py-1.5 rounded-lg bg-pink-100 dark:bg-pink-500/15 text-pink-700 dark:text-pink-300 border border-pink-400 dark:border-pink-500/30 hover:bg-pink-500/25 hover:border-pink-400 transition">ကိလေသာ (၁၀)</button>
            <span class="text-slate-600">=</span>
            <button onclick="jumpToGroup('asava')" class="px-2.5 py-1.5 rounded-lg bg-slate-500/20 text-slate-800 dark:text-slate-200 border border-slate-500/40 font-bold hover:bg-slate-500/30 hover:border-slate-400 transition">(၅၃) ပါး</button>"""
if "ကိလေသာ (၁၀)" not in content:
    content = content.replace(old_bar, new_bar)

# 3. Add Kilesa to kilesaData
old_data_end = """              example: 'သစ္စာလေးပါးကို အပြည့်အဝ ထိုးထွင်း သိမြင်ပြီးဖြစ်သော ရဟန္တာပုဂ္ဂိုလ်။' }
        ];"""
kilesa_data = """              example: 'သစ္စာလေးပါးကို အပြည့်အဝ ထိုးထွင်း သိမြင်ပြီးဖြစ်သော ရဟန္တာပုဂ္ဂိုလ်။' },

            // Kilesa (10) — pink — "defilements that afflict the mind"
            { id: 44, key: 'lobha_kil', pali: 'Lobha', name: 'လောဘ', group: 'kilesa', icon: 'fa-magnet',
              desc: 'အာရုံကို လိုလားတပ်မက်ခြင်း၊ တွယ်တာခြင်း။',
              example: 'ကာမဂုဏ်အာရုံများအပေါ် ပြင်းပြစွာ လိုချင်တပ်မက်ခြင်း။' },
            { id: 45, key: 'dosa_kil', pali: 'Dosa', name: 'ဒေါသ', group: 'kilesa', icon: 'fa-fire',
              desc: 'အာရုံကို မကျေနပ်ခြင်း၊ ကြမ်းတမ်းစွာ ဖျက်ဆီးလိုခြင်း။',
              example: 'မိမိအလိုနှင့် မကိုက်ညီသောအခါ ဒေါသထွက်ခြင်း၊ စိတ်ဆိုးခြင်း။' },
            { id: 46, key: 'moha_kil', pali: 'Moha', name: 'မောဟ', group: 'kilesa', icon: 'fa-cloud',
              desc: 'အာရုံ၏ အမှန်သဘောကို မသိခြင်း (အဝိဇ္ဇာ)။',
              example: 'အနိစ္စ, ဒုက္ခ, အနတ္တ ကို မသိဘဲ မြဲသည်, ချမ်းသာသည်ဟု ထင်မှတ်မှားခြင်း။' },
            { id: 47, key: 'mana_kil', pali: 'Māna', name: 'မာန', group: 'kilesa', icon: 'fa-arrow-up-right-dots',
              desc: 'မိမိကိုယ်ကို အခြားသူနှင့် နှိုင်းယှဉ်၍ ထောင်လွှားခြင်း။',
              example: 'ငါက ပိုသာသည် ဟု ဂုဏ်ယူဝင့်ကြွားခြင်း။' },
            { id: 48, key: 'ditthi_kil', pali: 'Diṭṭhi', name: 'ဒိဋ္ဌိ', group: 'kilesa', icon: 'fa-eye-slash',
              desc: 'မှားယွင်းသော အယူအဆကို စွဲကိုင်ထားခြင်း (မိစ္ဆာဒိဋ္ဌိ)။',
              example: 'ကံနှင့် ကံ၏အကျိုးကို မယုံကြည်ခြင်း။' },
            { id: 49, key: 'vicikiccha_kil', pali: 'Vicikicchā', name: 'ဝိစိကိစ္ဆာ', group: 'kilesa', icon: 'fa-question',
              desc: 'ရတနာသုံးပါး စသည်တို့၌ ယုံမှားသံသယဖြစ်ခြင်း။',
              example: 'ဘုရားရှင် တကယ်ရှိ/မရှိ သံသယဖြစ်ခြင်း။' },
            { id: 50, key: 'thina_kil', pali: 'Thīna', name: 'ထိန', group: 'kilesa', icon: 'fa-bed',
              desc: 'စိတ်၏ ထိုင်းမှိုင်းညောင်းညာမှု။',
              example: 'ကုသိုလ်လုပ်ငန်းများတွင် စိတ်မပါဘဲ လေးလံထိုင်းမှိုင်းနေခြင်း။' },
            { id: 51, key: 'uddhacca_kil', pali: 'Uddhacca', name: 'ဥဒ္ဓစ္စ', group: 'kilesa', icon: 'fa-wind',
              desc: 'စိတ်၏ ပျံ့လွင့်မှု၊ မငြိမ်မသက်ဖြစ်မှု။',
              example: 'အာရုံတစ်ခုတည်းပေါ်တွင် စိတ်မတည်ဘဲ ဟိုတွေးဒီတွေး ပျံ့လွင့်နေခြင်း။' },
            { id: 52, key: 'ahirika_kil', pali: 'Ahirika', name: 'အဟိရိက', group: 'kilesa', icon: 'fa-mask',
              desc: 'ဒုစရိုက် (မကောင်းမှု) ပြုလုပ်ရန် မရှက်ခြင်း။',
              example: 'မကောင်းမှုပြုလုပ်ရာတွင် ကိုယ်ကျင့်တရားအရ မရှက်ရွံ့ခြင်း။' },
            { id: 53, key: 'anottappa_kil', pali: 'Anottappa', name: 'အနောတ္တပ္ပ', group: 'kilesa', icon: 'fa-shield-halved',
              desc: 'ဒုစရိုက် (မကောင်းမှု) ပြုလုပ်ရန် မကြောက်ခြင်း။',
              example: 'အပါယ်ကျမည်ကို မကြောက်ဘဲ မကောင်းမှုများကို ရဲတင်းစွာ ပြုလုပ်ခြင်း။' }
        ];"""
if "Lobha_kil" not in content and "lobha_kil" not in content:
    content = content.replace(old_data_end, kilesa_data)

# 4. Update groupInfo and order
old_group_info = "samyojana: { label: 'သံယောဇဉ်', sub: 'Saṃyojana — သံသရာနှင့် ချည်နှောင်မှု', color: 'text-violet-700 dark:text-violet-300', border: 'border-violet-500', bg: 'bg-violet-500/10' }\n        };"
new_group_info = "samyojana: { label: 'သံယောဇဉ်', sub: 'Saṃyojana — သံသရာနှင့် ချည်နှောင်မှု', color: 'text-violet-700 dark:text-violet-300', border: 'border-violet-500', bg: 'bg-violet-500/10' },\n            kilesa:    { label: 'ကိလေသာ', sub: 'Kilesa — စိတ်ကို ပူပန်ညစ်နွမ်းစေမှု', color: 'text-pink-700 dark:text-pink-300', border: 'border-pink-500', bg: 'bg-pink-500/10' }\n        };"
content = content.replace(old_group_info, new_group_info)

content = content.replace("const order = ['asava', 'ogha', 'yoga', 'gantha', 'upadana', 'nivarana', 'anusaya', 'samyojana'];",
                          "const order = ['asava', 'ogha', 'yoga', 'gantha', 'upadana', 'nivarana', 'anusaya', 'samyojana', 'kilesa'];")


# 5. Add 14-to-53 Mapping Section right after <div id="kilesa-groups" class="space-y-6"></div>
insert_point_matrix = "        <!-- Cross-links -->"

matrix_html = """        <!-- Matrix: 14 Akusala Cetasikas to 53 Defilements -->
        <details class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-indigo-500/20">
            <summary class="flex items-center justify-between font-bold text-indigo-700 dark:text-indigo-300 text-base">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>အကုသိုလ်စေတသိက် (၁၄) ပါးမှ ဤ (၅၃) ပါးသို့ ဖြန့်ခွဲမှု</span>
            </summary>
            <div class="mt-4 overflow-x-auto pb-4">
                <p class="text-xs text-slate-600 dark:text-slate-400 mb-4 pr-4">
                    အထက်ပါ သမုစ္စယအုပ်စု (၉) မျိုး (၅၃ ပါး) လုံးသည် အနှစ်သာရအားဖြင့် အကုသိုလ်စေတသိက် (၁၄) ပါးသာ ဖြစ်သည်။ မည်သည့်စေတသိက်သည် မည်သည့်အုပ်စုတွင် ပါဝင်သည်ကို အောက်ပါဇယားတွင် ကြည့်ရှုနိုင်ပါသည်။
                </p>
                <div class="min-w-[800px]">
                    <div id="akusala-matrix"></div>
                </div>
            </div>
            <div class="text-[11px] text-slate-500 dark:text-slate-500 mt-2 border-t border-slate-200 dark:border-slate-800 pt-2 pl-2">
                * ဣဿာ (မနာလိုမှု) နှင့် မစ္ဆရိယ (ဝန်တိုမှု) သည် အထက်ပါ ၉ အုပ်စုတွင် သီးသန့်မပါဝင်သော်လည်း၊ ယေဘုယျအားဖြင့် ဒေါသအုပ်စုတွင် အကျုံးဝင်သည်။
            </div>
        </details>

"""
if "အကုသိုလ်စေတသိက် (၁၄) ပါးမှ ဤ (၅၃) ပါးသို့ ဖြန့်ခွဲမှု" not in content:
    content = content.replace(insert_point_matrix, matrix_html + insert_point_matrix)


# 6. Add Matrix Render JS
matrix_js = """
        // 14 Akusala Cetasikas -> 9 Categories Mapping
        const akusalaCetasikas = [
            { id: 'moha', name: 'မောဟ', map: ['asava','ogha','yoga','nivarana','anusaya','samyojana','kilesa'] },
            { id: 'ahirika', name: 'အဟိရိက', map: ['kilesa'] },
            { id: 'anottappa', name: 'အနောတ္တပ္ပ', map: ['kilesa'] },
            { id: 'uddhacca', name: 'ဥဒ္ဓစ္စ', map: ['nivarana','samyojana','kilesa'] },
            { id: 'lobha', name: 'လောဘ', map: ['asava','ogha','yoga','gantha','upadana','nivarana','anusaya','samyojana','kilesa'] },
            { id: 'ditthi', name: 'ဒိဋ္ဌိ', map: ['asava','ogha','yoga','gantha','upadana','anusaya','samyojana','kilesa'] },
            { id: 'mana', name: 'မာန', map: ['anusaya','samyojana','kilesa'] },
            { id: 'dosa', name: 'ဒေါသ', map: ['gantha','nivarana','anusaya','samyojana','kilesa'] },
            { id: 'issa', name: 'ဣဿာ', map: [] },
            { id: 'macchariya', name: 'မစ္ဆရိယ', map: [] },
            { id: 'kukkucca', name: 'ကုက္ကုစ္စ', map: ['nivarana'] },
            { id: 'thina', name: 'ထိန', map: ['nivarana','kilesa'] },
            { id: 'middha', name: 'မိဒ္ဓ', map: ['nivarana'] },
            { id: 'vicikiccha', name: 'ဝိစိကိစ္ဆာ', map: ['nivarana','anusaya','samyojana','kilesa'] }
        ];

        function renderAkusalaMatrix() {
            const container = document.getElementById('akusala-matrix');
            if (!container) return;

            const groups = ['asava', 'ogha', 'yoga', 'gantha', 'upadana', 'nivarana', 'anusaya', 'samyojana', 'kilesa'];
            
            let html = `<table class="w-full text-xs text-left border-collapse">
                <thead>
                    <tr class="bg-slate-100 dark:bg-slate-800 border-b-2 border-slate-300 dark:border-slate-600">
                        <th class="p-2 border-r border-slate-200 dark:border-slate-700 font-bold sticky left-0 bg-slate-100 dark:bg-slate-800 z-10 w-28">အကုသိုလ် (၁၄)</th>`;
            
            groups.forEach(g => {
                html += `<th class="p-2 text-center border-r border-slate-200 dark:border-slate-700 font-bold whitespace-nowrap ${groupInfo[g].color}">${groupInfo[g].label}</th>`;
            });
            html += `</tr></thead><tbody>`;

            akusalaCetasikas.forEach((c, idx) => {
                const bgClass = idx % 2 === 0 ? 'bg-white dark:bg-slate-900' : 'bg-slate-50 dark:bg-slate-900/50';
                html += `<tr class="${bgClass} border-b border-slate-100 dark:border-slate-800 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 transition">`;
                html += `<td class="p-2 border-r border-slate-200 dark:border-slate-700 font-semibold sticky left-0 ${bgClass} z-10">${c.name}</td>`;
                
                groups.forEach(g => {
                    if (c.map.includes(g)) {
                        html += `<td class="p-2 text-center border-r border-slate-200 dark:border-slate-800">
                            <div class="mx-auto w-5 h-5 rounded-full ${groupInfo[g].bg} flex items-center justify-center">
                                <i class="fa-solid fa-check text-[10px] ${groupInfo[g].color}"></i>
                            </div>
                        </td>`;
                    } else {
                        html += `<td class="p-2 text-center border-r border-slate-200 dark:border-slate-800 text-slate-300 dark:text-slate-700">-</td>`;
                    }
                });
                html += `</tr>`;
            });
            html += `</tbody></table>`;
            container.innerHTML = html;
        }
"""
if "function renderAkusalaMatrix()" not in content:
    js_insert_point = "        function renderGroups() {"
    content = content.replace(js_insert_point, matrix_js + "\n" + js_insert_point)

if "renderAkusalaMatrix();" not in content:
    init_js = "        document.addEventListener('DOMContentLoaded', () => {\n            renderGroups();\n            renderAkusalaMatrix();"
    content = content.replace("        document.addEventListener('DOMContentLoaded', () => {\n            renderGroups();", init_js)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated kilesa_sangaha successfully!")
