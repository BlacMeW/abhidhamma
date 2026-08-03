import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing CSS block for markmap overrides
old_css = """        /* Dark mode overrides for Markmap SVG elements */
        .dark .markmap-node text {
            fill: #e2e8f0 !important;
            font-family: 'Pyidaungsu', sans-serif !important;
        }
        .light .markmap-node text {
            fill: #1e293b !important;
            font-family: 'Pyidaungsu', sans-serif !important;
        }
        .dark .markmap-link {
            stroke: #475569 !important;
        }"""

new_css = """        /* High-contrast overrides for Markmap text */
        .dark #markmap text, 
        .dark .markmap-node text {
            fill: #f8fafc !important; /* Very light slate */
            font-family: 'Pyidaungsu', 'Myanmar Text', sans-serif !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            text-shadow: 0px 1px 3px rgba(0,0,0,0.9) !important;
        }
        .light #markmap text,
        .light .markmap-node text {
            fill: #0f172a !important; /* Very dark slate */
            font-family: 'Pyidaungsu', 'Myanmar Text', sans-serif !important;
            font-size: 15px !important;
            font-weight: 600 !important;
        }
        /* Make links visible in dark mode */
        .dark .markmap-link {
            stroke: #64748b !important; /* Lighter slate for links */
        }
        /* Make circles larger and visible */
        .markmap-node circle {
            r: 6 !important;
            stroke-width: 2px !important;
        }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    # If not found exactly, just inject it before </style>
    if "/* High-contrast overrides" not in content:
        content = content.replace("</style>", new_css + "\n    </style>")

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors fixed in concept_map.html")
