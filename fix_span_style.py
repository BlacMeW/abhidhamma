with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the style to remove font-size and just keep color, this fixes the vertical alignment issue
content = content.replace('style="font-size:0.8em; color:gray"', 'style="color:#777"')

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed span style.")
