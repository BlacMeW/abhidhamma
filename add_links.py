import re
import json

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will write a regex substitution to update the JS array or just rewrite the script entirely.
# Since rewriting is safer, let's locate the terms array and replace it.
match = re.search(r"const terms = (\[.*?\]);", content, re.DOTALL)
if match:
    terms_str = match.group(1)
    
    # We will just manually construct the updated JS string. 
    # It's easier to replace the entire `const terms = [...];` block with a pre-defined string.
    pass

