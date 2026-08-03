import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_samuccaya = False
for i, line in enumerate(lines):
    if line.strip().startswith("## သမုစ္စည်း"):
        in_samuccaya = True
    elif line.strip().startswith("## ပစ္စည်း"):
        in_samuccaya = False
        break
        
    if in_samuccaya:
        match = re.match(r'^(\s*)-\s+(.*)$', line.rstrip())
        if match:
            indent = match.group(1)
            # check if it has a child
            has_child = False
            if i + 1 < len(lines):
                next_match = re.match(r'^(\s*)-\s+(.*)$', lines[i+1].rstrip())
                if next_match and len(next_match.group(1)) > len(indent):
                    has_child = True
            
            if not has_child:
                print(line.rstrip())
