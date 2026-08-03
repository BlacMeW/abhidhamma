import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_overlay = r"""        <!-- Instruction Overlay -->
        <div class="hidden md:block absolute top-4 right-4 z-10 pointer-events-none text-right">
            <div class="bg-white/80 dark:bg-slate-800/80 backdrop-blur px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-700 shadow-lg inline-block text-left">
                <h3 class="font-bold text-sm text-indigo-600 dark:text-indigo-400 mb-1"><i class="fa-solid fa-hand-pointer mr-1"></i> Interactive Map</h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                    • <b>Click</b> on nodes to expand/collapse them.<br>
                    • <b>Drag</b> anywhere to move the map.<br>
                    • <b>Scroll</b> or pinch to zoom in/out.
                </p>
            </div>
        </div>"""

new_overlay = """        <!-- Instruction Overlay -->
        <div class="absolute top-2 right-2 md:top-4 md:right-4 z-10 pointer-events-none text-right opacity-80 md:opacity-100">
            <div class="bg-white/80 dark:bg-slate-800/80 backdrop-blur px-2 py-1.5 md:px-4 md:py-3 rounded-lg md:rounded-xl border border-slate-200 dark:border-slate-700 shadow-lg inline-block text-left scale-[0.8] md:scale-100 origin-top-right">
                <h3 class="font-bold text-xs md:text-sm text-indigo-600 dark:text-indigo-400 mb-0.5 md:mb-1"><i class="fa-solid fa-hand-pointer mr-1"></i> Interactive Map</h3>
                <p class="text-[10px] md:text-xs text-slate-600 dark:text-slate-300 leading-tight md:leading-relaxed">
                    • <b>Click</b> to expand/collapse.<br>
                    • <b>Drag</b> to move.<br>
                    • <b>Pinch/Scroll</b> to zoom.
                </p>
            </div>
        </div>"""

content = content.replace(old_overlay, new_overlay)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Overlay fixed")
