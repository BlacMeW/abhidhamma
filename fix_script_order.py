import os
import re

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # Ensure tailwind config is BEFORE tailwind cdn script just in case
        tailwind_config = """<script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {}
            }
        }
    </script>
    <script src="https://cdn.tailwindcss.com"></script>"""
        
        # Remove old tailwind.config at the end of head
        content = re.sub(r'<script>\s*tailwind\.config = \{[^}]*\}[^<]*</script>', '', content)
        
        # Replace the cdn script with config + cdn script
        content = re.sub(r'<script src="https://cdn.tailwindcss.com"></script>', tailwind_config, content)
        
        with open(f, 'w') as file:
            file.write(content)
        print(f"Fixed script order in {f}")
