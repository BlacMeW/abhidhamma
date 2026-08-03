import re
import json

with open("glossary.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Extract the terms array
start_str = "const terms = ["
end_str = "];"
start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find terms array")
    exit(1)

terms_text = content[start_idx:end_idx+2]
html_before = content[:start_idx]
html_after = content[end_idx+2:]

# 2. Modify the HTML to include new UI controls
# Let's find the search bar area
search_bar_end = html_before.find('<div id="resultCount"')

if search_bar_end != -1:
    # Inject UI controls before resultCount
    ui_controls = """
            <!-- Feature Controls -->
            <div class="max-w-4xl mx-auto mt-6 space-y-4">
                <!-- Categories -->
                <div class="flex items-center gap-2 overflow-x-auto pb-2 hide-scrollbar" id="categoryFilters">
                    <button class="filter-btn active" data-cat="all">All</button>
                    <button class="filter-btn text-amber-500" data-cat="favorites"><i class="fa-solid fa-star"></i> Favorites</button>
                    <button class="filter-btn" data-cat="citta">စိတ် (Citta)</button>
                    <button class="filter-btn" data-cat="cetasika">စေတသိက် (Cetasika)</button>
                    <button class="filter-btn" data-cat="rupa">ရုပ် (Rupa)</button>
                    <button class="filter-btn" data-cat="paccaya">ပစ္စည်း (Paccaya)</button>
                    <button class="filter-btn" data-cat="kammatthana">ကမ္မဋ္ဌာန်း (Kammaṭṭhāna)</button>
                    <button class="filter-btn" data-cat="kilesa">ကိလေသာ (Kilesa)</button>
                    <button class="filter-btn" data-cat="misc">အခြား (Misc)</button>
                </div>
                
                <!-- View Toggles -->
                <div class="flex items-center justify-between border-t border-slate-200 dark:border-slate-700 pt-4">
                    <div id="resultCount" class="text-sm font-medium text-slate-500 dark:text-slate-400"></div>
                    
                    <div class="flex items-center gap-2 bg-slate-100 dark:bg-slate-800 p-1 rounded-lg">
                        <button class="view-btn active" data-view="list" title="List View"><i class="fa-solid fa-list"></i></button>
                        <button class="view-btn" data-view="grid" title="Grid View"><i class="fa-solid fa-border-all"></i></button>
                        <button class="view-btn text-indigo-500" data-view="flashcard" title="Flashcard Mode"><i class="fa-solid fa-clone"></i></button>
                    </div>
                </div>
            </div>
"""
    # We replace the original resultCount with the new UI block that contains resultCount
    html_before = html_before[:search_bar_end] + ui_controls + "\n"

# 3. Add CSS for new features in <head>
css_additions = """
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        
        .filter-btn {
            white-space: nowrap;
            padding: 0.4rem 1rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            background: rgba(241, 245, 249, 0.5); /* slate-100 */
            border: 1px solid rgba(226, 232, 240, 0.8); /* slate-200 */
            color: #64748b; /* slate-500 */
            transition: all 0.2s;
            cursor: pointer;
        }
        .dark .filter-btn {
            background: rgba(30, 41, 59, 0.5); /* slate-800 */
            border-color: rgba(51, 65, 85, 0.8); /* slate-700 */
            color: #94a3b8; /* slate-400 */
        }
        .filter-btn:hover { background: #e2e8f0; color: #334155; }
        .dark .filter-btn:hover { background: #334155; color: #cbd5e1; }
        .filter-btn.active {
            background: #10b981; /* emerald-500 */
            border-color: #10b981;
            color: white;
            box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.2);
        }
        .dark .filter-btn.active {
            background: #059669; /* emerald-600 */
            border-color: #059669;
        }

        .view-btn {
            padding: 0.4rem 0.75rem;
            border-radius: 0.5rem;
            color: #64748b;
            transition: all 0.2s;
            cursor: pointer;
        }
        .dark .view-btn { color: #94a3b8; }
        .view-btn:hover { color: #0f172a; background: #e2e8f0; }
        .dark .view-btn:hover { color: #f8fafc; background: #334155; }
        .view-btn.active {
            background: white;
            color: #10b981;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .dark .view-btn.active {
            background: #1e293b;
            color: #34d399;
            box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        }

        /* Grid Layout */
        .layout-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1rem;
        }
        .layout-grid .glass-card {
            flex-direction: column !important;
            height: 100%;
        }
        .layout-grid .md\\:w-1\\/3 { width: 100%; padding-bottom: 0.5rem; border-bottom: 1px solid rgba(0,0,0,0.05); }
        .dark .layout-grid .md\\:w-1\\/3 { border-color: rgba(255,255,255,0.05); }
        .layout-grid .md\\:w-2\\/3 { width: 100%; margin-top: 0.5rem; }

        /* Flashcard Mode */
        .flashcard-container {
            perspective: 1000px;
            width: 100%;
            max-width: 32rem;
            margin: 2rem auto;
            height: 24rem;
        }
        .flashcard {
            width: 100%;
            height: 100%;
            position: relative;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            cursor: pointer;
        }
        .flashcard.is-flipped {
            transform: rotateY(180deg);
        }
        .flashcard-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            text-align: center;
            border-radius: 1.5rem;
            background: white;
            border: 2px solid #e2e8f0;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        }
        .dark .flashcard-face {
            background: #1e293b;
            border-color: #334155;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        }
        .flashcard-back {
            transform: rotateY(180deg);
            background: linear-gradient(to bottom right, #f8fafc, #f1f5f9);
        }
        .dark .flashcard-back {
            background: linear-gradient(to bottom right, #1e293b, #0f172a);
        }
        
        .bookmark-btn {
            transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .bookmark-btn:hover { transform: scale(1.1); }
        .bookmark-btn.active { color: #f59e0b; /* amber-500 */ }
"""

head_end = html_before.find('</style>\n</head>')
if head_end != -1:
    html_before = html_before[:head_end] + css_additions + "\n" + html_before[head_end:]
else:
    head_end_fallback = html_before.find('</head>')
    html_before = html_before[:head_end_fallback] + "<style>" + css_additions + "</style>\n" + html_before[head_end_fallback:]

# 4. Process and categorize terms in JavaScript
# We will just write a new <script> block and replace the whole html_after
new_script = """
    <script>
        // Load Terms
        const originalTerms = """ + terms_text.strip() + """;
        
        // Add ID and Categories
        let terms = originalTerms.map(t => {
            // Generate simple ID
            const id = 'term_' + t.term.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
            t.id = id;
            
            // Auto Categorize based on links or keywords
            let cat = 'misc';
            const linksStr = JSON.stringify(t.links || []).toLowerCase();
            const textStr = (t.term + ' ' + t.meaning).toLowerCase();
            
            if (linksStr.includes('citta') || textStr.includes('စိတ်')) cat = 'citta';
            else if (linksStr.includes('cetasika') || textStr.includes('စေတသိက်')) cat = 'cetasika';
            else if (linksStr.includes('rūpa') || textStr.includes('ရုပ်')) cat = 'rupa';
            else if (linksStr.includes('paccaya') || linksStr.includes('paṭiccasamuppāda')) cat = 'paccaya';
            else if (linksStr.includes('kammaṭṭhāna')) cat = 'kammatthana';
            else if (linksStr.includes('kilesa') || textStr.includes('ကိလေသာ')) cat = 'kilesa';
            
            t.category = cat;
            return t;
        });

        // Add related terms dynamically based on category and shared keywords
        terms.forEach(t => {
            t.related = terms
                .filter(other => other.id !== t.id && (other.category === t.category || t.meaning.includes(other.term.split(' ')[0])))
                .slice(0, 3)
                .map(other => other.id);
        });

        // State
        let currentView = 'list'; // list, grid, flashcard
        let currentCategory = 'all';
        let searchQuery = '';
        let flashcardIndex = 0;
        let filteredTerms = [...terms];
        
        // Bookmarks
        let bookmarks = JSON.parse(localStorage.getItem('abhidhamma_bookmarks') || '[]');

        // DOM Elements
        const searchInput = document.getElementById('searchInput');
        const clearBtn = document.getElementById('clearSearch');
        const listEl = document.getElementById('glossaryList');
        const countEl = document.getElementById('resultCount');
        const alphabetIndexEl = document.getElementById('alphabetIndex');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const viewBtns = document.querySelectorAll('.view-btn');

        function toggleBookmark(id, event) {
            if(event) {
                event.stopPropagation();
                event.preventDefault();
            }
            if (bookmarks.includes(id)) {
                bookmarks = bookmarks.filter(b => b !== id);
            } else {
                bookmarks.push(id);
            }
            localStorage.setItem('abhidhamma_bookmarks', JSON.stringify(bookmarks));
            render(); // Re-render to update UI
        }

        function getBaseLetter(str) {
            const firstChar = str.trim().charAt(0).toUpperCase();
            const map = { 'Ā': 'A', 'Ī': 'I', 'Ū': 'U', 'Ṭ': 'T', 'Ḍ': 'D', 'Ṇ': 'N', 'Ḷ': 'L', 'Ṁ': 'M', 'Ṅ': 'N', 'Ñ': 'N' };
            return map[firstChar] || firstChar;
        }

        // Fuzzy match function
        function fuzzyMatch(str, pattern) {
            if (!pattern) return true;
            pattern = pattern.toLowerCase().replace(/\\s+/g, '');
            str = str.toLowerCase().replace(/\\s+/g, '');
            
            // Exact match
            if (str.includes(pattern)) return true;
            
            // Simple subset character match for slight typos (e.g. ဉာဏ် vs ညဏ်)
            // Just checks if letters appear in order
            let patternIdx = 0;
            for (let i = 0; i < str.length && patternIdx < pattern.length; i++) {
                if (str[i] === pattern[patternIdx]) {
                    patternIdx++;
                }
            }
            return patternIdx === pattern.length;
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
            
            let relatedHtml = '';
            if (t.related && t.related.length > 0) {
                const relTerms = t.related.map(rid => terms.find(x => x.id === rid)).filter(Boolean);
                relatedHtml = '<div class="mt-3 flex flex-wrap gap-1.5 items-center"><span class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Related:</span> ' + 
                    relTerms.map(rt => `<span class="inline-flex items-center text-[11px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 cursor-help" title="${rt.meaning}">${rt.term.split(' ')[0]}</span>`).join('') + '</div>';
            }
            
            const isBookmarked = bookmarks.includes(t.id);
            const bkmIcon = isBookmarked ? 'fa-solid text-amber-500' : 'fa-regular text-slate-300 dark:text-slate-600';
            
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-start gap-2 md:gap-4 relative group">
                    <button onclick="toggleBookmark('${t.id}', event)" class="bookmark-btn absolute top-4 right-4 text-lg ${bkmIcon} hover:text-amber-500 z-10" title="Bookmark">
                        <i class="fa-star"></i>
                    </button>
                    <div class="md:w-1/3 pt-1 pr-6">
                        <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg">${highlight(t.term, q)}</div>
                        <span class="inline-block mt-1 text-[10px] uppercase tracking-wider font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">${t.category}</span>
                    </div>
                    <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
                        <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed pr-6">
                            ${highlight(t.meaning, q)}
                        </div>
                        ${linksHtml}
                        ${relatedHtml}
                    </div>
                </div>
            `;
        }
        
        function renderFlashcard() {
            if (filteredTerms.length === 0) {
                listEl.innerHTML = `<div class="text-center text-slate-500 py-12">No terms found for studying in this category/search.</div>`;
                return;
            }
            if (flashcardIndex >= filteredTerms.length) flashcardIndex = 0;
            if (flashcardIndex < 0) flashcardIndex = filteredTerms.length - 1;
            
            const t = filteredTerms[flashcardIndex];
            const isBookmarked = bookmarks.includes(t.id);
            const bkmIcon = isBookmarked ? 'fa-solid text-amber-500' : 'fa-regular text-slate-300 dark:text-slate-600';
            
            listEl.innerHTML = `
                <div class="flex flex-col items-center">
                    <div class="text-sm text-slate-500 font-medium mb-2">Card ${flashcardIndex + 1} of ${filteredTerms.length}</div>
                    
                    <div class="flashcard-container" onclick="this.querySelector('.flashcard').classList.toggle('is-flipped')">
                        <div class="flashcard shadow-lg rounded-2xl">
                            <!-- Front -->
                            <div class="flashcard-face">
                                <button onclick="toggleBookmark('${t.id}', event)" class="bookmark-btn absolute top-6 right-6 text-2xl ${bkmIcon} hover:text-amber-500 z-10" title="Bookmark">
                                    <i class="fa-star"></i>
                                </button>
                                <span class="absolute top-6 left-6 text-xs uppercase tracking-widest font-bold text-emerald-600/50 dark:text-emerald-400/50 bg-emerald-50 dark:bg-emerald-900/20 px-3 py-1 rounded-full">${t.category}</span>
                                
                                <h2 class="text-3xl md:text-4xl font-bold text-emerald-800 dark:text-emerald-300 leading-tight">${t.term}</h2>
                                <p class="text-sm text-slate-400 mt-6"><i class="fa-solid fa-hand-pointer animate-pulse"></i> Click to flip</p>
                            </div>
                            
                            <!-- Back -->
                            <div class="flashcard-face flashcard-back">
                                <h3 class="text-xl md:text-2xl font-bold text-slate-800 dark:text-slate-100 mb-6 leading-relaxed px-4">${t.meaning}</h3>
                                <div class="w-12 h-1 bg-emerald-500/30 rounded-full mx-auto mb-6"></div>
                                <p class="text-sm text-slate-400"><i class="fa-solid fa-hand-pointer animate-pulse"></i> Click to flip back</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex items-center gap-4 mt-6">
                        <button onclick="flashcardIndex--; renderCore();" class="w-12 h-12 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow flex items-center justify-center hover:bg-slate-50 dark:hover:bg-slate-700 transition">
                            <i class="fa-solid fa-arrow-left"></i>
                        </button>
                        <button onclick="flashcardIndex = Math.floor(Math.random() * filteredTerms.length); renderCore();" class="w-12 h-12 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow flex items-center justify-center hover:text-emerald-500 transition" title="Random Card">
                            <i class="fa-solid fa-shuffle"></i>
                        </button>
                        <button onclick="flashcardIndex++; renderCore();" class="w-12 h-12 rounded-full bg-emerald-500 hover:bg-emerald-600 text-white shadow-md flex items-center justify-center transition">
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            `;
            if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
        }

        function filterData() {
            filteredTerms = terms.filter(t => {
                // Category Filter
                if (currentCategory === 'favorites' && !bookmarks.includes(t.id)) return false;
                if (currentCategory !== 'all' && currentCategory !== 'favorites' && t.category !== currentCategory) return false;
                
                // Search Filter
                if (searchQuery) {
                    return fuzzyMatch(t.term, searchQuery) || fuzzyMatch(t.meaning, searchQuery);
                }
                return true;
            });
        }

        function renderCore() {
            if (currentView === 'flashcard') {
                renderFlashcard();
            } else {
                if (filteredTerms.length === 0) {
                    listEl.innerHTML = `<div class="text-center text-slate-500 dark:text-slate-500 py-12 flex flex-col items-center"><i class="fa-solid fa-ghost text-4xl mb-4 opacity-50"></i><span>ရှာဖွေမှု ရလဒ် မတွေ့ရှိပါ</span></div>`;
                    if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
                } else {
                    let html = `<div class="${currentView === 'grid' ? 'layout-grid' : 'space-y-4'} w-full">`;
                    
                    if (searchQuery === '' && currentCategory === 'all' && currentView === 'list') {
                        // Group by letter for default view
                        const groups = {};
                        filteredTerms.forEach(t => {
                            const letter = getBaseLetter(t.term);
                            if (!groups[letter]) groups[letter] = [];
                            groups[letter].push(t);
                        });
                        
                        // Render Index
                        const sortedLetters = Object.keys(groups).sort();
                        if(alphabetIndexEl) {
                            alphabetIndexEl.innerHTML = sortedLetters.map(letter => 
                                `<a href="#letter-${letter}" class="w-9 h-9 flex items-center justify-center rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-emerald-50 hover:border-emerald-300 hover:text-emerald-700 dark:hover:bg-emerald-900/30 dark:hover:border-emerald-700 dark:hover:text-emerald-400 text-sm font-bold transition shadow-sm">${letter}</a>`
                            ).join('');
                        }

                        // Render List
                        sortedLetters.forEach(letter => {
                            html += `<h3 id="letter-${letter}" class="text-2xl font-bold text-slate-800 dark:text-slate-200 mt-10 mb-4 border-b-2 border-emerald-500/20 dark:border-emerald-500/10 pb-2 scroll-mt-24 pl-2">${letter}</h3>`;
                            html += '<div class="space-y-4">';
                            html += groups[letter].map(t => renderCard(t, searchQuery)).join('');
                            html += '</div>';
                        });
                    } else {
                        if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
                        html += filteredTerms.map(t => renderCard(t, searchQuery)).join('');
                    }
                    html += `</div>`;
                    listEl.innerHTML = html;
                }
            }
            
            countEl.textContent = `စုစုပေါင်း ဝေါဟာရ (${filteredTerms.length}) ခု ပြသထားပါသည်`;
            clearBtn.classList.toggle('hidden', searchQuery === '');
        }

        function render(query = searchQuery) {
            searchQuery = query.toLowerCase().trim();
            filterData();
            renderCore();
        }

        // Event Listeners
        searchInput.addEventListener('input', (e) => render(e.target.value));
        
        clearBtn.addEventListener('click', () => {
            searchInput.value = '';
            render('');
            searchInput.focus();
        });

        filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                filterBtns.forEach(b => b.classList.remove('active', 'bg-emerald-500', 'text-white'));
                e.currentTarget.classList.add('active');
                currentCategory = e.currentTarget.dataset.cat;
                flashcardIndex = 0; // reset
                render();
            });
        });

        viewBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                viewBtns.forEach(b => b.classList.remove('active'));
                const targetBtn = e.currentTarget.closest('.view-btn');
                targetBtn.classList.add('active');
                currentView = targetBtn.dataset.view;
                renderCore();
            });
        });

        // Initialize Bookmarks state in filter UI
        const favBtn = document.querySelector('[data-cat="favorites"]');
        if (favBtn) {
            setInterval(() => {
                const favCount = bookmarks.length;
                if (favCount > 0 && currentCategory !== 'favorites') {
                    favBtn.innerHTML = `<i class="fa-solid fa-star"></i> Favorites (${favCount})`;
                } else {
                    favBtn.innerHTML = `<i class="fa-solid fa-star"></i> Favorites`;
                }
            }, 1000);
        }

        // Init
        render();
    </script>
    <script src="accessibility.js"></script>
</body>
</html>
"""

# Let's find where the script starts to replace it
script_start = html_after.find('<script>')
if script_start != -1:
    # Because there are two scripts (one for terms, one for accessibility), we replace everything from <script> to the end, but we already have accessibility.js in new_script.
    html_after_new = new_script
else:
    html_after_new = new_script

with open("glossary_new.html", "w", encoding="utf-8") as f:
    f.write(html_before + html_after_new)
print("Processed successfully!")
