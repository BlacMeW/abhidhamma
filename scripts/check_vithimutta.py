import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_vithimutta = False
vithimutta_lines = []
for line in lines:
    if line.strip().startswith("## ဝီထိမုတ္တ"):
        in_vithimutta = True
    elif line.strip().startswith("## သမုစ္စည်း"):
        in_vithimutta = False
        
    if in_vithimutta:
        vithimutta_lines.append(line.rstrip())

print('\n'.join(vithimutta_lines[:20]))
