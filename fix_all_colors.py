import os
import re

color_mappings = {
    # Text slates
    r'(?<!dark:)text-slate-200': 'text-slate-800 dark:text-slate-200',
    r'(?<!dark:)text-slate-300': 'text-slate-700 dark:text-slate-300',
    r'(?<!dark:)text-slate-400': 'text-slate-600 dark:text-slate-400',
    r'(?<!dark:)text-slate-100': 'text-slate-900 dark:text-slate-100',
    
    # Text colors
    r'(?<!dark:)text-amber-300': 'text-amber-700 dark:text-amber-300',
    r'(?<!dark:)text-amber-400': 'text-amber-700 dark:text-amber-400',
    r'(?<!dark:)text-sky-300': 'text-sky-700 dark:text-sky-300',
    r'(?<!dark:)text-violet-300': 'text-violet-700 dark:text-violet-300',
    r'(?<!dark:)text-rose-300': 'text-rose-700 dark:text-rose-300',
    r'(?<!dark:)text-emerald-300': 'text-emerald-700 dark:text-emerald-300',
    
    # Backgrounds
    r'(?<!dark:)bg-slate-800/90': 'bg-slate-100/90 dark:bg-slate-800/90',
}

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
            
        for old, new in color_mappings.items():
            pattern = old + r'(?!\S)'
            content = re.sub(pattern, new, content)
            
        with open(f, 'w') as file:
            file.write(content)
        print(f"Fixed {f}")
