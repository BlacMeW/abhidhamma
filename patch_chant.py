import re

html_block = """
        <!-- The Chant of Metta -->
        <div class="glass-card rounded-3xl p-4 sm:p-6 md:p-10 border-t-4 border-t-violet-500 shadow-sm relative overflow-hidden max-w-5xl mx-auto mb-10">
            <div class="absolute -right-20 -top-20 text-9xl text-violet-500/5 dark:text-violet-500/10 pointer-events-none"><i class="fa-solid fa-om"></i></div>
            
            <div class="flex items-center justify-between mb-8 flex-wrap gap-4">
                <div>
                    <h3 class="text-2xl font-bold text-slate-800 dark:text-slate-100 flex items-center gap-3">
                        <i class="fa-solid fa-microphone-lines text-violet-500"></i> မေတ္တာပို့ ရွတ်စဉ် (The Chant of Mettā)
                    </h3>
                    <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mt-1">လက်တွေ့ မေတ္တာပွားများရာတွင် အစဉ်အလိုက် ရွတ်ဖတ်ပွားများရန် (၁၂) ဆင့်</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
                <!-- Verse 1 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၁)</span>
                        <span class="text-xs text-slate-400 font-medium">မိမိကိုယ်ကို အရင်ပို့ခြင်း</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Ahaṃ avero homi,<br>abyāpajjho homi,<br>anīgho homi,<br>sukhī-attānaṃ pariharāmi
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        ငါသည် ဘေးရန်ကင်းပါစေ၊ စိတ်ဆင်းရဲကင်းပါစေ၊ ကိုယ်ဆင်းရဲကင်းပါစေ၊ ချမ်းသာစွာဖြင့် မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ပါစေ။
                    </p>
                </div>

                <!-- Verse 2 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၂)</span>
                        <span class="text-xs text-slate-400 font-medium">ချစ်ခင်ရသူများ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Mama mātāpitu, ācariya ca, ñātimitta ca<br>averā hontu, abyāpajjhā hontu, anīghā hontu, sukhī-attānaṃ pariharantu
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        ငါ၏ မိဘ၊ ဆရာသမား၊ ဆွေမျိုး မိတ္တဆွေအပေါင်းတို့သည် ဘေးရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်းကြပါစေ၊ ချမ်းသာစွာ မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ကြပါစေ။
                    </p>
                </div>

                <!-- Verse 3 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၃)</span>
                        <span class="text-xs text-slate-400 font-medium">ကျောင်းတိုက်တွင်းရှိ ယောဂီများ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Imasmiṃ ārāme sabbe yogino<br>averā hontu, abyāpajjhā hontu, anīghā hontu, sukhī-attānaṃ pariharantu
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        ဤကျောင်းတိုက်အတွင်းရှိ ယောဂီသူတော်စင်အပေါင်းတို့သည် ဘေးရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်းကြပါစေ၊ ချမ်းသာစွာ မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ကြပါစေ။
                    </p>
                </div>

                <!-- Verse 4 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၄)</span>
                        <span class="text-xs text-slate-400 font-medium">အစောင့်အရှောက် နတ်ဒေဝါများ (အနီး)</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Amhākaṃ ārakkha devatā<br>Imasmiṃ āvāse, imasmiṃ ārāme<br>averā hontu, abyāpajjhā hontu, anīghā hontu, sukhī-attānaṃ pariharantu
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        ဤကျောင်းတိုက်၊ ဤနေရာကို စောင့်ရှောက်ကြကုန်သော အစောင့်အရှောက် နတ်ဒေဝါအပေါင်းတို့သည် ဘေးရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်းကြပါစေ၊ ချမ်းသာစွာ နေနိုင်ကြပါစေ။
                    </p>
                </div>

                <!-- Verse 5 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၅)</span>
                        <span class="text-xs text-slate-400 font-medium">အစောင့်အရှောက် နတ်ဒေဝါများ (အဝေး)</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Sabbe ārakkha devatā<br>averā hontu, abyāpajjhā hontu, anīghā hontu, sukhī-attānaṃ pariharantu
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အစောင့်အရှောက် နတ်ဒေဝါ အားလုံးတို့သည် ဘေးရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်းကြပါစေ၊ ချမ်းသာစွာ နေနိုင်ကြပါစေ။
                    </p>
                </div>

                <!-- Verse 6 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၆)</span>
                        <span class="text-xs text-slate-400 font-medium">၁၂ မျိုးသော သတ္တဝါများ</span>
                    </div>
                    <p class="text-[13px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Sabbe sattā, sabbe pāṇā, sabbe bhūtā<br>Sabbe puggalā, sabbe attabhāva-pariyāpannā<br>Sabbā itthiyo, sabbe purisā<br>Sabbe ariyā, sabbe anariyā<br>Sabbe devā, sabbe manussā, Sabbe vinipātikā<br>averā hontu... sukhī-attānaṃ pariharantu
                    </p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        သတ္တဝါ၊ ထွက်သက်ဝင်သက်ရှိသူ၊ ထင်ရှားဖြစ်သူ၊ ပုဂ္ဂိုလ်၊ ခန္ဓာကိုယ်အကျုံးဝင်သူ၊ မိန်းမ၊ ယောက်ျား၊ အရိယာ၊ ပုထုဇဉ်၊ နတ်ဗြဟ္မာ၊ လူ၊ အပါယ်လေးဘုံသား အားလုံးတို့သည် ဘေးရန်ကင်းကြပါစေ...
                    </p>
                </div>

                <!-- Verse 7 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၇)</span>
                        <span class="text-xs text-slate-400 font-medium">ကရုဏာ၊ မုဒိတာ နှင့် ကမ္မဿကတာ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Dukkhā muccantu<br>Yathā-laddha-sampattito māvigacchantu<br>Anāgataṃ lābhaṃ āgacchantu samicchantu<br>Kammassakā
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        သတ္တဝါအားလုံး ဆင်းရဲဒုက္ခမှ ကင်းဝေးကြပါစေ။ ရရှိပြီးသော ချမ်းသာစည်းစိမ်မှ မကင်းကွာကြပါစေနှင့်။ မရသေးသော ချမ်းသာကို ရရှိကြပါစေ။ သတ္တဝါအားလုံးသည် ကံသာလျှင် ကိုယ်ပိုင်ဥစ္စာ ရှိကြသည်။
                    </p>
                </div>

                <!-- Verse 8 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၈)</span>
                        <span class="text-xs text-slate-400 font-medium">ဒိသာဖရဏ (၁၀) မျက်နှာ</span>
                    </div>
                    <p class="text-[13px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Puratthimāya disāya, Pacchimāya disāya<br>Uttarāya disāya, Dakkhināya disāya<br>Puratthimāya anudisāya, Pacchimāya anudisāya<br>Uttarāya anudisāya, Dakkhināya anudisāya<br>Heṭṭhimāya disāya, Uparimāya disāya<br>Sabbe sattā... averā hontu...
                    </p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အရှေ့၊ အနောက်၊ မြောက်၊ တောင်၊ အရှေ့တောင်၊ အနောက်မြောက်၊ အရှေ့မြောက်၊ အနောက်တောင်၊ အောက်အရပ်၊ အထက်အရပ် (အရပ် ၁၀ မျက်နှာရှိ) သတ္တဝါအားလုံးတို့သည် ဘေးရန်ကင်းကြပါစေ...
                    </p>
                </div>

                <!-- Verse 9 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၉)</span>
                        <span class="text-xs text-slate-400 font-medium">ကရုဏာ၊ မုဒိတာ နှင့် ကမ္မဿကတာ (ထပ်မံ)</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Dukkhā muccantu<br>Yathā-laddha-sampattito māvigaccantu<br>Anāgataṃ lābhaṃ āgacchantu samicchantu<br>Kammassakā
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အရပ် ၁၀ မျက်နှာရှိ သတ္တဝါအားလုံး ဆင်းရဲဒုက္ခမှ ကင်းဝေးကြပါစေ။ ရရှိပြီးသော ချမ်းသာစည်းစိမ်မှ မကင်းကွာကြပါစေနှင့်။ မရသေးသော ချမ်းသာကို ရရှိကြပါစေ။ ကံသာလျှင် ကိုယ်ပိုင်ဥစ္စာ ရှိကြသည်။
                    </p>
                </div>

                <!-- Verse 10 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၁၀)</span>
                        <span class="text-xs text-slate-400 font-medium">မြေပြင်နေ သတ္တဝါများ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Uddhaṃ yāva bhavaggā ca, adho yāva aviccito<br>Samantā cakkavāḷesu, ye sattā paṭhavīcarā<br>abyāpajjhā niverā ca, nidukkhā ca nupaddavā
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အထက် ဘဝဂ်တိုင်အောင်၊ အောက် အဝီစိတိုင်အောင်၊ စကြဝဠာ အနန္တတဝိုက်ရှိ မြေပြင်၌ သွားလာနေထိုင်ကြသော သတ္တဝါအားလုံးတို့သည် ရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်း၍ ဘေးဥပဒ်ကင်းကြပါစေ။
                    </p>
                </div>

                <!-- Verse 11 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၁၁)</span>
                        <span class="text-xs text-slate-400 font-medium">ရေ၌နေ သတ္တဝါများ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Uddhaṃ yāva bhavaggā ca, adho yāva aviccito<br>Samantā cakkavāḷesu, ye sattā udakecarā<br>abyāpajjhā niverā ca, nidukkhā ca nupaddavā
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အထက် ဘဝဂ်တိုင်အောင်၊ အောက် အဝီစိတိုင်အောင်၊ စကြဝဠာ အနန္တတဝိုက်ရှိ ရေ၌ သွားလာနေထိုင်ကြသော သတ္တဝါအားလုံးတို့သည် ရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်း၍ ဘေးဥပဒ်ကင်းကြပါစေ။
                    </p>
                </div>

                <!-- Verse 12 -->
                <div class="bg-white/80 dark:bg-slate-800/80 p-5 rounded-2xl border border-violet-200/60 dark:border-violet-900/40 shadow-sm hover:shadow-md transition">
                    <div class="flex items-center justify-between mb-3">
                        <span class="px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-950/60 text-violet-800 dark:text-violet-300 font-bold text-xs border border-violet-300 dark:border-violet-800">အဆင့် (၁၂)</span>
                        <span class="text-xs text-slate-400 font-medium">ကောင်းကင်၌နေ သတ္တဝါများ</span>
                    </div>
                    <p class="text-[15px] font-bold text-violet-800 dark:text-violet-300 leading-relaxed mb-3">
                        Uddhaṃ yāva bhavaggā ca, adho yāva aviccito<br>Samantā cakkavāḷesu, ye sattā ākāsecarā<br>abyāpajjhā niverā ca, nidukkhā ca nupaddavā
                    </p>
                    <p class="text-sm text-slate-700 dark:text-slate-300 leading-relaxed pt-3 border-t border-slate-100 dark:border-slate-700/60">
                        အထက် ဘဝဂ်တိုင်အောင်၊ အောက် အဝီစိတိုင်အောင်၊ စကြဝဠာ အနန္တတဝိုက်ရှိ ကောင်းကင်၌ သွားလာနေထိုင်ကြသော သတ္တဝါအားလုံးတို့သည် ရန်ကင်းကြပါစေ၊ စိတ်ဆင်းရဲကင်းကြပါစေ၊ ကိုယ်ဆင်းရဲကင်း၍ ဘေးဥပဒ်ကင်းကြပါစေ။
                    </p>
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
    print("Successfully added The Chant of Metta section.")
else:
    print("Could not find the insertion point.")
