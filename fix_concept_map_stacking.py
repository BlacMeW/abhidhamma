import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """        /* Fix Burmese Font Vertical Clipping */
        #markmap foreignObject {
            overflow: visible !important;
            height: auto !important;
        }
        #markmap .markmap-node div,
        #markmap .markmap-node span,
        #markmap .markmap-node text {
            line-height: 1.8 !important;
            padding-top: 4px !important;
            padding-bottom: 4px !important;
            display: inline-block;
        }"""

replacement = """        /* Fix Burmese Font Vertical Clipping without breaking layout */
        #markmap foreignObject {
            overflow: visible !important;
        }
        #markmap .markmap-node div {
            /* Minimal line-height so layout matches calculation */
            line-height: 1.2 !important; 
        }"""

if target in content:
    content = content.replace(target, replacement)
    with open('concept_map.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed CSS stacking issue.")
else:
    print("Could not find the CSS block to replace.")
