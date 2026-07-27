import re

niddesa_map = {
    'hetu': 'ဟေတူ ဟေတုသမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ ဟေတုပစ္စယေန ပစ္စယော။',
    'arammana': 'ရူပါယတနံ စက္ခုဝိညာဏဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ အာရမ္မဏပစ္စယေန ပစ္စယော။ သဒ္ဒါယတနံ သောတဝိညာဏဓာတုယာ... ယံ ယံ ဓမ္မံ အာရဗ္ဘ ယေ ယေ ဓမ္မာ ဥပ္ပဇ္ဇန္တိ စိတ္တစေတသိကာ ဓမ္မာ၊ တေ တေ ဓမ္မာ တေသံ တေသံ ဓမ္မာနံ အာရမ္မဏပစ္စယေန ပစ္စယော။',
    'adhipati': 'ဆန္ဒာဓိပတိ ဆန္ဒသမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ အဓိပတိပစ္စယေန ပစ္စယော။ ... ယံ ယံ ဓမ္မံ ဂရုံ ကတွာ ယေ ယေ ဓမ္မာ ဥပ္ပဇ္ဇန္တိ စိတ္တစေတသိကာ ဓမ္မာ၊ တေ တေ ဓမ္မာ တေသံ တေသံ ဓမ္မာနံ အဓိပတိပစ္စယေန ပစ္စယော။',
    'anantara': 'စက္ခုဝိညာဏဓာတု တံသမ္ပယုတ္တကာ စ ဓမ္မာ မနောဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ အနန္တရပစ္စယေန ပစ္စယော။ ... ယေသံ ယေသံ ဓမ္မာနံ အနန္တရာ ယေ ယေ ဓမ္မာ ဥပ္ပဇ္ဇန္တိ စိတ္တစေတသိကာ ဓမ္မာ၊ တေ တေ ဓမ္မာ တေသံ တေသံ ဓမ္မာနံ အနန္တရပစ္စယေန ပစ္စယော။',
    'samanantara': 'စက္ခုဝိညာဏဓာတု တံသမ္ပယုတ္တကာ စ ဓမ္မာ မနောဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ သမနန္တရပစ္စယေန ပစ္စယော။ ... ယေသံ ယေသံ ဓမ္မာနံ သမနန္တရာ ယေ ယေ ဓမ္မာ ဥပ္ပဇ္ဇန္တိ စိတ္တစေတသိကာ ဓမ္မာ၊ တေ တေ ဓမ္မာ တေသံ တေသံ ဓမ္မာနံ သမနန္တရပစ္စယေန ပစ္စယော။',
    'sahajata': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ သဟဇာတပစ္စယေန ပစ္စယော။ စတ္တာရော မဟာဘူတာ အညမညံ သဟဇာတပစ္စယေန ပစ္စယော။ ...',
    'annamanna': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညပစ္စယေန ပစ္စယော။ စတ္တာရော မဟာဘူတာ အညမညပစ္စယေန ပစ္စယော။ ဩက္ကန္တိက္ခဏေ နာမရူပံ အညမညပစ္စယေန ပစ္စယော။',
    'nissaya': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ နိဿယပစ္စယေန ပစ္စယော။ ... စက္ခာယတနံ စက္ခုဝိညာဏဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ နိဿယပစ္စယေန ပစ္စယော။ ... ယံ ရူပံ နိဿာယ မနောဓာတု စ မနောဝိညာဏဓာတု စ ဝတ္တန္တိ၊ တံ ရူပံ မနောဓာတုယာ စ မနောဝိညာဏဓာတုယာ စ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ နိဿယပစ္စယေန ပစ္စယော။',
    'upanissaya': 'ပုရိမာ ပုရိမာ ကုသလာ ဓမ္မာ ပစ္ဆိမာနံ ပစ္ဆိမာနံ ကုသလာနံ ဓမ္မာနံ ဥပနိဿယပစ္စယေန ပစ္စယော။ ... ဥတုဘောဇနမ္ပိ ဥပနိဿယပစ္စယေန ပစ္စယော။ ပုဂ္ဂလောပိ ဥပနိဿယပစ္စယေန ပစ္စယော။ သေနာသနမ္ပိ ဥပနိဿယပစ္စယေန ပစ္စယော။',
    'purejata': 'စက္ခာယတနံ စက္ခုဝိညာဏဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ ပုရေဇာတပစ္စယေန ပစ္စယော။ ... ယံ ရူပံ နိဿာယ မနောဓာတု စ မနောဝိညာဏဓာတု စ ဝတ္တန္တိ၊ တံ ရူပံ မနောဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ ပုရေဇာတပစ္စယေန ပစ္စယော။ မနောဝိညာဏဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ ကိဉ္စိ ကာလေ ပုရေဇာတပစ္စယေန ပစ္စယော၊ ကိဉ္စိ ကာလေ န ပုရေဇာတပစ္စယေန ပစ္စယော။',
    'pacchajata': 'ပစ္ဆာဇာတာ စိတ္တစေတသိကာ ဓမ္မာ ပုရေဇာတဿ ဣမဿ ကာယဿ ပစ္ဆာဇာတပစ္စယေန ပစ္စယော။',
    'asevana': 'ပုရိမာ ပုရိမာ ကုသလာ ဓမ္မာ ပစ္ဆိမာနံ ပစ္ဆိမာနံ ကုသလာနံ ဓမ္မာနံ အာသေဝနပစ္စယေန ပစ္စယော။ ပုရိမာ ပုရိမာ အကုသလာ ဓမ္မာ... ပုရိမာ ပုရိမာ ကိရိယာဗျာကတာ ဓမ္မာ ပစ္ဆိမာနံ ပစ္ဆိမာနံ ကိရိယာဗျာကတာနံ ဓမ္မာနံ အာသေဝနပစ္စယေန ပစ္စယော။',
    'kamma': 'ကုသလာကုသလံ ကမ္မံ ဝိပါကာနံ ခန္ဓာနံ ကဋတ္တာ စ ရူပါနံ ကမ္မပစ္စယေန ပစ္စယော။ စေတနာ သမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ ကမ္မပစ္စယေန ပစ္စယော။',
    'vipaka': 'ဝိပါကာ စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ ဝိပါကပစ္စယေန ပစ္စယော။',
    'ahara': 'ကဗဠီကာရော အာဟာရော ဣမဿ ကာယဿ အာဟာရပစ္စယေန ပစ္စယော။ အရူပိနော အာဟာရာ သမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ အာဟာရပစ္စယေန ပစ္စယော။',
    'indriya': 'စက္ခုန္ဒြိယံ စက္ခုဝိညာဏဓာတုယာ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ ဣန္ဒြိယပစ္စယေန ပစ္စယော။ ... ရူပဇီဝိတိန္ဒြိယံ ကဋတ္တာရူပါနံ ဣန္ဒြိယပစ္စယေန ပစ္စယော။ အရူပိနော ဣန္ဒြိယာ သမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ ဣန္ဒြိယပစ္စယေန ပစ္စယော။',
    'jhana': 'ဈာနင်္ဂါနိ ဈာနသမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ ဈာနပစ္စယေန ပစ္စယော။',
    'magga': 'မဂ္ဂင်္ဂါနိ မဂ္ဂသမ္ပယုတ္တကာနံ ဓမ္မာနံ တံသမုဋ္ဌာနာနဉ္စ ရူပါနံ မဂ္ဂပစ္စယေန ပစ္စယော။',
    'sampayutta': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ သမ္ပယုတ္တပစ္စယေန ပစ္စယော။',
    'vippayutta': 'ရူပိနော ဓမ္မာ အရူပီနံ ဓမ္မာနံ ဝိပ္ပယုတ္တပစ္စယေန ပစ္စယော။ အရူပိနော ဓမ္မာ ရူပီနံ ဓမ္မာနံ ဝိပ္ပယုတ္တပစ္စယေန ပစ္စယော။',
    'atthi': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ အတ္ထိပစ္စယေန ပစ္စယော။ စတ္တာရော မဟာဘူတာ အညမညံ အတ္ထိပစ္စယေန ပစ္စယော။ ... ယံ ရူပံ နိဿာယ မနောဓာတု စ မနောဝိညာဏဓာတု စ ဝတ္တန္တိ၊ တံ ရူပံ မနောဓာတုယာ စ မနောဝိညာဏဓာတုယာ စ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ အတ္ထိပစ္စယေန ပစ္စယော။',
    'natthi': 'သမနန္တရနိရုဒ္ဓါ စိတ္တစေတသိကာ ဓမ္မာ ပဋုပ္ပန္နာနံ စိတ္တစေတသိကာနံ ဓမ္မာနံ နတ္ထိပစ္စယေန ပစ္စယော။',
    'vigata': 'သမနန္တရဝိဂတာ စိတ္တစေတသိကာ ဓမ္မာ ပဋုပ္ပန္နာနံ စိတ္တစေတသိကာနံ ဓမ္မာနံ ဝိဂတပစ္စယေန ပစ္စယော။',
    'avigata': 'စတ္တာရော ခန္ဓာ အရူပိနော အညမညံ အဝိဂတပစ္စယေန ပစ္စယော။ ... ယံ ရူပံ နိဿာယ မနောဓာတု စ မနောဝိညာဏဓာတု စ ဝတ္တန္တိ၊ တံ ရူပံ မနောဓာတုယာ စ မနောဝိညာဏဓာတုယာ စ တံသမ္ပယုတ္တကာနဉ္စ ဓမ္မာနံ အဝိဂတပစ္စယေန ပစ္စယော။'
}

html_file = 'paccaya_sangaha.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Add niddesaPali to each object in paccayaData array
for key, pali_text in niddesa_map.items():
    pattern = r"(\{.*?key:\s*'" + key + r"'.*?)( \})"
    replacement = r"\1,\n              niddesaPali: '" + pali_text + r"'\2"
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Update openPaccayaModal to display the niddesaPali
modal_script = """
        function openPaccayaModal(key) {
            const p = paccayaData.find(x => x.key === key);
            if (!p) return;
            const modal = document.getElementById('modal');
            const content = document.getElementById('modal-content');
            const info = clusterInfo[p.cluster];
            content.innerHTML = `
                <div class="text-center space-y-2">
                    <div class="w-16 h-16 mx-auto rounded-2xl bg-slate-800 flex items-center justify-center text-3xl border border-slate-700 ${info.color}">
                        <i class="fa-solid ${p.icon}"></i>
                    </div>
                    <div>
                        <span class="text-xs text-slate-400 uppercase font-mono">${info.label} — အမှတ် ${mm(p.id)}/၂၄</span>
                        <h3 class="text-xl font-bold ${info.color}">${p.name}</h3>
                        <p class="text-[11px] text-slate-500 font-mono mt-1">${p.pali}</p>
                    </div>
                </div>
                
                ${p.niddesaPali ? `
                <div class="mt-4 bg-amber-950/20 border border-amber-500/20 p-4 rounded-xl text-center space-y-2 relative overflow-hidden">
                    <div class="absolute -right-4 -top-4 opacity-10 text-amber-500 text-6xl"><i class="fa-solid fa-leaf"></i></div>
                    <span class="text-[10px] font-bold text-amber-500/70 block uppercase tracking-widest">ပစ္စယနိဒ္ဒေသ ပါဠိတော်</span>
                    <p class="text-amber-200/90 leading-relaxed font-[Pyidaungsu] text-[13px] md:text-sm">" ${p.niddesaPali} "</p>
                </div>
                ` : ''}

                <div class="mt-4 space-y-3 bg-slate-950/50 p-4 rounded-xl border border-slate-800 text-sm">
                    <div>
                        <span class="text-xs font-semibold text-slate-400 block uppercase">အနက်အဓိပ္ပာယ်</span>
                        <p class="text-slate-200 mt-1 leading-relaxed">${p.desc}</p>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-2 pt-2 text-xs">
                        <div class="p-2.5 rounded-lg bg-sky-950/40 border border-sky-500/20">
                            <span class="font-bold text-sky-300 block">ပစ္စယတရား (အကြောင်း)</span>
                            <span class="text-slate-300 text-[11px]">${p.paccayaText || 'သဟဇာတ နာမ်/ရုပ် တရားများ'}</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/20">
                            <span class="font-bold text-emerald-300 block">ပစ္စယုပ္ပန္နတရား (အကျိုး)</span>
                            <span class="text-slate-300 text-[11px]">${p.paccayuppannaText || 'ယှဉ်ဖက် နာမ်/ရုပ် တရားများ'}</span>
                        </div>
                    </div>
                    <div class="pt-3 border-t border-slate-800">
                        <span class="text-xs font-semibold text-amber-400 block uppercase"><i class="fa-solid fa-lightbulb mr-1"></i>ဥပမာ သရုပ်ပြ</span>
                        <p class="text-slate-300 mt-1 leading-relaxed">${p.example}</p>
                    </div>
                </div>
            `;
            modal.classList.remove('hidden');
        }
"""

content = re.sub(r'function openPaccayaModal\(key\) \{.*?(?=function showPatthanaPali)', modal_script.strip() + '\n\n        ', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated paccaya_sangaha.html with Paccayaniddesa successfully!")
