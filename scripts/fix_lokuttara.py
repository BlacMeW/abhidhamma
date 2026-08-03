with open('concept_map.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("- သောတာပတ္တိမဂ်\n", "- သောတာပတ္တိမဂ်\n  - သောတာပန်အဖြစ်သို့ ရောက်စေသော မဂ်စိတ်\n")
content = content.replace("- သကဒါဂါမိမဂ်\n", "- သကဒါဂါမိမဂ်\n  - သကဒါဂါမ်အဖြစ်သို့ ရောက်စေသော မဂ်စိတ်\n")
content = content.replace("- အနာဂါမိမဂ်\n", "- အနာဂါမိမဂ်\n  - အနာဂါမ်အဖြစ်သို့ ရောက်စေသော မဂ်စိတ်\n")
content = content.replace("- အရဟတ္တမဂ်\n", "- အရဟတ္တမဂ်\n  - ရဟန္တာအဖြစ်သို့ ရောက်စေသော မဂ်စိတ်\n")

content = content.replace("- သောတာပတ္တိဖိုလ်\n", "- သောတာပတ္တိဖိုလ်\n  - သောတာပတ္တိမဂ်၏ အကျိုး (ဖိုလ်) စိတ်\n")
content = content.replace("- သကဒါဂါမိဖိုလ်\n", "- သကဒါဂါမိဖိုလ်\n  - သကဒါဂါမိမဂ်၏ အကျိုး (ဖိုလ်) စိတ်\n")
content = content.replace("- အနာဂါမိဖိုလ်\n", "- အနာဂါမိဖိုလ်\n  - အနာဂါမိမဂ်၏ အကျိုး (ဖိုလ်) စိတ်\n")
content = content.replace("- အရဟတ္တဖိုလ်\n", "- အရဟတ္တဖိုလ်\n  - အရဟတ္တမဂ်၏ အကျိုး (ဖိုလ်) စိတ်\n")

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(content)
