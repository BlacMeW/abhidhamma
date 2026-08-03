import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # Skip HTML boilerplate
    if not line.strip().startswith('-') and not line.strip().startswith('#'):
        continue
        
    matches = re.finditer(r'\s*\(([^)]+)\)', line)
    for m in matches:
        inner = m.group(1)
        has_burmese = re.search(r'[\u1000-\u103F]', inner)
        is_just_number = re.match(r'^[၀-၉0-9/\s\-ပါး]+$', inner) # allowed 'ပါး' or '-' to count as number-like
        
        if has_burmese and not is_just_number:
            print(f"Line {i+1}: {line.strip()}")
            break
