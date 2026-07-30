import re

file_path = "/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/metta_bhavana_guide.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the badge background (avoid 950 which might not exist in older Tailwind)
content = content.replace("dark:bg-violet-950/60", "dark:bg-violet-900")

# Fix the subtitle text (was missing dark mode variant, so it looked bad in light or dark depending on context)
content = content.replace('class="text-xs text-slate-400 font-medium"', 'class="text-xs text-slate-500 dark:text-slate-400 font-medium"')

# Brighten the bottom Burmese text in dark mode for better readability
content = content.replace("dark:text-slate-300 leading-relaxed pt-3", "dark:text-slate-200 leading-relaxed pt-3")
# The class for verse 6 and 8 was slightly different (text-xs)
content = content.replace("text-xs text-slate-700 dark:text-slate-300 leading-relaxed pt-3", "text-xs text-slate-700 dark:text-slate-200 leading-relaxed pt-3")


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Color contrast fixed!")
