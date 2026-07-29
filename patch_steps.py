import re

file_path = "/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/metta_bhavana_guide.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Step 2 replacement
old_step_2 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ချစ်ခင်လေးစားရသူများ (Piya puggala)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            မိဘ၊ ဆရာသမား စသော မိမိ အလွန်ချစ်ခင် လေးစားရသူများကို အာရုံပြု၍ ပို့ပါ။ ဤအဆင့်တွင် မေတ္တာစစ် ဖြစ်ရန် အလွယ်ဆုံး ဖြစ်ပြီး၊ အပ္ပနာဈာန် (ဈာန် ၃ ပါး) အထိ ရရှိနိုင်သည်။
                        </p>
                        <div class="bg-amber-50 dark:bg-amber-900/20 p-3 rounded-lg border border-amber-200 dark:border-amber-800 text-xs text-amber-800 dark:text-amber-300">
                            <strong><i class="fa-solid fa-triangle-exclamation mr-1"></i> ရှေးဦးစွာ မပို့သင့်သူ (၄) မျိုး:</strong><br>
                            ၁။ မုန်းတီးသူ (ဒေါသဖြစ်မည်စိုး၍) ၂။ အလွန်ချစ်သူ (စိုးရိမ်သောက ဖြစ်မည်စိုး၍) ၃။ အလယ်အလတ်ပုဂ္ဂိုလ် (မေတ္တာဖြစ်ရန် ခဲယဉ်း၍) ၄။ ဆန့်ကျင်ဘက်လိင် (ရာဂဖြစ်မည်စိုး၍)။ <strong>မှတ်ချက်:</strong> သေဆုံးပြီးသူကို အာရုံပြု၍ မေတ္တာပို့ပါက ဥပစာရသမာဓိသာ ရနိုင်ပြီး ဈာန်မရနိုင်ပါ။
                        </div>
                    </div>"""

new_step_2 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ချစ်ခင်လေးစားရသူများ (Piya puggala)</h4>
                        <div class="mb-3 p-3 bg-rose-50 dark:bg-rose-900/30 rounded-lg text-sm font-medium text-slate-700 dark:text-slate-300">
                            "အယံ သပ္ပုရိသော အဝေရော ဟောတု၊ အဗျာပဇ္ဇော ဟောတု၊ အနီဃော ဟောတု၊ သုခီ အတ္တာနံ ပရိဟရတု"<br>
                            ဤကောင်းမြတ်သော ပုဂ္ဂိုလ်သည် ဘေးရန်ကင်းပါစေ၊ စိတ်ဆင်းရဲကင်းပါစေ၊ ကိုယ်ဆင်းရဲကင်းပါစေ၊ ချမ်းသာစွာဖြင့် မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ပါစေ။
                        </div>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            မိဘ၊ ဆရာသမား စသော မိမိ အလွန်ချစ်ခင် လေးစားရသူများကို အာရုံပြု၍ ပို့ပါ။ ဤအဆင့်တွင် မေတ္တာစစ် ဖြစ်ရန် အလွယ်ဆုံး ဖြစ်ပြီး၊ အပ္ပနာဈာန် (ဈာန် ၃ ပါး) အထိ ရရှိနိုင်သည်။
                        </p>
                        <div class="bg-amber-50 dark:bg-amber-900/20 p-3 rounded-lg border border-amber-200 dark:border-amber-800 text-xs text-amber-800 dark:text-amber-300">
                            <strong><i class="fa-solid fa-triangle-exclamation mr-1"></i> ရှေးဦးစွာ မပို့သင့်သူ (၄) မျိုး:</strong><br>
                            ၁။ မုန်းတီးသူ (ဒေါသဖြစ်မည်စိုး၍) ၂။ အလွန်ချစ်သူ (စိုးရိမ်သောက ဖြစ်မည်စိုး၍) ၃။ အလယ်အလတ်ပုဂ္ဂိုလ် (မေတ္တာဖြစ်ရန် ခဲယဉ်း၍) ၄။ ဆန့်ကျင်ဘက်လိင် (ရာဂဖြစ်မည်စိုး၍)။ <strong>မှတ်ချက်:</strong> သေဆုံးပြီးသူကို အာရုံပြု၍ မေတ္တာပို့ပါက ဥပစာရသမာဓိသာ ရနိုင်ပြီး ဈာန်မရနိုင်ပါ။
                        </div>
                    </div>"""

# Step 3 replacement
old_step_3 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ချစ်/မုန်း မရှိ အလယ်အလတ်ပုဂ္ဂိုလ် (Majjhatta puggala)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400">
                            ချစ်ခင်သူများကို ပို့၍ မေတ္တာအားကောင်းလာသောအခါ၊ မိမိနှင့် အထူးတလည် မရင်းနှီးသူ၊ မုန်းလည်းမမုန်း၊ ချစ်လည်းမချစ်သော အလယ်အလတ် ပုဂ္ဂိုလ်များကို အာရုံပြု၍ ပို့ပါ။
                        </p>
                    </div>"""

new_step_3 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ချစ်/မုန်း မရှိ အလယ်အလတ်ပုဂ္ဂိုလ် (Majjhatta puggala)</h4>
                        <div class="mb-3 p-3 bg-rose-50 dark:bg-rose-900/30 rounded-lg text-sm font-medium text-slate-700 dark:text-slate-300">
                            "အယံ မဇ္ဈတ္တပုဂ္ဂလော အဝေရော ဟောတု၊ အဗျာပဇ္ဇော ဟောတု၊ အနီဃော ဟောတု၊ သုခီ အတ္တာနံ ပရိဟရတု"<br>
                            ဤအလယ်အလတ် ပုဂ္ဂိုလ်သည် ဘေးရန်ကင်းပါစေ၊ စိတ်ဆင်းရဲကင်းပါစေ၊ ကိုယ်ဆင်းရဲကင်းပါစေ၊ ချမ်းသာစွာဖြင့် မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ပါစေ။
                        </div>
                        <p class="text-sm text-slate-600 dark:text-slate-400">
                            ချစ်ခင်သူများကို ပို့၍ မေတ္တာအားကောင်းလာသောအခါ၊ မိမိနှင့် အထူးတလည် မရင်းနှီးသူ၊ မုန်းလည်းမမုန်း၊ ချစ်လည်းမချစ်သော အလယ်အလတ် ပုဂ္ဂိုလ်များကို အာရုံပြု၍ ပို့ပါ။
                        </p>
                    </div>"""

# Step 4 replacement
old_step_4 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ရန်သူ / မုန်းတီးသူ (Verī puggala) နှင့် သီမသမ္ဘေဒ</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            နောက်ဆုံးတွင် မိမိအပေါ် မကောင်းကျင့်ဖူးသူ၊ မုန်းတီးသူများကိုပါ မေတ္တာ အာရုံပြုပါ။ ဒေါသဖြစ်လာလျှင် ဗုဒ္ဓ၏ အဆုံးအမများကို ဆင်ခြင်၍ ဒေါသကို ပယ်ဖျောက်ပါ။
                        </p>
                        <div class="bg-emerald-50 dark:bg-emerald-900/20 p-4 rounded-lg border border-emerald-200 dark:border-emerald-800">
                            <h5 class="font-bold text-emerald-800 dark:text-emerald-400 mb-1">သီမသမ္ဘေဒ (နယ်နိမိတ် ကျိုးပေါက်ခြင်း)</h5>
                            <p class="text-xs text-emerald-700 dark:text-emerald-300">
                                ထိုရန်သူ၊ မိမိကိုယ်တိုင်၊ ချစ်ခင်ရသူ၊ အလယ်အလတ်ပုဂ္ဂိုလ် ဤ (၄) ဦးအပေါ်၌ မည်သူ့ကို ပိုချစ်သည်ဟူ၍ ခွဲခြားမှု မရှိတော့ဘဲ၊ အားလုံးအပေါ် မေတ္တာထားနိုင်မှု <strong>အညီအမျှ</strong> ဖြစ်သွားသောအခါ "သီမသမ္ဘေဒ" ဖြစ်သည်ဟု ခေါ်သည်။ ထိုအချိန်တွင် အပ္ပနာဈာန် (ပထမ၊ ဒုတိယ၊ တတိယ ဈာန်) သို့ ရောက်ရှိနိုင်ပါသည်။ (ဥပေက္ခာဝေဒနာ ယှဉ်သော စတုတ္ထဈာန် မရနိုင်ပါ၊ မေတ္တာသည် သောမနဿဝေဒနာနှင့်သာ ယှဉ်သောကြောင့် ဖြစ်သည်)။
                            </p>
                        </div>
                    </div>"""

new_step_4 = """                    <div class="bg-white/60 dark:bg-slate-800/60 p-4 sm:p-5 rounded-xl border border-slate-200 dark:border-slate-700 flex-1 shadow-sm">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 text-lg mb-2">ရန်သူ / မုန်းတီးသူ (Verī puggala) နှင့် သီမသမ္ဘေဒ</h4>
                        <div class="mb-3 p-3 bg-rose-50 dark:bg-rose-900/30 rounded-lg text-sm font-medium text-slate-700 dark:text-slate-300">
                            "အယံ ဝေရီပုဂ္ဂလော အဝေရော ဟောတု၊ အဗျာပဇ္ဇော ဟောတု၊ အနီဃော ဟောတု၊ သုခီ အတ္တာနံ ပရိဟရတု"<br>
                            ဤရန်သူပုဂ္ဂိုလ်သည် ဘေးရန်ကင်းပါစေ၊ စိတ်ဆင်းရဲကင်းပါစေ၊ ကိုယ်ဆင်းရဲကင်းပါစေ၊ ချမ်းသာစွာဖြင့် မိမိခန္ဓာဝန်ကို ရွက်ဆောင်နိုင်ပါစေ။
                        </div>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">
                            နောက်ဆုံးတွင် မိမိအပေါ် မကောင်းကျင့်ဖူးသူ၊ မုန်းတီးသူများကိုပါ မေတ္တာ အာရုံပြုပါ။ အကယ်၍ ဒေါသဖြစ်လာလျှင် အောက်ပါ ဝိသုဒ္ဓိမဂ်လာ နည်းလမ်းများဖြင့် ဒေါသကို ပယ်ဖျောက်ပါ။
                        </p>
                        
                        <details class="mb-5 group">
                            <summary class="text-sm font-bold text-rose-600 dark:text-rose-400 cursor-pointer flex items-center gap-2 select-none hover:text-rose-700 dark:hover:text-rose-300 bg-rose-50 dark:bg-rose-900/20 px-3 py-2.5 rounded-lg border border-rose-200 dark:border-rose-800 transition">
                                <i class="fa-solid fa-fire-extinguisher"></i> ဒေါသကို ပယ်ဖျောက်နည်း (၉) မျိုး (ဝိသုဒ္ဓိမဂ်)
                            </summary>
                            <div class="mt-2 p-4 bg-white dark:bg-slate-900/50 rounded-lg text-sm text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 border-l-4 border-l-rose-500 space-y-3 leading-relaxed shadow-sm">
                                <p>၁။ <strong>ကကစူပမသုတ် ဆင်ခြင်ခြင်း:</strong> "လွှဖြင့် တိုက်ဖြတ်ခံရလျှင်ပင် ဒေါသမထွက်ရ" ဟူသော ဘုရားရှင်၏ အဆုံးအမကို သတိရပါ။</p>
                                <p>၂။ <strong>ကောင်းကွက်ကို ရှာခြင်း:</strong> ရန်သူ၏ ကိုယ်အမူအရာ၊ နှုတ်အမူအရာ၊ စိတ်နေသဘောထား (၃) မျိုးအနက်မှ ကောင်းကွက် တစ်ခုခုကို ရှာဖွေ အာရုံပြုပါ။</p>
                                <p>၃။ <strong>ကိုယ့်ကိုယ်ကို ဆုံးမခြင်း:</strong> "သူက နင့်ကို စိတ်ဆင်းရဲအောင်လုပ်တာ၊ နင်က ဘာလို့ ဒေါသထွက်ပြီး ကိုယ့်ကိုယ်ကို ထပ်ဆင်းရဲအောင် လုပ်နေတာလဲ" ဟု ဆုံးမပါ။</p>
                                <p>၄။ <strong>ကမ္မဿကတာ ဆင်ခြင်ခြင်း:</strong> "မိမိ၏ ဒေါသကံသည် မိမိ၏ အမွေသာဖြစ်၍ အပါယ်သို့ ကျစေမည်။ သူ၏ မကောင်းမှုကံသည် သူ၏ အမွေသာဖြစ်သည်" ဟု ကံကိုသာ ပိုင်ဆိုင်ကြောင်း ဆင်ခြင်ပါ။</p>
                                <p>၅။ <strong>ဘုရားရှင်၏ ကျင့်စဉ်ကို သတိရခြင်း:</strong> အလောင်းတော်ဘဝက ရန်သူများအပေါ်၌ပင် သည်းခံခဲ့ပုံ၊ မေတ္တာထားခဲ့ပုံ အတ္ထုပ္ပတ္တိများကို ပြန်လည် အောက်မေ့ပါ။</p>
                                <p>၆။ <strong>သံသရာ၏ ရှည်လျားပုံကို ဆင်ခြင်ခြင်း:</strong> "အစမထင် သံသရာတစ်ကွေ့တွင် ဤသူသည် ငါ၏ အမိ၊ အဖ၊ ညီအစ်ကို မောင်နှမ မဖြစ်ခဲ့ဖူးသူဟူ၍ မရှိ" ဟု ဆင်ခြင်ပါ။</p>
                                <p>၇။ <strong>မေတ္တာအကျိုး (၁၁) ပါးကို ဆင်ခြင်ခြင်း:</strong> ဒေါသထွက်နေပါက မေတ္တာ၏ အကျိုးကျေးဇူးများကို ဆုံးရှုံးရမည်ဟု သတိပြုပါ။</p>
                                <p>၈။ <strong>ဓာတ်ခွဲ၍ ဆင်ခြင်ခြင်း:</strong> "သူ၏ ဆံပင်ကို စိတ်ဆိုးသလား၊ အသားကို စိတ်ဆိုးသလား၊ ရုပ်တရားကို စိတ်ဆိုးသလား" ဟု ဓာတ်သဘောသက်သက် ခွဲခြမ်းစိတ်ဖြာလိုက်လျှင် စိတ်ဆိုးစရာ ပုဂ္ဂိုလ် မတွေ့ရတော့ပါ။</p>
                                <p>၉။ <strong>လက်ဆောင်ပေးခြင်း:</strong> အထက်ပါနည်းများဖြင့် မရပါက၊ ထိုသူအား မိမိပိုင်ဆိုင်သော ပစ္စည်းတစ်ခုခုကို ပေးကမ်းလိုက်ပါ။ (ဒါနဖြင့် ဒေါသကို ဖြိုခွဲခြင်း)</p>
                            </div>
                        </details>

                        <div class="bg-emerald-50 dark:bg-emerald-900/20 p-4 rounded-lg border border-emerald-200 dark:border-emerald-800">
                            <h5 class="font-bold text-emerald-800 dark:text-emerald-400 mb-1">သီမသမ္ဘေဒ (နယ်နိမိတ် ကျိုးပေါက်ခြင်း)</h5>
                            <p class="text-xs text-emerald-700 dark:text-emerald-300">
                                ထိုရန်သူ၊ မိမိကိုယ်တိုင်၊ ချစ်ခင်ရသူ၊ အလယ်အလတ်ပုဂ္ဂိုလ် ဤ (၄) ဦးအပေါ်၌ မည်သူ့ကို ပိုချစ်သည်ဟူ၍ ခွဲခြားမှု မရှိတော့ဘဲ၊ အားလုံးအပေါ် မေတ္တာထားနိုင်မှု <strong>အညီအမျှ</strong> ဖြစ်သွားသောအခါ "သီမသမ္ဘေဒ" ဖြစ်သည်ဟု ခေါ်သည်။ ထိုအချိန်တွင် အပ္ပနာဈာန် (ပထမ၊ ဒုတိယ၊ တတိယ ဈာန်) သို့ ရောက်ရှိနိုင်ပါသည်။ (ဥပေက္ခာဝေဒနာ ယှဉ်သော စတုတ္ထဈာန် မရနိုင်ပါ၊ မေတ္တာသည် သောမနဿဝေဒနာနှင့်သာ ယှဉ်သောကြောင့် ဖြစ်သည်)။
                            </p>
                        </div>
                    </div>"""

if old_step_2 in content and old_step_3 in content and old_step_4 in content:
    content = content.replace(old_step_2, new_step_2)
    content = content.replace(old_step_3, new_step_3)
    content = content.replace(old_step_4, new_step_4)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched steps 2, 3, 4.")
else:
    print("Failed to find exact strings.")
