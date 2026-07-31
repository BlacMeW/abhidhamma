import json, re

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const originalTerms = (\[.*?\]);', content, re.DOTALL)
if match:
    # Need to convert JS object to valid JSON to parse it
    js_array = match.group(1)
    
    # Very hacky JS to JSON conversion
    js_array = re.sub(r'(\w+):', r'"\1":', js_array)
    js_array = js_array.replace("'", '"')
    
    # We might have trailing commas or issues, let's just write the raw string to a text file
    with open('terms_raw.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
    print("Extracted to terms_raw.txt")
else:
    print("Not found")
