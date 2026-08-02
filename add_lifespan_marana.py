import re

with open('vithimutta_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Lifespan Table insertion
# Target: </details> inside sec-bhumi (the one for bhumi-matrix-container)
bhumi_target = """                <details class="glass-card rounded-xl p-4 md:p-6 border border-indigo-500/30" open>
                    <summary class="flex items-center justify-between font-bold text-indigo-700 dark:text-indigo-300 text-sm md:text-base">
                        <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>ဘုံ (၃၁) ပါး အကျဉ်းချုပ် ဇယား (Matrix Table)</span>
                    </summary>
                    <div id="bhumi-matrix-container" class="mt-4 w-full overflow-x-auto pb-2"></div>
                </details>"""

lifespan_html = bhumi_target + """
                
                <!-- Lifespan Table -->
                <details class="glass-card rounded-xl p-4 md:p-6 border border-amber-500/30 mt-4" open>
                    <summary class="flex items-center justify-between font-bold text-amber-700 dark:text-amber-300 text-sm md:text-base">
                        <span><i class="fa-solid fa-clock tree-chevron mr-2 text-xs"></i>နတ်ပြည် (၆) ထပ် သက်တမ်း တွက်ချက်မှုဇယား</span>
                    </summary>
                    <div id="lifespan-matrix-container" class="mt-4 w-full overflow-x-auto pb-2"></div>
                    <div class="mt-3 text-[11px] md:text-xs text-slate-700 dark:text-slate-300 bg-amber-50 dark:bg-amber-500/10 p-3 rounded-lg border border-amber-200 dark:border-amber-500/20 leading-relaxed">
                        <i class="fa-solid fa-circle-info text-amber-600 dark:text-amber-400 mr-1.5"></i> <b class="text-amber-800 dark:text-amber-200">မှတ်ချက်။</b> လူတို့၏ အသက်တမ်းမှာ အမြဲမရှိ၊ ကပ်အလိုက် ပြောင်းလဲတတ်ပါသည်။ ငရဲ၊ တိရစ္ဆာန်၊ ပြိတ္တာ၊ အသုရကာယ် စသော အပါယ် (၄) ဘုံတို့တွင်လည်း ကံမကုန်မချင်း ခံစားရသဖြင့် အတိအကျ သက်တမ်း မရှိပါ။ ရူပဗြဟ္မာ၊ အရူပဗြဟ္မာတို့၏ သက်တမ်းကိုမူ အထက်ပါ 'ဘုံ၊ ပဋိသန္ဓေ ဆက်စပ်မှုဇယားကြီး' တွင် ကမ္ဘာအရေအတွက်ဖြင့် ပြဆိုထားပြီး ဖြစ်ပါသည်။
                    </div>
                </details>"""

if bhumi_target in content:
    content = content.replace(bhumi_target, lifespan_html)
else:
    print("Error: Could not find bhumi_target")

# 2. Marana Table insertion
marana_target = """                <details class="glass-card rounded-xl p-4 border border-rose-500/20" open>
                    <summary class="flex items-center justify-between font-bold text-rose-700 dark:text-rose-300 text-sm">
                        <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-xs"></i>မရဏုပ္ပတ္တိ — သေခြင်း၏ အကြောင်း (၄) မျိုး</span>
                    </summary>
                    <div class="mt-3 pl-2 flex flex-wrap gap-2" id="marana-chips"></div>
                </details>"""

marana_html = marana_target + """
                
                <!-- Marana Causes Table -->
                <details class="glass-card rounded-xl p-4 md:p-6 border border-rose-500/30 mt-4" open>
                    <summary class="flex items-center justify-between font-bold text-rose-700 dark:text-rose-300 text-sm md:text-base">
                        <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>မရဏုပ္ပတ္တိ (သေခြင်းအကြောင်း ၄ မျိုး) အကျဉ်းချုပ်ဇယား</span>
                    </summary>
                    <div id="marana-matrix-container" class="mt-4 w-full pb-2"></div>
                </details>"""

if marana_target in content:
    content = content.replace(marana_target, marana_html)
else:
    print("Error: Could not find marana_target")

# 3. Insert JS logic
js_code = """
        function renderLifespanTable() {
            const container = document.getElementById('lifespan-matrix-container');
            if (!container) return;

            const data = [
                { name: 'စတုမဟာရာဇ်', humanYears: '၅၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၅၀၀', totalHumanYears: '၉ သန်း' },
                { name: 'တာဝတိံသာ', humanYears: '၁၀၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၁,၀၀၀', totalHumanYears: '၃၆ သန်း' },
                { name: 'ယာမာ', humanYears: '၂၀၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၂,၀၀၀', totalHumanYears: '၁၄၄ သန်း' },
                { name: 'တုသိတာ', humanYears: '၄၀၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၄,၀၀၀', totalHumanYears: '၅၇၆ သန်း' },
                { name: 'နိမ္မာနရတိ', humanYears: '၈၀၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၈,၀၀၀', totalHumanYears: '၂,၃၀၄ သန်း' },
                { name: 'ပရနိမ္မိတဝသဝတ္တီ', humanYears: '၁၆၀၀ နှစ်', devaDays: '၁ ရက်', devaYears: 'အနှစ် ၁၆,၀၀၀', totalHumanYears: '၉,၂၁၆ သန်း' }
            ];

            let html = `<table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead>
                    <tr class="bg-amber-100 dark:bg-amber-900/40 border-b-2 border-amber-300 dark:border-amber-600/50">
                        <th class="p-2.5 border-r border-amber-300/50 dark:border-amber-700/50 font-bold text-amber-800 dark:text-amber-200 text-center">နတ်ဘုံ အမည်</th>
                        <th class="p-2.5 border-r border-amber-300/50 dark:border-amber-700/50 font-bold text-amber-800 dark:text-amber-200 text-center">လူတို့၏ နှစ်</th>
                        <th class="p-2.5 border-r border-amber-300/50 dark:border-amber-700/50 font-bold text-amber-800 dark:text-amber-200 text-center">နတ်တို့၏ အရက်</th>
                        <th class="p-2.5 border-r border-amber-300/50 dark:border-amber-700/50 font-bold text-amber-800 dark:text-amber-200 text-center">နတ်တို့၏ သက်တမ်း</th>
                        <th class="p-2.5 font-bold text-amber-800 dark:text-amber-200 text-center">လူနှစ်ဖြင့် တွက်လျှင် စုစုပေါင်း</th>
                    </tr>
                </thead>
                <tbody>`;

            data.forEach(d => {
                html += `<tr class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-700 hover:bg-amber-50 dark:hover:bg-amber-900/20 transition">
                    <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 font-semibold text-emerald-700 dark:text-emerald-300 text-center">${d.name}</td>
                    <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-center whitespace-nowrap">${d.humanYears}</td>
                    <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-center font-bold whitespace-nowrap text-[11px] md:text-xs">ညီမျှသည် <i class="fa-solid fa-arrow-right-long text-amber-500/50 mx-1"></i> ${d.devaDays}</td>
                    <td class="p-2.5 border-r border-slate-200 dark:border-slate-700 text-sky-700 dark:text-sky-300 text-center font-bold whitespace-nowrap">${d.devaYears}</td>
                    <td class="p-2.5 text-rose-700 dark:text-rose-400 text-center font-bold font-mono tracking-wider whitespace-nowrap">${d.totalHumanYears}</td>
                </tr>`;
            });
            html += `</tbody></table>`;
            container.innerHTML = html;
        }

        function renderMaranaTable() {
            const container = document.getElementById('marana-matrix-container');
            if (!container) return;

            const data = [
                { name: '၁။ အာယုက္ခယ မရဏ', meaning: 'သက်တမ်းကုန်၍ သေခြင်း', example: 'ဆီကျန်နေသေးသော်လည်း <b class="text-amber-600 dark:text-amber-400">မီးစာကုန်၍</b> မီးငြိမ်းသွားခြင်း (ကံကြွင်းကျန်သော်လည်း ထိုဘုံ၏ သက်တမ်းစေ့၍ သေရခြင်း)', icon: 'fa-hourglass-empty' },
                { name: '၂။ ကမ္မက္ခယ မရဏ', meaning: 'ကံကုန်၍ သေခြင်း', example: 'မီးစာကျန်နေသေးသော်လည်း <b class="text-amber-600 dark:text-amber-400">ဆီကုန်၍</b> မီးငြိမ်းသွားခြင်း (သက်တမ်းကြွင်းကျန်သော်လည်း ပဋိသန္ဓေအကျိုးပေးသော ဇနကကံ စွမ်းအင်ကုန်၍ သေရခြင်း)', icon: 'fa-scale-unbalanced' },
                { name: '၃။ ဥဘယက္ခယ မရဏ', meaning: 'သက်တမ်းရော ကံပါ နှစ်ပါးစလုံးကုန်၍ သေခြင်း', example: '<b class="text-amber-600 dark:text-amber-400">ဆီရော မီးစာပါ နှစ်မျိုးလုံးကုန်၍</b> မီးငြိမ်းသွားခြင်း', icon: 'fa-battery-empty' },
                { name: '၄။ ဥပစ္ဆေဒက မရဏ', meaning: 'ဥပဃာတကကံ ဝင်ဖြတ်၍ သေခြင်း', example: 'ဆီနှင့်မီးစာ ကျန်သေးသော်လည်း <b class="text-amber-600 dark:text-amber-400">လေပြင်းတိုက်ခံရ၍ (သို့) တမင်ငြိမ်းသတ်ခံရ၍</b> မီးငြိမ်းသွားခြင်း (ကံရော သက်တမ်းပါ ကျန်ရှိနေသေးသော်လည်း အခြားသော အားကြီးသည့် ဥပဃာတကကံက ဝင်ရောက်ဖြတ်တောက်လိုက်သဖြင့် ရုတ်တရက် သေရခြင်း - ဥပမာ ယာဉ်တိုက်မှု၊ လုပ်ကြံခံရမှု၊ ရုတ်တရက် ဘေးအန္တရာယ်တစ်ခုခု ကျရောက်မှု)', icon: 'fa-bolt' }
            ];

            let html = `<div class="grid grid-cols-1 lg:grid-cols-2 gap-4">`;
            data.forEach((d, i) => {
                html += `
                <div class="bg-white/50 dark:bg-slate-900/50 border border-rose-200 dark:border-rose-500/20 rounded-xl p-4 hover:border-rose-400 dark:hover:border-rose-500/50 transition relative overflow-hidden group">
                    <div class="absolute -right-4 -top-4 w-24 h-24 bg-rose-500/5 rounded-full flex items-center justify-center transform group-hover:scale-110 transition duration-500">
                        <i class="fa-solid ${d.icon} text-4xl text-rose-500/10"></i>
                    </div>
                    <h4 class="font-bold text-rose-700 dark:text-rose-300 text-sm mb-2 relative z-10">${d.name}</h4>
                    <p class="text-xs font-semibold text-slate-800 dark:text-slate-200 mb-3 relative z-10 bg-rose-50 dark:bg-rose-500/10 inline-block px-2.5 py-1.5 rounded border border-rose-200/50 dark:border-rose-500/20 shadow-sm">${d.meaning}</p>
                    <p class="text-[11px] md:text-xs text-slate-700 dark:text-slate-300 leading-relaxed relative z-10 border-l-[3px] border-amber-400 dark:border-amber-500/70 pl-3 py-1 bg-amber-50/50 dark:bg-amber-900/10 rounded-r">
                        <span class="text-[10px] text-amber-700 dark:text-amber-400 font-bold block uppercase mb-1"><i class="fa-solid fa-lightbulb mr-1"></i> မီးအိမ် ဥပမာ</span>
                        ${d.example}
                    </p>
                </div>`;
            });
            html += `</div>`;
            container.innerHTML = html;
        }
"""
js_target = """        function renderPatisandhiMasterTable() {"""
if js_target in content:
    content = content.replace(js_target, js_code + "\n" + js_target)
else:
    print("Error: Could not find js_target")

# 4. Call render functions in DOMContentLoaded
init_target = """            renderKammaMasterTable();"""
init_replacement = init_target + """
            renderLifespanTable();
            renderMaranaTable();"""
if init_target in content:
    content = content.replace(init_target, init_replacement)
else:
    print("Error: Could not find init_target")

with open('vithimutta_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)

