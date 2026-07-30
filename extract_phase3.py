import re

files = [
    'pakinnaka_sangaha.html',
    'vithi_sangaha.html',
    'vithimutta_sangaha.html'
]

for file in files:
    with open(f'/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/{file}', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will just print out the JS variable declarations for the main data.
    # Usually it's something like `const pakinnakaData = [ ... ]`
    # Let's use a regex to capture it.
    
    m = re.search(r'const [a-zA-Z]+Data = \[.*?\];', content, flags=re.DOTALL)
    if m:
        out_name = f"extracted_{file.replace('.html', '.js')}"
        with open(out_name, 'w', encoding='utf-8') as outf:
            outf.write(m.group(0))
        print(f"Extracted data from {file} to {out_name}")
    else:
        # Some might use let or different naming
        print(f"Data block not found in {file}")

