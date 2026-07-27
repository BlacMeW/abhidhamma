import os
import re

class_mappings = {
    # Backgrounds
    r'(?<!dark:)bg-slate-900/90': 'bg-white/90 dark:bg-slate-900/90',
    r'(?<!dark:)bg-slate-900/80': 'bg-white/80 dark:bg-slate-900/80',
    r'(?<!dark:)bg-slate-900/60': 'bg-white/60 dark:bg-slate-900/60',
    r'(?<!dark:)bg-slate-900/40': 'bg-white/40 dark:bg-slate-900/40',
    r'(?<!dark:)bg-slate-900': 'bg-white dark:bg-slate-900',
    r'(?<!dark:)bg-slate-800': 'bg-slate-50 dark:bg-slate-800',
    r'(?<!dark:)bg-slate-700': 'bg-slate-100 dark:bg-slate-700',
    r'(?<!dark:)hover:bg-slate-700': 'hover:bg-slate-100 dark:hover:bg-slate-700',
    r'(?<!dark:)hover:bg-slate-800': 'hover:bg-slate-50 dark:hover:bg-slate-800',
    
    # Borders
    r'(?<!dark:)border-slate-800': 'border-slate-200 dark:border-slate-800',
    r'(?<!dark:)border-slate-700': 'border-slate-200 dark:border-slate-700',
    r'(?<!dark:)border-slate-600': 'border-slate-300 dark:border-slate-600',
    
    # Text
    r'(?<!dark:)text-slate-200': 'text-slate-800 dark:text-slate-200',
    r'(?<!dark:)text-slate-300': 'text-slate-700 dark:text-slate-300',
    r'(?<!dark:)text-slate-400': 'text-slate-600 dark:text-slate-400',
    
    # Custom colored backgrounds (add dark prefix)
    r'(?<!dark:)bg-slate-950/50': 'bg-slate-50/50 dark:bg-slate-950/50',
    r'(?<!dark:)bg-slate-950/80': 'bg-slate-50/80 dark:bg-slate-950/80',
}

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        # 1. Update body tag
        body_pattern = r'<body class="([^"]*)">'
        match = re.search(body_pattern, content)
        if match:
            cls = match.group(1)
            if 'bg-slate-50' not in cls:
                new_cls = cls + " bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-200"
                content = content.replace(f'<body class="{cls}">', f'<body class="{new_cls}">')
        
        # 2. Remove hardcoded styles
        content = re.sub(r'background-color:\s*#0f172a;', '', content)
        content = re.sub(r'color:\s*#f8fafc;', '', content)
        
        # 3. Update tailwind classes
        # We need to only match whole words for classes.
        for old, new in class_mappings.items():
            # Use negative lookbehind and lookahead to match full class names
            pattern = old + r'(?!\S)'
            content = re.sub(pattern, new, content)
            
        # 4. Handle glass-card base styles in <style>
        glass_card_style = """
        .glass-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .dark .glass-card {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        """
        old_glass = r'\.glass-card\s*\{[^}]*\}'
        content = re.sub(old_glass, glass_card_style.strip(), content)
        
        with open(f, 'w') as file:
            file.write(content)
        print(f"Refactored {f}")
