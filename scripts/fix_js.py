import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_new = """
        const searchInput = document.getElementById('searchInput');
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
            let linksHtml = '';
            if (t.links && t.links.length > 0) {
                linksHtml = '<div class="mt-3 flex flex-wrap gap-2">' + t.links.map(l => 
                    `<a href="${l.url}" class="inline-flex items-center gap-1 text-[11px] font-medium px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-700 hover:bg-emerald-100 dark:bg-emerald-500/10 dark:text-emerald-300 dark:hover:bg-emerald-500/20 transition-colors border border-emerald-200/50 dark:border-emerald-500/20"><i class="fa-solid fa-link text-[9px] opacity-70"></i> ${l.name}</a>`
                ).join('') + '</div>';
            }
            
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-start gap-2 md:gap-4">
                    <div class="md:w-1/3 pt-1">
                        <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg">${highlight(t.term, q)}</div>
                    </div>
                    <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
                        <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed">
                            ${highlight(t.meaning, q)}
                        </div>
                        ${linksHtml}
                    </div>
                </div>
            `;
        }

        function render(query = '') {
            const q = query.toLowerCase().trim();
            const filtered = terms.filter(t => t.term.toLowerCase().includes(q) || t.meaning.toLowerCase().includes(q));
            
            if (filtered.length === 0) {
                listEl.innerHTML = `<div class="text-center text-slate-500 dark:text-slate-500 py-8">ရှာဖွေမှု ရလဒ် မတွေ့ရှိပါ</div>`;
                if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
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
                    if(alphabetIndexEl) {
                        alphabetIndexEl.innerHTML = sortedLetters.map(letter => 
                            `<a href="#letter-${letter}" class="w-8 h-8 flex items-center justify-center rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-emerald-50 hover:border-emerald-300 hover:text-emerald-700 dark:hover:bg-emerald-900/30 dark:hover:border-emerald-700 dark:hover:text-emerald-400 text-sm font-bold transition shadow-sm">${letter}</a>`
                        ).join('');
                    }

                    // Render List
                    sortedLetters.forEach(letter => {
                        html += `<h3 id="letter-${letter}" class="text-2xl font-bold text-slate-800 dark:text-slate-200 mt-10 mb-4 border-b-2 border-emerald-500/20 dark:border-emerald-500/10 pb-2 scroll-mt-24 pl-2">${letter}</h3>`;
                        html += '<div class="space-y-3">';
                        html += groups[letter].map(t => renderCard(t, q)).join('');
                        html += '</div>';
                    });
                } else {
                    if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
                    html += '<div class="space-y-3">';
                    html += filtered.map(t => renderCard(t, q)).join('');
                    html += '</div>';
                }
                
                listEl.innerHTML = html;
            }
            countEl.textContent = `စုစုပေါင်း ဝေါဟာရ (${filtered.length}) ခု ပြသထားပါသည်`;
            clearBtn.classList.toggle('hidden', q === '');
        }

        searchInput.addEventListener('input', (e) => render(e.target.value));
        clearBtn.addEventListener('click', () => {
            searchInput.value = '';
            render();
            searchInput.focus();
        });

        // Init
        render();
"""

# Replace everything from `const searchInput =` to `// Init\n        render();`
pattern = r"const searchInput = document\.getElementById\('searchInput'\);.*// Init\s+render\(\);"
new_content = re.sub(pattern, js_new.strip(), content, flags=re.DOTALL)

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Fixed JS successfully")

