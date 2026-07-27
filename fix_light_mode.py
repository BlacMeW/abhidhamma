import os
import re

color_mappings = {
    # Ambers
    r'(?<!dark:)text-amber-300': 'text-amber-700 dark:text-amber-300',
    r'(?<!dark:)text-amber-400': 'text-amber-700 dark:text-amber-400',
    r'(?<!dark:)text-amber-200': 'text-amber-800 dark:text-amber-200',
    r'(?<!dark:)bg-amber-500/20': 'bg-amber-100 dark:bg-amber-500/20',
    r'(?<!dark:)border-amber-500/20': 'border-amber-300 dark:border-amber-500/20',
    r'(?<!dark:)border-amber-500/30': 'border-amber-400 dark:border-amber-500/30',
    r'(?<!dark:)border-amber-500/50': 'border-amber-500 dark:border-amber-500/50',
    r'(?<!dark:)ring-amber-400': 'ring-amber-500 dark:ring-amber-400',
    
    # Skys
    r'(?<!dark:)text-sky-300': 'text-sky-700 dark:text-sky-300',
    r'(?<!dark:)text-sky-400': 'text-sky-700 dark:text-sky-400',
    r'(?<!dark:)text-sky-200': 'text-sky-800 dark:text-sky-200',
    r'(?<!dark:)bg-sky-500/10': 'bg-sky-100 dark:bg-sky-500/10',
    r'(?<!dark:)bg-sky-500/15': 'bg-sky-100 dark:bg-sky-500/15',
    r'(?<!dark:)border-sky-500/30': 'border-sky-400 dark:border-sky-500/30',
    r'(?<!dark:)border-sky-500/50': 'border-sky-500 dark:border-sky-500/50',
    
    # Violets
    r'(?<!dark:)text-violet-300': 'text-violet-700 dark:text-violet-300',
    r'(?<!dark:)text-violet-400': 'text-violet-700 dark:text-violet-400',
    r'(?<!dark:)text-violet-200': 'text-violet-800 dark:text-violet-200',
    r'(?<!dark:)bg-violet-500/15': 'bg-violet-100 dark:bg-violet-500/15',
    r'(?<!dark:)bg-violet-500/20': 'bg-violet-100 dark:bg-violet-500/20',
    r'(?<!dark:)border-violet-500/30': 'border-violet-400 dark:border-violet-500/30',

    # Roses
    r'(?<!dark:)text-rose-300': 'text-rose-700 dark:text-rose-300',
    r'(?<!dark:)text-rose-400': 'text-rose-700 dark:text-rose-400',
    r'(?<!dark:)text-rose-200': 'text-rose-800 dark:text-rose-200',
    r'(?<!dark:)text-red-300': 'text-red-700 dark:text-red-300',
    r'(?<!dark:)text-red-200': 'text-red-800 dark:text-red-200',
    r'(?<!dark:)bg-rose-500/15': 'bg-rose-100 dark:bg-rose-500/15',
    r'(?<!dark:)bg-rose-500/20': 'bg-rose-100 dark:bg-rose-500/20',
    r'(?<!dark:)border-rose-500/30': 'border-rose-400 dark:border-rose-500/30',

    # Emeralds
    r'(?<!dark:)text-emerald-300': 'text-emerald-700 dark:text-emerald-300',
    r'(?<!dark:)text-emerald-400': 'text-emerald-700 dark:text-emerald-400',
    r'(?<!dark:)text-emerald-200': 'text-emerald-800 dark:text-emerald-200',
    r'(?<!dark:)bg-emerald-500/15': 'bg-emerald-100 dark:bg-emerald-500/15',
    r'(?<!dark:)bg-emerald-500/20': 'bg-emerald-100 dark:bg-emerald-500/20',
    r'(?<!dark:)border-emerald-500/30': 'border-emerald-400 dark:border-emerald-500/30',
    
    # Indigos
    r'(?<!dark:)text-indigo-300': 'text-indigo-700 dark:text-indigo-300',
    r'(?<!dark:)text-indigo-400': 'text-indigo-700 dark:text-indigo-400',
    r'(?<!dark:)bg-indigo-500/15': 'bg-indigo-100 dark:bg-indigo-500/15',
    r'(?<!dark:)border-indigo-500/30': 'border-indigo-400 dark:border-indigo-500/30',
    
    # Cyans
    r'(?<!dark:)text-cyan-300': 'text-cyan-700 dark:text-cyan-300',
    r'(?<!dark:)text-cyan-400': 'text-cyan-700 dark:text-cyan-400',
    r'(?<!dark:)text-teal-300': 'text-teal-700 dark:text-teal-300',

    # Common missing slates
    r'(?<!dark:)bg-slate-800/80': 'bg-slate-100/80 dark:bg-slate-800/80',
    r'(?<!dark:)border-slate-600': 'border-slate-300 dark:border-slate-600',
    r'(?<!dark:)text-slate-400': 'text-slate-600 dark:text-slate-400',
    r'(?<!dark:)text-slate-500': 'text-slate-500 dark:text-slate-500',
    r'(?<!dark:)text-white': 'text-slate-900 dark:text-white',
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
        print(f"Fixed colors in {f}")
