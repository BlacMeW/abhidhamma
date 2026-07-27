import re

map_html = """
        <!-- 31 Planes Interactive Map -->
        <details class="glass-card rounded-2xl p-4 md:p-6 max-w-4xl mx-auto border border-sky-500/30">
            <summary class="flex items-center justify-between font-bold text-sky-300 text-base md:text-lg">
                <span><i class="fa-solid fa-chevron-right tree-chevron mr-2 text-sm"></i>၃၁-ဘုံ အပြန်အလှန်လေ့လာနိုင်သော မြေပုံ (Interactive Map)</span>
                <span class="text-xs font-normal bg-sky-500/20 px-2 py-1 rounded">Click to expand</span>
            </summary>
            
            <div class="mt-6 pt-4 border-t border-slate-700/50">
                <p class="text-center text-xs text-slate-400 mb-6">ဘုံတစ်ခုစီကို နှိပ်၍ အသေးစိတ်ဖတ်ရှုနိုင်ပါသည်။</p>
                <div id="interactive-map-container" class="flex flex-col items-center gap-1 md:gap-2 w-full overflow-x-auto pb-4">
                    <!-- Rendered by JS -->
                </div>
            </div>
        </details>
"""

map_js = """
        function renderInteractiveMap() {
            const mapContainer = document.getElementById('interactive-map-container');
            if (!mapContainer) return;

            // Structure of planes (top to bottom)
            const mapStructure = [
                { group: 'arupabhumi', items: [31, 30, 29, 28], color: 'border-amber-500/50 bg-amber-500/10 hover:bg-amber-500/30 text-amber-300', title: 'အရူပဘုံ (၄) ဘုံ' },
                
                // Rupa planes (16)
                { group: 'rupabhumi', items: [27, 26, 25, 24, 23], color: 'border-emerald-500/50 bg-emerald-500/10 hover:bg-emerald-500/30 text-emerald-300', title: 'သုဒ္ဓါဝါသဘုံ (၅)' }, // Suddhavasa
                { group: 'rupabhumi', items: [22, 21], color: 'border-sky-500/50 bg-sky-500/10 hover:bg-sky-500/30 text-sky-300', title: 'စတုတ္ထဈာန်ဘုံ' }, 
                { group: 'rupabhumi', items: [20, 19, 18], color: 'border-sky-500/50 bg-sky-500/10 hover:bg-sky-500/30 text-sky-300', title: 'တတိယဈာန်ဘုံ (၃)' },
                { group: 'rupabhumi', items: [17, 16, 15], color: 'border-sky-500/50 bg-sky-500/10 hover:bg-sky-500/30 text-sky-300', title: 'ဒုတိယဈာန်ဘုံ (၃)' },
                { group: 'rupabhumi', items: [14, 13, 12], color: 'border-sky-500/50 bg-sky-500/10 hover:bg-sky-500/30 text-sky-300', title: 'ပဌမဈာန်ဘုံ (၃)' },
                
                // Kama Sugati planes (7)
                { group: 'kamabhumi_deva', items: [11, 10, 9, 8, 7, 6], color: 'border-indigo-500/50 bg-indigo-500/10 hover:bg-indigo-500/30 text-indigo-300', title: 'နတ်ဘုံ (၆)' },
                { group: 'kamabhumi_manussa', items: [5], color: 'border-violet-500/50 bg-violet-500/10 hover:bg-violet-500/30 text-violet-300', title: 'လူ့ဘုံ (၁)' },
                
                // Apaya planes (4)
                { group: 'apayabhumi', items: [4, 3, 2, 1], color: 'border-rose-500/50 bg-rose-500/10 hover:bg-rose-500/30 text-rose-300', title: 'အပါယ်ဘုံ (၄)' }
            ];

            let html = '';
            mapStructure.forEach((level) => {
                html += `
                    <div class="flex items-center gap-2 mb-2 w-full justify-center">
                        <div class="hidden md:block w-32 text-right text-[10px] uppercase text-slate-500 font-bold pr-4 border-r border-slate-700/50">\${level.title}</div>
                        <div class="flex flex-wrap items-center justify-center gap-1.5 md:gap-2 flex-1 max-w-2xl">
                `;
                
                level.items.forEach(id => {
                    const b = bhumiData.find(x => x.id === id);
                    if (b) {
                        html += `
                            <button onclick="openBhumiModal('\${b.key}')" 
                                class="vm-card flex flex-col items-center justify-center p-2 rounded-xl border \${level.color} transition-all w-20 h-20 sm:w-24 sm:h-24 md:w-28 md:h-28 shadow-lg">
                                <i class="fa-solid \${b.icon} text-lg md:text-xl mb-1 md:mb-2 opacity-80"></i>
                                <span class="text-[9px] md:text-[11px] font-bold text-center leading-tight">\${b.name}</span>
                                <span class="text-[8px] md:text-[9px] opacity-60 font-mono mt-0.5">#\${mm(b.id)}</span>
                            </button>
                        `;
                    }
                });
                
                html += `
                        </div>
                    </div>
                `;
            });
            
            mapContainer.innerHTML = html;
        }
"""

filename = 'vithimutta_sangaha.html'
with open(filename, 'r') as f:
    content = f.read()

# Insert HTML before bhumi-groups
content = re.sub(r'(<div id="bhumi-groups")', map_html + r'\n        \1', content)

# Insert JS before renderBhumiGroups
content = re.sub(r'(function renderBhumiGroups\(\) \{)', map_js + r'\n        \1', content)

# Call renderInteractiveMap in init
content = re.sub(r'(renderBhumiGroups\(\);)', r'\1\n        renderInteractiveMap();', content)

with open(filename, 'w') as f:
    f.write(content)
print("Added 31 planes map successfully!")
