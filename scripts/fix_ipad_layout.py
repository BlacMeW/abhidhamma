import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Body to use fixed inset-0 (Very robust for iOS Safari)
content = re.sub(
    r'<body class="([^"]*)h-screen([^"]*)">',
    r'<body class="\1 fixed inset-0 \2">',
    content
)

# 2. Add ResizeObserver to JS to re-fit the map when layout changes
old_js = """                mm = Markmap.create('#markmap', {
                    autoFit: true,
                    fitRatio: 0.9,
                    duration: 500,
                    paddingX: 8,
                    spacingHorizontal: 80,
                    color: (node) => {
                        const colors = isDark ? darkColors : lightColors;
                        return colors[node.depth % colors.length];
                    }
                }, root);"""

new_js = """                mm = Markmap.create('#markmap', {
                    autoFit: true,
                    fitRatio: 0.9,
                    duration: 500,
                    paddingX: 8,
                    spacingHorizontal: 80,
                    color: (node) => {
                        const colors = isDark ? darkColors : lightColors;
                        return colors[node.depth % colors.length];
                    }
                }, root);
                
                // Fix for iOS/iPad Safari: ensure it fits when container resizes
                const resizeObserver = new ResizeObserver(() => {
                    if (mm) {
                        setTimeout(() => mm.fit(), 50);
                    }
                });
                resizeObserver.observe(document.getElementById('markmap-container'));
                
                // Extra fit call to catch delayed layout computation on iOS WebKit
                setTimeout(() => mm.fit(), 300);
                setTimeout(() => mm.fit(), 1000);"""

content = content.replace(old_js, new_js)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("iPad layout fixes applied!")
