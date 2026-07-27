import os
import re

# We want to replace things like text-cyan-300 with text-cyan-700 dark:text-cyan-300
# But only if it doesn't already have dark: in front of it.
pattern = re.compile(r'(?<!dark:)text-([a-z]+)-([1234]00)')

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
            
        # Perform replacement
        # \1 is color (e.g. cyan), \2 is shade (e.g. 300)
        # We replace with text-\1-700 dark:text-\1-\2
        new_content = pattern.sub(r'text-\1-700 dark:text-\1-\2', content)
        
        if new_content != content:
            with open(f, 'w') as file:
                file.write(new_content)
            print(f"Fixed {f}")

