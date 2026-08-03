import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add padding-top to shift text down without breaking Safari's bounding boxes
old_css = r"""        .markmap-node text,
        .markmap-node tspan,
        .markmap-node div,
        .markmap-node span,
        #markmap text,
        #markmap tspan,
        #markmap div,
        #markmap span {
            font-family: 'Pyidaungsu', 'Myanmar Text', sans-serif !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            white-space: nowrap !important;
            line-height: 1.2 !important;
        }"""

new_css = """        .markmap-node text,
        .markmap-node tspan,
        .markmap-node div,
        .markmap-node span,
        #markmap text,
        #markmap tspan,
        #markmap div,
        #markmap span {
            font-family: 'Pyidaungsu', 'Myanmar Text', sans-serif !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            white-space: nowrap !important;
            line-height: 1.2 !important;
            padding-top: 5px !important; /* Shifts text down to align with circles */
        }"""

content = content.replace(old_css, new_css)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Alignment fix applied")
