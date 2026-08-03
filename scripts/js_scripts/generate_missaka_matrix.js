const fs = require('fs');

const html = fs.readFileSync('missaka_sangaha.html', 'utf8');

const matrixCode = `
        <!-- Matrix Table Section -->
        <div class="mt-16 mb-8 text-center max-w-3xl mx-auto space-y-2">
            <h2 class="text-2xl md:text-3xl font-bold"><i class="fa-solid fa-table-cells text-violet-500 mr-2"></i> မိဿကရုပ်ခွဲ ဇယားကြီး</h2>
            <p class="text-slate-600 dark:text-slate-400 text-sm">
                တရားကိုယ် (၆၄) ပါးလုံးကို ၎င်းတို့၏ မူလ အခြေခံ ပရမတ္ထတရား (၃၅) မျိုးဖြင့် ချိန်ထိုးပြသထားသော ဇယား (Mapping Table) ဖြစ်ပါသည်။ မည်သည့်တရားက မည်သည့်အုပ်စုတွင် ပါဝင်ကြောင်း လေ့လာနိုင်ပါသည်။
            </p>
        </div>

        <div class="glass-card rounded-2xl border border-slate-200 dark:border-slate-700 overflow-x-auto shadow-sm mb-12">
            <table class="w-full text-left text-sm whitespace-nowrap">
                <thead>
                    <tr class="bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-700">
                        <th class="p-4 font-bold text-slate-700 dark:text-slate-300 w-48 sticky left-0 bg-slate-50 dark:bg-slate-800/90 z-10 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.1)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.5)]">အခြေခံ ပရမတ္ထတရား</th>
                        <th class="p-4 font-bold text-center text-rose-700 dark:text-rose-400">ဟေတု<br><span class="text-[10px] font-normal text-slate-500">(၆)</span></th>
                        <th class="p-4 font-bold text-center text-sky-700 dark:text-sky-400">ဈာနင်္ဂ<br><span class="text-[10px] font-normal text-slate-500">(၇)</span></th>
                        <th class="p-4 font-bold text-center text-emerald-700 dark:text-emerald-400">မဂ္ဂင်္ဂ<br><span class="text-[10px] font-normal text-slate-500">(၁၂)</span></th>
                        <th class="p-4 font-bold text-center text-amber-700 dark:text-amber-400">ဣန္ဒြိယ<br><span class="text-[10px] font-normal text-slate-500">(၂၂)</span></th>
                        <th class="p-4 font-bold text-center text-violet-700 dark:text-violet-400">ဗလ<br><span class="text-[10px] font-normal text-slate-500">(၉)</span></th>
                        <th class="p-4 font-bold text-center text-indigo-700 dark:text-indigo-400">အဓိပတိ<br><span class="text-[10px] font-normal text-slate-500">(၄)</span></th>
                        <th class="p-4 font-bold text-center text-fuchsia-700 dark:text-fuchsia-400">အာဟာရ<br><span class="text-[10px] font-normal text-slate-500">(၄)</span></th>
                    </tr>
                </thead>
                <tbody id="matrix-tbody" class="divide-y divide-slate-100 dark:divide-slate-800/50">
                    <!-- Rows will be injected by JS -->
                </tbody>
            </table>
        </div>
`;

// Insert just before </main>
const updatedHtml = html.replace('    </main>', matrixCode + '\n    </main>');

// Script for matrix logic
const scriptCode = `
        const baseParamatthas = [
            { category: 'စိတ် (Citta)', items: [
                { name: 'စိတ် (၈၉) ပါး', map: { indriya: ['မနိန္ဒြေ'], adhipati: ['စိတ္တာဓိပတိ'], ahara: ['ဝိညာဏာဟာရ'] } }
            ]},
            { category: 'အညသမာန်း စေတသိက် (၁၃)', items: [
                { name: 'ဝေဒနာ', map: { jhananga: ['သောမနဿ', 'ဒေါမနဿ', 'ဥပေက္ခာ'], indriya: ['သုခ', 'ဒုက္ခ', 'သောမနဿ', 'ဒေါမနဿ', 'ဥပေက္ခာ'] } },
                { name: 'ဧကဂ္ဂတာ (သမာဓိ)', map: { jhananga: ['ဧကဂ္ဂတာ'], magganga: ['သမ္မာသမာဓိ', 'မိစ္ဆာသမာဓိ'], indriya: ['သမာဓိန္ဒြေ'], bala: ['သမာဓိဗလ'] } },
                { name: 'ဝီရိယ', map: { magganga: ['သမ္မာဝါယာမ', 'မိစ္ဆာဝါယာမ'], indriya: ['ဝီရိယိန္ဒြေ'], bala: ['ဝီရိယဗလ'], adhipati: ['ဝီရိယာဓိပတိ'] } },
                { name: 'ဝိတက်', map: { jhananga: ['ဝိတက်'], magganga: ['သမ္မာသင်္ကပ္ပ', 'မိစ္ဆာသင်္ကပ္ပ'] } },
                { name: 'ဇီဝိတ (နာမ်)', map: { indriya: ['ဇီဝိတိန္ဒြေ (နာမ်)'] } },
                { name: 'ဖဿ', map: { ahara: ['ဖဿာဟာရ'] } },
                { name: 'စေတနာ', map: { ahara: ['မနောသဉ္စေတနာဟာရ'] } },
                { name: 'ဝိစာရ', map: { jhananga: ['ဝိစာရ'] } },
                { name: 'ပီတိ', map: { jhananga: ['ပီတိ'] } },
                { name: 'ဆန္ဒ', map: { adhipati: ['ဆန္ဒာဓိပတိ'] } }
            ]},
            { category: 'အကုသိုလ် စေတသိက် (၁၄)', items: [
                { name: 'လောဘ', map: { hetu: ['လောဘ'] } },
                { name: 'ဒေါသ', map: { hetu: ['ဒေါသ'] } },
                { name: 'မောဟ', map: { hetu: ['မောဟ'] } },
                { name: 'ဒိဋ္ဌိ', map: { magganga: ['မိစ္ဆာဒိဋ္ဌိ'] } },
                { name: 'အဟိရိက', map: { bala: ['အဟိရိကဗလ'] } },
                { name: 'အနောတ္တပ္ပ', map: { bala: ['အနောတ္တပ္ပဗလ'] } }
            ]},
            { category: 'သောဘဏ စေတသိက် (၂၅)', items: [
                { name: 'ပညာ (အမောဟ)', map: { hetu: ['အမောဟ'], magganga: ['သမ္မာဒိဋ္ဌိ'], indriya: ['ပညိန္ဒြေ', 'အနညတညဿာမီတိန္ဒြေ', 'အညိန္ဒြေ', 'အညာတာဝိန္ဒြေ'], bala: ['ပညာဗလ'], adhipati: ['ဝီမံသာဓိပတိ'] } },
                { name: 'သတိ', map: { magganga: ['သမ္မာသတိ'], indriya: ['သတိန္ဒြေ'], bala: ['သတိဗလ'] } },
                { name: 'သဒ္ဓါ', map: { indriya: ['သဒ္ဓိန္ဒြေ'], bala: ['သဒ္ဓါဗလ'] } },
                { name: 'အလောဘ', map: { hetu: ['အလောဘ'] } },
                { name: 'အဒေါသ', map: { hetu: ['အဒေါသ'] } },
                { name: 'သမ္မာဝါစာ', map: { magganga: ['သမ္မာဝါစာ'] } },
                { name: 'သမ္မာကမ္မန္တ', map: { magganga: ['သမ္မာကမ္မန္တ'] } },
                { name: 'သမ္မာအာဇီဝ', map: { magganga: ['သမ္မာအာဇီဝ'] } },
                { name: 'ဟိရီ', map: { bala: ['ဟိရီဗလ'] } },
                { name: 'ဩတ္တပ္ပ', map: { bala: ['ဩတ္တပ္ပဗလ'] } }
            ]},
            { category: 'ရုပ် (Rupa)', items: [
                { name: 'ပသာဒရုပ် (၅) ပါး', map: { indriya: ['စက္ခုန္ဒြေ', 'သောတိန္ဒြေ', 'ဃာနိန္ဒြေ', 'ဇိဝှိန္ဒြေ', 'ကာယိန္ဒြေ'] } },
                { name: 'ဘာဝရုပ် (၂) ပါး', map: { indriya: ['ဣတ္ထိန္ဒြေ', 'ပုရိသိန္ဒြေ'] } },
                { name: 'ဇီဝိတရုပ်', map: { indriya: ['ဇီဝိတိန္ဒြေ (ရုပ်)'] } },
                { name: 'ဩဇာ (ရုပ်အစာ)', map: { ahara: ['ကဗဠီကာရာဟာရ'] } }
            ]}
        ];

        function renderMatrix() {
            const tbody = document.getElementById('matrix-tbody');
            const groups = ['hetu', 'jhananga', 'magganga', 'indriya', 'bala', 'adhipati', 'ahara'];
            
            const groupColors = {
                hetu: 'bg-rose-500/10 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800/30',
                jhananga: 'bg-sky-500/10 text-sky-700 dark:text-sky-300 border-sky-200 dark:border-sky-800/30',
                magganga: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800/30',
                indriya: 'bg-amber-500/10 text-amber-700 dark:text-amber-300 border-amber-200 dark:border-amber-800/30',
                bala: 'bg-violet-500/10 text-violet-700 dark:text-violet-300 border-violet-200 dark:border-violet-800/30',
                adhipati: 'bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800/30',
                ahara: 'bg-fuchsia-500/10 text-fuchsia-700 dark:text-fuchsia-300 border-fuchsia-200 dark:border-fuchsia-800/30'
            };

            let html = '';
            
            baseParamatthas.forEach(category => {
                html += \`
                    <tr class="bg-slate-100/50 dark:bg-slate-800/30">
                        <td colspan="8" class="p-3 font-bold text-slate-600 dark:text-slate-400 text-xs tracking-wider sticky left-0 z-10">\${category.category}</td>
                    </tr>
                \`;
                
                category.items.forEach(item => {
                    html += \`<tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">\`;
                    html += \`<td class="p-3 font-medium text-slate-800 dark:text-slate-200 sticky left-0 bg-white dark:bg-slate-900 shadow-[2px_0_5px_-2px_rgba(0,0,0,0.05)] dark:shadow-[2px_0_5px_-2px_rgba(0,0,0,0.3)] z-10">\${item.name}</td>\`;
                    
                    groups.forEach(g => {
                        if (item.map[g]) {
                            const labels = item.map[g].map(l => \`<span class="inline-block px-2 py-1 m-0.5 rounded-md border text-[11px] font-semibold \${groupColors[g]} shadow-sm">\${l}</span>\`).join('');
                            html += \`<td class="p-2 text-center align-middle">\${labels}</td>\`;
                        } else {
                            html += \`<td class="p-2 text-center align-middle"><span class="w-1.5 h-1.5 rounded-full bg-slate-200 dark:bg-slate-800 inline-block"></span></td>\`;
                        }
                    });
                    
                    html += \`</tr>\`;
                });
            });
            
            tbody.innerHTML = html;
        }
`;

const finalHtml = updatedHtml.replace("container.innerHTML += renderGroup(k);\n            });", "container.innerHTML += renderGroup(k);\n            });\n            renderMatrix();\n        });\n\n" + scriptCode);

fs.writeFileSync('missaka_sangaha_matrix.html', finalHtml);
