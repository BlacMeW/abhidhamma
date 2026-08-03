with open('missaka_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Replace the bad regex strings with the good one
new_content = re.sub(r'replace\(/<b>.*?<\\\\/b>\\\\s\*-\\\\s\*/,\s*\'\'\)', r"replace(/<b>.*?<\/b>\s*-\s*/, '')", content)
new_content = re.sub(r'replace\(/<b>.*?<\\/b>\\s\*-\\s\*/,\s*\'\'\)', r"replace(/<b>.*?<\/b>\s*-\s*/, '')", new_content)

with open('missaka_sangaha.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
