import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove adjustLayout
content = re.sub(
    r'// Adjust layout dynamically for iOS[\s\S]*?setTimeout\(adjustLayout, 300\);',
    r'',
    content
)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("JS layout logic removed")
