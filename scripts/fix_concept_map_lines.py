import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the markmap-link block
old_css = """        /* Make links visible in dark mode */
        html.dark .markmap-link {
            stroke-width: 2px !important;
        }
        html.light .markmap-link {
            stroke-width: 2px !important;
        }
        /* Make circles larger and visible */
        .markmap-node circle {
            r: 7 !important;
            stroke-width: 3px !important;
        }"""

new_css = """        /* Make links (lines) highly visible */
        html.dark path.markmap-link,
        html.dark .markmap-link {
            stroke: #94a3b8 !important; /* Bright slate grey for dark mode lines */
            stroke-width: 2.5px !important;
            opacity: 1 !important;
        }
        html.light path.markmap-link,
        html.light .markmap-link {
            stroke: #64748b !important; /* Dark slate grey for light mode lines */
            stroke-width: 2.5px !important;
            opacity: 1 !important;
        }
        
        /* Make circles larger and visible */
        html.dark .markmap-node circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #38bdf8 !important; /* Sky blue stroke */
            fill: #0f172a !important;
        }
        html.light .markmap-node circle {
            r: 7 !important;
            stroke-width: 3px !important;
            stroke: #0284c7 !important; /* Sky blue stroke */
            fill: #ffffff !important;
        }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find old_css exactly. Adding new_css manually before </style>")
    content = content.replace("</style>", new_css + "\n    </style>")

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Lines fixed in concept_map.html")
