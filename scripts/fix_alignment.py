import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the span completely to fix alignment
content = content.replace(' <span style="color:#777">', ' ')
content = content.replace('</span>', '')

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed spans to fix alignment.")
