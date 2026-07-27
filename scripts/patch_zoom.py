import re

filename = 'citta_cetasikas_visual_guide.html'
with open(filename, 'r') as f:
    content = f.read()

hint_html = """
            <div class="text-center mb-4 md:hidden">
                <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-xs border border-emerald-500/20">
                    <i class="fa-solid fa-magnifying-glass-plus"></i> ဖုန်းဖြင့်ကြည့်ပါက ဇယားကို လက်ဖြင့်ဆွဲချဲ့၍ (Pinch to zoom) ကြည့်နိုင်ပါသည်။
                </span>
            </div>
"""

# Find <div id="citta-grid" ...> and insert before it
content = re.sub(r'(<div\s+id="citta-grid")', hint_html + r'\n            \1', content)

# Enable pinch to zoom on body by NOT having user-scalable=no (it already is viewport-fit=cover without user-scalable=no)

with open(filename, 'w') as f:
    f.write(content)
print("Added zoom hint successfully!")
