with open('accessibility.js', 'r') as f:
    content = f.read()

replacement = """
        if (theme === 'dark') {
            htmlEl.classList.add('dark');
            document.body.style.removeProperty('background-color');
            btnDark.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-slate-900', 'dark:text-white');
"""

old_code = """
        if (theme === 'dark') {
            htmlEl.classList.add('dark');
            btnDark.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm',
'text-slate-900', 'dark:text-white');
"""

content = content.replace(
    "        if (theme === 'dark') {\n            htmlEl.classList.add('dark');",
    "        if (theme === 'dark') {\n            htmlEl.classList.add('dark');\n            document.body.style.removeProperty('background-color');"
)

content = content.replace(
    "        } else {\n            htmlEl.classList.remove('dark');",
    "        } else {\n            htmlEl.classList.remove('dark');\n            document.body.style.setProperty('background-color', '#f8fafc', 'important');"
)

with open('accessibility.js', 'w') as f:
    f.write(content)
print("Patched accessibility.js")
