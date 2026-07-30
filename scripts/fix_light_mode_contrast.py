import re

file_path = "/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/metta_bhavana_guide.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Darken slate-500 to slate-700
content = content.replace('text-slate-500 dark:text-slate-400', 'text-slate-700 dark:text-slate-400')

# Darken slate-700 to slate-900 for Burmese text in Chant
content = content.replace('text-slate-700 dark:text-slate-200', 'text-slate-900 dark:text-slate-200')
content = content.replace('text-slate-700 dark:text-slate-300', 'text-slate-900 dark:text-slate-300')

# Darken violet-800 to violet-950 or violet-900 (950 might not exist, use 900)
content = content.replace('text-violet-800 dark:text-violet-300', 'text-violet-900 dark:text-violet-300')

# Darken rose-600 to rose-800 on the dropdown
content = content.replace('text-rose-600 dark:text-rose-400', 'text-rose-800 dark:text-rose-400')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Light mode text contrast increased!")
