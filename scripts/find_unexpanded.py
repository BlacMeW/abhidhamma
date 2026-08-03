import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

unexpanded = []
for i in range(len(lines)):
    line = lines[i].strip()
    if line.startswith('-') or line.startswith('#'):
        # match (N) or (N/M) at the end or before a parenthesis
        # like (၂) or (၅)
        m = re.search(r'\((\d+|[၀-၉]+)(?:/\d+|/[၀-၉]+)?\)', line)
        if m:
            # Check if next line is more indented
            current_indent = len(lines[i]) - len(lines[i].lstrip())
            is_leaf = True
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if next_line.strip() == '' or next_line.strip().startswith('#'):
                    is_leaf = True
                elif next_line.startswith(' '):
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > current_indent:
                        is_leaf = False
            
            # If it's a leaf node but has a count > 1
            num_str = m.group(1)
            # convert burmese digits to english if necessary
            burmese_digits = str.maketrans('၀၁၂၃၄၅၆၇၈၉', '0123456789')
            num_val = int(num_str.translate(burmese_digits))
            
            if is_leaf and num_val > 1:
                unexpanded.append((i+1, line))

for idx, text in unexpanded:
    print(f"Line {idx}: {text}")

