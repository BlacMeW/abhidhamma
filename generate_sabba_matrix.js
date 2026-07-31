const fs = require('fs');
const html = fs.readFileSync('sabba_sangaha.html', 'utf8');

const matrixCode = `
        <!-- Sabba Matrix Table Section -->
        <div class="mt-16 mb-8 text-center max-w-4xl mx-auto space-y-2">
            <h2 class="text-2xl md:text-3xl font-bold"><i class="fa-solid fa-table-cells text-fuchsia-500 mr-2"></i> သဗ္ဗသင်္ဂဟ ဇယားကြီး (Mapping to Paramattha)</h2>
            <p class="text-slate-600 dark:text-slate-400 text-sm">
                ခန္ဓာ (၅)၊ အာယတန (၁၂)၊ ဓာတ် (၁၈)၊ သစ္စာ (၄) ပါးတို့ကို မူလ ပရမတ္ထတရား (၄) ပါးဖြင့် ချိန်ထိုးပြသထားသော ဇယားဖြစ်ပါသည်။
            </p>
        </div>

        <div class="glass-card rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto shadow-sm mb-12">
            <table class="w-full text-left text-sm whitespace-nowrap">
                <thead>
                    <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-700">
                        <th class="p-4 font-bold text-slate-700 dark:text-slate-300 w-48 sticky left-0 bg-slate-50 dark:bg-slate-800/90 z-10 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.5)]">ပရမတ္ထတရား (၄) ပါး</th>
                        <th class="p-4 font-bold text-center text-rose-700 dark:text-rose-400">ခန္ဓာ<br><span class="text-[10px] font-normal text-slate-500">(၅)</span></th>
                        <th class="p-4 font-bold text-center text-sky-700 dark:text-sky-400">အာယတန<br><span class="text-[10px] font-normal text-slate-500">(၁၂)</span></th>
                        <th class="p-4 font-bold text-center text-emerald-700 dark:text-emerald-400">ဓာတ်<br><span class="text-[10px] font-normal text-slate-500">(၁၈)</span></th>
                        <th class="p-4 font-bold text-center text-amber-700 dark:text-amber-400">သစ္စာ<br><span class="text-[10px] font-normal text-slate-500">(၄)</span></th>
                    </tr>
                </thead>
                <tbody id="matrix-tbody" class="divide-y divide-slate-100 dark:divide-slate-800/50">
                    <!-- Rows will be injected by JS -->
                </tbody>
            </table>
        </div>
`;

// Insert just before </main>
let updatedHtml = html.replace('    </main>', matrixCode + '\n    </main>');

// We need to inject the script. Wait, `sabba_sangaha.html` might not have a `script` tag at the end, or it does. Let's append before </body>
const scriptCode = `
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const paramatthas = [
                { 
                    name: 'စိတ် (၈၉) ပါး', 
                    map: { 
                        khandha: ['ဝိညာဏက္ခန္ဓာ'], 
                        ayatana: ['မနာယတန'], 
                        dhatu: ['ဝိညာဏဓာတ် ၇ ပါး'], 
                        sacca: ['ဒုက္ခသစ္စာ (လောကီ ၈၁)'] 
                    } 
                },
                { 
                    name: 'စေတသိက် (၅၂) ပါး', 
                    map: { 
                        khandha: ['ဝေဒနာက္ခန္ဓာ', 'သညာက္ခန္ဓာ', 'သင်္ခါရက္ခန္ဓာ (၅၀)'], 
                        ayatana: ['ဓမ္မာယတန'], 
                        dhatu: ['ဓမ္မဓာတ်'], 
                        sacca: ['ဒုက္ခသစ္စာ (၅၁)', 'သမုဒယသစ္စာ (လောဘ)', 'မဂ္ဂသစ္စာ (မဂ္ဂင် ၈ ပါး)'] 
                    } 
                },
                { 
                    name: 'ရုပ် (၂၈) ပါး', 
                    map: { 
                        khandha: ['ရူပက္ခန္ဓာ'], 
                        ayatana: ['ဩဠာရိကာယတန ၁၀', 'ဓမ္မာယတန (သုခုမ ၁၆)'], 
                        dhatu: ['ဩဠာရိကဓာတ် ၁၀', 'ဓမ္မဓာတ် (သုခုမ ၁၆)'], 
                        sacca: ['ဒုက္ခသစ္စာ'] 
                    } 
                },
                { 
                    name: 'နိဗ္ဗာန်', 
                    map: { 
                        khandha: ['ခန္ဓဝိမုတ် (မပါဝင်ပါ)'], 
                        ayatana: ['ဓမ္မာယတန'], 
                        dhatu: ['ဓမ္မဓာတ်'], 
                        sacca: ['နိရောဓသစ္စာ'] 
                    } 
                }
            ];

            const tbody = document.getElementById('matrix-tbody');
            if(tbody) {
                const groups = ['khandha', 'ayatana', 'dhatu', 'sacca'];
                const groupColors = {
                    khandha: 'bg-rose-50 text-rose-700 dark:bg-slate-800 dark:text-rose-300 border-rose-200 dark:border-rose-700/50',
                    ayatana: 'bg-sky-50 text-sky-700 dark:bg-slate-800 dark:text-sky-300 border-sky-200 dark:border-sky-700/50',
                    dhatu: 'bg-emerald-50 text-emerald-700 dark:bg-slate-800 dark:text-emerald-300 border-emerald-200 dark:border-emerald-700/50',
                    sacca: 'bg-amber-50 text-amber-700 dark:bg-slate-800 dark:text-amber-300 border-amber-200 dark:border-amber-700/50'
                };

                let html = '';
                paramatthas.forEach(item => {
                    html += \`<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">\`;
                    html += \`<td class="p-4 font-bold text-base text-slate-800 dark:text-slate-200 sticky left-0 bg-white dark:bg-slate-900 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.3)] z-10">\${item.name}</td>\`;
                    
                    groups.forEach(g => {
                        if (item.map[g]) {
                            const labels = item.map[g].map(l => \`<div class="inline-block px-3 py-1.5 m-1 rounded-md border text-sm font-semibold \${groupColors[g]} shadow-sm">\${l}</div>\`).join('<br>');
                            html += \`<td class="p-3 text-center align-middle">\${labels}</td>\`;
                        } else {
                            html += \`<td class="p-3 text-center align-middle"><span class="w-1.5 h-1.5 rounded-full bg-slate-200 dark:bg-slate-800 inline-block"></span></td>\`;
                        }
                    });
                    
                    html += \`</tr>\`;
                });
                tbody.innerHTML = html;
            }
        });
    </script>
`;

updatedHtml = updatedHtml.replace('</body>', scriptCode + '\n</body>');
fs.writeFileSync('sabba_sangaha.html', updatedHtml);
