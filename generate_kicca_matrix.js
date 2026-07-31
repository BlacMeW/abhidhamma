const fs = require('fs');
const html = fs.readFileSync('pakinnaka_sangaha.html', 'utf8');

const matrixCode = `
        <!-- Kicca Sangaha Matrix Table Section -->
        <div class="mt-16 mb-8 text-center max-w-4xl mx-auto space-y-2">
            <h2 class="text-2xl md:text-3xl font-bold"><i class="fa-solid fa-briefcase text-sky-500 mr-2"></i> ကိစ္စနှင့် စိတ် ဇယားကြီး</h2>
            <p class="text-slate-600 dark:text-slate-400 text-sm">
                စိတ် (၈၉) ပါးကို ၎င်းတို့ လုပ်ဆောင်နိုင်သော အလုပ်တာဝန် (ကိစ္စ ၁၄ မျိုး) အရေအတွက်အလိုက် ခွဲခြားပြသထားသော ဇယားဖြစ်ပါသည်။
            </p>
        </div>

        <div class="glass-card rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto shadow-sm mb-12">
            <table class="w-full text-left text-sm whitespace-nowrap">
                <thead>
                    <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-700">
                        <th rowspan="2" class="p-4 font-bold text-slate-700 dark:text-slate-300 min-w-[200px] sticky left-0 bg-slate-50 dark:bg-slate-800/90 z-10 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.5)] border-r border-slate-200 dark:border-slate-700">စိတ်အုပ်စုများ (ကိစ္စအရေအတွက်အလိုက်)</th>
                        <th colspan="14" class="p-2 font-bold text-center text-sky-700 dark:text-sky-400 border-b border-slate-200 dark:border-slate-700">ကိစ္စ (၁၄) မျိုး</th>
                    </tr>
                    <tr class="bg-slate-50/50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-700 text-xs">
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 mt-8 w-8">ပဋိသန္ဓေ</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဘဝင်</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">အာဝဇ္ဇန်း</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဒဿန</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">သဝန</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဃာယန</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">သာယန</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဖုသန</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 mt-4 w-8">သမ္ပဋိစ္ဆိုင်း</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">သန္တီရဏ</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဝုဋ္ဌော</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">ဇော</div></th>
                        <th class="p-2 text-center border-r border-slate-100 dark:border-slate-800"><div class="-rotate-45 origin-bottom-left ml-4 w-8">တဒါရုံ</div></th>
                        <th class="p-2 text-center"><div class="-rotate-45 origin-bottom-left ml-4 w-8">စုတိ</div></th>
                    </tr>
                </thead>
                <tbody id="kicca-matrix-tbody" class="divide-y divide-slate-100 dark:divide-slate-800/50">
                    <!-- Rows injected by JS -->
                </tbody>
            </table>
        </div>
`;

let updatedHtml = html.replace('    </main>', matrixCode + '\n    </main>');

const scriptCode = `
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const kiccaData = [
                {
                    group: '၁-ကိစ္စတတ်သော စိတ်များ (၆၈ ပါး)',
                    items: [
                        { name: 'ပဉ္စဒွါရာဝဇ္ဇန်း (၁)', kiccas: ['avajjana'] },
                        { name: 'စက္ခုဝိညာဏ် (၂)', kiccas: ['dassana'] },
                        { name: 'သောတဝိညာဏ် (၂)', kiccas: ['savana'] },
                        { name: 'ဃာနဝိညာဏ် (၂)', kiccas: ['ghayana'] },
                        { name: 'ဇိဝှာဝိညာဏ် (၂)', kiccas: ['sayana'] },
                        { name: 'ကာယဝိညာဏ် (၂)', kiccas: ['phusana'] },
                        { name: 'သမ္ပဋိစ္ဆိုင်း (၂)', kiccas: ['sampaticchana'] },
                        { name: 'ဇောစိတ် (၅၅)', kiccas: ['javana'] }
                    ]
                },
                {
                    group: '၂-ကိစ္စတတ်သော စိတ်များ (၂ ပါး)',
                    items: [
                        { name: 'မနောဒွါရာဝဇ္ဇန်း (၁)', kiccas: ['avajjana', 'votthapana'] },
                        { name: 'သောမနဿ သန္တီရဏ (၁)', kiccas: ['santirana', 'tadalambana'] }
                    ]
                },
                {
                    group: '၃-ကိစ္စတတ်သော စိတ်များ (၉ ပါး)',
                    items: [
                        { name: 'မဟဂ္ဂုတ် ဝိပါက် (၉)', kiccas: ['patisandhi', 'bhavanga', 'cuti'] }
                    ]
                },
                {
                    group: '၄-ကိစ္စတတ်သော စိတ်များ (၈ ပါး)',
                    items: [
                        { name: 'မဟာဝိပါက် (၈)', kiccas: ['patisandhi', 'bhavanga', 'cuti', 'tadalambana'] }
                    ]
                },
                {
                    group: '၅-ကိစ္စတတ်သော စိတ်များ (၂ ပါး)',
                    items: [
                        { name: 'ဥပေက္ခာ သန္တီရဏ (၂)', kiccas: ['patisandhi', 'bhavanga', 'cuti', 'santirana', 'tadalambana'] }
                    ]
                }
            ];

            const tbody = document.getElementById('kicca-matrix-tbody');
            if(tbody) {
                const cols = ['patisandhi', 'bhavanga', 'avajjana', 'dassana', 'savana', 'ghayana', 'sayana', 'phusana', 'sampaticchana', 'santirana', 'votthapana', 'javana', 'tadalambana', 'cuti'];
                const checkHtml = '<div class="w-5 h-5 mx-auto rounded bg-sky-100 dark:bg-sky-900/50 text-sky-600 dark:text-sky-400 flex items-center justify-center"><i class="fa-solid fa-check text-[10px]"></i></div>';
                const dash = '<span class="text-slate-200 dark:text-slate-700/50">-</span>';

                let html = '';
                kiccaData.forEach(g => {
                    html += \`<tr class="bg-slate-100/50 dark:bg-slate-800/30">
                        <td colspan="15" class="p-3 font-bold text-slate-600 dark:text-slate-400 text-xs tracking-wider sticky left-0 z-10">\${g.group}</td>
                    </tr>\`;
                    
                    g.items.forEach(item => {
                        html += \`<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">\`;
                        html += \`<td class="p-3 font-medium text-slate-800 dark:text-slate-200 sticky left-0 bg-white dark:bg-slate-900 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.3)] border-r border-slate-100 dark:border-slate-800 z-10">\${item.name}</td>\`;
                        
                        cols.forEach(c => {
                            if (item.kiccas.includes(c)) {
                                html += \`<td class="p-2 text-center align-middle border-r border-slate-100 dark:border-slate-800/50 bg-sky-50/30 dark:bg-sky-900/10">\${checkHtml}</td>\`;
                            } else {
                                html += \`<td class="p-2 text-center align-middle border-r border-slate-100 dark:border-slate-800/50">\${dash}</td>\`;
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
fs.writeFileSync('pakinnaka_sangaha.html', updatedHtml);
