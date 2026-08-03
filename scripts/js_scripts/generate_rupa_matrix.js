const fs = require('fs');
const html = fs.readFileSync('rupa_sangaha.html', 'utf8');

const matrixCode = `
        <!-- Rupa Samutthana Matrix Table Section -->
        <div class="mt-16 mb-8 text-center max-w-4xl mx-auto space-y-2">
            <h2 class="text-2xl md:text-3xl font-bold"><i class="fa-solid fa-seedling text-emerald-500 mr-2"></i> ရုပ် နှင့် သမုဋ္ဌာန် ဇယားကြီး</h2>
            <p class="text-slate-600 dark:text-slate-400 text-sm">
                ရုပ် (၂၈) ပါး ကို ၎င်းတို့ ဖြစ်ပေါ်စေသော အကြောင်းရင်း (သမုဋ္ဌာန် ၄ ပါး) နှင့် ချိတ်ဆက်ပြသထားသော ဇယား (Mapping Table) ဖြစ်ပါသည်။
            </p>
        </div>

        <div class="glass-card rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto shadow-sm mb-12">
            <table class="w-full text-left text-sm whitespace-nowrap">
                <thead>
                    <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-700">
                        <th class="p-4 font-bold text-slate-700 dark:text-slate-300 w-64 sticky left-0 bg-slate-50 dark:bg-slate-800/90 z-10 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.5)]">ရုပ်တရား (၂၈) ပါး</th>
                        <th class="p-4 font-bold text-center text-rose-700 dark:text-rose-400">ကံ<br><span class="text-[10px] font-normal text-slate-500">(Kamma)</span></th>
                        <th class="p-4 font-bold text-center text-sky-700 dark:text-sky-400">စိတ်<br><span class="text-[10px] font-normal text-slate-500">(Citta)</span></th>
                        <th class="p-4 font-bold text-center text-amber-700 dark:text-amber-400">ဥတု<br><span class="text-[10px] font-normal text-slate-500">(Utu)</span></th>
                        <th class="p-4 font-bold text-center text-emerald-700 dark:text-emerald-400">အာဟာရ<br><span class="text-[10px] font-normal text-slate-500">(Ahara)</span></th>
                    </tr>
                </thead>
                <tbody id="rupa-matrix-tbody" class="divide-y divide-slate-100 dark:divide-slate-800/50">
                    <!-- Rows will be injected by JS -->
                </tbody>
            </table>
        </div>
`;

let updatedHtml = html.replace('    </main>', matrixCode + '\n    </main>');

const scriptCode = `
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const rupaData = [
                {
                    category: 'ဧကသမုဋ္ဌာနိက (အကြောင်း ၁-ပါးတည်းကြောင့် ဖြစ်သောရုပ်) - ၁၁ ပါး',
                    items: [
                        { name: 'ပသာဒ ၅၊ ဘာဝ ၂၊ ဟဒယ၊ ဇီဝိတ', causes: ['kamma'], note: 'ကမ္မဇရုပ်စစ်စစ် (၉) ပါး' },
                        { name: 'ကာယဝိညတ်၊ ဝစီဝိညတ်', causes: ['citta'], note: 'စိတ္တဇရုပ်စစ်စစ် (၂) ပါး' }
                    ]
                },
                {
                    category: 'ဒွိသမုဋ္ဌာနိက (အကြောင်း ၂-ပါးကြောင့် ဖြစ်သောရုပ်) - ၁ ပါး',
                    items: [
                        { name: 'သဒ္ဒ (အသံ)', causes: ['citta', 'utu'], note: 'စိတ်၊ ဥတု ကြောင့်ဖြစ်သည်' }
                    ]
                },
                {
                    category: 'တိသမုဋ္ဌာနိက (အကြောင်း ၃-ပါးကြောင့် ဖြစ်သောရုပ်) - ၃ ပါး',
                    items: [
                        { name: 'လဟုတာ၊ မုဒုတာ၊ ကမ္မညတာ', causes: ['citta', 'utu', 'ahara'], note: 'လဟုတာဒိ (၃) ပါး' }
                    ]
                },
                {
                    category: 'စတုသမုဋ္ဌာနိက (အကြောင်း ၄-ပါးလုံးကြောင့် ဖြစ်သောရုပ်) - ၉ ပါး',
                    items: [
                        { name: 'အဝိနိဗ္ဘောဂရုပ် (၈) ပါး', causes: ['kamma', 'citta', 'utu', 'ahara'], note: 'မခွဲမခွာ အမြဲတွဲဖြစ်သော ရုပ် ၈-ပါး' },
                        { name: 'အာကာသ (ပရိစ္ဆေဒရုပ်)', causes: ['kamma', 'citta', 'utu', 'ahara'], note: 'ရုပ်ကလာပ်တို့ကို ပိုင်းခြားပေးသောရုပ်' }
                    ]
                },
                {
                    category: 'န ကုတောစိ သမုဋ္ဌာနိက (မည်သည့်အကြောင်းကြောင့်မျှ မဖြစ်သောရုပ်) - ၄ ပါး',
                    items: [
                        { name: 'ဥပစယ၊ သန္တတိ၊ ဇရတာ၊ အနိစ္စတာ', causes: [], note: 'လက္ခဏာရုပ် ၄ ပါး (ရုပ်များ၏ သဘာဝမျှသာဖြစ်သည်)' }
                    ]
                }
            ];

            const tbody = document.getElementById('rupa-matrix-tbody');
            if(tbody) {
                const cols = ['kamma', 'citta', 'utu', 'ahara'];
                const checks = {
                    kamma: '<div class="w-6 h-6 mx-auto rounded-full bg-rose-100 dark:bg-rose-900/40 text-rose-600 dark:text-rose-400 flex items-center justify-center"><i class="fa-solid fa-check text-xs"></i></div>',
                    citta: '<div class="w-6 h-6 mx-auto rounded-full bg-sky-100 dark:bg-sky-900/40 text-sky-600 dark:text-sky-400 flex items-center justify-center"><i class="fa-solid fa-check text-xs"></i></div>',
                    utu: '<div class="w-6 h-6 mx-auto rounded-full bg-amber-100 dark:bg-amber-900/40 text-amber-600 dark:text-amber-400 flex items-center justify-center"><i class="fa-solid fa-check text-xs"></i></div>',
                    ahara: '<div class="w-6 h-6 mx-auto rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400 flex items-center justify-center"><i class="fa-solid fa-check text-xs"></i></div>'
                };
                const dash = '<span class="text-slate-300 dark:text-slate-600/50">-</span>';

                let html = '';
                rupaData.forEach(cat => {
                    html += \`<tr class="bg-slate-100/50 dark:bg-slate-800/30">
                        <td colspan="5" class="p-3 font-bold text-slate-600 dark:text-slate-400 text-xs tracking-wider sticky left-0 z-10">\${cat.category}</td>
                    </tr>\`;
                    
                    cat.items.forEach(item => {
                        html += \`<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">\`;
                        html += \`<td class="p-4 sticky left-0 bg-white dark:bg-slate-900 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.3)] z-10">
                            <div class="font-bold text-slate-800 dark:text-slate-200 mb-0.5 text-base">\${item.name}</div>
                            <div class="text-[11px] text-slate-500 dark:text-slate-400">\${item.note}</div>
                        </td>\`;
                        
                        cols.forEach(c => {
                            if (item.causes.includes(c)) {
                                html += \`<td class="p-3 text-center align-middle">\${checks[c]}</td>\`;
                            } else {
                                html += \`<td class="p-3 text-center align-middle">\${dash}</td>\`;
                            }
                        });
                        
                        html += \`</tr>\`;
                    });
                });
                tbody.innerHTML = html;
            }
        });
    </script>
`;

updatedHtml = updatedHtml.replace('</body>', scriptCode + '\n</body>');
fs.writeFileSync('rupa_sangaha.html', updatedHtml);
