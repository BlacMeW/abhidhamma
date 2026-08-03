import re

with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Manodvara Vithi
old_mano = """- မနောဒွါရဝီထိ 
  - ဘဝင်္ဂစလန၊ ဘဝင်္ဂုပစ္ဆေဒ၊ မနောဒွါရာဝဇ္ဇန်း၊ ဇော ၇ ကြိမ်၊ တဒါရုံ ၂ ကြိမ်"""
new_mano = """- မနောဒွါရဝီထိ 
  - ဘဝင်္ဂစလန
  - ဘဝင်္ဂုပစ္ဆေဒ
  - မနောဒွါရာဝဇ္ဇန်း
  - ဇော ၇ ကြိမ်
  - တဒါရုံ ၂ ကြိမ်"""
content = content.replace(old_mano, new_mano)

# Fix Appana Vithi
old_appana = """- အပ္ပနာဝီထိ 
  - ပရိကံ၊ ဥပစာ၊ အနုလုံ၊ ဂေါတြဘူ၊ ဈာန်/မဂ် (ဇော ၁ ကြိမ်)"""
new_appana = """- အပ္ပနာဝီထိ 
  - ပရိကံ
  - ဥပစာ
  - အနုလုံ
  - ဂေါတြဘူ
  - ဈာန်/မဂ် (ဇော ၁ ကြိမ်)"""
content = content.replace(old_appana, new_appana)

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed.")
