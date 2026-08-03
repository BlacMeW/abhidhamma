import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation for Responsiveness
old_nav = """    <nav class="glass-nav sticky top-0 z-50 transition-colors duration-300 h-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full">
            <div class="flex items-center justify-between h-full">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-sky-500 to-indigo-500 flex items-center justify-center shadow-lg">
                        <i class="fa-solid fa-project-diagram text-white text-sm"></i>
                    </div>
                    <a href="index.html" class="font-bold text-lg md:text-xl tracking-wide bg-clip-text text-transparent bg-gradient-to-r from-sky-600 to-indigo-600 dark:from-sky-400 dark:to-indigo-400">
                        Concept Map (Interactive)
                    </a>
                </div>
                <div class="flex items-center gap-4">
                    <a href="index.html" class="text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 transition flex items-center gap-2">
                        <i class="fa-solid fa-home"></i> <span class="hidden md:inline">ပင်မစာမျက်နှာ
                    </a>
                    <div class="relative hidden sm:flex items-center gap-2">
                        <div class="relative">
                            <input type="text" id="search-input" placeholder="ရှာရန် (ဥပမာ- လောဘ)..." class="w-48 md:w-64 px-4 py-1.5 pl-9 text-sm rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-700 dark:text-slate-300 transition-all">
                            <i class="fa-solid fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 text-xs"></i>
                        </div>
                        <div id="search-controls" class="hidden items-center gap-1 text-sm text-slate-600 dark:text-slate-300">
                            <span id="search-counter" class="text-xs font-bold px-2 whitespace-nowrap">0 / 0</span>
                            <button id="search-prev" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-up text-xs"></i></button>
                            <button id="search-next" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-down text-xs"></i></button>
                        </div>
                    </div>
                    <button id="theme-toggle" class="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-800 transition">
                        <i class="fa-solid fa-moon dark:hidden text-lg"></i>
                        <i class="fa-solid fa-sun hidden dark:block text-lg"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>"""

new_nav = """    <nav class="glass-nav sticky top-0 z-50 transition-colors duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 md:py-3">
            <div class="flex flex-wrap items-center justify-between gap-y-3">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-sky-500 to-indigo-500 flex items-center justify-center shadow-lg shrink-0">
                        <i class="fa-solid fa-project-diagram text-white text-sm"></i>
                    </div>
                    <a href="index.html" class="font-bold text-base md:text-xl tracking-wide bg-clip-text text-transparent bg-gradient-to-r from-sky-600 to-indigo-600 dark:from-sky-400 dark:to-indigo-400 truncate">
                        Concept Map
                    </a>
                </div>
                
                <div class="flex items-center gap-4 order-2 md:order-3">
                    <a href="index.html" class="text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 transition flex items-center gap-2">
                        <i class="fa-solid fa-home"></i> <span class="hidden md:inline">ပင်မစာမျက်နှာ</span>
                    </a>
                    <button id="theme-toggle" class="w-9 h-9 md:w-10 md:h-10 rounded-full flex items-center justify-center text-slate-500 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-800 transition">
                        <i class="fa-solid fa-moon dark:hidden text-lg"></i>
                        <i class="fa-solid fa-sun hidden dark:block text-lg"></i>
                    </button>
                </div>
                
                <div class="w-full md:w-auto order-3 md:order-2 flex items-center gap-2">
                    <div class="relative flex-1 md:flex-none">
                        <input type="text" id="search-input" placeholder="ရှာရန် (ဥပမာ- လောဘ)..." class="w-full md:w-64 px-4 py-1.5 md:py-2 pl-9 text-sm rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-700 dark:text-slate-300 transition-all">
                        <i class="fa-solid fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 text-xs"></i>
                    </div>
                    <div id="search-controls" class="hidden items-center gap-1 text-sm text-slate-600 dark:text-slate-300">
                        <span id="search-counter" class="text-xs font-bold px-1 whitespace-nowrap">0 / 0</span>
                        <button id="search-prev" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-up text-xs"></i></button>
                        <button id="search-next" class="w-7 h-7 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 flex items-center justify-center transition"><i class="fa-solid fa-chevron-down text-xs"></i></button>
                    </div>
                </div>
            </div>
        </div>
    </nav>"""

content = content.replace(old_nav, new_nav)

# 2. Hide instruction overlay on small screens to avoid overlapping
old_overlay = """        <!-- Instruction Overlay -->
        <div class="absolute top-4 right-4 z-10 pointer-events-none text-right">"""

new_overlay = """        <!-- Instruction Overlay -->
        <div class="hidden md:block absolute top-4 right-4 z-10 pointer-events-none text-right">"""

content = content.replace(old_overlay, new_overlay)

# 3. Make #markmap-container flex-1 (it's inside flex flex-col body)
old_main = """    <main id="markmap-container" class="bg-slate-50 dark:bg-slate-900">"""
new_main = """    <main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 flex-1 relative overflow-hidden">"""

content = content.replace(old_main, new_main)

# 4. Make SVG take full size of container
old_svg = """        <svg id="markmap"></svg>"""
new_svg = """        <svg id="markmap" class="w-full h-full absolute inset-0"></svg>"""

content = content.replace(old_svg, new_svg)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Responsiveness improved!")
