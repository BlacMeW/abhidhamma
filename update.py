import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/bodhipakkhiya_dhamma.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the cross-check block
old_block = """        <!-- Underlying 14 unique dhamma cross-check -->
        <div class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-amber-400 dark:border-amber-500/30 space-y-3" style="box-shadow: 0 0 20px rgba(234,179,8,0.15);">
            <h3 class="font-bold text-amber-700 dark:text-amber-300 text-base flex items-center gap-2"><i class="fa-solid fa-star"></i> (၃၇) ပါးအောက်က အခြေခံ စေတသိက် (၁၄) ပါးသာ</h3>
            <p class="text-xs text-slate-700 dark:text-slate-300">ဗောဓိပက္ခိယဓမ္မာ (၃၇) ပါးသည် နာမည်အသစ် (၃၇) မျိုး မဟုတ်ဘဲ၊ အောက်ပါ စေတသိက် (၁၄) ပါးသာ အုပ်စု (၇) စု အတွင်း ထပ်ခါထပ်ခါ ပေါင်းစပ် ပါဝင်နေခြင်း ဖြစ်သည် — ဥပမာ "ဝီရိယ" တစ်ပါးတည်းက (၉) နေရာတွင် ထပ်ခါထပ်ခါ ပါဝင်နေသည်:</p>
            <div id="unique-dhamma-chips" class="flex flex-wrap gap-1.5"></div>
            <p class="text-[11px] text-slate-500 dark:text-slate-500 pt-1">* ဤအချက်ကပင် ဗောဓိပက္ခိယဓမ္မာသည် "အသစ်ရှာစရာ မလိုဘဲ၊ ရှိပြီးသား စေတသိက်များကို မှန်ကန်သော အချိုးအစားဖြင့် ဖွံ့ဖြိုးအားထုတ်ရုံမျှသာ" ဖြစ်ကြောင်း ညွှန်ပြသည်။</p>
        </div>"""

new_block = """        <!-- Underlying 14 unique dhamma cross-check & Matrix -->
        <div class="glass-card rounded-2xl overflow-hidden border border-amber-400 dark:border-amber-500/30 max-w-5xl mx-auto" style="box-shadow: 0 0 20px rgba(234,179,8,0.15);">
            <div class="p-5 border-b border-amber-200 dark:border-amber-500/20 bg-amber-50 dark:bg-amber-500/5">
                <h3 class="font-bold text-amber-800 dark:text-amber-300 text-lg flex items-center gap-2"><i class="fa-solid fa-table-cells"></i> ဓမ္မသရုပ်ခွဲ ဇယား (၁၄ ပါး → ၃၇ ပါး Mapping)</h3>
                <p class="text-xs text-slate-700 dark:text-slate-300 mt-2 leading-relaxed">
                    ဗောဓိပက္ခိယဓမ္မာ (၃၇) ပါးသည် နာမည်အသစ်များ မဟုတ်ဘဲ၊ <b>အခြေခံ စေတသိက်/စိတ် (၁၄) ပါးသာ</b> အုပ်စု (၇) စု အတွင်း ထပ်ခါထပ်ခါ ပေါင်းစပ် ပါဝင်နေခြင်း ဖြစ်သည်။
                    အောက်ပါဇယားတွင် မည်သည့်တရားက မည်သည့်အုပ်စု၌ ပါဝင်နေကြောင်းကို အသေးစိတ် လေ့လာနိုင်သည်။
                </p>
                <div id="unique-dhamma-chips" class="flex flex-wrap gap-1.5 mt-4"></div>
            </div>
            
            <div class="overflow-x-auto">
                <table class="w-full text-left text-sm whitespace-nowrap min-w-[800px]">
                    <thead class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-400 text-[11px] uppercase border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="px-4 py-3 font-bold sticky left-0 bg-slate-100 dark:bg-slate-800/90 z-10 border-r border-slate-200 dark:border-slate-700 shadow-[2px_0_5px_rgba(0,0,0,0.05)]">အခြေခံတရား (၁၄)</th>
                            <th class="px-3 py-3 font-bold text-center border-r border-slate-200 dark:border-slate-700">ပေါင်း</th>
                            <th class="px-3 py-3 text-sky-700 dark:text-sky-400">သတိပဋ္ဌာန်</th>
                            <th class="px-3 py-3 text-emerald-700 dark:text-emerald-400">သမ္မပ္ပဓာန်</th>
                            <th class="px-3 py-3 text-cyan-700 dark:text-cyan-400">ဣဒ္ဓိပါဒ်</th>
                            <th class="px-3 py-3 text-violet-700 dark:text-violet-400">ဣန္ဒြေ</th>
                            <th class="px-3 py-3 text-rose-700 dark:text-rose-400">ဗလ</th>
                            <th class="px-3 py-3 text-amber-700 dark:text-amber-400">ဗောဇ္ဈင်</th>
                            <th class="px-3 py-3 text-indigo-700 dark:text-indigo-400">မဂ္ဂင်</th>
                        </tr>
                    </thead>
                    <tbody id="matrix-tbody" class="divide-y divide-slate-100 dark:divide-slate-800/50 bg-white dark:bg-slate-900">
                        <!-- Rendered by JS -->
                    </tbody>
                </table>
            </div>
            <div class="p-4 bg-slate-50 dark:bg-slate-800/50 text-[11px] text-slate-500">
                * ဤအချက်ကပင် ဗောဓိပက္ခိယဓမ္မာသည် "အသစ်ရှာစရာ မလိုဘဲ၊ ရှိပြီးသား စေတသိက်များကို မှန်ကန်သော အချိုးအစားဖြင့် ဖွံ့ဖြိုးအားထုတ်ရုံမျှသာ" ဖြစ်ကြောင်း ညွှန်ပြသည်။
            </div>
        </div>"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("Could not find the old block!")
    sys.exit(1)

# 2. Find renderUniqueDhammaChips function and inject renderMatrix right after it.
inject_point = "        function renderUniqueDhammaChips() {"
matrix_func = """
        function renderMatrix() {
            const tbody = document.getElementById('matrix-tbody');
            const groups = ['satipatthana', 'sammappadhana', 'iddhipada', 'indriya', 'bala', 'bojjhanga', 'magganga'];
            const colors = ['bg-sky-500', 'bg-emerald-500', 'bg-cyan-500', 'bg-violet-500', 'bg-rose-500', 'bg-amber-500', 'bg-indigo-500'];
            const darkBgColors = ['dark:bg-sky-500/20', 'dark:bg-emerald-500/20', 'dark:bg-cyan-500/20', 'dark:bg-violet-500/20', 'dark:bg-rose-500/20', 'dark:bg-amber-500/20', 'dark:bg-indigo-500/20'];
            
            let html = '';
            for (let dKey of Object.keys(dhammaInfo)) {
                const d = dhammaInfo[dKey];
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="px-4 py-2.5 font-bold text-slate-800 dark:text-slate-200 sticky left-0 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-700 z-10 shadow-[2px_0_5px_rgba(0,0,0,0.02)]">${d.label}</td>
                    <td class="px-3 py-2.5 text-center border-r border-slate-200 dark:border-slate-700"><span class="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 font-mono text-[11px] font-bold text-slate-600 dark:text-slate-400">${mm(d.count)}</span></td>`;
                
                for (let i = 0; i < groups.length; i++) {
                    const groupKey = groups[i];
                    const items = bpData.filter(b => b.group === groupKey && b.dhamma === dKey);
                    
                    if (items.length > 0) {
                        let text = items[0].name;
                        if (items.length === 4) text = '၄ ပါးလုံး';
                        if (items.length === 3) text = '၃ ပါး';
                        
                        html += `<td class="px-3 py-2.5 text-[11px]">
                                   <div class="inline-flex items-center gap-1.5 cursor-pointer hover:opacity-75 transition bg-slate-50 ${darkBgColors[i]} px-2 py-1 rounded-md border border-slate-100 dark:border-slate-700/50" onclick="openBpModal('${items[0].key}')" title="${items.map(x=>x.name).join(', ')}">
                                      <div class="w-1.5 h-1.5 flex-shrink-0 rounded-full ${colors[i]} shadow-[0_0_5px_currentColor]"></div>
                                      <span class="font-medium opacity-90">${text}</span>
                                   </div>
                                 </td>`;
                    } else {
                        html += `<td class="px-3 py-2.5 text-center text-slate-200 dark:text-slate-800/80">-</td>`;
                    }
                }
                html += `</tr>`;
            }
            tbody.innerHTML = html;
        }

"""

if inject_point in content and "function renderMatrix()" not in content:
    content = content.replace(inject_point, matrix_func + inject_point)
else:
    print("Could not find inject point for renderMatrix or it's already there.")
    sys.exit(1)

# 3. Add call to renderMatrix in DOMContentLoaded
init_block = """            renderGroups();
            renderUniqueDhammaChips();"""
new_init_block = """            renderGroups();
            renderUniqueDhammaChips();
            renderMatrix();"""
if init_block in content:
    content = content.replace(init_block, new_init_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated bodhipakkhiya_dhamma.html successfully!")
