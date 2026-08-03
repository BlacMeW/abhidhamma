import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Body
old_body = r'<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300   fixed inset-0     overflow-hidden" style="width: 100vw; height: 100vh;">'
new_body = '<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 overflow-hidden" style="display: flex; flex-direction: column; width: 100vw; height: 100vh; margin: 0; padding: 0; position: fixed; inset: 0;">'
content = content.replace(old_body, new_body)
# Fallback in case spacing changed
content = re.sub(r'<body[^>]*>', new_body, content, count=1)


# Replace Nav
old_nav = r'<nav id="site-nav" class="glass-nav absolute top-0 left-0 right-0 z-50 transition-colors duration-300">'
new_nav = '<nav id="site-nav" class="glass-nav relative z-50 transition-colors duration-300" style="flex: 0 0 auto;">'
content = content.replace(old_nav, new_nav)
content = re.sub(r'<nav id="site-nav"[^>]*>', new_nav, content, count=1)


# Replace Main
old_main = r'<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 absolute left-0 right-0 bottom-0 overflow-hidden">'
new_main = '<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 overflow-hidden" style="flex: 1 1 auto; position: relative; width: 100%; height: 100%; min-height: 0;">'
content = content.replace(old_main, new_main)
content = re.sub(r'<main id="markmap-container"[^>]*>', new_main, content, count=1)


# Replace SVG
old_svg = r'<svg id="markmap" class="w-full h-full absolute inset-0"></svg>'
new_svg = '<svg id="markmap" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></svg>'
content = content.replace(old_svg, new_svg)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final bulletproof layout applied")
