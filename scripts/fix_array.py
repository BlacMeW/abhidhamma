with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Fix empty array elements: "},\n    ,\n" -> "},\n"
content = re.sub(r'\},[\s\n]*,', '},', content)
# Also fix any rogue isolated commas between objects
content = re.sub(r'[\s\n]*,[\s\n]+{', ',\n        {', content)
# To be safe, just remove any line that is purely a comma
lines = content.split('\n')
new_lines = []
for line in lines:
    if line.strip() == ',':
        continue
    new_lines.append(line)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
