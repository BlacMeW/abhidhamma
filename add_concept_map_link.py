import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

html_target = "        <!-- Practical Meditation Guides -->"
html_new = """        <!-- Concept Map Banner -->
        <a href="concept_map.html" class="block group relative overflow-hidden glass-card rounded-3xl p-8 md:p-12 border-2 border-indigo-400 dark:border-indigo-500/50 bg-gradient-to-br from-indigo-50 to-sky-50 dark:from-indigo-950/40 dark:to-sky-950/40 hover:scale-[1.01] hover:shadow-2xl transition-all duration-300">
            <div class="absolute -right-20 -bottom-20 opacity-10 group-hover:opacity-20 transition-opacity">
                <i class="fa-solid fa-project-diagram text-9xl text-indigo-900 dark:text-indigo-100"></i>
            </div>
            <div class="relative z-10 flex flex-col md:flex-row items-center gap-6 text-center md:text-left">
                <div class="w-20 h-20 shrink-0 rounded-2xl bg-indigo-600 dark:bg-indigo-500 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                    <i class="fa-solid fa-project-diagram text-white text-3xl"></i>
                </div>
                <div class="space-y-2">
                    <h3 class="text-2xl md:text-3xl font-extrabold text-indigo-900 dark:text-indigo-200">
                        အဘိဓမ္မာ ၉ ပိုင်း ဆက်စပ်မှု မြေပုံကြီး (Concept Map)
                    </h3>
                    <p class="text-indigo-800/80 dark:text-indigo-300/80 font-medium max-w-2xl">
                        စိတ်၊ စေတသိက်၊ ရုပ်၊ နိဗ္ဗာန်၊ ဝီထိ၊ ဘုံ၊ ပဋ္ဌာန်း စသည့် အဘိဓမ္မာ သဘောတရားများ အချင်းချင်း မည်သို့ ချိတ်ဆက်နေသည်ကို Interactive Mind-Map ဖြင့် ခြုံငုံကြည့်ရှုရန် နှိပ်ပါ။
                    </p>
                </div>
                <div class="hidden md:block ml-auto">
                    <span class="bg-indigo-100 dark:bg-indigo-900/50 text-indigo-700 dark:text-indigo-300 px-4 py-2 rounded-full font-bold text-sm border border-indigo-200 dark:border-indigo-700 group-hover:bg-indigo-600 group-hover:text-white transition-colors flex items-center gap-2">
                        Explore <i class="fa-solid fa-arrow-right"></i>
                    </span>
                </div>
            </div>
        </a>

        <!-- Practical Meditation Guides -->"""

if "<!-- Concept Map Banner -->" not in content:
    content = content.replace(html_target, html_new)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Concept Map link")
else:
    print("Concept Map link already exists")
