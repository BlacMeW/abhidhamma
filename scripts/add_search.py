import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Search Input to Navbar
nav_search = """                    <div class="relative hidden sm:block">
                        <input type="text" id="search-input" placeholder="ရှာရန် (ဥပမာ- လောဘ)..." class="w-48 md:w-64 px-4 py-1.5 pl-9 text-sm rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-700 dark:text-slate-300 transition-all">
                        <i class="fa-solid fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 text-xs"></i>
                    </div>
                    <button id="theme-toggle\""""

content = content.replace('                    <button id="theme-toggle"', nav_search)

# 2. Add Search CSS
search_css = """        .map-btn:hover { background: rgba(99, 102, 241, 0.8); color: white; border-color: transparent; }
        
        .highlight-match text, .highlight-match tspan, .highlight-match div, .highlight-match span {
            color: #ef4444 !important;
            fill: #ef4444 !important;
            text-shadow: 0 0 10px rgba(239, 68, 68, 0.5) !important;
        }"""

content = content.replace('        .map-btn:hover { background: rgba(99, 102, 241, 0.8); color: white; border-color: transparent; }', search_css)

# 3. Add Search JS
search_js = """                mm = Markmap.create('#markmap', {
                    autoFit: true,
                    fitRatio: 0.9,
                    duration: 500,
                    paddingX: 8,
                    spacingHorizontal: 80,
                    color: (node) => {
                        const colors = isDark ? darkColors : lightColors;
                        return colors[node.depth % colors.length];
                    }
                }, root);
                
                // Search Functionality
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
                });
                
            }, 100);"""

content = content.replace("""                mm = Markmap.create('#markmap', {
                    autoFit: true,
                    fitRatio: 0.9,
                    duration: 500,
                    paddingX: 8,
                    spacingHorizontal: 80,
                    color: (node) => {
                        const colors = isDark ? darkColors : lightColors;
                        return colors[node.depth % colors.length];
                    }
                }, root);
            }, 100);""", search_js)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Search feature added!")
