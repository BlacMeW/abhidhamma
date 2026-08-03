import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the custom foreignObject CSS entirely as it breaks Safari's bounding box calculation
content = re.sub(
    r'\/\* Fix Burmese Font Vertical Clipping for Safari \*\/[\s\S]*?overflow: hidden; \/\* Safari might need this \*\/\n\s*\}',
    r'/* Removed Safari-breaking foreignObject styles */',
    content
)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("foreignObject CSS removed")
