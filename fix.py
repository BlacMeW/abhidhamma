with open("glossary.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the end of the feature controls block.
# Actually, let's just insert the missing divs right before the <script> block
missing_divs = """
        </div>
        <div id="alphabetIndex" class="flex flex-wrap gap-2 justify-center mt-6"></div>
        <div id="glossaryList" class="w-full mt-8">
            <!-- Items injected by JS -->
        </div>
    </main>
"""

# Let's see where </main> is
if "</main>" not in content:
    script_idx = content.find("<script>")
    content = content[:script_idx] + missing_divs + content[script_idx:]

with open("glossary.html", "w", encoding="utf-8") as f:
    f.write(content)

