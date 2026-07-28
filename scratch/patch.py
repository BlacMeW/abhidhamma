import sys

html_file = "/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/satipatthana_guide.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We will use re.sub or exact string replacement for each pabba

nivarana_old = """<!-- 1. Nivarana -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-cloud-showers-heavy text-slate-500 text-xl"></i>
<h4 class="font-bold text-emerald-700 dark:text-emerald-400 text-base sm:text-lg">၁။ နီဝရဏ ပဗ္ဗ (အဆီးအတား ၅ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-3">စိတ်၏ တည်ကြည်မှုနှင့် ပညာကို တားဆီးတတ်သော တရား ၅ ပါး မိမိသန္တာန်၌ ရှိ/မရှိ သိခြင်း၊ ဖြစ်ပေါ်ကြောင်းနှင့် ပယ်နိုင်ကြောင်းကို သိခြင်း -</p>
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400">
<div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
<strong class="text-slate-800 dark:text-slate-200 block">၁။ ကာမစ္ဆန္ဒ:</strong> ကာမဂုဏ်ကို လိုချင်တပ်မက်မှု ရှိ/မရှိ သိ၏။ (အသုဘနိမိတ်ဖြင့် ပယ်၏)
                            </div>
<div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
<strong class="text-slate-800 dark:text-slate-200 block">၂။ ဗျာပါဒ:</strong> အမျက်ထွက်မှု၊ ဖျက်ဆီးလိုမှု ရှိ/မရှိ သိ၏။ (မေတ္တာဘာဝနာဖြင့် ပယ်၏)
                            </div>
<div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
<strong class="text-slate-800 dark:text-slate-200 block">၃။ ထိနမိဒ္ဓ:</strong> စိတ်/စေတသိက် ထိုင်းမှိုင်းမှု ရှိ/မရှိ သိ၏။ (ဝီရိယပွား၍ ပယ်၏)
                            </div>
<div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
<strong class="text-slate-800 dark:text-slate-200 block">၄။ ဥဒ္ဓစ္စကုက္ကုစ္စ:</strong> စိတ်ပျံ့လွင့်မှု နှင့် နောင်တတပူပန်ဖြစ်မှု ရှိ/မရှိ သိ၏။ (သမထသမာဓိဖြင့် ပယ်၏)
                            </div>
<div class="bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200/60 dark:border-slate-700/60 sm:col-span-2 md:col-span-1">
<strong class="text-slate-800 dark:text-slate-200 block">၅။ ဝိစိကိစ္ဆာ:</strong> ဘုရား၊ တရား၊ သံဃာ၊ ကံတို့အပေါ် ယုံမှားသံသယဖြစ်မှု ရှိ/မရှိ သိ၏။ (ဓမ္မဆင်ခြင်မှုဖြင့် ပယ်၏)
                            </div>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
                        ကာမစ္ဆန္ဒ (ကာမဂုဏ်ကို လိုလားခြင်း)၊ ဗျာပါဒ (ဖျက်ဆီးလိုခြင်း၊ စိတ်ဆိုးခြင်း)၊ ထိနမိဒ္ဓ (ငိုက်မျဉ်းခြင်း၊ ပျင်းရိခြင်း)၊ ဥဒ္ဓစ္စကုက္ကုစ္စ (ပျံ့လွင့်ခြင်းနှင့် နောင်တပူပန်ခြင်း)၊ ဝိစိကိစ္ဆာ (ယုံမှားသံသယဖြစ်ခြင်း) ဟူသော နီဝရဏ ၅ ပါးတို့သည် မိမိသန္တာန်၌ ရှိလျှင် ရှိသည်ဟု သိပါ၊ မရှိလျှင် မရှိဟု သိပါ။ မဖြစ်ပေါ်သေးသော နီဝရဏ ဖြစ်ပေါ်လာကြောင်းကိုလည်းကောင်း၊ ဖြစ်ပေါ်ပြီးသော နီဝရဏ ပယ်ပျောက်သွားကြောင်းကိုလည်းကောင်း၊ ပယ်ပြီးသော နီဝရဏ နောင်တဖန် ပြန်မလာတော့ကြောင်းကိုလည်းကောင်း ဉာဏ်ဖြင့် ထိုးထွင်း၍ ရှုမှတ်ပါ။ ဤတရားတို့သည် ကုသိုလ်တရားတို့ကို တားဆီးပိတ်ပင်တတ်သော အနှောင့်အယှက်များ ဖြစ်ကြောင်းကို အဖန်ဖန် ဆင်ခြင်ပါ။
                    </div>
</details>
</div>"""

nivarana_new = """<!-- 1. Nivarana -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm border-l-4 border-l-slate-400">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-cloud-showers-heavy text-slate-500 text-xl"></i>
<h4 class="font-bold text-slate-700 dark:text-slate-400 text-base sm:text-lg">၁။ နီဝရဏ ပဗ္ဗ (အဆီးအတား ၅ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-4">
    စိတ်၏ တည်ကြည်မှုနှင့် ပညာကို တားဆီးတတ်သော တရား ၅ ပါး မိမိသန္တာန်၌ ရှိ/မရှိ သိခြင်း၊ ဖြစ်ပေါ်ကြောင်းနှင့် ပယ်နိုင်ကြောင်းကို သိခြင်း -
</p>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-5">
    <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60 flex flex-col items-center text-center">
        <i class="fa-solid fa-heart text-rose-500 mb-2 text-lg"></i>
        <strong class="text-slate-800 dark:text-slate-200 block mb-1">၁။ ကာမစ္ဆန္ဒ</strong>
        <span class="text-xs">ကာမဂုဏ်ကို လိုချင်တပ်မက်မှု</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60 flex flex-col items-center text-center">
        <i class="fa-solid fa-fire text-orange-500 mb-2 text-lg"></i>
        <strong class="text-slate-800 dark:text-slate-200 block mb-1">၂။ ဗျာပါဒ</strong>
        <span class="text-xs">အမျက်ထွက်မှု၊ ဖျက်ဆီးလိုမှု</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60 flex flex-col items-center text-center">
        <i class="fa-solid fa-bed text-blue-400 mb-2 text-lg"></i>
        <strong class="text-slate-800 dark:text-slate-200 block mb-1">၃။ ထိနမိဒ္ဓ</strong>
        <span class="text-xs">စိတ်/စေတသိက် ထိုင်းမှိုင်းမှု</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60 flex flex-col items-center text-center">
        <i class="fa-solid fa-wind text-teal-500 mb-2 text-lg"></i>
        <strong class="text-slate-800 dark:text-slate-200 block mb-1">၄။ ဥဒ္ဓစ္စကုက္ကုစ္စ</strong>
        <span class="text-xs">စိတ်ပျံ့လွင့်မှု၊ နောင်တပူပန်မှု</span>
    </div>
    <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60 flex flex-col items-center text-center md:col-span-2 lg:col-span-1">
        <i class="fa-solid fa-circle-question text-purple-500 mb-2 text-lg"></i>
        <strong class="text-slate-800 dark:text-slate-200 block mb-1">၅။ ဝိစိကိစ္ဆာ</strong>
        <span class="text-xs">ယုံမှားသံသယဖြစ်မှု</span>
    </div>
</div>

<div class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border border-slate-200 dark:border-slate-700/60">
    <h5 class="font-bold text-slate-800 dark:text-slate-300 text-xs sm:text-sm mb-3">နီဝရဏ ရှုမှတ်မှု (၃) ဆင့်</h5>
    <ul class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-2 list-decimal pl-4">
        <li><b class="text-slate-900 dark:text-slate-200">ရှိ/မရှိ သိခြင်း:</b> မိမိသန္တာန်၌ နီဝရဏတစ်ခုခု ရှိလျှင် "ရှိသည်" ဟု သိ၏။ မရှိလျှင် "မရှိ" ဟု သိ၏။ (ဥပမာ- ထိုင်းမှိုင်းလာလျှင် ထိုင်းမှိုင်းနေကြောင်း သိမှတ်ပါ)။</li>
        <li><b class="text-slate-900 dark:text-slate-200">ဖြစ်ပေါ်ကြောင်းကို သိခြင်း:</b> မဖြစ်သေးသော နီဝရဏသည် မည်သည့်အကြောင်းကြောင့် ဖြစ်ပေါ်လာသည်ကို ဉာဏ်ဖြင့် သိ၏။ (အယောနိသော မနသိကာရ ကြောင့် ဖြစ်သည်)။</li>
        <li><b class="text-slate-900 dark:text-slate-200">ပယ်နိုင်ကြောင်းကို သိခြင်း:</b> ဖြစ်ပေါ်ပြီးသော နီဝရဏကို မည်သို့ပယ်ရမည်၊ ပယ်ပြီးသော နီဝရဏ နောင်တဖန် ပြန်မဖြစ်အောင် မည်သို့နေထိုင်ရမည်ကို ဉာဏ်ဖြင့် သိ၏။</li>
    </ul>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
    ကာမစ္ဆန္ဒ (ကာမဂုဏ်ကို လိုလားခြင်း)၊ ဗျာပါဒ (ဖျက်ဆီးလိုခြင်း၊ စိတ်ဆိုးခြင်း)၊ ထိနမိဒ္ဓ (ငိုက်မျဉ်းခြင်း၊ ပျင်းရိခြင်း)၊ ဥဒ္ဓစ္စကုက္ကုစ္စ (ပျံ့လွင့်ခြင်းနှင့် နောင်တပူပန်ခြင်း)၊ ဝိစိကိစ္ဆာ (ယုံမှားသံသယဖြစ်ခြင်း) ဟူသော နီဝရဏ ၅ ပါးတို့သည် မိမိသန္တာန်၌ ရှိလျှင် ရှိသည်ဟု သိပါ၊ မရှိလျှင် မရှိဟု သိပါ။ မဖြစ်ပေါ်သေးသော နီဝရဏ ဖြစ်ပေါ်လာကြောင်းကိုလည်းကောင်း၊ ဖြစ်ပေါ်ပြီးသော နီဝရဏ ပယ်ပျောက်သွားကြောင်းကိုလည်းကောင်း၊ ပယ်ပြီးသော နီဝရဏ နောင်တဖန် ပြန်မလာတော့ကြောင်းကိုလည်းကောင်း ဉာဏ်ဖြင့် ထိုးထွင်း၍ ရှုမှတ်ပါ။ ဤတရားတို့သည် ကုသိုလ်တရားတို့ကို တားဆီးပိတ်ပင်တတ်သော အနှောင့်အယှက်များ ဖြစ်ကြောင်းကို အဖန်ဖန် ဆင်ခြင်ပါ။
</div>
</details>
</div>"""

content = content.replace(nivarana_old, nivarana_new)

khandha_old = """<!-- 2. Khandha -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-cubes text-emerald-500 text-xl"></i>
<h4 class="font-bold text-emerald-700 dark:text-emerald-400 text-base sm:text-lg">၂။ ခန္ဓ ပဗ္ဗ (ဥပါဒါနက္ခန္ဓာ ၅ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-3">ရုပ်၊ ဝေဒနာ (ခံစားမှု)၊ သညာ (မှတ်သားမှု)၊ သင်္ခါရ (ပြုပြင်အားထုတ်မှု)၊ ဝိညာဏ် (သိမှု) တို့၏ ဖြစ်ခြင်း၊ တည်ခြင်း၊ ပျက်ခြင်း (ဥဒယဗ္ဗယ) သဘောများကို အဖန်ဖန် ဆင်ခြင်သိမြင်ခြင်း -</p>
<div class="bg-emerald-50/50 dark:bg-slate-900/50 p-4 rounded-xl border border-emerald-100 dark:border-slate-700/60 text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-300">
                            "ဣတိ ရူပံ၊ ဣတိ ရူပဿ သမုဒယော၊ ဣတိ ရူပဿ အတ္ထင်္ဂမော..." - 'ဤကား ရုပ်တည်း၊ ဤကား ရုပ်၏ ဖြစ်ပေါ်ခြင်းတည်း၊ ဤကား ရုပ်၏ ချုပ်ငြိမ်းခြင်းတည်း' ဟု ခန္ဓာ (၅) ပါးလုံးအပေါ် အရှိအတိုင်း ဉာဏ်ဖြင့် ထိုးထွင်းသိမြင်ခြင်း။
                        </div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
                        ရူပက္ခန္ဓာ (ရုပ်တရား)၊ ဝေဒနာက္ခန္ဓာ (ခံစားမှု)၊ သညာက္ခန္ဓာ (မှတ်သားမှု)၊ သင်္ခါရက္ခန္ဓာ (စေ့ဆော်ပြုလုပ်မှု)၊ ဝိညာဏက္ခန္ဓာ (သိမှု) ဟူသော ခန္ဓာငါးပါးတို့၏ အဖြစ်အပျက်ကို အမြဲတစေ ရှုမှတ်ပါ။ 'ဤကား ရုပ်၊ ဤကား ရုပ်၏ ဖြစ်ပေါ်ခြင်း၊ ဤကား ရုပ်၏ ချုပ်ငြိမ်းခြင်း' ဟူ၍ ခန္ဓာတစ်ပါးစီတိုင်းကို ဉာဏ်ဖြင့် ခွဲခြမ်းစိတ်ဖြာ၍ ဆင်ခြင်ပါ။ ငါ၊ သူတစ်ပါး ဟူ၍ မရှိ၊ ခန္ဓာငါးပါးသာ အကြောင်းတိုက်ဆိုင်၍ ဖြစ်ပေါ်လာပြီး အကြောင်းကင်းလျှင် ချုပ်ငြိမ်းသွားကြောင်းကို ပိုင်းခြားသိမြင်အောင် အားထုတ်ပါ။
                    </div>
</details>
</div>"""

khandha_new = """<!-- 2. Khandha -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm border-l-4 border-l-emerald-500">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-cubes text-emerald-500 text-xl"></i>
<h4 class="font-bold text-emerald-700 dark:text-emerald-400 text-base sm:text-lg">၂။ ခန္ဓ ပဗ္ဗ (ဥပါဒါနက္ခန္ဓာ ၅ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-4">
    ရုပ်၊ ဝေဒနာ (ခံစားမှု)၊ သညာ (မှတ်သားမှု)၊ သင်္ခါရ (ပြုပြင်အားထုတ်မှု)၊ ဝိညာဏ် (သိမှု) တို့၏ ဖြစ်ခြင်း နှင့် ပျက်ခြင်း သဘောများကို အဖန်ဖန် ဆင်ခြင်သိမြင်ခြင်း -
</p>

<div class="grid grid-cols-2 md:grid-cols-5 gap-3 text-xs mb-5">
    <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-200/50 dark:border-emerald-800/40 text-center">
        <i class="fa-solid fa-child-reaching text-emerald-600 mb-1.5 text-lg"></i>
        <strong class="text-emerald-800 dark:text-emerald-300 block">ရူပက္ခန္ဓာ</strong>
        <span class="text-[10px] text-slate-500">ဖောက်ပြန်တတ်သော သဘောတရား</span>
    </div>
    <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-200/50 dark:border-emerald-800/40 text-center">
        <i class="fa-solid fa-heart-crack text-emerald-600 mb-1.5 text-lg"></i>
        <strong class="text-emerald-800 dark:text-emerald-300 block">ဝေဒနာက္ခန္ဓာ</strong>
        <span class="text-[10px] text-slate-500">ခံစားတတ်သော သဘောတရား</span>
    </div>
    <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-200/50 dark:border-emerald-800/40 text-center">
        <i class="fa-solid fa-brain text-emerald-600 mb-1.5 text-lg"></i>
        <strong class="text-emerald-800 dark:text-emerald-300 block">သညာက္ခန္ဓာ</strong>
        <span class="text-[10px] text-slate-500">မှတ်သားတတ်သော သဘောတရား</span>
    </div>
    <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-200/50 dark:border-emerald-800/40 text-center">
        <i class="fa-solid fa-gears text-emerald-600 mb-1.5 text-lg"></i>
        <strong class="text-emerald-800 dark:text-emerald-300 block">သင်္ခါရက္ခန္ဓာ</strong>
        <span class="text-[10px] text-slate-500">ပြုပြင်စီရင်တတ်သော သဘောတရား</span>
    </div>
    <div class="bg-emerald-50/50 dark:bg-emerald-950/20 p-3 rounded-xl border border-emerald-200/50 dark:border-emerald-800/40 text-center col-span-2 md:col-span-1">
        <i class="fa-regular fa-lightbulb text-emerald-600 mb-1.5 text-lg"></i>
        <strong class="text-emerald-800 dark:text-emerald-300 block">ဝိညာဏက္ခန္ဓာ</strong>
        <span class="text-[10px] text-slate-500">အာရုံကို သိတတ်သော သဘောတရား</span>
    </div>
</div>

<div class="bg-emerald-50/50 dark:bg-slate-900/50 p-4 rounded-xl border border-emerald-100 dark:border-slate-700/60 mb-4">
    <h5 class="font-bold text-emerald-800 dark:text-emerald-400 text-xs sm:text-sm mb-2">ခန္ဓာ (၅) ပါး ဖြစ်/ပျက် ရှုမှတ်ပုံ</h5>
    <p class="text-[11px] sm:text-xs text-slate-700 dark:text-slate-300 italic mb-2">
        "ဣတိ ရူပံ၊ ဣတိ ရူပဿ သမုဒယော၊ ဣတိ ရူပဿ အတ္ထင်္ဂမော..."
    </p>
    <ul class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-1.5 list-disc pl-4">
        <li><strong>ခန္ဓာကို ပိုင်းခြားသိခြင်း (ဣတိ ရူပံ):</strong> ဤကား ရုပ်တရားတည်း၊ နာမ်တရားတည်း ဟု အရှိအတိုင်း သိခြင်း။</li>
        <li><strong>ဖြစ်ပေါ်ခြင်းကို သိခြင်း (သမုဒယော):</strong> အကြောင်းတိုက်ဆိုင်၍ ဤရုပ်/နာမ် ဖြစ်ပေါ်လာပုံကို ဉာဏ်ဖြင့် သိခြင်း။</li>
        <li><strong>ချုပ်ငြိမ်းခြင်းကို သိခြင်း (အတ္ထင်္ဂမော):</strong> အကြောင်းကင်း၍ ဤရုပ်/နာမ် ချုပ်ငြိမ်းပျက်စီးသွားပုံကို ဉာဏ်ဖြင့် သိခြင်း။</li>
    </ul>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
    ရူပက္ခန္ဓာ (ရုပ်တရား)၊ ဝေဒနာက္ခန္ဓာ (ခံစားမှု)၊ သညာက္ခန္ဓာ (မှတ်သားမှု)၊ သင်္ခါရက္ခန္ဓာ (စေ့ဆော်ပြုလုပ်မှု)၊ ဝိညာဏက္ခန္ဓာ (သိမှု) ဟူသော ခန္ဓာငါးပါးတို့၏ အဖြစ်အပျက်ကို အမြဲတစေ ရှုမှတ်ပါ။ 'ဤကား ရုပ်၊ ဤကား ရုပ်၏ ဖြစ်ပေါ်ခြင်း၊ ဤကား ရုပ်၏ ချုပ်ငြိမ်းခြင်း' ဟူ၍ ခန္ဓာတစ်ပါးစီတိုင်းကို ဉာဏ်ဖြင့် ခွဲခြမ်းစိတ်ဖြာ၍ ဆင်ခြင်ပါ။ ငါ၊ သူတစ်ပါး ဟူ၍ မရှိ၊ ခန္ဓာငါးပါးသာ အကြောင်းတိုက်ဆိုင်၍ ဖြစ်ပေါ်လာပြီး အကြောင်းကင်းလျှင် ချုပ်ငြိမ်းသွားကြောင်းကို ပိုင်းခြားသိမြင်အောင် အားထုတ်ပါ။
</div>
</details>
</div>"""

content = content.replace(khandha_old, khandha_new)

ayatana_old = """<!-- 3. Ayatana -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-link text-emerald-500 text-xl"></i>
<h4 class="font-bold text-emerald-700 dark:text-emerald-400 text-base sm:text-lg">၃။ အာယတန ပဗ္ဗ (အာယတန ၁၂ ပါး နှင့် သံယောဇဉ်)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-3">အတွင်း အာယတန ၆ ပါး (မျက်စိ၊ နား၊ နှာခေါင်း၊ လျှာ၊ ကိုယ်၊ စိတ်) နှင့် အပြင် အာယတန ၆ ပါး (အဆင်း၊ အသံ၊ အနံ့၊ အရသာ၊ အတွေ့အထိ၊ ဓမ္မာရုံ) တို့ တိုက်မိကြရာမှ သံယောဇဉ် (တွယ်တာနှောင်ကြိုး) များ ဖြစ်ပေါ်လာပုံ၊ ပယ်သတ်ပုံတို့ကို ထိုးထွင်းသိမြင်ခြင်း။</p>
<div class="text-[11px] sm:text-xs bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl text-slate-600 dark:text-slate-400 font-medium">
                            ဆင်ခြင်နည်း - မျက်စိနှင့် အဆင်းတိုက်သည့်အခါ မြင်ရုံသက်သက်ဖြင့် ရပ်တန့်ကာ လိုချင်တပ်မက်မှု သံယောဇဉ် (၁၀) ပါး မဖြစ်ပေါ်အောင် သတိဖြင့် ထိန်းသိမ်း ရှုမှတ်ပါ။
                        </div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
                        မျက်စိ (စက္ခု) နှင့် အဆင်း (ရူပ)၊ နား (သောတ) နှင့် အသံ (သဒ္ဒ)၊ နှာခေါင်း (ဃာန) နှင့် အနံ့ (ဂန္ဓ)၊ လျှာ (ဇိဝှာ) နှင့် အရသာ (ရသ)၊ ကိုယ် (ကာယ) နှင့် အတွေ့အထိ (ဖောဋ္ဌဗ္ဗ)၊ စိတ် (မန) နှင့် သဘောတရား (ဓမ္မ) ဟူသော အတွင်း အပြင် အာယတန (၁၂) ပါးတို့ကို သိပါ။ ထိုမျက်စိနှင့် အဆင်းကို အကြောင်းပြု၍ ဖြစ်ပေါ်လာသော သံယောဇဉ် (တပ်မက်ခြင်း၊ ငြိတွယ်ခြင်း) ကိုလည်း သိပါ။ ထိုသံယောဇဉ်တို့ မည်သို့ ဖြစ်ပေါ်လာသည်၊ ဖြစ်ပေါ်ပြီးနောက် မည်သို့ ပယ်ဖျောက်ရသည်၊ ပယ်ပြီးနောက် နောင်တစ်ဖန် ပြန်မဖြစ်ပေါ်အောင် မည်သို့ လုပ်ရမည်ကို ဉာဏ်ဖြင့် စူးစိုက်ဆင်ခြင်ပါ။
                    </div>
</details>
</div>"""

ayatana_new = """<!-- 3. Ayatana -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm border-l-4 border-l-indigo-500">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-link text-indigo-500 text-xl"></i>
<h4 class="font-bold text-indigo-700 dark:text-indigo-400 text-base sm:text-lg">၃။ အာယတန ပဗ္ဗ (အာယတန ၁၂ ပါး နှင့် သံယောဇဉ်)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-4">
    အတွင်း အာယတန ၆ ပါး နှင့် အပြင် အာယတန ၆ ပါး တို့ တိုက်မိကြရာမှ သံယောဇဉ် (တွယ်တာနှောင်ကြိုး ၁၀ ပါး) များ ဖြစ်ပေါ်လာပုံ၊ ပယ်သတ်ပုံတို့ကို ထိုးထွင်းသိမြင်ရန် ဖြစ်သည်။
</p>

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
    <div class="bg-indigo-50/50 dark:bg-indigo-950/20 p-4 rounded-xl border border-indigo-200/50 dark:border-indigo-800/40">
        <h5 class="font-bold text-indigo-800 dark:text-indigo-300 text-xs sm:text-sm mb-3">အာယတန တိုက်ဆိုင်မှု (၆) တွဲ</h5>
        <ul class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-2">
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">စက္ခု (မျက်စိ)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">ရူပ (အဆင်း)</span></li>
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">သောတ (နား)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">သဒ္ဒ (အသံ)</span></li>
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">ဃာန (နှာခေါင်း)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">ဂန္ဓ (အနံ့)</span></li>
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">ဇိဝှာ (လျှာ)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">ရသ (အရသာ)</span></li>
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">ကာယ (ကိုယ်)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">ဖောဋ္ဌဗ္ဗ (အတွေ့အထိ)</span></li>
            <li class="flex items-center justify-between"><span class="bg-indigo-100 dark:bg-indigo-900/50 px-2 py-0.5 rounded font-medium text-indigo-800 dark:text-indigo-300">မန (စိတ်)</span> <i class="fa-solid fa-arrow-right-arrow-left text-slate-400 mx-2"></i> <span class="bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">ဓမ္မ (သဘောတရား)</span></li>
        </ul>
    </div>
    
    <div class="bg-rose-50/50 dark:bg-rose-950/20 p-4 rounded-xl border border-rose-200/50 dark:border-rose-800/40">
        <h5 class="font-bold text-rose-800 dark:text-rose-300 text-xs sm:text-sm mb-3">သံယောဇဉ် ဖြစ်ပေါ်/ပယ်ဖျောက်ပုံ (၃ အဆင့်)</h5>
        <ul class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-3 list-decimal pl-4">
            <li><b class="text-rose-900 dark:text-rose-200">အာယတနကို သိခြင်း:</b> မျက်စိ၊ နား စသည်တို့ကိုလည်းကောင်း၊ အဆင်း၊ အသံ စသည်တို့ကိုလည်းကောင်း အရှိအတိုင်း သိ၏။</li>
            <li><b class="text-rose-900 dark:text-rose-200">သံယောဇဉ်ကို သိခြင်း:</b> ဒွါရ နှင့် အာရုံ တိုက်မိရာမှ လိုချင်မှု (သို့) မလိုချင်မှု ဟူသော သံယောဇဉ် ဖြစ်ပေါ်လာလျှင် ဉာဏ်ဖြင့် သိ၏။</li>
            <li><b class="text-rose-900 dark:text-rose-200">ပယ်ဖျောက်ကြောင်းကို သိခြင်း:</b> ထိုသံယောဇဉ်ကို မည်သို့ပယ်ဖျောက်ရမည်၊ ပယ်ပြီးသော သံယောဇဉ် နောက်ထပ်မဖြစ်ပေါ်အောင် မည်သို့နေထိုင်ရမည်ကို သိ၏။</li>
        </ul>
    </div>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
    မျက်စိ (စက္ခု) နှင့် အဆင်း (ရူပ)၊ နား (သောတ) နှင့် အသံ (သဒ္ဒ)၊ နှာခေါင်း (ဃာန) နှင့် အနံ့ (ဂန္ဓ)၊ လျှာ (ဇိဝှာ) နှင့် အရသာ (ရသ)၊ ကိုယ် (ကာယ) နှင့် အတွေ့အထိ (ဖောဋ္ဌဗ္ဗ)၊ စိတ် (မန) နှင့် သဘောတရား (ဓမ္မ) ဟူသော အတွင်း အပြင် အာယတန (၁၂) ပါးတို့ကို သိပါ။ ထိုမျက်စိနှင့် အဆင်းကို အကြောင်းပြု၍ ဖြစ်ပေါ်လာသော သံယောဇဉ် (တပ်မက်ခြင်း၊ ငြိတွယ်ခြင်း) ကိုလည်း သိပါ။ ထိုသံယောဇဉ်တို့ မည်သို့ ဖြစ်ပေါ်လာသည်၊ ဖြစ်ပေါ်ပြီးနောက် မည်သို့ ပယ်ဖျောက်ရသည်၊ ပယ်ပြီးနောက် နောင်တစ်ဖန် ပြန်မဖြစ်ပေါ်အောင် မည်သို့ လုပ်ရမည်ကို ဉာဏ်ဖြင့် စူးစိုက်ဆင်ခြင်ပါ။
</div>
</details>
</div>"""

content = content.replace(ayatana_old, ayatana_new)


bojjhanga_old = """<!-- 4. Bojjhanga -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-stairs text-emerald-500 text-xl"></i>
<h4 class="font-bold text-emerald-700 dark:text-emerald-400 text-base sm:text-lg">၄။ ဗောဇ္ဈင်္ဂ ပဗ္ဗ (ဗောဇ္ဈင် ၇ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-3">သစ္စာလေးပါးကို သိရန်အတွက် အထောက်အကူပြုသော အင်္ဂါ ၇ ပါး မိမိသန္တာန်၌ ဖြစ်ပေါ်နေမှု၊ ရင့်ကျက်လာမှုတို့ကို သိမြင်ခြင်း -</p>
<div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs font-semibold text-emerald-900 dark:text-emerald-300">
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၁။ သတိသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">မမေ့မလျော့ အောက်မေ့မှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၂။ ဓမ္မဝိစယသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">ပညာဖြင့် စူးစမ်းမှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၃။ ဝီရိယသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">ကြိုးစား အားထုတ်မှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၄။ ပီတိသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">စိတ်နှစ်သက် ဝမ်းမြောက်မှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၅။ ပဿဒ္ဓိသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">ကိုယ်စိတ် ငြိမ်းအေးမှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၆။ သမာဓိသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">စိတ်တည်ကြည် ငြိမ်သက်မှု</span>
</div>
<div class="bg-emerald-50 dark:bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-200/60 dark:border-emerald-800/40 text-center sm:col-span-2 flex flex-col justify-center">
<span class="font-bold text-emerald-700 dark:text-emerald-400">၇။ ဥပေက္ခာသမ္ဗောဇ္ဈင်</span>
<span class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">အစွန်းမရောက် လစ်လျူရှု တည်ငြိမ်မှု</span>
</div>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
                        သတိ၊ ဓမ္မဝိစယ (တရားကို စူးစမ်းခြင်း)၊ ဝီရိယ၊ ပီတိ၊ ပဿဒ္ဓိ (ငြိမ်းအေးခြင်း)၊ သမာဓိ၊ ဥပေက္ခာ ဟူသော ဗောဇ္ဈင် ၇ ပါး (သစ္စာလေးပါးကို သိရန် အကြောင်းတရားများ) သည် မိမိသန္တာန်၌ ရှိလျှင် ရှိသည်ဟု သိပါ၊ မရှိလျှင် မရှိဟု သိပါ။ မဖြစ်ပေါ်သေးသော ဗောဇ္ဈင်တရားများ ဖြစ်ပေါ်လာရန်နှင့်၊ ဖြစ်ပေါ်ပြီးသော ဗောဇ္ဈင်တရားများ ပိုမို ပြည့်စုံ တိုးပွားလာစေရန် ဉာဏ်ဖြင့် အားထုတ် ရှုမှတ်ပါ။ ဤတရားတို့သည် နိဗ္ဗာန်သို့ ရောက်ရန်အတွက် မရှိမဖြစ် လိုအပ်သော တရားများ ဖြစ်ကြောင်းကို အမြဲ ဆင်ခြင်ပါ။
                    </div>
</details>
</div>"""

bojjhanga_new = """<!-- 4. Bojjhanga -->
<div class="p-5 sm:p-6 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl shadow-sm border-l-4 border-l-sky-500">
<div class="flex items-center gap-3 mb-3 border-b border-slate-100 dark:border-slate-700 pb-2">
<i class="fa-solid fa-stairs text-sky-500 text-xl"></i>
<h4 class="font-bold text-sky-700 dark:text-sky-400 text-base sm:text-lg">၄။ ဗောဇ္ဈင်္ဂ ပဗ္ဗ (ဗောဇ္ဈင် ၇ ပါး)</h4>
</div>
<p class="text-xs sm:text-sm text-slate-600 dark:text-slate-400 mb-4">
    သစ္စာလေးပါးကို သိရန်အတွက် အထောက်အကူပြုသော အင်္ဂါ ၇ ပါး မိမိသန္တာန်၌ ဖြစ်ပေါ်နေမှု၊ ရင့်ကျက်လာမှုတို့ကို သိမြင်ခြင်း -
</p>

<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs mb-5">
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-anchor text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၁။ သတိသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">မမေ့မလျော့ အောက်မေ့မှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-magnifying-glass text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၂။ ဓမ္မဝိစယသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">ပညာဖြင့် ခွဲခြမ်းစူးစမ်းမှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-person-running text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၃။ ဝီရိယသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">မလျှော့သော ကြိုးစားအားထုတ်မှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-face-smile-beam text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၄။ ပီတိသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">စိတ်နှစ်သက် ဝမ်းမြောက်မှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-leaf text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၅။ ပဿဒ္ဓိသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">ကိုယ်/စိတ် ငြိမ်းအေးမှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center flex flex-col justify-center">
        <i class="fa-solid fa-bullseye text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၆။ သမာဓိသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">စိတ်တည်ကြည် ငြိမ်သက်မှု</span>
    </div>
    <div class="bg-sky-50 dark:bg-sky-950/40 p-3 rounded-xl border border-sky-200/60 dark:border-sky-800/40 text-center lg:col-span-2 flex flex-col justify-center">
        <i class="fa-solid fa-scale-balanced text-sky-500 mb-1.5 text-lg"></i>
        <span class="font-bold text-sky-800 dark:text-sky-300">၇။ ဥပေက္ခာသမ္ဗောဇ္ဈင်</span>
        <span class="text-[10px] text-slate-500 dark:text-slate-400 mt-1">အစွန်းမရောက် လစ်လျူရှု တည်ငြိမ်မှု</span>
    </div>
</div>

<div class="bg-white/80 dark:bg-slate-800/80 p-4 rounded-xl border border-sky-200 dark:border-sky-700/60">
    <h5 class="font-bold text-sky-800 dark:text-sky-400 text-xs sm:text-sm mb-3">ဗောဇ္ဈင် ပွားများမှု (၃) ဆင့်</h5>
    <ul class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-2 list-decimal pl-4">
        <li><b class="text-sky-900 dark:text-sky-200">ရှိ/မရှိ သိခြင်း:</b> မိမိသန္တာန်၌ သတိ၊ ဝီရိယ စသော ဗောဇ္ဈင်တရား ရှိလျှင် "ရှိသည်" ဟု သိ၏။ မရှိလျှင် "မရှိ" ဟု သိ၏။</li>
        <li><b class="text-sky-900 dark:text-sky-200">ဖြစ်ပေါ်ကြောင်းကို သိခြင်း:</b> မဖြစ်သေးသော ဗောဇ္ဈင်တရားသည် ယောနိသော မနသိကာရ (သင့်တင့်စွာ နှလုံးသွင်းမှု) ကြောင့် ဖြစ်ပေါ်လာကြောင်းကို ဉာဏ်ဖြင့် သိ၏။</li>
        <li><b class="text-sky-900 dark:text-sky-200">ပွားများပြည့်စုံကြောင်းကို သိခြင်း:</b> ဖြစ်ပေါ်ပြီးသော ဗောဇ္ဈင်တရားကို ထပ်ခါတလဲလဲ ပွားများခြင်းဖြင့် ရင့်ကျက်ပြည့်စုံလာကြောင်း (ဘာဝနာပါရိပူရိ) ကို သိ၏။</li>
    </ul>
</div>

<details class="explanation-details mt-4 group">
<summary class="text-xs sm:text-sm font-bold text-sky-600 dark:text-sky-400 cursor-pointer flex items-center gap-2 select-none hover:text-sky-700 dark:hover:text-sky-300 transition-colors">
<i class="fa-solid fa-book-open"></i>
<span>အကျယ် ရှင်းပြချက် ဖတ်ရန်</span>
</summary>
<div class="mt-3 p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg text-[13px] text-slate-700 dark:text-slate-300 leading-relaxed text-justify border-l-2 border-sky-400">
    သတိ၊ ဓမ္မဝိစယ (တရားကို စူးစမ်းခြင်း)၊ ဝီရိယ၊ ပီတိ၊ ပဿဒ္ဓိ (ငြိမ်းအေးခြင်း)၊ သမာဓိ၊ ဥပေက္ခာ ဟူသော ဗောဇ္ဈင် ၇ ပါး (သစ္စာလေးပါးကို သိရန် အကြောင်းတရားများ) သည် မိမိသန္တာန်၌ ရှိလျှင် ရှိသည်ဟု သိပါ၊ မရှိလျှင် မရှိဟု သိပါ။ မဖြစ်ပေါ်သေးသော ဗောဇ္ဈင်တရားများ ဖြစ်ပေါ်လာရန်အတွက် အကြောင်းတရားကို ဆင်ခြင်ပြီး၊ ဖြစ်ပေါ်ပြီးသော ဗောဇ္ဈင်တရားများ ပိုမို ပြည့်စုံ တိုးပွား (ဘာဝနာပါရိပူရိ) လာစေရန် ဉာဏ်ဖြင့် အားထုတ် ရှုမှတ်ပါ။ ဤတရားတို့သည် နိဗ္ဗာန်သို့ ရောက်ရန်အတွက် မရှိမဖြစ် လိုအပ်သော တရားများ ဖြစ်ကြောင်းကို အမြဲ ဆင်ခြင်ပါ။
</div>
</details>
</div>"""

content = content.replace(bojjhanga_old, bojjhanga_new)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
