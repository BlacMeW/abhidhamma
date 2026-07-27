import re

filename = 'citta_cetasikas_visual_guide.html'
with open(filename, 'r') as f:
    content = f.read()

# Pattern to match the entire Cittakkhana block
pattern = r'(\s*<!-- Cittakkhana \(Micro-Animation\) -->.*?</script>\s*)(?=<!-- Live Vithi Animation)'

# Remove the block
new_content, count = re.subn(pattern, '\n            ', content, flags=re.DOTALL)

if count > 0:
    with open(filename, 'w') as f:
        f.write(new_content)
    print("Removed Cittakkhana animation successfully!")
else:
    print("Could not find the Cittakkhana block.")
