import re

html_block = """
        <!-- 528 Metta -->
        <div class="glass-card rounded-3xl p-4 sm:p-6 md:p-10 border-t-4 border-t-indigo-500 shadow-sm relative overflow-hidden max-w-5xl mx-auto mb-10">
            <div class="absolute -right-10 -top-10 text-9xl text-indigo-500/5 dark:text-indigo-500/10 pointer-events-none"><i class="fa-solid fa-infinity"></i></div>
            
            <div class="flex items-center justify-between mb-8 flex-wrap gap-4">
                <div>
                    <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-3">
                        <i class="fa-solid fa-network-wired text-indigo-500"></i> မေတ္တာ ၅၂၈ သွယ် (The 528 Ways of Mettā)
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1">ဝိသုဒ္ဓိမဂ်လာ နည်းစနစ်အတိုင်း မေတ္တာပွားများခြင်း အသေးစိတ်</p>
                </div>
            </div>

            <!-- The 4 Core Wishes -->
            <div class="mb-8">
                <h4 class="font-bold text-indigo-800 dark:text-indigo-300 text-lg mb-4 border-b border-indigo-100 dark:border-indigo-900/50 pb-2">၁။ အာကာရ ၄ ပါး (The 4 Core Wishes)</h4>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
                    <div class="bg-indigo-50 dark:bg-indigo-900/20 p-4 rounded-xl border border-indigo-200 dark:border-indigo-800 text-center">
                        <div class="text-2xl mb-2 text-indigo-500"><i class="fa-solid fa-shield-halved"></i></div>
                        <h5 class="font-bold text-slate-800 dark:text-slate-200 text-sm">အဝေရာ ဟောန္တု</h5>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">ဘေးရန် ကင်းကြပါစေ</p>
                    </div>
                    <div class="bg-indigo-50 dark:bg-indigo-900/20 p-4 rounded-xl border border-indigo-200 dark:border-indigo-800 text-center">
                        <div class="text-2xl mb-2 text-indigo-500"><i class="fa-solid fa-face-smile"></i></div>
                        <h5 class="font-bold text-slate-800 dark:text-slate-200 text-sm">အဗျာပဇ္ဇာ ဟောန္တု</h5>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">စိတ်ဆင်းရဲ ကင်းကြပါစေ</p>
                    </div>
                    <div class="bg-indigo-50 dark:bg-indigo-900/20 p-4 rounded-xl border border-indigo-200 dark:border-indigo-800 text-center">
                        <div class="text-2xl mb-2 text-indigo-500"><i class="fa-solid fa-heart-pulse"></i></div>
                        <h5 class="font-bold text-slate-800 dark:text-slate-200 text-sm">အနီဃာ ဟောန္တု</h5>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">ကိုယ်ဆင်းရဲ ကင်းကြပါစေ</p>
                    </div>
                    <div class="bg-indigo-50 dark:bg-indigo-900/20 p-4 rounded-xl border border-indigo-200 dark:border-indigo-800 text-center">
                        <div class="text-2xl mb-2 text-indigo-500"><i class="fa-solid fa-hands-holding-child"></i></div>
                        <h5 class="font-bold text-slate-800 dark:text-slate-200 text-sm">သုခီ အတ္တာနံ ပရိဟရန္တု</h5>
                        <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">ချမ်းသာစွာ မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ကြပါစေ</p>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <!-- Anodhisoka -->
                <div>
                    <h4 class="font-bold text-teal-700 dark:text-teal-400 text-lg mb-4 border-b border-teal-100 dark:border-teal-900/50 pb-2">၂။ အနောဓိသ (၅) မျိုး (Unspecified)</h4>
                    <ul class="space-y-3">
                        <li class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-teal-100 dark:bg-teal-900/50 flex items-center justify-center text-teal-600 text-xs font-bold shrink-0 mt-0.5">၁</div>
                            <div>
                                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ သတ္တာ</span>
                                <p class="text-xs text-slate-600 dark:text-slate-400">သတ္တဝါ အားလုံး</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-teal-100 dark:bg-teal-900/50 flex items-center justify-center text-teal-600 text-xs font-bold shrink-0 mt-0.5">၂</div>
                            <div>
                                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ပါဏာ</span>
                                <p class="text-xs text-slate-600 dark:text-slate-400">ထွက်သက်ဝင်သက်ရှိသူ အားလုံး</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-teal-100 dark:bg-teal-900/50 flex items-center justify-center text-teal-600 text-xs font-bold shrink-0 mt-0.5">၃</div>
                            <div>
                                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ဘူတာ</span>
                                <p class="text-xs text-slate-600 dark:text-slate-400">ထင်ရှားဖြစ်ပေါ်လာသူ အားလုံး</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-teal-100 dark:bg-teal-900/50 flex items-center justify-center text-teal-600 text-xs font-bold shrink-0 mt-0.5">၄</div>
                            <div>
                                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ပုဂ္ဂလာ</span>
                                <p class="text-xs text-slate-600 dark:text-slate-400">ပုဂ္ဂိုလ် အားလုံး</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-teal-100 dark:bg-teal-900/50 flex items-center justify-center text-teal-600 text-xs font-bold shrink-0 mt-0.5">၅</div>
                            <div>
                                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ အတ္တဘာဝ ပရိယာပန္နာ</span>
                                <p class="text-xs text-slate-600 dark:text-slate-400">ခန္ဓာကိုယ် အတ္တဘော အကျုံးဝင်သူ အားလုံး</p>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Odhisoka -->
                <div>
                    <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-4 border-b border-rose-100 dark:border-rose-900/50 pb-2">၃။ ဩဓိသ (၇) မျိုး (Specified)</h4>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၁</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗာ ဣတ္ထိယော</span><p class="text-[11px] text-slate-600 dark:text-slate-400">အမျိုးသမီး အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၂</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ပုရိသာ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">အမျိုးသား အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၃</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ အရိယာ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">အရိယာ အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၄</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ အနရိယာ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">ပုထုဇဉ် အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၅</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ဒေဝါ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">နတ်, ဗြဟ္မာ အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၆</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ မနုဿာ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">လူ အားလုံး</p></div>
                        </div>
                        <div class="flex items-start gap-3 p-3 bg-white/60 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm sm:col-span-2">
                            <div class="w-6 h-6 rounded-full bg-rose-100 dark:bg-rose-900/50 flex items-center justify-center text-rose-600 text-xs font-bold shrink-0 mt-0.5">၇</div>
                            <div><span class="font-bold text-slate-800 dark:text-slate-200 text-sm">သဗ္ဗေ ဝိနိပါတိကာ</span><p class="text-[11px] text-slate-600 dark:text-slate-400">အပါယ် (၄) ဘုံသား အားလုံး</p></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Calculation and Directions -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div>
                    <h4 class="font-bold text-indigo-800 dark:text-indigo-300 text-lg mb-4 border-b border-indigo-100 dark:border-indigo-900/50 pb-2">၄။ ဒိသာဖရဏ (၁၀) မျက်နှာ</h4>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                        အထက်ပါ (၁၂) မျိုးသော အုပ်စုတို့ကို အရပ် (၁၀) မျက်နှာသို့ အာရုံပြု၍ ပို့လွှတ်ခြင်းကို ဒိသာဖရဏ ဟုခေါ်သည်။
                    </p>
                    <div class="flex flex-wrap gap-2 text-xs font-medium">
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အရှေ့ (Puratthima)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အနောက် (Pacchima)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">မြောက် (Uttara)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">တောင် (Dakkhina)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အရှေ့တောင် (Puratthimānudisā)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အနောက်မြောက် (Pacchimānudisā)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အရှေ့မြောက် (Uttarānudisā)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အနောက်တောင် (Dakkhinānudisā)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အောက် (Hetthima)</span>
                        <span class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded border border-slate-200 dark:border-slate-700">အထက် (Uparima)</span>
                    </div>
                </div>

                <div class="bg-gradient-to-br from-indigo-50 to-purple-50 dark:from-indigo-950/40 dark:to-purple-950/40 p-5 rounded-2xl border border-indigo-200 dark:border-indigo-800/60 shadow-inner">
                    <h4 class="font-bold text-indigo-900 dark:text-indigo-200 text-base mb-4 flex items-center gap-2">
                        <i class="fa-solid fa-calculator text-indigo-500"></i> မေတ္တာ (၅၂၈) သွယ် တွက်ချက်ပုံ
                    </h4>
                    <div class="space-y-3 text-sm text-slate-700 dark:text-slate-300">
                        <div class="flex justify-between items-center bg-white/50 dark:bg-slate-900/50 p-2.5 rounded border border-slate-100 dark:border-slate-700/50">
                            <span>အရပ် မသတ်မှတ်သော မေတ္တာ</span>
                            <span class="font-bold font-mono">(၅ + ၇) × ၄ = ၄၈ သွယ်</span>
                        </div>
                        <div class="flex justify-between items-center bg-white/50 dark:bg-slate-900/50 p-2.5 rounded border border-slate-100 dark:border-slate-700/50">
                            <span>အရပ် (၁၀) မျက်နှာ ရည်စူးသော မေတ္တာ</span>
                            <span class="font-bold font-mono">၁၂ × ၁၀ × ၄ = ၄၈၀ သွယ်</span>
                        </div>
                        <div class="flex justify-between items-center bg-indigo-100 dark:bg-indigo-900/60 p-3 rounded border border-indigo-200 dark:border-indigo-800 font-bold text-indigo-900 dark:text-indigo-200 text-base mt-2 shadow-sm">
                            <span>စုစုပေါင်း မေတ္တာ</span>
                            <span class="font-mono">၅၂၈ သွယ်</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

file_path = "/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/metta_bhavana_guide.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Insert before "<!-- 11 Benefits -->"
target = "        <!-- 11 Benefits -->"
if target in content:
    content = content.replace(target, html_block + "\n" + target)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added 528 Metta section.")
else:
    print("Could not find the insertion point.")
