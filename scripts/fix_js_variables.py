with open('vithi_sangaha.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """        function scrollToSection(id) {
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }

        const appanaDetailedData = [
            { name: '၁။ ဈာနဝီထိ (Jhāna Vīthi)', icon: 'fa-mountain', color: 'sky', desc: '<b>ဈာနဝီထိ</b> - သမထ ကမ္မဋ္ဌာန်း စီးဖြန်း၍ ရူပ/အရူပ ဈာန် ရရှိဝင်စားသော ဝီထိ။ (ပရိကံ၊ ဥပစာ၊ အနုလုံ၊ ဂေါတြဘူ ဟူသော ကာမဇောအပြီးတွင် ဈာန်အပ္ပနာဇော ဖြစ်ပေါ်သည်)' },
            { name: '၂။ မဂ္ဂဝီထိ (Magga Vīthi)', icon: 'fa-dharmachakra', color: 'amber', desc: '<b>မဂ္ဂဝီထိ</b> - ဝိပဿနာ ရှုမှတ်၍ မဂ်ဉာဏ် ရရှိသော ဝီထိ။ (ပရိကံ၊ ဥပစာ၊ အနုလုံ၊ ဂေါတြဘူ ပြီးနောက် မဂ်စိတ် ၁ ကြိမ်၊ ထို့နောက် ဖိုလ်စိတ် ၂/၃ ကြိမ် ဖြစ်ပေါ်သည်)' },
            { name: '၃။ ဖလသမာပတ္တိဝီထိ (Phala-samāpatti Vīthi)', icon: 'fa-sun', color: 'emerald', desc: 'အရိယာပုဂ္ဂိုလ်များ (သောတာပန်၊ သကဒါဂါမ်၊ အနာဂါမ်၊ ရဟန္တာ) မိမိတို့ ရရှိပြီးသော ဖိုလ်သမာပတ်ကို ဝင်စား၍ နိဗ္ဗာန်ချမ်းသာကို နာရီပေါင်းများစွာ ဆက်တိုက် ခံစားသော ဝီထိ။' },
            { name: '၄။ နိရောဓသမာပတ္တိဝီထိ (Nirodha-samāpatti Vīthi)', icon: 'fa-peace', color: 'rose', desc: 'အနာဂါမီ သို့မဟုတ် အရဟတ္တဖလဋ္ဌာန် ရဟန္တာအရှင်မြတ်များ စိတ်၊ စေတသိက်၊ စိတ္တဇရုပ် တရားအားလုံးကို ၇ ရက်တိုင်တိုင် အကြွင်းမဲ့ ငြိမ်းအေးစေလျက် ဝင်စားသော အမြင့်ဆုံး သမာပတ် ဝီထိ။' }
        ];"""

replacement = """        function scrollToSection(id) {
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }

        const appanaJhanaSeq = ['b', 'mano', 'parikamma', 'upacara', 'anuloma', 'gotrabhu', 'appana', 'b', 'b'];
        const appanaMaggaSeq = ['b', 'mano', 'parikamma', 'upacara', 'anuloma', 'gotrabhu', 'magga', 'phala', 'phala', 'b'];
        const appanaPhalaSeq = ['b', 'mano', 'anuloma', 'anuloma', 'anuloma', 'anuloma', 'phala', 'phala', 'phala', 'phala', 'b'];
        const appanaNirodhaSeq = ['b', 'mano', 'parikamma', 'upacara', 'anuloma', 'gotrabhu', 'neva', 'neva', 'nirodha', 'anagami', 'b']; 

        const appanaDetailedData = [
            { id: 'jhana', seq: appanaJhanaSeq, name: '၁။ ဈာနဝီထိ (Jhāna Vīthi)', icon: 'fa-mountain', color: 'sky', desc: '<b>ဈာနဝီထိ</b> - သမထ ကမ္မဋ္ဌာန်း စီးဖြန်း၍ ရူပ/အရူပ ဈာန် ရရှိဝင်စားသော ဝီထိ။ (ပရိကံ၊ ဥပစာ၊ အနုလုံ၊ ဂေါတြဘူ ဟူသော ကာမဇောအပြီးတွင် ဈာန်အပ္ပနာဇော ဖြစ်ပေါ်သည်)' },
            { id: 'magga', seq: appanaMaggaSeq, name: '၂။ မဂ္ဂဝီထိ (Magga Vīthi)', icon: 'fa-dharmachakra', color: 'amber', desc: '<b>မဂ္ဂဝီထိ</b> - ဝိပဿနာ ရှုမှတ်၍ မဂ်ဉာဏ် ရရှိသော ဝီထိ။ (ပရိကံ၊ ဥပစာ၊ အနုလုံ၊ ဂေါတြဘူ ပြီးနောက် မဂ်စိတ် ၁ ကြိမ်၊ ထို့နောက် ဖိုလ်စိတ် ၂/၃ ကြိမ် ဖြစ်ပေါ်သည်)' },
            { id: 'phala', seq: appanaPhalaSeq, name: '၃။ ဖလသမာပတ္တိဝီထိ (Phala-samāpatti Vīthi)', icon: 'fa-sun', color: 'emerald', desc: 'အရိယာပုဂ္ဂိုလ်များ (သောတာပန်၊ သကဒါဂါမ်၊ အနာဂါမ်၊ ရဟန္တာ) မိမိတို့ ရရှိပြီးသော ဖိုလ်သမာပတ်ကို ဝင်စား၍ နိဗ္ဗာန်ချမ်းသာကို နာရီပေါင်းများစွာ ဆက်တိုက် ခံစားသော ဝီထိ။' },
            { id: 'nirodha', seq: appanaNirodhaSeq, name: '၄။ နိရောဓသမာပတ္တိဝီထိ (Nirodha-samāpatti Vīthi)', icon: 'fa-peace', color: 'rose', desc: 'အနာဂါမီ သို့မဟုတ် အရဟတ္တဖလဋ္ဌာန် ရဟန္တာအရှင်မြတ်များ စိတ်၊ စေတသိက်၊ စိတ္တဇရုပ် တရားအားလုံးကို ၇ ရက်တိုင်တိုင် အကြွင်းမဲ့ ငြိမ်းအေးစေလျက် ဝင်စားသော အမြင့်ဆုံး သမာပတ် ဝီထိ။' }
        ];"""

if target in content:
    content = content.replace(target, replacement)
    with open('vithi_sangaha.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed JS variables.")
else:
    print("Target not found.")
