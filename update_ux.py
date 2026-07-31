import re

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_addition = """
        .bookmark-btn.active { color: #f59e0b; /* amber-500 */ }
        
        @keyframes staggerFadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-stagger {
            animation: staggerFadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            opacity: 0;
        }
        
        .sticky-scrolled {
            border-bottom-color: rgba(226, 232, 240, 0.8) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .dark .sticky-scrolled {
            border-bottom-color: rgba(51, 65, 85, 0.8) !important;
        }
"""
content = content.replace('.bookmark-btn.active { color: #f59e0b; /* amber-500 */ }', css_addition)

# 2. Add Sticky Wrapper
old_search = """            <div class="relative max-w-lg mx-auto mt-6">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                    <i class="fa-solid fa-magnifying-glass text-slate-500"></i>
                </div>
                <input type="text" id="searchInput" class="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-full py-3 pl-11 pr-4 text-slate-800 dark:text-slate-200 placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition shadow-inner" placeholder="ဝေါဟာရ (သို့) အဓိပ္ပာယ်ကို ရှာဖွေပါ">
                <button id="clearSearch" class="absolute inset-y-0 right-0 pr-4 flex items-center text-slate-500 dark:text-slate-500 hover:text-slate-700 dark:text-slate-300 hidden">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            
            <!-- Feature Controls -->
            <div class="max-w-4xl mx-auto mt-6 space-y-4">"""

new_search = """            <!-- Sticky Controls Wrapper -->
            <div class="sticky top-[64px] z-30 bg-slate-50/95 dark:bg-slate-900/95 backdrop-blur-sm pt-4 pb-4 -mx-4 px-4 sm:mx-0 sm:px-0 border-b border-transparent transition-all duration-200" id="stickyControls">
                <div class="relative max-w-lg mx-auto">
                    <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                        <i class="fa-solid fa-magnifying-glass text-slate-500"></i>
                    </div>
                    <input type="text" id="searchInput" class="w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-full py-3 pl-11 pr-4 text-slate-800 dark:text-slate-200 placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition shadow-inner" placeholder="ဝေါဟာရ (သို့) အဓိပ္ပာယ်ကို ရှာဖွေပါ">
                    <button id="clearSearch" class="absolute inset-y-0 right-0 pr-4 flex items-center text-slate-500 dark:text-slate-500 hover:text-slate-700 dark:text-slate-300 hidden">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>
                
                <!-- Feature Controls -->
                <div class="max-w-4xl mx-auto mt-4 space-y-4">"""
content = content.replace(old_search, new_search)

# Add closing div for sticky header
old_closing = """                    </div>
                </div>
            </div>



        </div>"""

new_closing = """                    </div>
                </div>
            </div>
            </div> <!-- End Sticky Wrapper -->

        </div>"""
content = content.replace(old_closing, new_closing)


# 3. Update renderCard
old_render = "function renderCard(t, q) {"
new_render = "function renderCard(t, q, index = 0) {"
content = content.replace(old_render, new_render)

old_card_div = '<div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-start gap-2 md:gap-4 relative group">'
new_card_div = '<div class="glass-card animate-stagger p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition-all duration-300 hover:shadow-lg hover:-translate-y-1 flex flex-col md:flex-row md:items-start gap-2 md:gap-4 relative group" style="animation-delay: ${Math.min(index * 0.05, 0.5)}s">'
content = content.replace(old_card_div, new_card_div)


# 4. Update Hover effects for related
old_rel = 'relTerms.map(rt => `<span class="inline-flex items-center text-[11px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 cursor-help" title="${rt.meaning}">${rt.term.split(\' \')[0]}</span>`).join(\'\') + \'</div>\';'
new_rel = 'relTerms.map(rt => `<span class="inline-flex items-center text-[11px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 cursor-help hover:-translate-y-0.5 hover:shadow-sm hover:border-emerald-300 dark:hover:border-emerald-600 transition-all duration-200" title="${rt.meaning}">${rt.term.split(\' \')[0]}</span>`).join(\'\') + \'</div>\';'
content = content.replace(old_rel, new_rel)

# 5. Update renderCore to pass index
old_map1 = "html += groups[letter].map(t => renderCard(t, searchQuery)).join('');"
new_map1 = "html += groups[letter].map((t, idx) => renderCard(t, searchQuery, idx)).join('');"
content = content.replace(old_map1, new_map1)

old_map2 = "html += filteredTerms.map(t => renderCard(t, searchQuery)).join('');"
new_map2 = "html += filteredTerms.map((t, idx) => renderCard(t, searchQuery, idx)).join('');"
content = content.replace(old_map2, new_map2)

# 6. Ghost pulse
old_ghost = '<i class="fa-solid fa-ghost text-4xl mb-4 opacity-50"></i>'
new_ghost = '<i class="fa-solid fa-ghost text-4xl mb-4 opacity-50 animate-pulse text-emerald-500/50"></i>'
content = content.replace(old_ghost, new_ghost)

# 7. Add Back to Top button and Scroll logic
scroll_js = """
        // Sticky Header & Back to Top logic
        const stickyControls = document.getElementById('stickyControls');
        const backToTopBtn = document.getElementById('backToTopBtn');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 100) {
                if(stickyControls) stickyControls.classList.add('sticky-scrolled');
                if(backToTopBtn) {
                    backToTopBtn.classList.remove('opacity-0', 'pointer-events-none');
                    backToTopBtn.classList.add('opacity-100');
                }
            } else {
                if(stickyControls) stickyControls.classList.remove('sticky-scrolled');
                if(backToTopBtn) {
                    backToTopBtn.classList.add('opacity-0', 'pointer-events-none');
                    backToTopBtn.classList.remove('opacity-100');
                }
            }
        });

        if(backToTopBtn) {
            backToTopBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
"""
content = content.replace("render();", scroll_js + "\n        render();")

btn_html = """
    <button id="backToTopBtn" class="fixed bottom-6 right-6 w-12 h-12 bg-emerald-600 text-white rounded-full shadow-lg flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 hover:bg-emerald-700 hover:scale-110 z-50">
        <i class="fa-solid fa-arrow-up"></i>
    </button>
</body>"""
content = content.replace("</body>", btn_html)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
