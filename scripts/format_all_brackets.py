import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
span_start = '<span style="font-size:0.8em; color:gray">'
span_end = '</span>'

def process_line(line):
    # Skip if not a markdown list or heading
    if not (line.lstrip().startswith('- ') or line.lstrip().startswith('#')):
        return line
        
    # Remove existing spans if any to avoid double wrapping
    l = line.replace(span_start, '').replace(span_end, '')
    
    # We want to match ( ... ) where ... contains Burmese characters but isn't just a number
    # Regex to find all ( ... )
    def repl(m):
        full_match = m.group(0)
        inner_text = m.group(1)
        # Check if it has burmese characters
        has_burmese = re.search(r'[\u1000-\u103F]', inner_text)
        # Check if it looks like just a number (e.g. ၁၂, ၃/၅)
        is_just_number = re.match(r'^[၀-၉0-9/\s]+$', inner_text)
        
        if has_burmese and not is_just_number:
            # Wrap in span
            return f' {span_start}({inner_text}){span_end}'
        else:
            return full_match

    # replace ` (text)` or `(text)` with ` <span>(text)</span>`
    l = re.sub(r'\s*\(([^)]+)\)', repl, l)
    return l

for line in lines:
    new_lines.append(process_line(line))

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Formatted all explanations.")
