import os
import re
from collections import defaultdict

pattern = re.compile(r'(?<!dark:)text-([a-z]+)-([1234]00)')
results = defaultdict(list)

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
            matches = pattern.findall(content)
            for color, shade in matches:
                # We expect things like text-slate-800 for light mode, but text-slate-300 is suspicious
                results[f"{color}-{shade}"].append(f)

for k, v in results.items():
    print(f"text-{k} found in {len(v)} files: {set(v)}")

