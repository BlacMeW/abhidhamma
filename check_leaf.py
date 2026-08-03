import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    match = re.match(r'^(\s*)-\s+(.*)$', line.rstrip())
    if match:
        indent = match.group(1)
        name = match.group(2).strip()
        
        has_child = False
        if i + 1 < len(lines):
            next_match = re.match(r'^(\s*)-\s+(.*)$', lines[i+1].rstrip())
            if next_match and len(next_match.group(1)) > len(indent):
                has_child = True
                
        # Leaf nodes without ( numbers ) and not starting with "ဥပမာ" and not english
        if not has_child and "(" not in name and "ဥပမာ" not in name and not re.match(r'^[a-zA-Z]', name):
            print(f"Line {i+1}: {line.rstrip()}")
