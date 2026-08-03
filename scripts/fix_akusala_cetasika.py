with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <br> with a space for the Akusala section
content = content.replace('<br><span style="font-size:0.8em; color:gray">', ' <span style="font-size:0.8em; color:gray">')

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed formatting.")
