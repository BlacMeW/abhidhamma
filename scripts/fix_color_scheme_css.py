import os

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
            
        if '<style>\n        :root {\n            color-scheme: light dark;\n        }' not in content:
            content = content.replace(
                '</head>',
                '    <style>\n        :root {\n            color-scheme: light dark;\n        }\n    </style>\n</head>'
            )
            
            with open(f, 'w') as file:
                file.write(content)
            print(f"Fixed {f}")
