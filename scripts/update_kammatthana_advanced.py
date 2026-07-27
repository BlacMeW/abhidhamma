import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/kammatthana_sangaha.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderNanas in JS to include the Vipassanupakkilesa warning box for id == 2
old_render_nanas = """            html += nanaData.map(n => `
                <div class="relative flex gap-4">
                    <div class="absolute -left-6 top-1 w-6 h-6 rounded-full bg-amber-100 dark:bg-amber-900 border-2 border-amber-400 dark:border-amber-600 flex items-center justify-center z-10 text-[9px] font-bold text-amber-700 dark:text-amber-300">
                        ${mm(n.id)}
                    </div>
                    <div class="flex-1 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl p-3 shadow-sm hover:shadow-md transition group">
                        <div class="flex items-center gap-2 mb-1">
                            <i class="fa-solid ${n.icon} text-amber-500 dark:text-amber-600 w-4"></i>
                            <h4 class="font-bold text-amber-800 dark:text-amber-400 text-sm">${n.name}</h4>
                            <span class="text-[10px] text-slate-400 font-mono hidden sm:inline-block">${n.pali}</span>
                        </div>
                        <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed ml-6">${n.desc}</p>
                    </div>
                </div>
            `).join('');"""

new_render_nanas = """            html += nanaData.map(n => {
                let extraHtml = '';
                if (n.id === 2) {
                    extraHtml = `
                    <div class="mt-3 ml-6 bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/50 rounded-lg p-3 relative">
                        <div class="flex items-start gap-2">
                            <i class="fa-solid fa-triangle-exclamation text-rose-500 mt-0.5"></i>
                            <div>
                                <h5 class="text-xs font-bold text-rose-700 dark:text-rose-400">သတိပြုရန် — ဝိပဿနုပက္ကိလေသ (၁၀) ပါး (The 10 Corruptions of Insight)</h5>
                                <p class="text-[11px] text-slate-600 dark:text-slate-400 mt-1">
                                    ဥဒယဗ္ဗယဉာဏ် အစပိုင်းတွင် ယောဂီအား တရားထူးရပြီဟု အထင်မှားစေသော အလွန်ကောင်းမွန်သည့် အတွေ့အကြုံ (၁၀) မျိုး ပေါ်လာတတ်သည်။ ၎င်းတို့မှာ —
                                    <span class="block mt-1 font-semibold text-rose-800 dark:text-rose-300">
                                    ဩဘာသ (အလင်းရောင်)၊ ပီတိ (နှစ်သက်မှု)၊ ပဿဒ္ဓိ (ငြိမ်းအေးမှု)၊ အဓိမောက္ခ (ယုံကြည်မှု)၊ ပဂ္ဂဟ (လုံ့လ)၊ သုခ (ချမ်းသာ)၊ ဉာဏ် (ထက်မြက်မှု)၊ ဥပဋ္ဌာန (ခိုင်မြဲသောသတိ)၊ ဥပေက္ခာ (လျစ်လျူရှုနိုင်မှု)၊ နိကန္တိ (သာယာတွယ်တာမှု)။
                                    </span>
                                </p>
                                <p class="text-[11px] text-rose-600 dark:text-rose-500 mt-1 italic">ဤသည်တို့ကို မဂ်ဖိုလ်မဟုတ်ကြောင်း သိမြင်မှသာ (မဂ္ဂါမဂ္ဂဉာဏဒဿနဝိသုဒ္ဓိ) ရှေ့ဆက်တက်နိုင်သည်။</p>
                            </div>
                        </div>
                    </div>`;
                }
                return `
                <div class="relative flex gap-4">
                    <div class="absolute -left-6 top-1 w-6 h-6 rounded-full bg-amber-100 dark:bg-amber-900 border-2 border-amber-400 dark:border-amber-600 flex items-center justify-center z-10 text-[9px] font-bold text-amber-700 dark:text-amber-300">
                        ${mm(n.id)}
                    </div>
                    <div class="flex-1 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl p-3 shadow-sm hover:shadow-md transition group">
                        <div class="flex items-center gap-2 mb-1">
                            <i class="fa-solid ${n.icon} text-amber-500 dark:text-amber-600 w-4"></i>
                            <h4 class="font-bold text-amber-800 dark:text-amber-400 text-sm">${n.name}</h4>
                            <span class="text-[10px] text-slate-400 font-mono hidden sm:inline-block">${n.pali}</span>
                        </div>
                        <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed ml-6">${n.desc}</p>
                        ${extraHtml}
                    </div>
                </div>
                `;
            }).join('');"""

if "<!-- 10 Vipassana Nanas -->" in content and "ဝိပဿနုပက္ကိလေသ (၁၀) ပါး" not in content:
    content = content.replace(old_render_nanas, new_render_nanas)


# 2. Add Vimokkha (3) section right before <!-- Cross-links -->
insert_point = "        <!-- Cross-links -->"
vimokkha_html = """        <!-- Vimokkha (3) -->
        <div class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-indigo-500/20 space-y-4">
            <h3 class="font-bold text-indigo-700 dark:text-indigo-300 text-base flex items-center gap-2"><i class="fa-solid fa-door-open"></i> ဝိမောက္ခ (၃) ပါး — နိဗ္ဗာန်သို့ဝင်ရာ တံခါးပေါက်များ</h3>
            <p class="text-xs text-slate-700 dark:text-slate-300">
                ဝိပဿနာဉာဏ်များ ရင့်ကျက်ပြီး မဂ်ဖိုလ် (နိဗ္ဗာန်) သို့ ကူးပြောင်းရာတွင် ယောဂီအားထုတ်ခဲ့သော လက္ခဏာ (အနိစ္စ၊ ဒုက္ခ၊ အနတ္တ) အပေါ်မူတည်၍ လွတ်မြောက်မှု တံခါးပေါက် (၃) မျိုး ကွဲပြားသွားသည်။
            </p>
            <div class="grid md:grid-cols-3 gap-3">
                <div class="bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-800 rounded-xl p-4 text-center">
                    <span class="inline-block px-2 py-1 bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-300 rounded text-[10px] font-bold mb-2">အနိစ္စ လက္ခဏာ</span>
                    <i class="fa-solid fa-arrow-down text-indigo-300 block mb-2"></i>
                    <h4 class="font-bold text-indigo-700 dark:text-indigo-400 text-sm">အနိမိတ္တဝိမောက္ခ</h4>
                    <p class="text-[10px] text-slate-600 dark:text-slate-400 mt-1">အနိစ္စဟု များစွာရှုသဖြင့် အနိမိတ္တ (နိမိတ်အမှတ်အသား ကင်းမဲ့သော နိဗ္ဗာန်) မှတဆင့် လွတ်မြောက်ခြင်း။</p>
                </div>
                <div class="bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-800 rounded-xl p-4 text-center">
                    <span class="inline-block px-2 py-1 bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-300 rounded text-[10px] font-bold mb-2">ဒုက္ခ လက္ခဏာ</span>
                    <i class="fa-solid fa-arrow-down text-indigo-300 block mb-2"></i>
                    <h4 class="font-bold text-indigo-700 dark:text-indigo-400 text-sm">အပ္ပဏိဟိတဝိမောက္ခ</h4>
                    <p class="text-[10px] text-slate-600 dark:text-slate-400 mt-1">ဒုက္ခဟု များစွာရှုသဖြင့် အပ္ပဏိဟိတ (တောင့်တမှု တဏှာကင်းသော နိဗ္ဗာန်) မှတဆင့် လွတ်မြောက်ခြင်း။</p>
                </div>
                <div class="bg-indigo-50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-800 rounded-xl p-4 text-center">
                    <span class="inline-block px-2 py-1 bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-300 rounded text-[10px] font-bold mb-2">အနတ္တ လက္ခဏာ</span>
                    <i class="fa-solid fa-arrow-down text-indigo-300 block mb-2"></i>
                    <h4 class="font-bold text-indigo-700 dark:text-indigo-400 text-sm">သုညတဝိမောက္ခ</h4>
                    <p class="text-[10px] text-slate-600 dark:text-slate-400 mt-1">အနတ္တဟု များစွာရှုသဖြင့် သုညတ (အတ္တအနှစ်သာရ ဆိတ်သုဉ်းသော နိဗ္ဗာန်) မှတဆင့် လွတ်မြောက်ခြင်း။</p>
                </div>
            </div>
        </div>

"""

if "<!-- Vimokkha (3) -->" not in content:
    content = content.replace(insert_point, vimokkha_html + insert_point)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
