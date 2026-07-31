import re, json

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const originalTerms = (\[.*?\]);', content, re.DOTALL)
if not match:
    print("Could not find originalTerms array.")
    exit()

js_data = match.group(1)

# We have 139 terms. Let's parse them using regex because it's a JS object, not strict JSON.
terms_str = js_data.strip()[1:-1].strip() # remove [ and ]

# Split by "}," but keep the },
term_blocks = []
current_block = []
in_quotes = False
escape = False
brace_level = 0
for char in terms_str:
    if char == '"' or char == "'":
        if not escape:
            in_quotes = not in_quotes
    elif char == '\\':
        escape = not escape
    else:
        escape = False

    if char == '{' and not in_quotes:
        brace_level += 1
    elif char == '}' and not in_quotes:
        brace_level -= 1
        
    current_block.append(char)
    if brace_level == 0 and char == '}' and not in_quotes:
        term_blocks.append("".join(current_block).strip())
        current_block = []

print(f"Parsed {len(term_blocks)} terms.")

new_blocks = []
for block in term_blocks:
    if not block: continue
    
    # Extract fields
    term_match = re.search(r'term:\s*[\'"](.*?)[\'"]', block)
    if term_match:
        original_term = term_match.group(1)
        # Parse 'Abhidhamma (အဘိဓမ္မာ)'
        parts = re.match(r'(.*?)\s*\((.*?)\)', original_term)
        if parts:
            pali_eng = parts.group(1).strip()
            term_my = parts.group(2).strip()
        else:
            pali_eng = ''
            term_my = original_term
            
        nissaya = ''
        
        # Hardcode some examples
        if 'Abhidhamma' in original_term:
            nissaya = 'အဘိ - လွန်ကဲထူးမြတ်သော၊ ဓမ္မ - တရား'
        elif 'Kusala' in original_term and 'Akusala' not in original_term:
            nissaya = 'ကုသလံ - အပြစ်ကင်း၍ ကောင်းမြတ်သော အကျိုးကိုပေးတတ်သော (တရား)'
        elif 'Akusala' in original_term:
            nissaya = 'အကုသလံ - အပြစ်ရှိ၍ ဆင်းရဲသောအကျိုးကို ပေးတတ်သော (တရား)'
        elif 'Citta' in original_term and 'Cetasika' not in original_term:
            nissaya = 'စိတ္တံ - အာရုံကို သိတတ်သော (တရား)'
        elif 'Cetasika' in original_term:
            nissaya = 'စေတသိက - စိတ်၌ မှီ၍ဖြစ်သော (တရား)'
            
        # Replace the term field and add new fields
        # Find where term is and insert
        new_block = re.sub(
            r'term:\s*[\'"].*?[\'"]', 
            f"term: '{original_term}', term_my: '{term_my}', pali_eng: '{pali_eng}', nissaya: '{nissaya}'", 
            block
        )
        new_blocks.append(new_block)
    else:
        new_blocks.append(block)

new_array = "[\n    " + ",\n    ".join(new_blocks) + "\n]"
new_content = content.replace(js_data, new_array)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Data transformed successfully.")
