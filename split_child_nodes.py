import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []

def process_line(line):
    # Only process markdown list items
    match = re.match(r'^(\s*)-\s+(.*)$', line)
    if not match:
        return [line]
    
    indent = match.group(1)
    content = match.group(2)
    
    # We want to find ( ... ) at the end of the line, or anywhere, that contains text.
    # It's safer to find all (...) blocks and extract those that are "meanings"
    
    # Regex to find all (...) 
    # Use re.finditer to get all matches
    matches = list(re.finditer(r'\s*\(([^)]+)\)', content))
    
    meanings = []
    
    # We will build a new content string by replacing the matched meanings with empty string
    new_content = content
    
    # Go in reverse so replacing doesn't mess up indices, or just replace by string
    for m in reversed(matches):
        full_match = m.group(0)
        inner = m.group(1)
        
        # Check if inner has Burmese text (not just numbers)
        has_burmese = re.search(r'[\u1000-\u103F]', inner)
        is_just_number = re.match(r'^[၀-၉0-9/\s]+$', inner)
        
        if has_burmese and not is_just_number:
            meanings.append(inner)
            # Remove this from new_content
            # We replace only the exact match at the end if possible, or just replace the string.
            # Since we iterate in reverse, we can slice.
            start, end = m.span()
            new_content = new_content[:start] + new_content[end:]
            
    # meanings were collected in reverse order
    meanings.reverse()
    
    # If no meanings found, just return original line
    if not meanings:
        return [line]
    
    # Prepare lines
    result = [f"{indent}- {new_content.strip()}\n"]
    child_indent = indent + "  "
    for m_text in meanings:
        result.append(f"{child_indent}- {m_text.strip()}\n")
        
    return result

for line in lines:
    new_lines.extend(process_line(line))

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Split inline meanings into child nodes.")
