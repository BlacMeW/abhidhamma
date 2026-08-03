import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if not line.strip().startswith('-'):
        continue
    # A leaf node or a node without a child definition.
    # We can check if the next line is indented more and starts with '- ' but isn't a definition?
    # Actually, it's easier to just read the file manually or use Python to inject dict-based meanings.
