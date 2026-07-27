import re

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Map to assign links
pages = {
    'citta': {'title': 'စိတ်ပိုင်း (Citta)', 'url': 'citta_cetasikas_visual_guide.html'},
    'cetasika': {'title': 'စေတသိက်ပိုင်း (Cetasika)', 'url': 'citta_cetasikas_visual_guide.html'},
    'rupa': {'title': 'ရုပ်ပိုင်း (Rūpa)', 'url': 'rupa_sangaha.html'},
    'vithimutta': {'title': 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', 'url': 'vithimutta_sangaha.html'},
    'paticcasamuppada': {'title': 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', 'url': 'paticcasamuppada.html'},
    'paccaya': {'title': 'ပစ္စည်းပိုင်း (Paccaya)', 'url': 'paccaya_sangaha.html'},
    'kammatthana': {'title': 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', 'url': 'kammatthana_sangaha.html'},
    'bodhipakkhiya': {'title': 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', 'url': 'bodhipakkhiya_dhamma.html'},
    'kilesa': {'title': 'ကိလေသာပိုင်း (Kilesa)', 'url': 'kilesa_sangaha.html'},
    'sabba': {'title': 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', 'url': 'sabba_sangaha.html'}
}

mapping = {
    'Citta': ['citta'],
    'Cetasika': ['cetasika'],
    'Rūpa': ['rupa'],
    'Nibbāna': [],
    'Asaṅkhārika': ['citta'],
    'Sasaṅkhārika': ['citta'],
    'Ahetuka': ['citta'],
    'Sahetuka': ['citta'],
    'Kusala': ['citta'],
    'Akusala': ['citta', 'kilesa'],
    'Vipāka': ['citta'],
    'Kiriya': ['citta'],
    'Vīthi': ['citta'],
    'Bhavaṅga': ['vithimutta'],
    'Javana': ['citta'],
    'Paṭisandhi': ['vithimutta'],
    'Cuti': ['vithimutta'],
    'Uppāda': ['citta'],
    'Ṭhiti': ['citta'],
    'Bhaṅga': ['citta'],
    'Kicca': ['citta'],
    'Dvāra': ['citta'],
    'Ārammaṇa': ['citta'],
    'Vatthu': ['citta'],
    'Paccaya': ['paccaya'],
    'Kammaṭṭhāna': ['kammatthana'],
    'Samatha': ['kammatthana'],
    'Vipassanā': ['kammatthana'],
    'Jhāna': ['kammatthana'],
    'Magga': ['bodhipakkhiya'],
    'Phala': ['bodhipakkhiya'],
    'Kilesā': ['kilesa'],
    'Avijjā': ['paticcasamuppada', 'kilesa'],
    'Taṇhā': ['paticcasamuppada', 'kilesa'],
    'Upādāna': ['paticcasamuppada'],
    'Jāti': ['paticcasamuppada'],
    'Jarā': ['paticcasamuppada'],
    'Maraṇa': ['paticcasamuppada'],
    'Nāmarūpa': ['paticcasamuppada'],
    'Saḷāyatana': ['paticcasamuppada'],
    'Phassa': ['paticcasamuppada'],
    'Vedanā': ['paticcasamuppada'],
    'Satipaṭṭhāna': ['bodhipakkhiya'],
    'Sammappadhāna': ['bodhipakkhiya'],
    'Iddhipāda': ['bodhipakkhiya'],
    'Bala': ['bodhipakkhiya'],
    'Bojjhaṅga': ['bodhipakkhiya'],
    'Lobha': ['kilesa'],
    'Dosa': ['kilesa'],
    'Moha': ['kilesa'],
    'Māna': ['kilesa'],
    'Diṭṭhi': ['kilesa'],
    'Vicikicchā': ['kilesa'],
    'Thīna-Middha': ['kilesa'],
    'Uddhacca': ['kilesa'],
    'Kukkucca': ['kilesa'],
    'Alobha': ['cetasika'],
    'Adosa': ['cetasika'],
    'Amoha': ['cetasika'],
    'Saddhā': ['cetasika'],
    'Sati': ['cetasika'],
    'Hiri': ['cetasika'],
    'Ottappa': ['cetasika'],
    'Mahābhūta': ['rupa'],
    'Upādārūpa': ['rupa'],
    'Khandha': ['sabba'],
    'Āyatana': ['sabba'],
    'Dhātu': ['sabba'],
    'Indriya': ['sabba'],
    'Sacca': ['sabba'],
    'Paṭiccasamuppāda': ['paticcasamuppada'],
    'Paṭṭhāna': ['paccaya'],
    'Kamma': ['paccaya'],
    'Hetu': ['paccaya'],
    'Sampayutta': ['cetasika'],
    'Vippayutta': ['cetasika'],
    'Bhūmi': ['vithimutta'],
    'Nimitta': ['kammatthana'],
    'Saṅkhāra': ['paticcasamuppada'],
    'Paññatti': [],
    'Paramattha': []
}

# Find terms array
match = re.search(r"const terms = (\[.*?\]);", content, re.DOTALL)
if match:
    terms_str = match.group(1)
    
    # We can use regex to extract and rebuild
    blocks = re.findall(r"(\{.*?\})", terms_str)
    
    new_blocks = []
    for b in blocks:
        # extract term prefix
        t_match = re.search(r"term:\s*'([^\s(]+)", b)
        if t_match:
            base_term = t_match.group(1).replace("Kriyā", "Kiriya").replace("Thīna", "Thīna-Middha")
            
            # Find links
            links = []
            if base_term in mapping:
                for p_key in mapping[base_term]:
                    links.append(f"{{ name: '{pages[p_key]['title']}', url: '{pages[p_key]['url']}' }}")
                    
            if links:
                links_str = f", links: [{', '.join(links)}]"
                b = b[:-1] + links_str + " }"
        
        new_blocks.append("            " + b)
        
    new_terms_str = "[\n" + ",\n".join(new_blocks) + "\n        ]"
    content = content[:match.start(1)] + new_terms_str + content[match.end(1):]
    
# Now replace renderCard to display links
render_card_old = r"""        function renderCard\(t, q\) \{
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-center gap-2 md:gap-4">
                    <div class="md:w-1/3 font-bold text-emerald-700 dark:text-emerald-300 text-lg">
                        \$\{highlight\(t.term, q\)\}
                    </div>
                    <div class="md:w-2/3 text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed">
                        \$\{highlight\(t.meaning, q\)\}
                    </div>
                </div>
            `;
        \}"""

render_card_new = """        function renderCard(t, q) {
            let linksHtml = '';
            if (t.links && t.links.length > 0) {
                linksHtml = '<div class="mt-3 flex flex-wrap gap-2">' + t.links.map(l => 
                    `<a href="${l.url}" class="inline-flex items-center gap-1 text-[11px] font-medium px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-700 hover:bg-emerald-100 dark:bg-emerald-500/10 dark:text-emerald-300 dark:hover:bg-emerald-500/20 transition-colors border border-emerald-200/50 dark:border-emerald-500/20"><i class="fa-solid fa-link text-[9px] opacity-70"></i> ${l.name}</a>`
                ).join('') + '</div>';
            }
            
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-start gap-2 md:gap-4">
                    <div class="md:w-1/3 pt-1">
                        <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg">${highlight(t.term, q)}</div>
                    </div>
                    <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
                        <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed">
                            ${highlight(t.meaning, q)}
                        </div>
                        ${linksHtml}
                    </div>
                </div>
            `;
        }"""

content = re.sub(render_card_old, render_card_new, content, flags=re.DOTALL)

with open('/DATA/LLM_Projs/monledhamma.org/citta_cetasikas_visual_guide/glossary.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added links successfully")

