import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix cyan
content = content.replace("text: 'text-cyan-300'", "text: 'text-cyan-700 dark:text-cyan-300'")
# Fix indigo
content = content.replace("text: 'text-indigo-300'", "text: 'text-indigo-700 dark:text-indigo-300'")
# Fix teal
content = content.replace("text: 'text-teal-300'", "text: 'text-teal-700 dark:text-teal-300'")

with open('index.html', 'w') as f:
    f.write(content)
print("Fixed themeColors in index.html")
