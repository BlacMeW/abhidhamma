import sys

filepath = '/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/kammatthana_sangaha.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Abhinna (5) section right before <!-- Vipassana -->
insert_point_1 = "        <!-- Vipassana -->"
abhinna_html = """        <!-- Abhinna (5) -->
        <details class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-violet-500/20">
            <summary class="flex items-center justify-between font-bold text-violet-700 dark:text-violet-300 text-base">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>အဘိညာဉ် (၅) ပါး — သမထ၏ အထွတ်အထိပ် ရလဒ်</span>
            </summary>
            <div class="mt-4">
                <p class="text-xs text-slate-600 dark:text-slate-400 mb-4 pl-2 border-l-2 border-violet-400">
                    ကသိုဏ်းကို အခြေခံ၍ ရူပါဝစရ ပဉ္စမဈာန်သို့ ရောက်ရှိပြီးသောအခါ၊ ထိုဈာန်ကို အထူးလေ့ကျင့်ခြင်းဖြင့် အောက်ပါ လောကီအဘိညာဉ် (၅) ပါးကို ရရှိနိုင်သည်။
                </p>
                <div class="grid grid-cols-2 md:grid-cols-5 gap-2">
                    <div class="bg-violet-50 dark:bg-violet-900/30 border border-violet-200 dark:border-violet-700/50 rounded-lg p-3 text-center flex flex-col items-center gap-1.5">
                        <i class="fa-solid fa-person-rays text-violet-600 dark:text-violet-400 text-lg"></i>
                        <h4 class="font-bold text-violet-800 dark:text-violet-300 text-[11px]">ဣဒ္ဓိဝိဓ</h4>
                        <p class="text-[9px] text-slate-600 dark:text-slate-400">ကိုယ်ပွားခြင်း၊ ကောင်းကင်ပျံခြင်း၊ တောင်ကိုဖောက်ထွင်းခြင်း စသော တန်ခိုးများ ဖန်ဆင်းနိုင်ခြင်း။</p>
                    </div>
                    <div class="bg-violet-50 dark:bg-violet-900/30 border border-violet-200 dark:border-violet-700/50 rounded-lg p-3 text-center flex flex-col items-center gap-1.5">
                        <i class="fa-solid fa-ear-listen text-violet-600 dark:text-violet-400 text-lg"></i>
                        <h4 class="font-bold text-violet-800 dark:text-violet-300 text-[11px]">ဒိဗ္ဗသောတ</h4>
                        <p class="text-[9px] text-slate-600 dark:text-slate-400">အဝေး/အနီးမှ နတ်၊ လူ သတ္တဝါတို့၏ အသံကို နတ်တို့၏ နားကဲ့သို့ ကြားနိုင်ခြင်း။</p>
                    </div>
                    <div class="bg-violet-50 dark:bg-violet-900/30 border border-violet-200 dark:border-violet-700/50 rounded-lg p-3 text-center flex flex-col items-center gap-1.5">
                        <i class="fa-solid fa-brain text-violet-600 dark:text-violet-400 text-lg"></i>
                        <h4 class="font-bold text-violet-800 dark:text-violet-300 text-[11px]">စေတောပရိယ</h4>
                        <p class="text-[9px] text-slate-600 dark:text-slate-400">သူတစ်ပါး၏ စိတ်ထဲ၌ ဖြစ်ပေါ်နေသော အကြံအစည်ကို သိနိုင်ခြင်း။</p>
                    </div>
                    <div class="bg-violet-50 dark:bg-violet-900/30 border border-violet-200 dark:border-violet-700/50 rounded-lg p-3 text-center flex flex-col items-center gap-1.5">
                        <i class="fa-solid fa-clock-rotate-left text-violet-600 dark:text-violet-400 text-lg"></i>
                        <h4 class="font-bold text-violet-800 dark:text-violet-300 text-[11px]">ပုဗ္ဗေနိဝါသာနုဿတိ</h4>
                        <p class="text-[9px] text-slate-600 dark:text-slate-400">မိမိ၏ ရှေးဘဝများစွာ (ဖြစ်စဉ်၊ အမည်၊ အမျိုး) ကို အောက်မေ့ ပြန်လည်သိမြင်နိုင်ခြင်း။</p>
                    </div>
                    <div class="bg-violet-50 dark:bg-violet-900/30 border border-violet-200 dark:border-violet-700/50 rounded-lg p-3 text-center flex flex-col items-center gap-1.5 col-span-2 md:col-span-1">
                        <i class="fa-solid fa-eye text-violet-600 dark:text-violet-400 text-lg"></i>
                        <h4 class="font-bold text-violet-800 dark:text-violet-300 text-[11px]">ဒိဗ္ဗစက္ခု</h4>
                        <p class="text-[9px] text-slate-600 dark:text-slate-400">အဝေး/အနီးမှ အရာများကို နတ်တို့၏ မျက်စိကဲ့သို့ မြင်နိုင်ခြင်း (သတ္တဝါတို့၏ ကမ္မဿကတဉာဏ် အပါအဝင်)။</p>
                    </div>
                </div>
            </div>
        </details>

"""
if "<!-- Abhinna (5) -->" not in content:
    content = content.replace(insert_point_1, abhinna_html + insert_point_1)


# 2. Add Magga Pahana section right before <!-- Cross-links -->
insert_point_2 = "        <!-- Cross-links -->"
magga_pahana_html = """        <!-- Magga Pahana -->
        <div class="glass-card rounded-2xl p-5 max-w-4xl mx-auto border border-amber-400 dark:border-amber-500/30 space-y-4" style="box-shadow: 0 0 15px rgba(234,179,8,0.1);">
            <h3 class="font-bold text-amber-800 dark:text-amber-300 text-base flex items-center gap-2"><i class="fa-solid fa-crown text-amber-500"></i> မဂ် (၄) ပါးဖြင့် ကိလေသာ ပယ်သတ်ပုံ (အရိယပုဂ္ဂိုလ် ၄ မျိုး) — ဝိပဿနာ၏ အထွတ်အထိပ် ရလဒ်</h3>
            <p class="text-xs text-slate-700 dark:text-slate-300 mb-2">
                ဝိမောက္ခ (၃) ပါး တံခါးပေါက်မှတစ်ဆင့် နိဗ္ဗာန်သို့ ကူးပြောင်းဝင်ရောက်သွားသော ယောဂီသည် မဂ်ဖိုလ် (၁) ကြိမ် ရတိုင်း အရိယပုဂ္ဂိုလ် အဆင့် (၁) ဆင့် မြင့်တက်သွားပြီး၊ ကိလေသာများကို အပြီးတိုင် (သမုစ္ဆေဒပဟာန်) ပယ်သတ်သွားသည်။
            </p>
            <div class="space-y-3">
                <div class="bg-white dark:bg-slate-900 border-l-4 border-emerald-500 rounded-r-xl p-3 shadow-sm">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="font-bold text-slate-800 dark:text-slate-200 text-sm">၁။ သောတာပန် (Sotāpanna)</h4>
                        <span class="text-[10px] bg-emerald-100 dark:bg-emerald-900/50 text-emerald-700 dark:text-emerald-300 px-2 py-0.5 rounded">သောတာပတ္တိမဂ်</span>
                    </div>
                    <p class="text-xs text-slate-600 dark:text-slate-400">
                        <span class="font-bold text-rose-600 dark:text-rose-400">ပယ်သော ကိလေသာ:</span> 
                        ဒိဋ္ဌိ (အယူမှားခြင်း)၊ ဝိစိကိစ္ဆာ (ယုံမှားသံသယဖြစ်ခြင်း)၊ နှင့် အပါယ် ၄ ဘုံသို့ ကျရောက်စေနိုင်သော ကြမ်းတမ်းသည့် ကိလေသာ အားလုံး။
                    </p>
                </div>
                
                <div class="bg-white dark:bg-slate-900 border-l-4 border-sky-500 rounded-r-xl p-3 shadow-sm">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="font-bold text-slate-800 dark:text-slate-200 text-sm">၂။ သကဒါဂါမ် (Sakadāgāmi)</h4>
                        <span class="text-[10px] bg-sky-100 dark:bg-sky-900/50 text-sky-700 dark:text-sky-300 px-2 py-0.5 rounded">သကဒါဂါမိမဂ်</span>
                    </div>
                    <p class="text-xs text-slate-600 dark:text-slate-400">
                        <span class="font-bold text-rose-600 dark:text-rose-400">ပယ်သော ကိလေသာ:</span> 
                        အမြစ်ပြတ် ပယ်ခြင်း မရှိသေးသော်လည်း၊ ကာမရာဂ (ကာမဂုဏ်တပ်မက်မှု) နှင့် ဒေါသ ကို အလွန် ခေါင်းပါး အားနည်းသွားစေသည်။
                    </p>
                </div>
                
                <div class="bg-white dark:bg-slate-900 border-l-4 border-blue-500 rounded-r-xl p-3 shadow-sm">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="font-bold text-slate-800 dark:text-slate-200 text-sm">၃။ အနာဂါမ် (Anāgāmi)</h4>
                        <span class="text-[10px] bg-blue-100 dark:bg-blue-900/50 text-blue-700 dark:text-blue-300 px-2 py-0.5 rounded">အနာဂါမိမဂ်</span>
                    </div>
                    <p class="text-xs text-slate-600 dark:text-slate-400">
                        <span class="font-bold text-rose-600 dark:text-rose-400">ပယ်သော ကိလေသာ:</span> 
                        ကာမရာဂ နှင့် ဒေါသ ကို လုံးဝ အမြစ်ပြတ် ပယ်သတ်လိုက်သည်။ (ဒေါသ လုံးဝ မထွက်တော့ပါ၊ ကာမဘုံသို့လည်း ပြန်မလာတော့ပါ။)
                    </p>
                </div>
                
                <div class="bg-white dark:bg-slate-900 border-l-4 border-amber-500 rounded-r-xl p-3 shadow-sm">
                    <div class="flex items-center gap-2 mb-1">
                        <h4 class="font-bold text-slate-800 dark:text-slate-200 text-sm">၄။ ရဟန္တာ (Arahant)</h4>
                        <span class="text-[10px] bg-amber-100 dark:bg-amber-900/50 text-amber-700 dark:text-amber-300 px-2 py-0.5 rounded">အရဟတ္တမဂ်</span>
                    </div>
                    <p class="text-xs text-slate-600 dark:text-slate-400">
                        <span class="font-bold text-rose-600 dark:text-rose-400">ပယ်သော ကိလေသာ:</span> 
                        ကျန်ရှိနေသော ရူပရာဂ (ရူပဘုံကိုတပ်မက်မှု)၊ အရူပရာဂ (အရူပဘုံကိုတပ်မက်မှု)၊ မာန၊ ဥဒ္ဓစ္စ၊ အဝိဇ္ဇာ (မသိမမြင်မှု) — ကိလေသာအားလုံးကို အကြွင်းမဲ့ ပယ်ဖျက်လိုက်ပြီး သံသရာဝဋ်ဆင်းရဲမှ အပြီးတိုင် လွတ်မြောက်သည်။
                    </p>
                </div>
            </div>
        </div>

"""

if "<!-- Magga Pahana -->" not in content:
    content = content.replace(insert_point_2, magga_pahana_html + insert_point_2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
