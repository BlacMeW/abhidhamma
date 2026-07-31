import re

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update renderCard function
old_render = """        <div class="md:w-1/3 pt-1 pr-6">
            <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg">${highlight(t.term, q)}</div>
            <span class="inline-block mt-1 text-[10px] uppercase tracking-wider font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">${t.category}</span>
        </div>
        <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
            <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed pr-6">
                ${highlight(t.meaning, q)}
            </div>"""

new_render = """        <div class="md:w-1/3 pt-1 pr-6">
            <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg mb-1">${highlight(t.term_my || t.term, q)}</div>
            ${t.pali_eng ? `<div class="text-xs text-slate-500 font-serif italic mb-2">${highlight(t.pali_eng, q)}</div>` : ''}
            <span class="inline-block mt-1 text-[10px] uppercase tracking-wider font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">${t.category}</span>
        </div>
        <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
            ${t.nissaya ? `<div class="text-sm text-amber-700 dark:text-amber-400 bg-amber-50 dark:bg-amber-500/10 border border-amber-200/50 dark:border-amber-500/20 px-3 py-2 rounded-lg mb-3 leading-relaxed shadow-sm"><strong>နိဿယ - </strong>${highlight(t.nissaya, q)}</div>` : ''}
            <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed pr-6">
                <strong class="text-slate-900 dark:text-slate-100 font-medium">အဓိပ္ပာယ် - </strong>${highlight(t.meaning, q)}
            </div>"""

content = content.replace(old_render, new_render)

# Update Flashcard Back
old_flash = """                            <!-- Back -->
                            <div class="flashcard-face flashcard-back">
                                <h3 class="text-xl md:text-2xl font-bold text-slate-800 dark:text-slate-100 mb-6 leading-relaxed px-4">${t.meaning}</h3>
                                <div class="w-12 h-1 bg-emerald-500/30 rounded-full mx-auto mb-6"></div>"""

new_flash = """                            <!-- Back -->
                            <div class="flashcard-face flashcard-back overflow-y-auto hide-scrollbar">
                                <h3 class="text-xl font-bold text-emerald-800 dark:text-emerald-300 mb-2">${t.term_my || t.term}</h3>
                                ${t.pali_eng ? `<p class="text-sm text-slate-500 font-serif italic mb-4">${t.pali_eng}</p>` : ''}
                                <div class="w-12 h-1 bg-emerald-500/30 rounded-full mx-auto mb-4"></div>
                                
                                ${t.nissaya ? `<div class="w-full text-left bg-amber-50 dark:bg-amber-500/10 border border-amber-200/50 dark:border-amber-500/20 p-3 rounded-lg mb-4 text-sm text-amber-800 dark:text-amber-300"><span class="font-bold">နိဿယ -</span><br/>${t.nissaya}</div>` : ''}
                                
                                <div class="text-left w-full text-slate-700 dark:text-slate-200 text-base leading-relaxed">
                                    <span class="font-bold text-slate-900 dark:text-white">အဓိပ္ပာယ် -</span><br/>
                                    ${t.meaning}
                                </div>
                                <div class="mt-6"></div>"""

content = content.replace(old_flash, new_flash)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("UI updated.")
