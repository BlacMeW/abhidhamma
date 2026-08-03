import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    if line.startswith('-') or line.startswith('#'):
        # Check if line ends with (N) or (N/M)
        # Note: the regex checks anywhere, but let's check near the end
        m = re.search(r'\((\d+|[၀-၉]+)(?:/\d+|/[၀-၉]+)?\)[^\(]*$', line)
        if m:
            current_indent = len(lines[i]) - len(lines[i].lstrip())
            is_leaf = True
            if i + 1 < len(lines):
                next_line = lines[i+1]
                if next_line.strip() == '' or next_line.strip().startswith('#'):
                    # if next line is a heading, then this is a leaf (unless this is a heading too, but a lower level one)
                    pass
                elif next_line.startswith(' '):
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > current_indent:
                        is_leaf = False
            
            if is_leaf:
                num_str = m.group(1)
                burmese_digits = str.maketrans('၀၁၂၃၄၅၆၇၈၉', '0123456789')
                num_val = int(num_str.translate(burmese_digits))
                if num_val > 1:
                    print(f"Leaf with >1 count: {line}")
