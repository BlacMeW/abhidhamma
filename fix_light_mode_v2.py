import os
import re

color_mappings = {
    # Missed slates
    r'(?<!dark:)text-slate-100': 'text-slate-900 dark:text-slate-100',
    r'(?<!dark:)text-slate-50\b': 'text-slate-900 dark:text-slate-50',
    
    # Borders
    r'(?<!dark:)border-slate-800/80': 'border-slate-200 dark:border-slate-800/80',
    r'(?<!dark:)border-slate-800/50': 'border-slate-200 dark:border-slate-800/50',
    
    # Hovers
    r'(?<!dark:)hover:bg-slate-700': 'hover:bg-slate-200 dark:hover:bg-slate-700',
    r'(?<!dark:)hover:bg-slate-800': 'hover:bg-slate-100 dark:hover:bg-slate-800',
    
    # Fix the c-filter-btn specifically
    r'hover:bg-slate-700"': 'hover:bg-slate-200 dark:hover:bg-slate-700"',
    
    # Let's also check if there are any remaining text-white that don't have dark:text-white
    r'(?<!dark:)text-white': 'text-slate-900 dark:text-white',
    
    # Group hover text amber
    r'(?<!dark:)group-hover:text-amber-400': 'group-hover:text-amber-700 dark:group-hover:text-amber-400',
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
        print(f"Fixed v2 colors in {f}")
