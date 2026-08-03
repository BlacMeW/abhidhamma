import re

def process_match(m):
    prefix = m.group(1) # e.g. "- ကိစ္စကံ (၄)"
    items_str = m.group(2) # e.g. "ဇနက၊ ဥပတ္ထမ္ဘက၊ ဥပပီဠက၊ ဥပဃာတက"
    # Find the current indentation of prefix
    indent_match = re.match(r'^(\s*)-', prefix)
    indent = indent_match.group(1) if indent_match else ""
    child_indent = indent + "  "
    
    # Split items by ၊ or ,
    items = re.split(r'[၊,]\s*', items_str)
    
    result = prefix + "\n"
    for item in items:
        item = item.strip()
        if item:
            result += f"{child_indent}- {item}\n"
    return result.rstrip('\n')

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for matching: - Something (X) (a, b, c)
# We need to be careful not to match simple (meaning) parentheses.
# We'll target ones that contain "၊" which is the Burmese comma.
pattern1 = re.compile(r'^(\s*- .*?)\s*\(([^)]*၊[^)]*)\)', re.MULTILINE)
content = pattern1.sub(process_match, content)

# Also there are cases like:
# - မနောဒွါရဝီထိ \n  - ဘဝင်္ဂစလန၊ ဘဝင်္ဂုပစ္ဆေဒ၊ မနောဒွါရာဝဇ္ဇန်း၊ ဇော ၇ ကြိမ်၊ တဒါရုံ ၂ ကြိမ်
pattern2 = re.compile(r'^(\s*-) ([^()]*၊[^()]*)$', re.MULTILINE)
def process_match2(m):
    indent = m.group(1)
    items_str = m.group(2)
    # Split items by ၊
    items = re.split(r'[၊,]\s*', items_str)
    # Actually, for this, if it's already a bullet, we might not want to change the bullet to a parent unless it has a parent.
    # Let's handle it manually to be safe.
    pass

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced successfully")
