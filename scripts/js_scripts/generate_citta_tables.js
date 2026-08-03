const fs = require('fs');
const path = require('path');

const FILE_PATH = path.join(__dirname, 'citta_cetasikas_visual_guide.html');
let html = fs.readFileSync(FILE_PATH, 'utf-8');

// 1. Add Tab Button to Unified Bottom Tab Bar
const tabButtonHtml = `
        <button onclick="switchTab('tables')" id="tabm-tables" role="tab" aria-selected="false" aria-controls="sec-tables" class="tab-btn-mobile flex-1 flex flex-col items-center justify-center gap-0.5 py-2 lg:py-2.5 text-slate-400 hover:text-amber-300">
            <i class="fa-solid fa-table text-base lg:text-lg"></i>
            <span class="text-[10px] lg:text-xs font-semibold leading-tight">ဇယားများ</span>
        </button>
`;

// Insert before the search tab
if (html.includes("switchTab('tables')") === false) {
    html = html.replace(
        /<button onclick="switchTab\('search'\)" id="tabm-search"/g,
        tabButtonHtml.trim() + '\n        <button onclick="switchTab(\'search\')" id="tabm-search"'
    );
}

// 2. Generate Tables Section HTML
const tablesSectionHtml = `
        <!-- Tables Section -->
        <section id="sec-tables" role="tabpanel" aria-labelledby="tab-tables" class="hidden space-y-8 animate-fade-in pb-20">
            
            <div class="text-center max-w-3xl mx-auto space-y-4 mb-10">
                <h2 class="text-2xl md:text-3xl font-bold text-amber-700 dark:text-amber-400">
                    <i class="fa-solid fa-table"></i> စိတ်၊ စေတသိက် ဇယားများ
                </h2>
                <p class="text-slate-600 dark:text-slate-400">
                    စိတ်နှင့် စေတသိက်တို့၏ အုပ်စုခွဲခြားမှုများ၊ ယှဉ်တွဲဖြစ်ပေါ်မှု (သမ္ပယောဂ) နှင့် ပါဝင်ဖွဲ့စည်းမှု (သင်္ဂဟ) ဇယားများ
                </p>
            </div>

            <!-- Table 1: Citta Summary -->
            <div class="bg-white/80 dark:bg-slate-900/80 rounded-2xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
                <div class="bg-slate-50 dark:bg-slate-800/50 p-4 border-b border-slate-200 dark:border-slate-800">
                    <h3 class="text-lg font-bold text-slate-800 dark:text-slate-200"><i class="fa-solid fa-sitemap text-sky-500 mr-2"></i> စိတ် (၈၉) ပါး အုပ်စုခွဲ အကျဉ်းချုပ် ဇယား</h3>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm whitespace-nowrap min-w-[800px]">
                        <thead>
                            <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300">
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700">ဘုံ (Bhumi)</th>
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700">အကုသိုလ် (Akusala)</th>
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700">ကုသိုလ် (Kusala)</th>
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700">ဝိပါက် (Vipaka)</th>
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700">ကြိယာ (Kiriya)</th>
                                <th class="p-3 border-b border-slate-200 dark:border-slate-700 font-bold text-amber-600 dark:text-amber-400">စုစုပေါင်း</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
                            <tr>
                                <td class="p-3 font-semibold text-slate-700 dark:text-slate-300">ကာမဘုံ (၅၄ ပါး)</td>
                                <td class="p-3 bg-rose-50 dark:bg-rose-900/10 text-rose-700 dark:text-rose-400">၁၂ ပါး</td>
                                <td class="p-3 bg-emerald-50 dark:bg-emerald-900/10 text-emerald-700 dark:text-emerald-400">၈ ပါး <span class="text-xs text-slate-500">(မဟာ)</span></td>
                                <td class="p-3 bg-sky-50 dark:bg-sky-900/10 text-sky-700 dark:text-sky-400">၂၃ ပါး <span class="text-xs text-slate-500">(အဟိတ် ၁၅ + မဟာ ၈)</span></td>
                                <td class="p-3 bg-slate-100 dark:bg-slate-800/50 text-slate-600 dark:text-slate-400">၁၁ ပါး <span class="text-xs text-slate-500">(အဟိတ် ၃ + မဟာ ၈)</span></td>
                                <td class="p-3 font-bold text-amber-600 dark:text-amber-400">၅၄ ပါး</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-slate-700 dark:text-slate-300">ရူပဘုံ (၁၅ ပါး)</td>
                                <td class="p-3 text-slate-400">-</td>
                                <td class="p-3 bg-emerald-50 dark:bg-emerald-900/10 text-emerald-700 dark:text-emerald-400">၅ ပါး</td>
                                <td class="p-3 bg-sky-50 dark:bg-sky-900/10 text-sky-700 dark:text-sky-400">၅ ပါး</td>
                                <td class="p-3 bg-slate-100 dark:bg-slate-800/50 text-slate-600 dark:text-slate-400">၅ ပါး</td>
                                <td class="p-3 font-bold text-amber-600 dark:text-amber-400">၁၅ ပါး</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-slate-700 dark:text-slate-300">အရူပဘုံ (၁၂ ပါး)</td>
                                <td class="p-3 text-slate-400">-</td>
                                <td class="p-3 bg-emerald-50 dark:bg-emerald-900/10 text-emerald-700 dark:text-emerald-400">၄ ပါး</td>
                                <td class="p-3 bg-sky-50 dark:bg-sky-900/10 text-sky-700 dark:text-sky-400">၄ ပါး</td>
                                <td class="p-3 bg-slate-100 dark:bg-slate-800/50 text-slate-600 dark:text-slate-400">၄ ပါး</td>
                                <td class="p-3 font-bold text-amber-600 dark:text-amber-400">၁၂ ပါး</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-slate-700 dark:text-slate-300">လောကုတ္တရာ (၈ ပါး)</td>
                                <td class="p-3 text-slate-400">-</td>
                                <td class="p-3 bg-emerald-50 dark:bg-emerald-900/10 text-emerald-700 dark:text-emerald-400">၄ ပါး <span class="text-xs text-slate-500">(မဂ်)</span></td>
                                <td class="p-3 bg-sky-50 dark:bg-sky-900/10 text-sky-700 dark:text-sky-400">၄ ပါး <span class="text-xs text-slate-500">(ဖိုလ်)</span></td>
                                <td class="p-3 text-slate-400">-</td>
                                <td class="p-3 font-bold text-amber-600 dark:text-amber-400">၈ ပါး</td>
                            </tr>
                            <tr class="bg-amber-50/50 dark:bg-amber-900/10">
                                <td class="p-3 font-bold text-amber-700 dark:text-amber-400">စုစုပေါင်း (၈၉)</td>
                                <td class="p-3 font-bold text-rose-600 dark:text-rose-400">၁၂ ပါး</td>
                                <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">၂၁ ပါး</td>
                                <td class="p-3 font-bold text-sky-600 dark:text-sky-400">၃၆ ပါး</td>
                                <td class="p-3 font-bold text-slate-600 dark:text-slate-400">၂၀ ပါး</td>
                                <td class="p-3 font-bold text-amber-700 dark:text-amber-400 text-lg">၈၉ ပါး</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Table 2: Cetasika Summary -->
            <div class="bg-white/80 dark:bg-slate-900/80 rounded-2xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
                <div class="bg-slate-50 dark:bg-slate-800/50 p-4 border-b border-slate-200 dark:border-slate-800">
                    <h3 class="text-lg font-bold text-slate-800 dark:text-slate-200"><i class="fa-solid fa-cubes text-amber-500 mr-2"></i> စေတသိက် (၅၂) ပါး အုပ်စုခွဲ ဇယား</h3>
                </div>
                <div class="p-4 grid grid-cols-1 md:grid-cols-3 gap-4">
                    <!-- Annasamana -->
                    <div class="bg-amber-50 dark:bg-amber-500/10 border border-amber-200 dark:border-amber-500/30 rounded-xl p-4">
                        <h4 class="font-bold text-amber-700 dark:text-amber-400 mb-2 border-b border-amber-200 dark:border-amber-500/30 pb-2">အညသမန်း (၁၃) ပါး</h4>
                        <p class="text-xs text-amber-600 dark:text-amber-500 mb-3">ကုသိုလ်၊ အကုသိုလ် မရွေး ယှဉ်တွဲနိုင်သော ကြားနေစေတသိက်များ</p>
                        <ul class="text-sm space-y-1 text-slate-700 dark:text-slate-300">
                            <li><span class="font-semibold">သဗ္ဗစိတ္တသာဓာရဏ (၇):</span> ဖဿ၊ ဝေဒနာ၊ သညာ၊ စေတနာ၊ ဧကဂ္ဂတာ၊ ဇီဝိတိန္ဒြေ၊ မနသိကာရ</li>
                            <li class="pt-2"><span class="font-semibold">ပကိဏ်း (၆):</span> ဝိတက်၊ ဝိစာရ၊ အဓိမောက္ခ၊ ဝီရိယ၊ ပီတိ၊ ဆန္ဒ</li>
                        </ul>
                    </div>
                    <!-- Akusala -->
                    <div class="bg-rose-50 dark:bg-rose-500/10 border border-rose-200 dark:border-rose-500/30 rounded-xl p-4">
                        <h4 class="font-bold text-rose-700 dark:text-rose-400 mb-2 border-b border-rose-200 dark:border-rose-500/30 pb-2">အကုသိုလ် (၁၄) ပါး</h4>
                        <p class="text-xs text-rose-600 dark:text-rose-500 mb-3">မကောင်းသော၊ အပြစ်ရှိသော စိတ်များတွင်သာ ယှဉ်သော စေတသိက်များ</p>
                        <ul class="text-sm space-y-1 text-slate-700 dark:text-slate-300">
                            <li><span class="font-semibold">မောဟစတုက္က (၄):</span> မောဟ၊ အဟိရိက၊ အနောတ္တပ္ပ၊ ဥဒ္ဓစ္စ</li>
                            <li><span class="font-semibold">လောဘတိက (၃):</span> လောဘ၊ ဒိဋ္ဌိ၊ မာန</li>
                            <li><span class="font-semibold">ဒေါသစတုက္က (၄):</span> ဒေါသ၊ ဣဿာ၊ မစ္ဆရိယ၊ ကုက္ကုစ္စ</li>
                            <li><span class="font-semibold">ထီနဒုက (၂):</span> ထိန၊ မိဒ္ဓ</li>
                            <li><span class="font-semibold">ဝိစိကိစ္ဆာ (၁):</span> ဝိစိကိစ္ဆာ</li>
                        </ul>
                    </div>
                    <!-- Sobhana -->
                    <div class="bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/30 rounded-xl p-4">
                        <h4 class="font-bold text-emerald-700 dark:text-emerald-400 mb-2 border-b border-emerald-200 dark:border-emerald-500/30 pb-2">သောဘဏ (၂၅) ပါး</h4>
                        <p class="text-xs text-emerald-600 dark:text-emerald-500 mb-3">တင့်တယ်ကောင်းမွန်သော စိတ်များနှင့်သာ ယှဉ်သော စေတသိက်များ</p>
                        <ul class="text-sm space-y-1 text-slate-700 dark:text-slate-300">
                            <li><span class="font-semibold">သောဘဏသာဓာရဏ (၁၉):</span> သဒ္ဓါ၊ သတိ၊ ဟိရီ၊ ဩတ္တပ္ပ၊ အလောဘ၊ အဒေါသ စသည်</li>
                            <li><span class="font-semibold">ဝိရတီ (၃):</span> သမ္မာဝါစာ၊ သမ္မာကမ္မန္တ၊ သမ္မာအာဇီဝ</li>
                            <li><span class="font-semibold">အပ္ပမညာ (၂):</span> ကရုဏာ၊ မုဒိတာ</li>
                            <li><span class="font-semibold">ပညိန္ဒြေ (၁):</span> ပညာ</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Table 3: Sampayoga Naya Matrix -->
            <div class="bg-white/80 dark:bg-slate-900/80 rounded-2xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
                <div class="bg-slate-50 dark:bg-slate-800/50 p-4 border-b border-slate-200 dark:border-slate-800 flex justify-between items-center flex-wrap gap-2">
                    <h3 class="text-lg font-bold text-slate-800 dark:text-slate-200"><i class="fa-solid fa-diagram-project text-indigo-500 mr-2"></i> သမ္ပယောဂနည်း ဇယား (စေတသိက်တို့၏ ယှဉ်ခြင်း)</h3>
                    <span class="text-xs bg-slate-200 dark:bg-slate-700 px-2 py-1 rounded text-slate-600 dark:text-slate-300">အလျားလိုက်ကြည့်ရန်</span>
                </div>
                <div class="p-4 overflow-x-auto">
                    <table class="w-full text-left text-sm min-w-[1000px] border-collapse">
                        <thead>
                            <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 text-xs">
                                <th class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-slate-100 dark:bg-slate-800 z-10 w-48 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)]">စေတသိက်များ</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-rose-600 dark:text-rose-400" title="လောဘ(၈)၊ ဒေါသ(၂)၊ မောဟ(၂)">အကုသိုလ် (၁၂)</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-500" title="အကုသလဝိပါက်(၇)၊ ကုသလဝိပါက်(၈)၊ ကြိယာ(၃)">အဟိတ် (၁၈)</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-emerald-600 dark:text-emerald-400">ကာမသောဘဏ (၂၄)</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-sky-600 dark:text-sky-400">မဟဂ္ဂုတ် (၂၇)</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-amber-600 dark:text-amber-400">လောကုတ္တရာ (၈/၄၀)</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">ယှဉ်သောစိတ်ပေါင်း</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 dark:divide-slate-800/50 text-slate-700 dark:text-slate-300">
                            <!-- Sabba Citta -->
                            <tr class="bg-amber-50/30 dark:bg-amber-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-amber-50/95 dark:bg-[#1a1f2e] z-10 font-medium">သဗ္ဗစိတ္တသာဓာရဏ (၇)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၂</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၈</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂၄</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂၇</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈ / ၄၀</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-amber-600">၈၉ / ၁၂၁</td>
                            </tr>
                            <!-- Pakinnaka -->
                            <tr class="bg-amber-50/30 dark:bg-amber-500/5 text-xs">
                                <td colspan="7" class="p-2 font-bold text-amber-700 dark:text-amber-400">ပကိဏ်း (၆) ပါး - (အချို့စိတ်တို့၌သာ ယှဉ်သည်)</td>
                            </tr>
                            <tr class="bg-amber-50/30 dark:bg-amber-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-amber-50/95 dark:bg-[#1a1f2e] z-10 pl-6">ဝိတက်</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၂</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂၄</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၃ <span class="text-[10px]">(ပ-ဈာန်)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈ <span class="text-[10px]">(ပ-ဈာန်)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၅၅</td>
                            </tr>
                            <tr class="bg-amber-50/30 dark:bg-amber-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-amber-50/95 dark:bg-[#1a1f2e] z-10 pl-6">ဝိစာရ</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၂</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂၄</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၆ <span class="text-[10px]">(ပ, ဒု)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁۶ <span class="text-[10px]">(ပ, ဒု)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၆၆</td>
                            </tr>
                            <tr>
                                <td colspan="7" class="p-4 text-center text-slate-500 text-xs italic bg-slate-50 dark:bg-slate-800/30">
                                    (အထက်ပါဇယားသည် ပုံစံပြဖြစ်ပြီး စေတသိက်တစ်ပါးစီတိုင်း၏ ယှဉ်သောစိတ်များကို 'စေတသိက်' Tab တွင် အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။)
                                </td>
                            </tr>

                            <!-- Akusala -->
                            <tr class="bg-rose-50/30 dark:bg-rose-500/5 text-xs">
                                <td colspan="7" class="p-2 font-bold text-rose-700 dark:text-rose-400">အကုသိုလ် စေတသိက် (၁၄) ပါး</td>
                            </tr>
                            <tr class="bg-rose-50/30 dark:bg-rose-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-rose-50/95 dark:bg-[#1f1a1d] z-10 font-medium">မောဟစတုက္က (၄)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-rose-600">၁၂</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-rose-600">၁၂</td>
                            </tr>
                            <tr class="bg-rose-50/30 dark:bg-rose-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-rose-50/95 dark:bg-[#1f1a1d] z-10 pl-6">လောဘ</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈ <span class="text-[10px]">(လောဘမူ)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၈</td>
                            </tr>
                            <tr class="bg-rose-50/30 dark:bg-rose-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-rose-50/95 dark:bg-[#1f1a1d] z-10 pl-6">ဒေါသစတုက္က (၄)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂ <span class="text-[10px]">(ဒေါသမူ)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၂</td>
                            </tr>
                            
                            <!-- Sobhana -->
                            <tr class="bg-emerald-50/30 dark:bg-emerald-500/5 text-xs">
                                <td colspan="7" class="p-2 font-bold text-emerald-700 dark:text-emerald-400">သောဘဏ စေတသိက် (၂၅) ပါး</td>
                            </tr>
                            <tr class="bg-emerald-50/30 dark:bg-emerald-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-emerald-50/95 dark:bg-[#1a211e] z-10 font-medium">သောဘဏသာဓာရဏ (၁၉)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၂၄</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၂၇</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၈/၄၀</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၅၉ / ၉၁</td>
                            </tr>
                            <tr class="bg-emerald-50/30 dark:bg-emerald-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-emerald-50/95 dark:bg-[#1a211e] z-10 pl-6">ဝိရတီ (၃)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၈ <span class="text-[10px]">(မဟာကု)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၈/၄၀</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၁၆ / ၄၈</td>
                            </tr>
                            <tr class="bg-emerald-50/30 dark:bg-emerald-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-emerald-50/95 dark:bg-[#1a211e] z-10 pl-6">အပ္ပမညာ (၂)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၆ <span class="text-[10px]">(ကု၊ ကြိ)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၂ <span class="text-[10px]">(ပ,ဒု,တ,စ-ဈာန်)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၂၈</td>
                            </tr>
                            <tr class="bg-emerald-50/30 dark:bg-emerald-500/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-emerald-50/95 dark:bg-[#1a211e] z-10 pl-6">ပညာ (၁)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၁၂ <span class="text-[10px]">(ဉာဏသမ္ပယုတ်)</span></td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center">၂၇</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold text-emerald-600">၈/၄၀</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၄၇ / ၇၉</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Table 4: Sangaha Naya Matrix -->
            <div class="bg-white/80 dark:bg-slate-900/80 rounded-2xl border border-slate-200 dark:border-slate-800 overflow-hidden shadow-sm">
                <div class="bg-slate-50 dark:bg-slate-800/50 p-4 border-b border-slate-200 dark:border-slate-800">
                    <h3 class="text-lg font-bold text-slate-800 dark:text-slate-200"><i class="fa-solid fa-layer-group text-fuchsia-500 mr-2"></i> သင်္ဂဟနည်း ဇယား (စိတ်တစ်ခုစီ၌ ပါဝင်သော စေတသိက်များ)</h3>
                </div>
                <div class="p-4 overflow-x-auto">
                    <table class="w-full text-left text-sm min-w-[800px] border-collapse">
                        <thead>
                            <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 text-xs">
                                <th class="p-2 border border-slate-200 dark:border-slate-700 sticky left-0 bg-slate-100 dark:bg-slate-800 z-10 w-48 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)]">စိတ်အုပ်စုများ</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-amber-600">အညသမန်း (၁၃) မှ</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-rose-600">အကုသိုလ် (၁၄) မှ</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center text-emerald-600">သောဘဏ (၂၅) မှ</th>
                                <th class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">ပါဝင်သော စေတသိက် စုစုပေါင်း</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 dark:divide-slate-800/50 text-slate-700 dark:text-slate-300">
                            <!-- Akusala -->
                            <tr class="bg-rose-50/10 dark:bg-rose-900/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-rose-700 dark:text-rose-400 sticky left-0 bg-rose-50/90 dark:bg-[#1f1a1d] z-10">လောဘမူ (၈) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၁၃ (အကုန်)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">မောဟ(၄)၊ လောဘ(၃)၊ ထီန(၂)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၁၉ မှ ၂၂ ထိ</td>
                            </tr>
                            <tr class="bg-rose-50/10 dark:bg-rose-900/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-rose-700 dark:text-rose-400 sticky left-0 bg-rose-50/90 dark:bg-[#1f1a1d] z-10">ဒေါသမူ (၂) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၁၂ (ပီတိကြဉ်)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">မောဟ(၄)၊ ဒေါသ(၄)၊ ထီန(၂)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၂၀ နှင့် ၂၂</td>
                            </tr>
                            
                            <!-- Ahetuka -->
                            <tr class="bg-slate-50/50 dark:bg-slate-800/20">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-slate-700 dark:text-slate-400 sticky left-0 bg-slate-50/90 dark:bg-[#1a1c23] z-10">အဟိတ် (၁၈) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၇ မှ ၁၂ ထိ</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၇ မှ ၁၂ ထိ</td>
                            </tr>

                            <!-- Sobhana -->
                            <tr class="bg-emerald-50/10 dark:bg-emerald-900/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-emerald-700 dark:text-emerald-400 sticky left-0 bg-emerald-50/90 dark:bg-[#1a211e] z-10">ကာမသောဘဏ (၂၄) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၁၃ (အကုန်)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၂၅ အထိ</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၃၂ မှ ၃၈ ထိ</td>
                            </tr>
                            <tr class="bg-sky-50/10 dark:bg-sky-900/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-sky-700 dark:text-sky-400 sticky left-0 bg-sky-50/90 dark:bg-[#1a1f26] z-10">မဟဂ္ဂုတ် (၂၇) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၁၀ မှ ၁၃ ထိ (ဝိတက်၊ ဝိစာရ၊ ပီတိ လျော့)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၂၂ (ဝိရတီ ကြဉ်)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၃၀ မှ ၃၅ ထိ</td>
                            </tr>
                            <tr class="bg-amber-50/10 dark:bg-amber-900/5">
                                <td class="p-2 border border-slate-200 dark:border-slate-700 font-bold text-amber-700 dark:text-amber-400 sticky left-0 bg-amber-50/90 dark:bg-[#231e18] z-10">လောကုတ္တရာ (၈/၄၀) ပါး</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၁၀ မှ ၁၃ ထိ</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-slate-400">-</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center text-xs">၂၃ (အပ္ပမညာ ကြဉ်)</td>
                                <td class="p-2 border border-slate-200 dark:border-slate-700 text-center font-bold">၃၃ မှ ၃၆ ထိ</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

        </section>
`;

if (html.includes('<section id="sec-tables"') === false) {
    html = html.replace(
        /<section id="sec-search"/g,
        tablesSectionHtml + '\n        <section id="sec-search"'
    );
}

fs.writeFileSync(FILE_PATH, html, 'utf-8');
console.log('Successfully injected tables section and tab button into ' + FILE_PATH);
