import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert alphabetIndex div
html_replacement = """        </div>

        <div id="alphabetIndex" class="flex flex-wrap gap-2 justify-center mt-6"></div>

        <div id="glossaryList" class="w-full mt-8">"""

content = re.sub(r'        </div>\s*<div id="glossaryList" class="space-y-3 mt-8">', html_replacement, content)

# Replace JS logic
js_old = """        const searchInput = document.getElementById('searchInput');
        const clearBtn = document.getElementById('clearSearch');
        const listEl = document.getElementById('glossaryList');
        const countEl = document.getElementById('resultCount');

        function highlight(text, query) {
            if (!query) return text;
            const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
            return text.replace(regex, '<mark>$1</mark>');
        }

        function render(query = '') {
            const q = query.toLowerCase().trim();
            const filtered = terms.filter(t => t.term.toLowerCase().includes(q) || t.meaning.toLowerCase().includes(q));
            
            if (filtered.length === 0) {
                listEl.innerHTML = `<div class="text-center text-slate-500 dark:text-slate-500 py-8">ရှာဖွေမှု ရလဒ် မတွေ့ရှိပါ</div>`;
            } else {
                listEl.innerHTML = filtered.map(t => `
                    <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-center gap-2 md:gap-4">
                        <div class="md:w-1/3 font-bold text-emerald-700 dark:text-emerald-300 text-lg">
                            ${highlight(t.term, q)}
                        </div>
                        <div class="md:w-2/3 text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed">
                            ${highlight(t.meaning, q)}
                        </div>
                    </div>
                `).join('');
            }
            countEl.textContent = `စုစုပေါင်း ဝေါဟာရ (${filtered.length}) ခု ပြသထားပါသည်`;
            clearBtn.classList.toggle('hidden', q === '');
        }"""

js_new = """        const searchInput = document.getElementById('searchInput');
        const clearBtn = document.getElementById('clearSearch');
        const listEl = document.getElementById('glossaryList');
        const countEl = document.getElementById('resultCount');
        const alphabetIndexEl = document.getElementById('alphabetIndex');

        function getBaseLetter(str) {
            const firstChar = str.trim().charAt(0).toUpperCase();
            const map = { 'Ā': 'A', 'Ī': 'I', 'Ū': 'U', 'Ṭ': 'T', 'Ḍ': 'D', 'Ṇ': 'N', 'Ḷ': 'L', 'Ṁ': 'M', 'Ṅ': 'N', 'Ñ': 'N' };
            return map[firstChar] || firstChar;
        }

        function highlight(text, query) {
            if (!query) return text;
            const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
            return text.replace(regex, '<mark>$1</mark>');
        }

        function renderCard(t, q) {
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-center gap-2 md:gap-4">
                    <div class="md:w-1/3 font-bold text-emerald-700 dark:text-emerald-300 text-lg">
                        ${highlight(t.term, q)}
                    </div>
                    <div class="md:w-2/3 text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed">
                        ${highlight(t.meaning, q)}
                    </div>
                </div>
            `;
        }

        function render(query = '') {
            const q = query.toLowerCase().trim();
            const filtered = terms.filter(t => t.term.toLowerCase().includes(q) || t.meaning.toLowerCase().includes(q));
            
            if (filtered.length === 0) {
                listEl.innerHTML = `<div class="text-center text-slate-500 dark:text-slate-500 py-8">ရှာဖွေမှု ရလဒ် မတွေ့ရှိပါ</div>`;
                alphabetIndexEl.innerHTML = '';
            } else {
                let html = '';
                
                if (q === '') {
                    // Group by letter
                    const groups = {};
                    filtered.forEach(t => {
                        const letter = getBaseLetter(t.term);
                        if (!groups[letter]) groups[letter] = [];
                        groups[letter].push(t);
                    });
                    
                    // Render Index
                    const sortedLetters = Object.keys(groups).sort();
                    alphabetIndexEl.innerHTML = sortedLetters.map(letter => 
                        `<a href="#letter-${letter}" class="w-8 h-8 flex items-center justify-center rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-emerald-50 hover:border-emerald-300 hover:text-emerald-700 dark:hover:bg-emerald-900/30 dark:hover:border-emerald-700 dark:hover:text-emerald-400 text-sm font-bold transition shadow-sm">${letter}</a>`
                    ).join('');

                    // Render List
                    sortedLetters.forEach(letter => {
                        html += `<h3 id="letter-${letter}" class="text-2xl font-bold text-slate-800 dark:text-slate-200 mt-10 mb-4 border-b-2 border-emerald-500/20 dark:border-emerald-500/10 pb-2 scroll-mt-24 pl-2">${letter}</h3>`;
                        html += '<div class="space-y-3">';
                        html += groups[letter].map(t => renderCard(t, q)).join('');
                        html += '</div>';
                    });
                } else {
                    alphabetIndexEl.innerHTML = '';
                    html += '<div class="space-y-3">';
                    html += filtered.map(t => renderCard(t, q)).join('');
                    html += '</div>';
                }
                
                listEl.innerHTML = html;
            }
            countEl.textContent = `စုစုပေါင်း ဝေါဟာရ (${filtered.length}) ခု ပြသထားပါသည်`;
            clearBtn.classList.toggle('hidden', q === '');
        }"""

content = content.replace(js_old, js_new)

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")

