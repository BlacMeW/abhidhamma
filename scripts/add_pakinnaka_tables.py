import re

with open('pakinnaka_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Vedana & Hetu Master Table
hetu_target = """            <!-- Hetu Cards Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3" id="hetu-grid"></div>
        </section>"""

hetu_replacement = """            <!-- Hetu Cards Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3" id="hetu-grid"></div>
            
            <!-- Master Vedana and Hetu Table -->
            <details class="glass-card rounded-xl p-4 md:p-6 border border-emerald-500/30 mt-4" open>
                <summary class="flex items-center justify-between font-bold text-emerald-700 dark:text-emerald-300 text-sm md:text-base">
                    <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>ဝေဒနာ၊ ဟိတ် နှင့် စိတ် (၈၉) ပါး ဆက်စပ်မှု ဇယားကြီး</span>
                </summary>
                <div id="vedana-hetu-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </section>"""

if hetu_target in content:
    content = content.replace(hetu_target, hetu_replacement)
else:
    print("Error: Could not find hetu_target")

# 2. Insert Dvara, Arammana, Vatthu Master Table
vatthu_target = """            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3" id="vatthu-grid"></div>
        </section>"""

vatthu_replacement = """            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3" id="vatthu-grid"></div>
            
            <!-- Master Dvara, Arammana, Vatthu Table -->
            <details class="glass-card rounded-xl p-4 md:p-6 border border-violet-500/30 mt-4" open>
                <summary class="flex items-center justify-between font-bold text-violet-700 dark:text-violet-300 text-sm md:text-base">
                    <span><i class="fa-solid fa-table tree-chevron mr-2 text-xs"></i>ဒွါရ၊ အာရုံ၊ ဝတ္ထု သရုပ်ခွဲ အကျဉ်းချုပ် ဇယားကြီး</span>
                </summary>
                <div id="dvara-arammana-vatthu-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>
        </section>"""

if vatthu_target in content:
    content = content.replace(vatthu_target, vatthu_replacement)
else:
    print("Error: Could not find vatthu_target")

# 3. Insert JS logic
js_code = """
        function renderVedanaHetuMasterTable() {
            const container = document.getElementById('vedana-hetu-matrix');
            if (!container) return;
            
            let html = `<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">`;
            
            // Vedana Table
            html += `<div>
                <h4 class="font-bold text-rose-700 dark:text-rose-300 mb-2 flex items-center gap-2"><i class="fa-solid fa-face-smile"></i> ဝေဒနာ (၅) ပါး ခွဲခြားမှု</h4>
                <table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead class="bg-rose-50 dark:bg-rose-900/40">
                    <tr><th class="p-2 border border-slate-300 dark:border-slate-700 w-32">ဝေဒနာ</th><th class="p-2 border border-slate-300 dark:border-slate-700 w-24 text-center">အရေအတွက်</th><th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th></tr>
                </thead>
                <tbody class="bg-white dark:bg-slate-900">`;
            vedanaData.forEach(d => {
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.cittas}</td>
                </tr>`;
            });
            html += `</tbody></table></div>`;
            
            // Hetu Table
            html += `<div>
                <h4 class="font-bold text-emerald-700 dark:text-emerald-300 mb-2 flex items-center gap-2"><i class="fa-solid fa-seedling"></i> ဟိတ် (၄) မျိုး ခွဲခြားမှု</h4>
                <table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead class="bg-emerald-50 dark:bg-emerald-900/40">
                    <tr><th class="p-2 border border-slate-300 dark:border-slate-700 w-32">အုပ်စု</th><th class="p-2 border border-slate-300 dark:border-slate-700 w-24 text-center">အရေအတွက်</th><th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th></tr>
                </thead>
                <tbody class="bg-white dark:bg-slate-900">`;
            hetuData.forEach(d => {
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 leading-relaxed">${d.cittas}</td>
                </tr>`;
            });
            html += `</tbody></table></div>`;
            
            html += `</div>`;
            container.innerHTML = html;
        }

        function renderDvaraArammanaVatthuMasterTable() {
            const container = document.getElementById('dvara-arammana-vatthu-matrix');
            if (!container) return;
            
            let html = `<div class="grid grid-cols-1 xl:grid-cols-3 gap-6">`;
            
            // Dvara
            html += `<div>
                <h4 class="font-bold text-amber-700 dark:text-amber-300 mb-2 flex items-center gap-2"><i class="fa-solid fa-door-open"></i> ဒွါရ (၅) မျိုး ခွဲခြားမှု</h4>
                <table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead class="bg-amber-50 dark:bg-amber-900/40">
                    <tr><th class="p-2 border border-slate-300 dark:border-slate-700 w-28">အုပ်စု</th><th class="p-2 border border-slate-300 dark:border-slate-700 w-16 text-center">ပေါင်း</th><th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th></tr>
                </thead>
                <tbody class="bg-white dark:bg-slate-900">`;
            dvaradata.forEach(d => {
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${d.name}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count.replace(' ပါး', '')}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-[11px] leading-relaxed">${d.desc}</td>
                </tr>`;
            });
            html += `</tbody></table></div>`;
            
            // Arammana
            html += `<div>
                <h4 class="font-bold text-indigo-700 dark:text-indigo-300 mb-2 flex items-center gap-2"><i class="fa-solid fa-eye"></i> အာရုံ (၇) မျိုး ခွဲခြားမှု</h4>
                <table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead class="bg-indigo-50 dark:bg-indigo-900/40">
                    <tr><th class="p-2 border border-slate-300 dark:border-slate-700 w-28">အုပ်စု</th><th class="p-2 border border-slate-300 dark:border-slate-700 w-16 text-center">ပေါင်း</th><th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th></tr>
                </thead>
                <tbody class="bg-white dark:bg-slate-900">`;
            arammanaData.forEach(d => {
                let safeName = d.name.includes('။') ? d.name.split('။ ')[1] : d.name;
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${safeName}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count.replace(' ပါး', '')}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-[11px] leading-relaxed">${d.desc}</td>
                </tr>`;
            });
            html += `</tbody></table></div>`;
            
            // Vatthu
            html += `<div>
                <h4 class="font-bold text-violet-700 dark:text-violet-300 mb-2 flex items-center gap-2"><i class="fa-solid fa-building"></i> ဝတ္ထု (၃) မျိုး ခွဲခြားမှု</h4>
                <table class="w-full text-xs text-left border-collapse border border-slate-300 dark:border-slate-700">
                <thead class="bg-violet-50 dark:bg-violet-900/40">
                    <tr><th class="p-2 border border-slate-300 dark:border-slate-700 w-28">အုပ်စု</th><th class="p-2 border border-slate-300 dark:border-slate-700 w-16 text-center">ပေါင်း</th><th class="p-2 border border-slate-300 dark:border-slate-700">ပါဝင်သော စိတ်များ</th></tr>
                </thead>
                <tbody class="bg-white dark:bg-slate-900">`;
            vatthuData.forEach(d => {
                let safeName = d.name.includes('။') ? d.name.split('။ ')[1] : d.name;
                html += `<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-${d.color}-600 dark:text-${d.color}-400">${safeName}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 font-bold text-center">${d.count.replace(' ပါး', '')}</td>
                    <td class="p-2 border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-[11px] leading-relaxed">${d.desc}</td>
                </tr>`;
            });
            html += `</tbody></table></div>`;
            
            html += `</div>`;
            container.innerHTML = html;
        }
"""
js_target = """        function openPkModal(type, index) {"""
if js_target in content:
    content = content.replace(js_target, js_code + "\n" + js_target)
else:
    print("Error: Could not find js_target")

# 4. Add function calls
init_target = """        function renderGrids() {"""
init_replacement = """        function renderGrids() {
            renderVedanaHetuMasterTable();
            renderDvaraArammanaVatthuMasterTable();"""
if init_target in content:
    content = content.replace(init_target, init_replacement)
else:
    print("Error: Could not find init_target")

with open('pakinnaka_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(content)

