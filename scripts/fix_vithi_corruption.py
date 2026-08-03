import re

with open('vithi_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The corrupted block starts at line 324: `<p class="        const appanaJhanaSeq...`
# We'll use regex to find this corrupted block and replace it.

pattern = re.compile(r'<p class="\s+const appanaJhanaSeq.*?</section>', re.DOTALL)

correct_html = """<ul class="list-disc pl-4 space-y-1.5 text-slate-700 dark:text-slate-300 leading-relaxed mt-2">
                        <li><b>ကာမဘုံ</b> (၁၁) ဘုံ ၌သာ တဒါရုံ ကျနိုင်သည်။</li>
                        <li><b>ကာမဇော</b> (၂၉) ပါး စောပြီးမှသာ တဒါရုံ ကျနိုင်သည်။</li>
                        <li><b>ကာမာဝစရအာရုံ</b> (၆) ပါး ထင်လာသောအခါ၌သာ တဒါရုံ ကျနိုင်သည်။</li>
                        <li>ဤအင်္ဂါ (၃) ချက် ညီညွတ်မှသာ တဒါရုံစိတ် ဖြစ်ပေါ်နိုင်သည်။</li>
                    </ul>
                </div>
                
                <div class="bg-white/60 dark:bg-slate-900/60 p-4 rounded-xl border border-amber-500/30 space-y-2">
                    <h4 class="font-bold text-amber-700 dark:text-amber-300 text-sm border-b border-amber-200 dark:border-amber-900/50 pb-1">ဇဝနနိယာမ (Javana-niyāma)</h4>
                    <ul class="list-disc pl-4 space-y-1.5 text-slate-700 dark:text-slate-300 leading-relaxed mt-2">
                        <li><b>ကာမဇောများ:</b> သာမန်အားဖြင့် (၇) ကြိမ် စောသည်။ အားနည်းသောအခါ (သေခါနီးစသည်) တွင် (၅) ကြိမ်သာ စောသည်။</li>
                        <li><b>ပထမဆုံး ဈာန်ရချိန်:</b> အပ္ပနာဇော (၁) ကြိမ်သာ စောသည်။</li>
                        <li><b>ဈာန်သမာပတ် ဝင်စားချိန်:</b> အပ္ပနာဇော မရေတွက်နိုင်အောင် အကြိမ်ပေါင်းများစွာ ဆက်တိုက် စောနိုင်သည်။</li>
                        <li><b>မဂ်စိတ်:</b> မဂ်ဇောသည် မည်သည့်အခါမဆို (၁) ကြိမ်သာ စောသည်။</li>
                    </ul>
                </div>
            </div>
        </section>"""

if pattern.search(content):
    content = pattern.sub(correct_html, content)
    with open('vithi_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed corruption.")
else:
    print("Could not find corrupted block.")
