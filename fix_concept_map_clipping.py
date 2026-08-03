import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add foreignObject overflow visible
new_css = """        /* High Visibility Circles */
        html.dark .markmap-node circle,
        html.dark body #markmap circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #fbbf24 !important; /* Bright Amber stroke */
            fill: #0f172a !important;
        }
        html.light .markmap-node circle,
        html.light body #markmap circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #d97706 !important; /* Dark Amber stroke */
            fill: #ffffff !important;
        }
        
        /* Fix Burmese Font Vertical Clipping */
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

# find the circle CSS to replace it with itself + the new clipping fix
target = """        /* High Visibility Circles */
        html.dark .markmap-node circle,
        html.dark body #markmap circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #fbbf24 !important; /* Bright Amber stroke */
            fill: #0f172a !important;
        }
        html.light .markmap-node circle,
        html.light body #markmap circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #d97706 !important; /* Dark Amber stroke */
            fill: #ffffff !important;
        }"""

if target in content:
    content = content.replace(target, new_css)
else:
    print("Could not find target block. Appending before </style>")
    content = content.replace("</style>", "\n" + new_css + "\n    </style>")

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed font clipping in concept_map.html")
