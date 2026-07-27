import os
import re

script_tag = '\n    <script src="accessibility.js"></script>\n</body>'

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # Inject script tag just before </body>
        if 'accessibility.js' not in content:
            new_content = re.sub(r'</body>', script_tag, content)
            
            # Also, we need to add Tailwind config script in head if it's not there, 
            # to enable darkMode: 'class' for CDN usage.
            tailwind_config = """    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {}
            }
        }
    </script>
</head>"""
            new_content = re.sub(r'</head>', tailwind_config, new_content)
            
            with open(f, 'w') as file:
                file.write(new_content)
            print(f"Injected into {f}")
