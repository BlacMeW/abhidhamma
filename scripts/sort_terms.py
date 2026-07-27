import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the terms array
match = re.search(r"const terms = (\[.*?\]);", content, re.DOTALL)
if match:
    terms_str = match.group(1)
    
    # We can just extract all { ... } blocks
    blocks = re.findall(r"(\{.*?\})", terms_str)
    
    # Parse each block into a dictionary-like structure for sorting
    parsed_blocks = []
    for b in blocks:
        # extract term value for sorting
        term_match = re.search(r"term:\s*'(.*?)'", b)
        if term_match:
            parsed_blocks.append({
                'text': b,
                'term': term_match.group(1)
            })
    
    # Sort blocks
    parsed_blocks.sort(key=lambda x: x['term'].lower())
    
    # Reconstruct
    new_terms_lines = ["        const terms = ["]
    for i, pb in enumerate(parsed_blocks):
        line = f"            {pb['text']}"
        if i < len(parsed_blocks) - 1:
            line += ","
        new_terms_lines.append(line)
    new_terms_lines.append("        ];")
    
    new_terms_str = "\n".join(new_terms_lines)
    
    new_content = content[:match.start()] + new_terms_str + content[match.end():]
    
    with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully sorted the terms array in the code!")
else:
    print("Could not find terms array")

