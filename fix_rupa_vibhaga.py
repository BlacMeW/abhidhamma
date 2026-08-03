import re

with open('rupa_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a fifth table in the HTML section (at the very top of the tables)
html_target = "            <!-- Table 1: Rupa Kalapa -->"
if "<!-- Table 5: Rupa Vibhaga -->" not in content:
    html_new = """            <!-- Table 5: Rupa Vibhaga -->
            <details class="glass-card rounded-xl p-4 md:p-5 border border-sky-500/30" open>
                <summary class="flex items-center justify-between font-bold text-sky-700 dark:text-sky-300 text-sm md:text-base cursor-pointer outline-none">
                    <span><i class="fa-solid fa-shapes mr-2"></i>ရုပ်တို့၏ အပြား (Rūpa Vibhāga) - ရုပ် (၂၈) ပါးကို အမျိုးအစားခွဲခြားခြင်း</span>
                </summary>
                <div id="rupa-vibhaga-matrix" class="mt-4 w-full overflow-x-auto pb-2"></div>
            </details>

            <!-- Table 1: Rupa Kalapa -->"""
    content = content.replace(html_target, html_new)
    
    with open('rupa_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Rupa Vibhaga HTML")
else:
    print("Rupa Vibhaga HTML already exists")
