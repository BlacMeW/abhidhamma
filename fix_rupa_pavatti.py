import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a third table in the HTML section
html_target = "            <!-- Table 2: Rupa Bhumi -->"
if "<!-- Table 3: Rupa Pavatti -->" not in content:
    html_new = """            <!-- Table 3: Rupa Pavatti -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-amber-500/30" open>
                <summary class="flex items-center justify-between font-bold text-amber-700 dark:text-amber-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-seedling mr-2"></i>ရုပ်တို့၏ ဖြစ်စဉ် (ပဋိသန္ဓေအခါ နှင့် ပဝတ္တိအခါ ရုပ်ဖြစ်ပေါ်ပုံ)</span>
                </summary>
                <div id="rupa-pavatti-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 2: Rupa Bhumi -->"""
    content = content.replace(html_target, html_new)

    with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Rupa Pavatti HTML")
else:
    print("Rupa Pavatti HTML already exists")
