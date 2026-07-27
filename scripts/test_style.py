import re
with open('index.html', 'r') as f:
    content = f.read()
match = re.search(r'<style>([\s\S]*?)</style>', content)
if match:
    print(match.group(1))
