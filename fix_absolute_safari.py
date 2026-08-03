import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Body
content = re.sub(
    r'<body class="([^"]*)fixed inset-0([^"]*)flex flex-col([^"]*)">',
    r'<body class="\1 fixed inset-0 \2 \3" style="width: 100vw; height: 100vh;">',
    content
)

# 2. Update Nav
content = re.sub(
    r'<nav class="glass-nav sticky top-0 z-50 transition-colors duration-300 shrink-0">',
    r'<nav id="site-nav" class="glass-nav absolute top-0 left-0 right-0 z-50 transition-colors duration-300">',
    content
)

# 3. Update Main
content = re.sub(
    r'<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 flex-1 relative overflow-hidden" style="min-height: 0;">',
    r'<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 absolute left-0 right-0 bottom-0 overflow-hidden">',
    content
)

# 4. Add JS to adjust layout
js_layout = """            // Adjust layout dynamically for iOS
            function adjustLayout() {
                const nav = document.getElementById('site-nav');
                const main = document.getElementById('markmap-container');
                if (nav && main) {
                    main.style.top = nav.offsetHeight + 'px';
                }
            }
            window.addEventListener('resize', adjustLayout);
            adjustLayout();
            setTimeout(adjustLayout, 300);

            // Fetch and parse Markdown data"""

content = content.replace("            // Fetch and parse Markdown data", js_layout)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Absolute layout fix applied!")
