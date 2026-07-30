let cittaData = [];
(function buildCittaData() {
    let uid = 1;
    const push = (obj) => { cittaData.push(Object.assign({ id: uid++ }, obj)); };

    // --- Akusala (12): Lobha-mūla (8) ---
    ['သောမနဿ', 'ဥပေက္ခာ'].forEach(vedana => {
        [true, false].forEach(ditthi => {
            ['asankharika', 'sasankharika'].forEach(sankhara => {
                const sankharaTxt = sankhara === 'asankharika' ? 'အသင်္ခါရိက (အလိုလို)' : 'သသင်္ခါရိက (လှုံ့ဆော်မှုဖြင့်)';
                const ditthiTxt = ditthi ? 'ဒိဋ္ဌိဂတသမ္ပယုတ် (အယူမှားနှင့်ယှဉ်)' : 'ဒိဋ္ဌိဂတဝိပ္ပယုတ် (အယူမှားနှင့် မယှဉ်)';
                const vedanaPali = vedana === 'သောမနဿ' ? 'သောမနဿသဟဂတံ' : 'ဥပေက္ခာသဟဂတံ';
                const ditthiPali = ditthi ? 'ဒိဋ္ဌိဂတသမ္ပယုတ္တံ' : 'ဒိဋ္ဌိဂတဝိပ္ပယုတ္တံ';
                const sankharaPali = sankhara === 'asankharika' ? 'အသင်္ခါရိကံ' : 'သသင်္ခါရိကံ';
                const fullPali = `${vedanaPali} ${ditthiPali} ${sankharaPali} လောဘမူလစိတ္တံ`;

                push({
                    name: `${vedana}သဟဂတ် ${ditthiTxt} ${sankharaTxt} လောဘမူစိတ်`,
                    shortName: `လောဘမူ-${String(cittaData.filter(c => c.sub === 'လောဘမူ (၈)').length + 1).replace(/[0-9]/g, d => '၀၁၂၃၄၅၆၇၈၉'[d])}`,
                    pali: 'Lobha-mūla citta', group: 'akusala', groupLabel: 'အကုသိုလ်', sub: 'လောဘမူ (၈)',
                    desc: `<b>${fullPali}</b> - ${vedana} ခံစားမှုနှင့်တကွ${ditthi ? '၊ အယူမှားပါဝင်လျက်' : ''} အာရုံကို တပ်မက်ကပ်ငြိသော စိတ်။`,
                    cetasikaNote: `သဗ္ဗစိတ္တသာဓာရဏ (၇) + ပကိဏ္ဏက အများစု + အကုသိုလ်သာဓာရဏ (၄) + လောဘ${ditthi ? ' + ဒိဋ္ဌိ' : ''}${sankhara === 'sasankharika' ? ' + ထိန + မိဒ္ဓ (အခြေအနေအလိုက်)' : ''}`,
                    example: lobhaExample(vedana, ditthi, sankhara),
                    hetuCount: 2, vedanaType: vedana === 'သောမနဿ' ? 'somanassa' : 'upekkha', vatthuType: 'hadaya', dvaraType: 'other',
                    icon: 'fa-magnet', color: 'rose'
                });
            });
        });
    });

    // --- Dosa-mūla (2) ---
    ['asankharika', 'sasankharika'].forEach(sankhara => {
        const sankharaTxt = sankhara === 'asankharika' ? 'အသင်္ခါရိက (အလိုလို)' : 'သသင်္ခါရိက (လှုံ့ဆော်မှုဖြင့်)';
        const sankharaPali = sankhara === 'asankharika' ? 'အသင်္ခါရိကံ' : 'သသင်္ခါရိကံ';
        const fullPali = `ဒေါမနဿသဟဂတံ ပဋိဃသမ္ပယုတ္တံ ${sankharaPali} ဒေါသမူလစိတ္တံ`;

        push({
            name: `ဒေါမနဿသဟဂတ် ပဋိဃသမ္ပယုတ် ${sankharaTxt} ဒေါသမူစိတ်`,
            shortName: `ဒေါသမူ-${String(cittaData.filter(c => c.sub === 'ဒေါသမူ (၂)').length + 1).replace(/[0-9]/g, d => '၀၁၂၃၄၅၆၇၈၉'[d])}`,
            pali: 'Dosa-mūla citta', group: 'akusala', groupLabel: 'အကုသိုလ်', sub: 'ဒေါသမူ (၂)',
            desc: `<b>${fullPali}</b> - ဒေါမနဿ ခံစားမှုနှင့်တကွ ခက်ထန်ကြမ်းတမ်းစွာ ဖြစ်ပေါ်သော စိတ်။ ပီတိနှင့် လုံးဝ မယှဉ်ပေ။`,
            cetasikaNote: `သဗ္ဗစိတ္တသာဓာရဏ (၇) + ပကိဏ္ဏက (ပီတိမပါ) + အကုသိုလ်သာဓာရဏ (၄) + ဒေါသ${sankhara === 'sasankharika' ? ' + ထိန + မိဒ္ဓ (အခြေအနေအလိုက်)' : ''}`,
            example: dosaExample(sankhara),
            hetuCount: 2, vedanaType: 'domanassa', vatthuType: 'hadaya', dvaraType: 'other',
            icon: 'fa-fire', color: 'rose'
        });
    });

    // --- Moha-mūla (2) ---
    push({
        name: 'ဥပေက္ခာသဟဂတ် ဝိစိကိစ္ဆာသမ္ပယုတ် မောဟမူစိတ်', shortName: 'မောဟမူ-၁ (ဝိစိကိစ္ဆာ)', pali: 'Moha-mūla citta',
        group: 'akusala', groupLabel: 'အကုသိုလ်', sub: 'မောဟမူ (၂)',
        desc: '<b>ဥပေက္ခာသဟဂတံ ဝိစိကိစ္ဆာသမ္ပယုတ္တံ မောဟမူလစိတ္တံ</b> - ရတနာသုံးပါး၊ ကံနှင့် ကံ၏အကျိုးတို့၌ သံသယ ကင်းမဲ့စွာ ဖြစ်ပေါ်သော စိတ်။ ဆုံးဖြတ်ချက် (အဓိမောက္ခ) လုံးဝ မပါဝင်နိုင်ပေ။',
        cetasikaNote: 'သဗ္ဗစိတ္တသာဓာရဏ (၇) + ပကိဏ္ဏက (အဓိမောက္ခ၊ ဆန္ဒ မပါ) + အကုသိုလ်သာဓာရဏ (၄) + ဝိစိကိစ္ဆာ',
        example: '"ဤဘဝနောက် နောင်ဘဝ ရှိသလား မရှိဘူးလား" ဟု စွဲမြဲစွာ ဆုံးဖြတ်ချက်မရနိုင်အောင် သံသယဖြစ်နေသော အခိုက်။',
        hetuCount: 1, vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other',
        icon: 'fa-circle-question', color: 'rose'
    });
    push({
        name: 'ဥပေက္ခာသဟဂတ် ဥဒ္ဓစ္စသမ္ပယုတ် မောဟမူစိတ်', shortName: 'မောဟမူ-၂ (ဥဒ္ဓစ္စ)', pali: 'Moha-mūla citta',
        group: 'akusala', groupLabel: 'အကုသိုလ်', sub: 'မောဟမူ (၂)',
        desc: '<b>ဥပေက္ခာသဟဂတံ ဥဒ္ဓစ္စသမ္ပယုတ္တံ မောဟမူလစိတ္တံ</b> - အာရုံပေါင်းများစွာ ရောရှက်ကာ တစ်ခုမှ တည်ငြိမ်စွာ မဆွဲမကိုင်နိုင်ဘဲ ပျံ့လွင့်နေသော စိတ်။',
        cetasikaNote: 'သဗ္ဗစိတ္တသာဓာရဏ (၇) + ပကိဏ္ဏက အချို့ + အကုသိုလ်သာဓာရဏ (၄) + ဥဒ္ဓစ္စ',
        example: 'တရားထိုင်နေစဉ် အာရုံတစ်ခုမှ တစ်ခုသို့ အမြဲပြောင်းလဲ ပျံ့လွင့်နေပြီး ဘာမှ တည်ငြိမ်စွာ မဆုပ်ကိုင်နိုင်သော အခြေအနေ။',
        hetuCount: 1, vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other',
        icon: 'fa-wind', color: 'rose'
    });

    // --- Ahetuka (18) ---
    const ahetukaList = [
        { name: 'စက္ခုဝိညာဉ် (အကုသိုလ်ဝိပါက်)', fullPali: 'အကုသလဝိပါကံ စက္ခုဝိညာဏံ', desc: 'မကောင်းသော အကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် မလှပသော ပုံရိပ်ကို မြင်ခြင်း။', example: 'အရည်အသွေးညံ့ဖျင်း၍ မလှပသော ပုံရိပ်တစ်ခုကို မျက်စိဖြင့် မမျှော်လင့်ဘဲ မြင်လိုက်ရသော ခဏတာ။', icon: 'fa-eye', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'cakkhu', dvaraType: 'eka' },
        { name: 'သောတဝိညာဉ် (အကုသိုလ်ဝိပါက်)', fullPali: 'အကုသလဝိပါကံ သောတဝိညာဏံ', desc: 'အကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် နားမကြည်သော အသံကို ကြားခြင်း။', example: 'နားခေါင်းစူးစေသည့် အသံဆိုးကို ရုတ်တရက် ကြားလိုက်ရသော ခဏတာ။', icon: 'fa-ear-listen', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'sota', dvaraType: 'eka' },
        { name: 'ဃာနဝိညာဉ် (အကုသိုလ်ဝိပါက်)', fullPali: 'အကုသလဝိပါကံ ဃာနဝိညာဏံ', desc: 'အကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် နံ့ဆိုးကို ခံစားခြင်း။', example: 'နံ့ဆိုးတစ်မျိုးကို နှာခေါင်းဖြင့် ရုတ်တရက် ရလိုက်ရသော ခဏတာ။', icon: 'fa-wind', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'ghana', dvaraType: 'eka' },
        { name: 'ဇိဝှါဝိညာဉ် (အကုသိုလ်ဝိပါက်)', fullPali: 'အကုသလဝိပါကံ ဇိဝှာဝိညာဏံ', desc: 'အကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် အရသာဆိုးကို ခံစားခြင်း။', example: 'အရသာဆိုးသော အစားအစာကို လျှာဖြင့် တွေ့ကြုံလိုက်ရသော ခဏတာ။', icon: 'fa-utensils', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'jivha', dvaraType: 'eka' },
        { name: 'ကာယဝိညာဉ် (ဒုက္ခသဟဂတံ)', fullPali: 'ဒုက္ခသဟဂတံ ကာယဝိညာဏံ', desc: 'အကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် ခန္ဓာကိုယ်၌ ဒုက္ခခံစားမှုကို ခံစားခြင်း။', example: 'ဆူးထိုးမိသည့်အခါ ခံစားရသော ကိုယ်ထိအနာကျင်မှု ခဏတာ။', icon: 'fa-hand', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'dukkha', vatthuType: 'kaya', dvaraType: 'eka' },
        { name: 'သမ္ပဋိစ္ဆန (အကုသိုလ်)', fullPali: 'အကုသလဝိပါကံ သမ္ပဋိစ္ဆနစိတ္တံ', desc: 'မကောင်းသော အာရုံကို လက်ခံစဉ်းစားမိသည့် ပထမဆုံး တုံ့ပြန်မှု စိတ်။', example: 'ဆိုးသော အသံကို ကြားပြီးနောက် ချက်ချင်း လက်ခံမိသည့် ခဏတာ။', icon: 'fa-inbox', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other' },
        { name: 'သန္တီရဏ (အကုသိုလ်၊ ဥပေက္ခာ)', fullPali: 'ဥပေက္ခာသဟဂတံ အကုသလဝိပါကံ သန္တီရဏစိတ္တံ', desc: 'လက်ခံပြီးသော မကောင်းသည့် အာရုံကို ဥပေက္ခာစိတ်ဖြင့် စစ်ဆေးနေသည့် စိတ်။', example: 'မကောင်းသော အာရုံကို "ဒါဘာလဲ" ဟု လျစ်လျူသဘောဖြင့် စစ်ဆေးနေသော ခဏတာ။', icon: 'fa-magnifying-glass', sub: 'အကုသိုလ်ဝိပါက် (၇)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'vimutta' },
        { name: 'စက္ခုဝိညာဉ် (ကုသိုလ်ဝိပါက်)', fullPali: 'ကုသလဝိပါကံ စက္ခုဝိညာဏံ', desc: 'ကောင်းသော ကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် လှပသော ပုံရိပ်ကို မြင်ခြင်း။', example: 'လှပသော ပန်းချီကားတစ်ချပ်ကို မျက်စိဖြင့် မြင်လိုက်ရသော ခဏတာ။', icon: 'fa-eye', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'cakkhu', dvaraType: 'eka' },
        { name: 'သောတဝိညာဉ် (ကုသိုလ်ဝိပါက်)', fullPali: 'ကုသလဝိပါကံ သောတဝိညာဏံ', desc: 'ကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် နားထောင်ကောင်းသော အသံကို ကြားခြင်း။', example: 'နားထောင်ကောင်းသော တေးသွားလှလှကို ကြားလိုက်ရသော ခဏတာ။', icon: 'fa-ear-listen', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'sota', dvaraType: 'eka' },
        { name: 'ဃာနဝိညာဉ် (ကုသိုလ်ဝိပါက်)', fullPali: 'ကုသလဝိပါကံ ဃာနဝိညာဏံ', desc: 'ကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် နံ့သာကောင်းကို ခံစားခြင်း။', example: 'ပန်းနံ့သာကောင်းကို ရလိုက်ရသော ခဏတာ။', icon: 'fa-wind', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'ghana', dvaraType: 'eka' },
        { name: 'ဇိဝှါဝိညာဉ် (ကုသိုလ်ဝိပါက်)', fullPali: 'ကုသလဝိပါကံ ဇိဝှာဝိညာဏံ', desc: 'ကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် အရသာကောင်းကို ခံစားခြင်း။', example: 'အရသာချိုမြိန်သော အစားအစာကို လျှာဖြင့် တွေ့ကြုံလိုက်ရသော ခဏတာ။', icon: 'fa-utensils', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'jivha', dvaraType: 'eka' },
        { name: 'ကာယဝိညာဉ် (သုခသဟဂတံ)', fullPali: 'သုခသဟဂတံ ကာယဝိညာဏံ', desc: 'ကုသိုလ်ကံ၏ အကျိုးဆက်အနေဖြင့် ခန္ဓာကိုယ်၌ ချမ်းသာမှုကို ခံစားခြင်း။', example: 'နူးညံ့ပျော့ပျောင်းသည့် ထိတွေ့မှုကြောင့် ခံစားရသော ကိုယ်ချမ်းသာမှု ခဏတာ။', icon: 'fa-hand', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'sukha', vatthuType: 'kaya', dvaraType: 'eka' },
        { name: 'သမ္ပဋိစ္ဆန (ကုသိုလ်)', fullPali: 'ကုသလဝိပါကံ သမ္ပဋိစ္ဆနစိတ္တံ', desc: 'ကောင်းသော အာရုံကို လက်ခံစဉ်းစားမိသည့် ပထမဆုံး တုံ့ပြန်မှု စိတ်။', example: 'ကောင်းသော အသံကို ကြားပြီးနောက် ချက်ချင်း လက်ခံမိသည့် ခဏတာ။', icon: 'fa-inbox', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other' },
        { name: 'သန္တီရဏ (ကုသိုလ်၊ ဥပေက္ခာ)', fullPali: 'ဥပေက္ခာသဟဂတံ ကုသလဝိပါကံ သန္တီရဏစိတ္တံ', desc: 'လက်ခံပြီးသော ကောင်းသည့် အာရုံကို ဥပေက္ခာစိတ်ဖြင့် စစ်ဆေးနေသည့် စိတ်။', example: 'ရိုးရိုးသာ ကောင်းသည့် အာရုံကို လျစ်လျူသဘောဖြင့် စစ်ဆေးနေသော ခဏတာ။', icon: 'fa-magnifying-glass', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'vimutta' },
        { name: 'သန္တီရဏ (ကုသိုလ်၊ သောမနဿ)', fullPali: 'သောမနဿသဟဂတံ ကုသလဝိပါကံ သန္တီရဏစိတ္တံ', desc: 'အလွန်နှစ်သက်ဖွယ်ကောင်းသော အာရုံကို ဝမ်းမြောက်စွာ စစ်ဆေးနေသည့် စိတ်။', example: 'အလွန်နှစ်သက်ဖွယ် လှပသော ပန်းချီကားကို ဝမ်းမြောက်စွာ စိစစ်နေသော ခဏတာ။', icon: 'fa-magnifying-glass', sub: 'ကုသိုလ်ဝိပါက် (၈)', vedanaType: 'somanassa', vatthuType: 'hadaya', dvaraType: 'other' },
        { name: 'ပဉ္စဒွါရာဝဇ္ဇန်း', fullPali: 'ပဉ္စဒွါရာဝဇ္ဇနစိတ္တံ', desc: 'ခန္ဓာဒွါရ (၅) ပါးမှ အာရုံသစ် ဝင်ရောက်လာသည်နှင့် စိတ်ကို ထိုဒွါရဘက်သို့ ဦးစွာ လှည့်ပေးသည့် အလုပ်ဆောင်စိတ်။', example: 'အသံတစ်ခု ရုတ်တရက် ကြားလိုက်ရသည်နှင့် နားဘက်သို့ အာရုံလှည့်ပေးလိုက်သော ပထမဆုံး ခဏတာ (ရဟန္တာတွင်လည်း ဖြစ်တတ်သည်)။', icon: 'fa-door-open', sub: 'ကြိယာ (၃)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other' },
        { name: 'မနောဒွါရာဝဇ္ဇန်း (ဝေါဋ္ဌဗ္ဗန)', fullPali: 'မနောဒွါရာဝဇ္ဇနစိတ္တံ', desc: 'စိတ်တံခါးမှတစ်ဆင့် အာရုံသစ်ကို လက်ခံမည့် စိတ်ကို ဦးစွာ ဦးတည်ပေးသည့် အလုပ်ဆောင်စိတ်။', example: 'အတွေးတစ်ခု ရုတ်တရက် စိတ်ထဲ ပေါ်လာသည့်အခါ ထိုအတွေးဘက်သို့ ဦးစွာ အာရုံ ညွှန်ပေးလိုက်သော ခဏတာ။', icon: 'fa-brain', sub: 'ကြိယာ (၃)', vedanaType: 'upekkha', vatthuType: 'hadaya', dvaraType: 'other' },
        { name: 'ဟသိတုပ္ပါဒ', fullPali: 'ဟသိတုပ္ပါဒစိတ္တံ', desc: 'ရဟန္တာပုဂ္ဂိုလ်များ၌သာ ဖြစ်တတ်သော၊ ကိလေသာနှင့် ကင်းစင်သည့် အပြုံးဖြစ်ပေါ်စေသော ကြိယာစိတ်။', example: 'ရဟန္တာတစ်ပါးက ရိုးရိုးလေးသော အရာတစ်ခုကို မြင်လိုက်ရသည့်အခါ ကိလေသာ ကင်းစင်စွာ အပြုံးဖြစ်ပေါ်လာသော ခဏတာ။', icon: 'fa-face-grin', sub: 'ကြိယာ (၃)', vedanaType: 'somanassa', vatthuType: 'hadaya', dvaraType: 'other' }
    ];
    ahetukaList.forEach(a => push({
        name: a.name, shortName: a.name.split(' ')[0], pali: 'Ahetuka citta',
        group: 'ahetuka', groupLabel: 'အဟေတုက', sub: a.sub,
        desc: `<b>${a.fullPali}</b> - ${a.desc}`, cetasikaNote: 'သဗ္ဗစိတ္တသာဓာရဏ (၇) ပါးသာ ယှဉ်တွဲသည် (ဟိတ်မူလ၊ ပကိဏ္ဏက လုံးဝ မပါ)',
        example: a.example, icon: a.icon, color: 'slate',
        hetuCount: 0, vedanaType: a.vedanaType, vatthuType: a.vatthuType, dvaraType: a.dvaraType
    }));

    // --- Kāmāvacara Sobhana (24): Mahā-kusala / Mahā-vipāka / Mahā-kiriya ---
    const paliMap = { 'ကုသိုလ်': 'kusala', 'ဝိပါက်': 'vipāka', 'ကြိယာ': 'kiriya' };
    [{ key: 'ကုသိုလ်', groupLabel: 'ကာမာဝစရ ကုသိုလ်', color: 'emerald', icon: 'fa-hand-holding-heart' },
     { key: 'ဝိပါက်', groupLabel: 'ကာမာဝစရ ဝိပါက်', color: 'emerald', icon: 'fa-seedling' },
     { key: 'ကြိယာ', groupLabel: 'ကာမာဝစရ ကြိယာ', color: 'emerald', icon: 'fa-hand-fist' }
    ].forEach(g => {
        ['သောမနဿ', 'ဥပေက္ခာ'].forEach(vedana => {
            ['ဉာဏသမ္ပယုတ်', 'ဉာဏဝိပ္ပယုတ်'].forEach(nana => {
                ['asankharika', 'sasankharika'].forEach(sankhara => {
                    const sankharaTxt = sankhara === 'asankharika' ? 'အသင်္ခါရိက' : 'သသင်္ခါရိက';
                    
                    const vedanaPali = vedana === 'သောမနဿ' ? 'သောမနဿသဟဂတံ' : 'ဥပေက္ခာသဟဂတံ';
                    const nanaPali = nana === 'ဉာဏသမ္ပယုတ်' ? 'ဉာဏသမ္ပယုတ္တံ' : 'ဉာဏဝိပ္ပယုတ္တံ';
                    const sankharaPali = sankhara === 'asankharika' ? 'အသင်္ခါရိကံ' : 'သသင်္ခါရိကံ';
                    const typePali = g.key === 'ကုသိုလ်' ? 'မဟာကုသလစိတ္တံ' : (g.key === 'ဝိပါက်' ? 'မဟာဝိပါကစိတ္တံ' : 'မဟာကြိယာစိတ္တံ');
                    const fullPali = `${vedanaPali} ${nanaPali} ${sankharaPali} ${typePali}`;

                    const rawDesc = g.key === 'ကုသိုလ်' ? `ဒါန၊ သီလ၊ ဘာဝနာ ပြုလုပ်စဉ် ${vedana} ခံစားမှုနှင့် ${nana === 'ဉာဏသမ္ပယုတ်' ? 'ပညာ ယှဉ်တွဲလျက်' : 'ပညာ မယှဉ်ဘဲ'} ဖြစ်ပေါ်သော ကုသိုလ်စိတ်။`
                            : g.key === 'ဝိပါက်' ? `မဟာကုသိုလ်၏ အကျိုးအနေဖြင့် ပဋိသန္ဓေ၊ ဘဝင်၊ စုတိ အဖြစ် ${vedana} ခံစားမှုနှင့်တကွ ဆောင်ရွက်သော ဝိပါက်စိတ်။`
                            : `ရဟန္တာပုဂ္ဂိုလ်တို့၌သာ ဖြစ်တတ်သော၊ ${vedana} ခံစားမှုနှင့်တကွ အကျိုးမပေးတော့သည့် ကြိယာစိတ်။`;

                    push({
                        name: `${vedana}သဟဂတ် ${nana} ${sankharaTxt} မဟာ${g.key}စိတ်`,
                        shortName: `မဟာ${g.key}-${String(cittaData.filter(c => c.sub === `မဟာ${g.key} (၈)`).length + 1).replace(/[0-9]/g, d => '၀၁၂၃၄၅၆၇၈၉'[d])}`,
                        pali: `Mahā-${paliMap[g.key]} citta`, group: 'sobhana54', groupLabel: g.groupLabel, sub: `မဟာ${g.key} (၈)`,
                        desc: `<b>${fullPali}</b> - ${rawDesc}`,
                        cetasikaNote: g.key === 'ဝိပါက်'
                            ? `အညသမာန (၁၃) + သောဘဏသာဓာရဏ (၁၉)${nana === 'ဉာဏသမ္ပယုတ်' ? ' + ပညိန္ဒြေ' : ''} — ဝိရတီနှင့် အပ္ပမညာ မပါ`
                            : `အညသမာန (၁၃) + သောဘဏသာဓာရဏ (၁၉) + ဝိရတီ (အခြေအနေအလိုက်) + အပ္ပမညာ (အခြေအနေအလိုက်)${nana === 'ဉာဏသမ္ပယုတ်' ? ' + ပညိန္ဒြေ' : ''}`,
                        example: kusalaExample(vedana, nana, sankhara, g.key),
                        hetuCount: nana === 'ဉာဏသမ္ပယုတ်' ? 3 : 2,
                        vedanaType: vedana === 'သောမနဿ' ? 'somanassa' : 'upekkha',
                        vatthuType: 'hadaya',
                        dvaraType: g.key === 'ဝိပါက်' ? 'vimutta' : 'other',
                        icon: g.icon, color: g.color
                    });
                });
            });
        });
    });

    // --- Rūpāvacara (15) ---
    const jhanaLevels = [
        { name: 'ပဌမ', pali: 'Paṭhama', full: 'ပဌမဇ္ဈာန', factors: 'ဝိတက်၊ ဝိစာရ၊ ပီတိ၊ သုခ၊ ဧကဂ္ဂတာ (၅) ပါးလုံး ထင်ရှား' },
        { name: 'ဒုတိယ', pali: 'Dutiya', full: 'ဒုတိယဇ္ဈာန', factors: 'ဝိစာရ၊ ပီတိ၊ သုခ၊ ဧကဂ္ဂတာ (၄) ပါး (ဝိတက် ချုပ်ငြိမ်း)' },
        { name: 'တတိယ', pali: 'Tatiya', full: 'တတိယဇ္ဈာန', factors: 'ပီတိ၊ သုခ၊ ဧကဂ္ဂတာ (၃) ပါး (ဝိတက်၊ ဝိစာရ ချုပ်ငြိမ်း)' },
        { name: 'စတုတ္ထ', pali: 'Catuttha', full: 'စတုတ္ထဇ္ဈာန', factors: 'သုခ၊ ဧကဂ္ဂတာ (၂) ပါး (ပီတိပါ ချုပ်ငြိမ်း)' },
        { name: 'ပဉ္စမ', pali: 'Pañcama', full: 'ပဉ္စမဇ္ဈာန', factors: 'ဥပေက္ခာ၊ ဧကဂ္ဂတာ (၂) ပါး (သုခသည် ဥပေက္ခာအဖြစ် ပြောင်းလဲ)' }
    ];
    const typePaliMap = { 'ကုသိုလ်': 'ကုသလစိတ္တံ', 'ဝိပါက်': 'ဝိပါကစိတ္တံ', 'ကြိယာ': 'ကြိယာစိတ္တံ' };
    
    ['ကုသိုလ်', 'ဝိပါက်', 'ကြိယာ'].forEach(g => {
        jhanaLevels.forEach(j => {
            const fullPali = `${j.full} ${typePaliMap[g]}`;
            const rawDesc = `သမထဘာဝနာ အားထုတ်၍ ${j.name}ဈာန် ရရှိသူ၏ ${g === 'ကုသိုလ်' ? 'ဈာန်စံနေချိန် ဖြစ်ပေါ်သော ကုသိုလ်' : g === 'ဝိပါက်' ? 'ဗြဟ္မာဘုံ၌ ပဋိသန္ဓေအဖြစ် ဆောင်ရွက်သော ဝိပါက်' : 'ရဟန္တာ ဈာန်ဝင်စားချိန်၌သာ ဖြစ်တတ်သော ကြိယာ'} စိတ်။`;
            
            push({
                name: `${j.name}ဈာန် ${g}စိတ်`, shortName: `${j.name}ဈာန်-${g}`, pali: `${j.pali} jhāna ${paliMap[g]} citta`,
                group: 'rupa', groupLabel: 'ရူပါဝစရ', sub: `${j.name}ဈာန် (၃)`,
                desc: `<b>${fullPali}</b> - ${rawDesc}`,
                cetasikaNote: `အညသမာန (၁၃) + သောဘဏသာဓာရဏ (၁၉) + ပညိန္ဒြေ — ဈာန်အင်္ဂါများအနက် ${j.factors}`,
                example: g === 'ကုသိုလ်' ? `ယောဂီတစ်ဦးက ကသိုဏ်းအာရုံကို အားထုတ်၍ ${j.name}ဈာန်သို့ ပထမဆုံး ဝင်စားနေချိန် ဖြစ်ပေါ်သော စိတ်။`
                    : g === 'ဝိပါက်' ? `${j.name}ဈာန် ရရှိခဲ့သူ သေဆုံးပြီးနောက် ရူပဗြဟ္မာဘုံ၌ ပဋိသန္ဓေယူသော ခဏတာ။`
                    : `ရဟန္တာ ဈာန်လဒ်ရသူတစ်ပါးက ${j.name}ဈာန်သို့ တစ်ဖန် ပြန်ဝင်စားနေချိန် ဖြစ်ပေါ်သော စိတ်။`,
                hetuCount: 3, vedanaType: j.name === 'ပဉ္စမ' ? 'upekkha' : 'somanassa', vatthuType: 'hadaya', dvaraType: g === 'ဝိပါက်' ? 'vimutta' : 'other',
                icon: 'fa-mountain-sun', color: 'sky'
            });
        });
    });

    // --- Arūpāvacara (12) ---
    const arupaLevels = [
        { name: 'အာကာသာနဉ္စာယတန', pali: 'Ākāsānañcāyatana', full: 'အာကာသာနဉ္စာယတန' },
        { name: 'ဝိညာဏဉ္စာယတန', pali: 'Viññāṇañcāyatana', full: 'ဝိညာဏဉ္စာယတန' },
        { name: 'အာကိဉ္စညာယတန', pali: 'Ākiñcaññāyatana', full: 'အာကိဉ္စညာယတန' },
        { name: 'နေဝသညာနာသညာယတန', pali: 'Nevasaññānāsaññāyatana', full: 'နေဝသညာနာသညာယတန' }
    ];
    ['ကုသိုလ်', 'ဝိပါက်', 'ကြိယာ'].forEach(g => {
        arupaLevels.forEach(lvl => {
            const fullPali = `${lvl.full} ${typePaliMap[g]}`;
            const rawDesc = `ရူပါရုံမှပင် လွတ်မြောက်၍ ${lvl.name} အရူပဈာန်ကို အခြေခံသော ${g === 'ကုသိုလ်' ? 'ကုသိုလ်' : g === 'ဝိပါက်' ? 'အရူပဗြဟ္မာ ပဋိသန္ဓေ ဝိပါက်' : 'ရဟန္တာ့ ကြိယာ'} စိတ်။`;
            
            push({
                name: `${lvl.name} ${g}စိတ်`, shortName: `${lvl.name.slice(0, 6)}-${g}`, pali: `${lvl.pali} ${paliMap[g]} citta`,
                group: 'arupa', groupLabel: 'အရူပါဝစရ', sub: `${lvl.name} (၃)`,
                desc: `<b>${fullPali}</b> - ${rawDesc}`,
                cetasikaNote: 'အညသမာန (၁၃) + သောဘဏသာဓာရဏ (၁၉) + ပညိန္ဒြေ — ဥပေက္ခာနှင့် ဧကဂ္ဂတာသာ ဈာန်အင်္ဂါအဖြစ် ထင်ရှား',
                example: g === 'ကုသိုလ်' ? `ပဉ္စမဈာန်လဒ် ရရှိပြီးသား ယောဂီက ${lvl.name} အာရုံကို ထပ်မံ အားထုတ်နေချိန် ဖြစ်ပေါ်သော စိတ်။`
                    : g === 'ဝိပါက်' ? `${lvl.name} ဈာန်ရသူ သေဆုံးပြီးနောက် အရူပဗြဟ္မာဘုံ၌ ပဋိသန္ဓေယူသော ခဏတာ။`
                    : `ရဟန္တာ ဈာန်လဒ်ရသူတစ်ပါးက ${lvl.name} ဈာန်သို့ ပြန်ဝင်စားနေချိန် ဖြစ်ပေါ်သော စိတ်။`,
                hetuCount: 3, vedanaType: 'upekkha', vatthuType: 'none', dvaraType: g === 'ဝိပါက်' ? 'vimutta' : 'other',
                icon: 'fa-cloud-moon', color: 'indigo'
            });
        });
    });

    // --- Lokuttara (8) ---
    const ariyaStages = [
        { name: 'သောတာပတ္တိ', pali: 'Sotāpatti', full: 'သောတာပတ္တိ', cut: 'သက္ကာယဒိဋ္ဌိ (ကိုယ်ကိုယ်စွဲလမ်းမှု)၊ ဝိစိကိစ္ဆာ (သံသယ)၊ သီလဗ္ဗတပရာမာသ (ဓလေ့စွဲလမ်းမှု) သံယောဇဉ် (၃) ပါးကို အပြီးအပိုင် ပယ်ဖြတ်' },
        { name: 'သကဒါဂါမိ', pali: 'Sakadāgāmi', full: 'သကဒါဂါမိ', cut: 'ကာမရာဂ၊ ပဋိဃ သံယောဇဉ်တို့ကို ချုတွင်းစေ (အပြီးအပိုင် မပယ်သေး)' },
        { name: 'အနာဂါမိ', pali: 'Anāgāmi', full: 'အနာဂါမိ', cut: 'ကာမရာဂ၊ ပဋိဃ သံယောဇဉ် (၂) ပါးကို အပြီးအပိုင် ပယ်ဖြတ်' },
        { name: 'အရဟတ္တ', pali: 'Arahatta', full: 'အရဟတ္တ', cut: 'ကျန်ရှိသေးသော ရူပရာဂ၊ အရူပရာဂ၊ မာန၊ ဥဒ္ဓစ္စ၊ အဝိဇ္ဇာ သံယောဇဉ် (၅) ပါးလုံးကို အကြွင်းမဲ့ ပယ်ဖြတ်' }
    ];
    const maggaPhalaMap = { 'မဂ်': 'မဂ္ဂစိတ္တံ', 'ဖိုလ်': 'ဖလစိတ္တံ' };
    
    ariyaStages.forEach(s => {
        ['မဂ်', 'ဖိုလ်'].forEach(type => {
            const fullPali = `${s.full}${maggaPhalaMap[type]}`;
            const rawDesc = type === 'မဂ်' ? `${s.cut}သော ဉာဏ်အထွဋ်အခေါင် ဥတ္ပာဒ်ခဏ စိတ်။` : `${s.name}မဂ်၏ အကျိုးဆက်အနေဖြင့် နိဗ္ဗာန်ကို အာရုံပြု၍ ချမ်းသာစွာ ခံစားနေသော ဖိုလ်စိတ်။`;
            
            push({
                name: `${s.name}${type}စိတ်`, shortName: `${s.name}-${type}`, pali: `${s.pali}-${type === 'မဂ်' ? 'magga' : 'phala'} citta`,
                group: 'lokuttara', groupLabel: 'လောကုတ္တရာ', sub: `${type} (၄)`,
                desc: `<b>${fullPali}</b> - ${rawDesc}`,
                cetasikaNote: 'အညသမာန (၁၃) + သောဘဏသာဓာရဏ (၁၉) + ပညိန္ဒြေ + ဝိရတီ (၃) ပါးလုံး တစ်ပြိုင်နက် = (၃၆)',
                example: type === 'မဂ်' ? `ဝိပဿနာဉာဏ် အထွတ်အထိပ်သို့ ရောက်ပြီး နိဗ္ဗာန်ကို ပထမဆုံးအကြိမ် မျက်မှောက်ပြု၍ ${s.cut} ခဏတာ။`
                    : `${s.name}မဂ်ဖြင့် သိမြင်ပြီးနောက် ထိုအကျိုးဆက် နိဗ္ဗာန်သုခကို ဆက်လက် ခံစားနေသော ခဏတာ။`,
                hetuCount: 3, vedanaType: 'variable', vatthuType: 'hadaya', dvaraType: 'other',
                icon: 'fa-dharmachakra', color: 'amber'
            });
        });
    });
})();

function lobhaExample(vedana, ditthi, sankhara) {
    if (vedana === 'သောမနဿ' && ditthi && sankhara === 'asankharika') return 'ဈေးဝယ်ရာတွင် နှစ်သက်သော ပစ္စည်းကို တွေ့၍ "ငါ့ဟာပဲ" ဟု အလိုလို အယူမှားစွာ အလွန်အမင်း တပ်မက်နေသော အခိုက်။';
    if (vedana === 'သောမနဿ' && !ditthi && sankhara === 'sasankharika') return 'သူတစ်ပါးက တိုက်တွန်း၍ ကောင်းသော စားစရာကို ဝမ်းသာအားရ စားသောက်နေသော အခိုက်။';
    return 'အာရုံတစ်ခုကို အခြေအနေအလိုက် တပ်မက်နေသော သဘော (ဥပမာ ပြောင်းလဲနိုင်သည်)။';
}

function dosaExample(sankhara) {
    if (sankhara === 'asankharika') return 'မိမိမနှစ်သက်သော စကားကို ကြား၍ အလိုလို ဒေါသအမျက် ထွက်လာသော အခိုက်။';
    return 'သူတစ်ပါးက သွေးထိုးပေး၍ သို့မဟုတ် အကြိမ်ကြိမ် စဉ်းစားပြီးမှ ဒေါသထွက်လာသော အခိုက်။';
}

function kusalaExample(vedana, nana, sankhara, type) {
    if (type === 'ကုသိုလ်' && vedana === 'သောမနဿ' && nana === 'ဉာဏသမ္ပယုတ်' && sankhara === 'asankharika') return 'ကံနှင့် ကံ၏အကျိုးကို ရှင်းလင်းစွာ သိမြင်၍ ဝမ်းမြောက်ဝမ်းသာဖြင့် အလိုလို ကုသိုလ်ပြုနေသော အခိုက်။';
    if (type === 'ကုသိုလ်' && vedana === 'ဥပေက္ခာ' && nana === 'ဉာဏဝိပ္ပယုတ်') return 'ပညာဖြင့် အထူးဆင်ခြင်ခြင်း မရှိဘဲ၊ ဝမ်းသာခြင်းလည်း မရှိဘဲ သာမန်အားဖြင့် ကုသိုလ်ပြုနေသော အခိုက်။';
    return `${type}စိတ်၏ သဘောတရားအလိုက် ဖြစ်ပေါ်နေသော အခြေအနေ။`;
}

function mm(num) {
    return num.toString().replace(/[0-9]/g, d => '၀၁၂၃၄၅၆၇၈၉'[d]);
}