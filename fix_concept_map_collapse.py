import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the collapse logic right before mm = Markmap.create
target = "mm = Markmap.create('#markmap', {"
new_logic = """
                // Collapse nodes deeper than level 1 (0-indexed) so it doesn't shrink to microscopic size
                function collapseNodes(node, currentLevel = 0, maxLevel = 1) {
                    if (currentLevel >= maxLevel) {
                        if (!node.payload) node.payload = {};
                        node.payload.fold = 1; // 1 means folded
                    }
                    if (node.children) {
                        node.children.forEach(child => collapseNodes(child, currentLevel + 1, maxLevel));
                    }
                }
                collapseNodes(root);
                
                mm = Markmap.create('#markmap', {"""

if "collapseNodes" not in content:
    content = content.replace(target, new_logic)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added initial collapse logic to concept_map.html")
