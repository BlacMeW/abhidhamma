import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove overflow: visible from foreignObject which breaks Safari
content = content.replace("""        /* Fix Burmese Font Vertical Clipping without breaking layout */
        #markmap foreignObject {
            overflow: visible !important;
        }""", """        /* Fix Burmese Font Vertical Clipping for Safari */
        #markmap foreignObject {
            padding-bottom: 5px; /* Alternative to overflow visible */
            overflow: hidden; /* Safari might need this */
        }""")

# 2. Fix Safari Flexbox bug by adding explicit heights or min-height
old_body = '<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 min-h-screen flex flex-col">'
new_body = '<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 h-screen flex flex-col overflow-hidden">'
content = content.replace(old_body, new_body)

old_main = '<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 flex-1 relative overflow-hidden">'
new_main = '<main id="markmap-container" class="bg-slate-50 dark:bg-slate-900 flex-1 relative overflow-hidden" style="min-height: 0;">'
content = content.replace(old_main, new_main)

# Make sure navbar doesn't shrink
old_nav = '<nav class="glass-nav sticky top-0 z-50 transition-colors duration-300">'
new_nav = '<nav class="glass-nav sticky top-0 z-50 transition-colors duration-300 shrink-0">'
content = content.replace(old_nav, new_nav)


with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Safari fixes applied!")
