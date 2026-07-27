import sys
import re

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/bodhipakkhiya_dhamma.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the matrix render loop to use openMultiBpModal
old_click_action = "let clickAction = items.length > 1 ? `jumpToGroup('${groupKey}')` : `openBpModal('${items[0].key}')`;"
new_click_action = "let clickAction = `openMultiBpModal('${items.map(x=>x.key).join(',')}')`;"
content = content.replace(old_click_action, new_click_action)

# Also update the inline onclick if needed. Actually it uses ${clickAction}, so it's fine.

# 2. Add openMultiBpModal function
old_modal_func = """        function openBpModal(key) {
            const b = bpData.find(x => x.key === key);
            if (!b) return;
            const info = groupInfo[b.group];
            const modal = document.getElementById('modal');
            const content = document.getElementById('modal-content');
            content.innerHTML = `
                <div class="text-center space-y-2">
                    <div class="w-16 h-16 mx-auto rounded-2xl bg-slate-50 dark:bg-slate-800 flex items-center justify-center text-3xl border border-slate-200 dark:border-slate-700 ${info.color}">
                        <i class="fa-solid ${b.icon}"></i>
                    </div>
                    <div>
                        <span class="text-xs text-slate-600 dark:text-slate-400 uppercase font-mono">${info.label} — အမှတ် ${mm(b.id)}/၃၇</span>
                        <h3 class="text-xl font-bold ${info.color}">${b.name}</h3>
                        <p class="text-[11px] text-slate-500 dark:text-slate-500 font-mono mt-1">${b.pali}</p>
                    </div>
                </div>
                <div class="mt-4 space-y-3 bg-slate-50/50 dark:bg-slate-950/50 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-sm">
                    <div>
                        <span class="text-xs font-semibold text-slate-600 dark:text-slate-400 block uppercase">အနက်အဓိပ္ပာယ်</span>
                        <p class="text-slate-800 dark:text-slate-200 mt-1 leading-relaxed">${b.desc}</p>
                    </div>
                    <div class="pt-3 border-t border-slate-200 dark:border-slate-800">
                        <span class="text-xs font-semibold text-amber-700 dark:text-amber-400 block uppercase"><i class="fa-solid fa-lightbulb mr-1"></i>ဥပမာ</span>
                        <p class="text-slate-700 dark:text-slate-300 mt-1 leading-relaxed">${b.example}</p>
                    </div>
                </div>
            `;
            modal.classList.remove('hidden');
        }"""

new_modal_func = """        function openBpModal(key) { openMultiBpModal(key); }

        function openMultiBpModal(keysStr) {
            const keys = keysStr.split(',');
            const items = keys.map(k => bpData.find(x => x.key === k)).filter(Boolean);
            if (items.length === 0) return;
            
            const info = groupInfo[items[0].group];
            const modal = document.getElementById('modal');
            const content = document.getElementById('modal-content');
            
            if (items.length === 1) {
                const b = items[0];
                content.innerHTML = `
                    <div class="text-center space-y-2">
                        <div class="w-16 h-16 mx-auto rounded-2xl bg-slate-50 dark:bg-slate-800 flex items-center justify-center text-3xl border border-slate-200 dark:border-slate-700 ${info.color}">
                            <i class="fa-solid ${b.icon}"></i>
                        </div>
                        <div>
                            <span class="text-xs text-slate-600 dark:text-slate-400 uppercase font-mono">${info.label} — အမှတ် ${mm(b.id)}/၃၇</span>
                            <h3 class="text-xl font-bold ${info.color}">${b.name}</h3>
                            <p class="text-[11px] text-slate-500 dark:text-slate-500 font-mono mt-1">${b.pali}</p>
                        </div>
                    </div>
                    <div class="mt-4 space-y-3 bg-slate-50/50 dark:bg-slate-950/50 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-sm">
                        <div>
                            <span class="text-xs font-semibold text-slate-600 dark:text-slate-400 block uppercase">အနက်အဓိပ္ပာယ်</span>
                            <p class="text-slate-800 dark:text-slate-200 mt-1 leading-relaxed">${b.desc}</p>
                        </div>
                        <div class="pt-3 border-t border-slate-200 dark:border-slate-800">
                            <span class="text-xs font-semibold text-amber-700 dark:text-amber-400 block uppercase"><i class="fa-solid fa-lightbulb mr-1"></i>ဥပမာ</span>
                            <p class="text-slate-700 dark:text-slate-300 mt-1 leading-relaxed">${b.example}</p>
                        </div>
                    </div>
                `;
            } else {
                let bodyHtml = items.map(b => `
                    <div class="space-y-2 bg-slate-50/50 dark:bg-slate-950/50 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-sm">
                        <div class="flex items-center gap-2 border-b border-slate-200 dark:border-slate-700 pb-2 mb-2">
                            <div class="w-8 h-8 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center ${info.color} border border-slate-200 dark:border-slate-700 flex-shrink-0">
                                <i class="fa-solid ${b.icon} text-sm"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-slate-800 dark:text-slate-200">${b.name} <span class="text-[11px] text-slate-500 font-normal ml-1">(${mm(b.id)}/၃၇)</span></h4>
                                <p class="text-[10px] text-slate-500 font-mono">${b.pali}</p>
                            </div>
                        </div>
                        <div>
                            <p class="text-slate-800 dark:text-slate-200 leading-relaxed">${b.desc}</p>
                        </div>
                        <div class="pt-2">
                            <span class="text-[11px] font-semibold text-amber-700 dark:text-amber-400 block uppercase"><i class="fa-solid fa-lightbulb mr-1"></i>ဥပမာ</span>
                            <p class="text-slate-700 dark:text-slate-300 mt-0.5 leading-relaxed text-[13px]">${b.example}</p>
                        </div>
                    </div>
                `).join('');
                
                content.innerHTML = `
                    <div class="text-center space-y-2 mb-4">
                        <div class="w-16 h-16 mx-auto rounded-2xl bg-slate-50 dark:bg-slate-800 flex items-center justify-center text-3xl border border-slate-200 dark:border-slate-700 ${info.color}">
                            <i class="fa-solid fa-layer-group"></i>
                        </div>
                        <div>
                            <span class="text-xs text-slate-600 dark:text-slate-400 uppercase font-mono">${info.label}</span>
                            <h3 class="text-xl font-bold ${info.color}">စုပေါင်း ရှင်းလင်းချက် (${mm(items.length)} ပါး)</h3>
                        </div>
                    </div>
                    <div class="space-y-3">
                        ${bodyHtml}
                    </div>
                `;
            }
            modal.classList.remove('hidden');
        }"""

if old_modal_func in content:
    content = content.replace(old_modal_func, new_modal_func)
else:
    print("Could not find openBpModal!")
    sys.exit(1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
