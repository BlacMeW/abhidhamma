import os

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
            
        if '<meta name="color-scheme"' not in content:
            content = content.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n    <meta name="color-scheme" content="light dark">'
            )
            
            with open(f, 'w') as file:
                file.write(content)
            print(f"Fixed {f}")
