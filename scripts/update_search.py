import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML
old_html = """                    <div class="relative hidden sm:block">
                        <input type="text" id="search-input" placeholder="ရှာရန် (ဥပမာ- လောဘ)..." class="w-48 md:w-64 px-4 py-1.5 pl-9 text-sm rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-700 dark:text-slate-300 transition-all">
                        <i class="fa-solid fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 text-xs"></i>
                    </div>"""

new_html = """                    <div class="relative hidden sm:flex items-center gap-2">
                        <div class="relative">
                            <input type="text" id="search-input" placeholder="ရှာရန် (ဥပမာ- လောဘ)..." class="w-48 md:w-64 px-4 py-1.5 pl-9 text-sm rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-700 dark:text-slate-300 transition-all">
                            <i class="fa-solid fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 text-xs"></i>
                        </div>
                        <div id="search-controls" class="hidden items-center gap-1 text-sm text-slate-600 dark:text-slate-300">
                            <span id="search-counter" class="text-xs font-bold px-2 whitespace-nowrap">0 / 0</span>
                            <button id="search-prev" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-up text-xs"></i></button>
                            <button id="search-next" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-down text-xs"></i></button>
                        </div>
                    </div>"""

content = content.replace(old_html, new_html)

# Replace JS
old_js = """                // Search Functionality
                const searchInput = document.getElementById('search-input');
                
                function searchMap(query) {
                    query = query.toLowerCase();
                    
                    function resetAndCollapse(node, currentLevel = 0, maxLevel = 1) {
                        if (currentLevel >= maxLevel) {
                            if (!node.payload) node.payload = {};
                            node.payload.fold = 1; 
                        } else {
                            if (node.payload) node.payload.fold = 0;
                        }
                        if (node.children) {
                            node.children.forEach(child => resetAndCollapse(child, currentLevel + 1, maxLevel));
                        }
                    }

                    function unfoldMatching(node) {
                        let match = false;
                        if (node.content && node.content.toLowerCase().includes(query)) {
                            match = true;
                        }
                        
                        let childMatch = false;
                        if (node.children) {
                            for (let child of node.children) {
                                if (unfoldMatching(child)) {
                                    childMatch = true;
                                }
                            }
                        }
                        
                        if (query && (match || childMatch)) {
                            if (!node.payload) node.payload = {};
                            node.payload.fold = 0; // unfold
                            return true;
                        }
                        return match || childMatch;
                    }
                    
                    if (query) {
                        unfoldMatching(root);
                    } else {
                        resetAndCollapse(root);
                    }
                    
                    mm.setData(root);
                    mm.fit();
                    
                    setTimeout(() => {
                        const gs = document.querySelectorAll('#markmap g.markmap-node');
                        gs.forEach(g => {
                            const textEl = g.querySelector('text, foreignObject');
                            if (textEl && query && textEl.textContent.toLowerCase().includes(query)) {
                                g.classList.add('highlight-match');
                            } else {
                                g.classList.remove('highlight-match');
                            }
                        });
                    }, 600); // wait for animation
                }
                
                searchInput.addEventListener('input', (e) => {
                    searchMap(e.target.value);
                });"""

new_js = """                // Search Functionality
                const searchInput = document.getElementById('search-input');
                const searchControls = document.getElementById('search-controls');
                const searchCounter = document.getElementById('search-counter');
                const searchPrev = document.getElementById('search-prev');
                const searchNext = document.getElementById('search-next');
                
                let searchResults = [];
                let currentSearchIndex = -1;
                
                function resetAndCollapse(node, currentLevel = 0, maxLevel = 1) {
                    if (currentLevel >= maxLevel) {
                        if (!node.payload) node.payload = {};
                        node.payload.fold = 1; 
                    } else {
                        if (node.payload) node.payload.fold = 0;
                    }
                    if (node.children) {
                        node.children.forEach(child => resetAndCollapse(child, currentLevel + 1, maxLevel));
                    }
                }

                function searchMap(query) {
                    query = query.toLowerCase();
                    searchResults = [];
                    currentSearchIndex = -1;
                    
                    if (!query) {
                        searchControls.style.display = 'none';
                        resetAndCollapse(root);
                        mm.setData(root);
                        mm.fit();
                        highlightTarget(null);
                        return;
                    }
                    
                    // Traverse and find all matches, tracking parent paths
                    function findMatches(node, path) {
                        if (node.content && node.content.toLowerCase().includes(query)) {
                            searchResults.push({ node, path: [...path, node] });
                        }
                        if (node.children) {
                            node.children.forEach(child => findMatches(child, [...path, node]));
                        }
                    }
                    
                    findMatches(root, []);
                    
                    if (searchResults.length > 0) {
                        searchControls.style.display = 'flex';
                        currentSearchIndex = 0;
                        focusResult();
                    } else {
                        searchControls.style.display = 'none';
                        resetAndCollapse(root);
                        mm.setData(root);
                        mm.fit();
                        highlightTarget(null);
                    }
                }
                
                function focusResult() {
                    if (currentSearchIndex < 0 || currentSearchIndex >= searchResults.length) return;
                    
                    searchCounter.innerText = (currentSearchIndex + 1) + " / " + searchResults.length;
                    
                    // Fold everything first
                    resetAndCollapse(root);
                    
                    // Unfold the specific path
                    const path = searchResults[currentSearchIndex].path;
                    path.forEach(node => {
                        if (!node.payload) node.payload = {};
                        node.payload.fold = 0;
                    });
                    
                    mm.setData(root);
                    mm.fit();
                    
                    // Highlight ONLY the current target node
                    highlightTarget(searchResults[currentSearchIndex].node.content);
                }
                
                function highlightTarget(targetContent) {
                    setTimeout(() => {
                        const gs = document.querySelectorAll('#markmap g.markmap-node');
                        gs.forEach(g => {
                            const textEl = g.querySelector('text, foreignObject');
                            if (textEl && targetContent && textEl.textContent.trim() === targetContent.replace(/<[^>]*>?/gm, '').trim()) {
                                g.classList.add('highlight-match');
                            } else if (textEl && targetContent && textEl.textContent.includes(targetContent.replace(/<[^>]*>?/gm, ''))) {
                                // Fallback partial match if HTML tags exist
                                g.classList.add('highlight-match');
                            } else {
                                g.classList.remove('highlight-match');
                            }
                        });
                    }, 600); // wait for SVG render
                }
                
                searchInput.addEventListener('input', (e) => {
                    searchMap(e.target.value);
                });
                
                searchInput.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        if (searchResults.length > 0) {
                            currentSearchIndex = (currentSearchIndex + 1) % searchResults.length;
                            focusResult();
                        }
                    }
                });
                
                searchNext.addEventListener('click', () => {
                    if (searchResults.length > 0) {
                        currentSearchIndex = (currentSearchIndex + 1) % searchResults.length;
                        focusResult();
                    }
                });
                
                searchPrev.addEventListener('click', () => {
                    if (searchResults.length > 0) {
                        currentSearchIndex = (currentSearchIndex - 1 + searchResults.length) % searchResults.length;
                        focusResult();
                    }
                });"""

content = content.replace(old_js, new_js)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Search paginator added!")
