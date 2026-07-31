
        // Load Terms
        const originalTerms = [
            { term: 'Abhidhamma (အဘိဓမ္မာ)', meaning: 'လွန်ကဲထူးမြတ်သော တရား (အကြောင်းအကျိုး သက်သက်ကိုသာ ဟောကြားထားသော ဒေသနာ)' },
            { term: 'Adhikāra (အဓိကာရ)', meaning: 'အုပ်စိုးခြင်း၊ လွှမ်းမိုးခြင်း၊ အဓိကဖြစ်ခြင်း' },
            { term: 'Adhimokkha (အဓိမောက္ခ)', meaning: 'အာရုံကို ဆုံးဖြတ်ခြင်း (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Adosa (အဒေါသ)', meaning: 'မကြမ်းတမ်းခြင်း၊ မေတ္တာထားခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Ahetuka (အဟေတုက)', meaning: 'ဟေတု (လောဘ၊ ဒေါသ စသည့် အမြစ်) မပါဝင်သော စိတ်' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Ahirika (အဟိရိက)', meaning: 'ဒုစရိုက်ပြုရမည်ကို မရှက်ခြင်း (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }, { name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Ajjava (အဇ္ဇဝ)', meaning: 'ဖြောင့်မတ်ခြင်း' },
            { term: 'Akaṭṭhī (အကဋ္ဌီ)', meaning: 'အရိုးမရှိသော' },
            { term: 'Akusala (အကုသလ)', meaning: 'အပြစ်ရှိ၍ ဆင်းရဲသောအကျိုးကို ပေးတတ်သော သဘော (အကုသိုလ်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }, { name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Alobha (အလောဘ)', meaning: 'မလိုချင်ခြင်း၊ မတပ်မက်ခြင်း၊ စွန့်လွှတ်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Amoha (အမောဟ)', meaning: 'အမှန်အတိုင်း သိမြင်ခြင်း (ပညာ)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Anattā (အနတ္တ)', meaning: 'အစိုးမရခြင်း၊ အတ္တမဟုတ်ခြင်း' },
            { term: 'Aniccatā (အနိစ္စ)', meaning: 'မမြဲခြင်း' },
            { term: 'Anottappa (အနောတ္တပ္ပ)', meaning: 'ဒုစရိုက်ပြုရမည်ကို မကြောက်ခြင်း (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }, { name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Apariccāga (အပရိစ္စာဂ)', meaning: 'မစွန့်လွှတ်ခြင်း (မစ္ဆရိယ)' },
            { term: 'Ariya (အရိယ)', meaning: 'မြတ်သောသူ (သောတာပန်စသော ပုဂ္ဂိုလ်များ)' },
            { term: 'Arūpa (အရူပ)', meaning: 'ရုပ်မရှိသော၊ နာမ်တရား' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Asaṅkhārika (အသင်္ခါရိက)', meaning: 'တိုက်တွန်းမှု မပါဘဲ မိမိအလိုအလျောက် ထက်မြက်စွာ ဖြစ်ပေါ်သော စိတ်' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Asurakāya (အသုရကာယ)', meaning: 'အသုရာဘုံ (နတ်တို့နှင့် ဆန့်ကျင်ဘက်ဖြစ်သော သတ္တဝါများ)' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Avijjā (အဝိဇ္ဇာ)', meaning: 'သစ္စာလေးပါးကို မသိခြင်း (မောဟ)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }, { name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Ayoge yogo (အယောဂေ ယောဂေါ)', meaning: 'မယှဉ်အပ်သည်၌ ယှဉ်ခြင်း (မိစ္ဆာဒိဋ္ဌိ)' },
            { term: 'Aññasamānā (အညသမာန)', meaning: 'အခြား (ကုသိုလ်/အကုသိုလ်) နှင့် တူသော စေတသိက် (၁၃) ပါး' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Bala (ဗလ)', meaning: 'ဆန့်ကျင်ဘက်တရားတို့ကို မတုန်လှုပ်စေသော အစွမ်းခွန်အား (သဒ္ဓါ၊ ဝီရိယ၊ သတိ၊ သမာဓိ၊ ပညာ)' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Bhava (ဘဝ)', meaning: 'ဖြစ်တည်မှု (ကမ္မဘဝ၊ ဥပပတ္တိဘဝ)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Bhavaṅga (ဘဝင်)', meaning: 'ဘဝ၏ အင်္ဂါ၊ ဘဝကို ဆက်စပ်ပေးသော၊ ဝီထိစိတ် မဖြစ်ပေါ်ချိန်တွင် ဖြစ်ပေါ်နေသော စိတ်' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Bhāvanā (ဘာဝနာ)', meaning: 'ပွားများအားထုတ်ခြင်း (သမထ နှင့် ဝိပဿနာ)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Bhaṅga (ဘင်)', meaning: 'ချုပ်ပျောက်ခြင်း ခဏ' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Bhūmi (ဘူမိ / ဘုံ)', meaning: 'သတ္တဝါတို့ ဖြစ်တည်ရာ အရပ်၊ နေရာ (ဥပမာ - ကာမဘုံ၊ ရူပဘုံ၊ အရူပဘုံ)' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Bojjhaṅga (ဗောဇ္ဈင်္ဂ / ဗောဇ္ဈင်)', meaning: 'သစ္စာလေးပါးကို သိရန် အထောက်အကူပြုသော အင်္ဂါ' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Cetanā (စေတနာ)', meaning: 'တိုက်တွန်းနှိုးဆော်တတ်သော သဘော (ကံကို ဖြစ်စေသော အဓိက စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Cetasika (စေတသိက)', meaning: 'စိတ်နှင့် ယှဉ်တွဲ၍ ဖြစ်ပေါ်သော၊ စိတ်ကို ခြယ်လှယ်တတ်သော သဘောတရားများ (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Chanda (ဆန္ဒ)', meaning: 'ပြုလိုသော သဘော (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Citta (စိတ္တ)', meaning: 'အာရုံကို သိတတ်သော သဘော (စိတ်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Cuti (စုတိ)', meaning: 'ဘဝတစ်ခု၏ နောက်ဆုံး ပြတ်စဲသွားသော စိတ်' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Dassana (ဒဿန)', meaning: 'မြင်ခြင်း (သောတာပတ္တိမဂ်)' },
            { term: 'Dhātu (ဓာတု / ဓာတ်)', meaning: 'သတ္တဝါ၊ ဇီဝ မဟုတ်ဘဲ မိမိသဘောကို ဆောင်သော တရား (ဥပမာ - ပထဝီဓာတ်၊ စက္ခုဓာတ် စသည်)' , links: [{ name: 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', url: 'sabba_sangaha.html' }] },
            { term: 'Diṭṭhi (ဒိဋ္ဌိ)', meaning: 'မှားယွင်းစွာ ယူဆခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Domanassa (ဒေါမနဿ)', meaning: 'စိတ်ဆင်းရဲခြင်း (ဝေဒနာ)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Dosa (ဒေါသ)', meaning: 'ကြမ်းတမ်းခြင်း၊ အမျက်ထွက်ခြင်း၊ မကျေနပ်ခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Dukka (ဒုက္ခ)', meaning: 'ဆင်းရဲခြင်း' },
            { term: 'Dvāra (ဒွါရ)', meaning: 'စိတ်ဖြစ်ပေါ်ရန် ဝင်ပေါက်/ထွက်ပေါက် (တံခါး ၆ ပေါက်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Ekaggatā (ဧကဂ္ဂတာ)', meaning: 'အာရုံတစ်ခုတည်း၌ စိတ်တည်ငြိမ်ခြင်း (သမာဓိ)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Gati (ဂတိ)', meaning: 'လားရာ (ဥပမာ - သုဂတိ၊ ဒုဂ္ဂတိ)' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Hetu (ဟေတု / ဟိတ်)', meaning: 'အမြစ်သဖွယ်ဖြစ်သော အကြောင်းတရား (ဥပမာ - လောဘ၊ ဒေါသ၊ မောဟ၊ အလောဘ၊ အဒေါသ၊ အမောဟ)' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Hiri (ဟိရီ)', meaning: 'ဒုစရိုက်ပြုရမည်ကို ရှက်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Iddhipāda (ဣဒ္ဓိပါဒ / ဣဒ္ဓိပါဒ်)', meaning: 'ပြီးပြည့်စုံခြင်း၏ အခြေခံ (ဆန္ဒ၊ ဝီရိယ၊ စိတ္တ၊ ဝီမံသ)' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Indriya (ဣန္ဒြိယ / ဣန္ဒြေ)', meaning: 'မိမိဆိုင်ရာ ကိစ္စ၌ အစိုးရသော၊ လွှမ်းမိုးနိုင်သော သဘော (ဥပမာ - စက္ခုန္ဒြေ၊ သဒ္ဓိန္ဒြေ စသည်)' , links: [{ name: 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', url: 'sabba_sangaha.html' }] },
            { term: 'Issā (ဣဿာ)', meaning: 'သူတစ်ပါး ကြီးပွားချမ်းသာသည်ကို ငြူစူခြင်း (မနာလိုခြင်း)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Jarā (ဇရာ)', meaning: 'အိုမင်း ရင့်ရော်ခြင်း' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Javana (ဇောန / ဇော)', meaning: 'အာရုံ၏ အရသာကို လျင်မြန်စွာ ခံစားသော၊ ကံမြောက်စေသော စိတ်' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Jhāna (ဈာန / ဈာန်)', meaning: 'အာရုံကို စူးစိုက်စွာ ရှုတတ်သော၊ ဆန့်ကျင်ဘက် နီဝရဏတရားများကို လောင်ကျွမ်းစေတတ်သော သဘော' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Jīvitindriya (ဇီဝိတိန္ဒြိယ)', meaning: 'ရုပ်၊ နာမ်တို့၏ အသက် (အသက်ရှင်စေသော သဘော)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }, { name: 'ရုပ်ပိုင်း (Rūpa)', url: 'rupa_sangaha.html' }] },
            { term: 'Jāti (ဇာတိ)', meaning: 'ပဋိသန္ဓေတည်နေခြင်း၊ ပထမဆုံး ဖြစ်ပေါ်လာခြင်း' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Kalyāṇa (ကလျာဏ)', meaning: 'ကောင်းမွန်သော (ဥပမာ - ကလျာဏမိတ္တ = မိတ်ဆွေကောင်း)' },
            { term: 'Kamma (ကမ္မ / ကံ)', meaning: 'ပြုလုပ်ခြင်း၊ စီမံခြင်း (ကိုယ်၊ နှုတ်၊ စိတ်ဖြင့် ပြုလုပ်သော အကြောင်းတရား)' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Kammaṭṭhāna (ကမ္မဋ္ဌာန)', meaning: 'ဘာဝနာအလုပ်၏ တည်ရာ အာရုံ' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Karunā (ကရုဏာ)', meaning: 'ဆင်းရဲဒုက္ခရောက်နေသူများအပေါ် သနားကြင်နာခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Khandha (ခန္ဓာ)', meaning: 'အစုအဝေး (ဥပမာ - ရူပက္ခန္ဓာ၊ ဝေဒနာက္ခန္ဓာ စသည်)' , links: [{ name: 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', url: 'sabba_sangaha.html' }] },
            { term: 'Kicca (ကိစ္စ)', meaning: 'စိတ်၏ လုပ်ငန်းဆောင်တာ (၁၄ မျိုး ရှိသည်)' , links: [{ name: 'ပကိဏ္ဏကပိုင်း (Pakiṇṇaka)', url: 'pakinnaka_sangaha.html' }] },
            { term: 'Kilesā (ကိလေသာ)', meaning: 'စိတ်ကို ပူလောင် ညစ်နွမ်းစေတတ်သော သဘော' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Kiriya / Kriyā (ကြိယာ)', meaning: 'အကျိုး မပေးတော့သော၊ ပြုကာမတ္တမျှသာဖြစ်သော သဘော (ရဟန္တာများ၏ စိတ်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Kukkucca (ကုက္ကုစ္စ)', meaning: 'ပြုခဲ့မိသော အမှား၊ မပြုခဲ့မိသော အကောင်းများအတွက် နောင်တရ ပူပန်ခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Kusala (ကုသလ)', meaning: 'အပြစ်ကင်း၍ ကောင်းသောအကျိုးကို ပေးတတ်သော သဘော (ကုသိုလ်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Lobha (လောဘ)', meaning: 'လိုချင်တပ်မက်ခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Lokiya (လောကီ)', meaning: 'လောက၌ အကျုံးဝင်သော (ကာမ၊ ရူပ၊ အရူပ)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Lokuttarā (လောကုတ္တရာ)', meaning: 'လောကမှ လွတ်မြောက်သော (မဂ်၊ ဖိုလ်၊ နိဗ္ဗာန်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Macchariya (မစ္ဆရိယ)', meaning: 'မိမိစည်းစိမ်ချမ်းသာကို သူတစ်ပါးနှင့် မဆက်ဆံလိုခြင်း (ဝန်တိုခြင်း)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Magga (မဂ္ဂ / မဂ်)', meaning: 'နိဗ္ဗာန်သို့ သွားရာလမ်း၊ ကိလေသာများကို ပယ်သတ်တတ်သော သဘော' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Mahābhūta (မဟာဘူတ)', meaning: 'ကြီးမား ထင်ရှားသော ရုပ်တရား (ပထဝီ၊ အာပေါ၊ တေဇော၊ ဝါယော)' , links: [{ name: 'ရုပ်ပိုင်း (Rūpa)', url: 'rupa_sangaha.html' }] },
            { term: 'Manasikāra (မနသိကာရ)', meaning: 'အာရုံကို နှလုံးသွင်းခြင်း (စေတသိက်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Maraṇa (မရဏ)', meaning: 'သေဆုံးခြင်း၊ ပျက်စီးခြင်း' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Middha (မိဒ္ဓ)', meaning: 'စေတသိက်တို့၏ ထိုင်းမှိုင်းခြင်း၊ ငိုက်မျဉ်းခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Moha (မောဟ)', meaning: 'တွေဝေခြင်း၊ အမှန်ကို မသိခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Muditā (မုဒိတာ)', meaning: 'သူတစ်ပါး ကြီးပွားချမ်းသာသည်ကို ဝမ်းမြောက်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Māna (မာန)', meaning: 'ထောင်လွှားခြင်း၊ မိမိကိုယ်ကို အထင်ကြီးခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Nibbāna (နိဗ္ဗာန)', meaning: 'တဏှာမှ ကင်းလွတ်ရာ၊ ဒုက္ခငြိမ်းရာ (နိဗ္ဗာန်)' },
            { term: 'Nimitta (နိမိတ္တ / နိမိတ်)', meaning: 'အာရုံ၏ အမှတ်အသား (ဥပမာ - ပရိကမ္မနိမိတ်၊ ဥဂ္ဂဟနိမိတ်၊ ပဋိဘာဂနိမိတ်)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Nāma (နာမ / နာမ်)', meaning: 'အာရုံသို့ ညွတ်တတ်သော သဘော (စိတ် နှင့် စေတသိက်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Nāmarūpa (နာမရူပ / နာမ်ရုပ်)', meaning: 'စိတ်၊ စေတသိက် (နာမ်) နှင့် ဖောက်ပြန်တတ်သော သဘော (ရုပ်)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Ogha (ဩဃ)', meaning: 'သံသရာဝဲဩဃ၊ နစ်မြုပ်စေတတ်သော တရား ၄ ပါး' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Ottappa (ဩတ္တပ္ပ)', meaning: 'ဒုစရိုက်ပြုရမည်ကို ကြောက်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Paccaya (ပစ္စယ)', meaning: 'တစ်ခုက တစ်ခုကို ထောက်ပံ့ ကျေးဇူးပြုတတ်သော အခြေအနေ' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Paññatti (ပညတ္တိ / ပညတ်)', meaning: 'အမှန်တကယ် မရှိသော်လည်း ခေါ်ဝေါ်သမုတ်ထားသော အမည်နာမ သို့မဟုတ် အရာဝတ္ထု' , links: [{ name: 'ပညတ် (Paññatti)', url: 'pannatti.html' }] },
            { term: 'Paññā (ပညာ)', meaning: 'အမှန်အတိုင်း ထိုးထွင်းသိမြင်သော သဘော (အမောဟ)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Paramattha (ပရမတ္ထ / ပရမတ်)', meaning: 'ဖောက်ပြန်လွဲမှားခြင်း မရှိသော၊ အမှန်တကယ် ရှိသော တရား (စိတ်၊ စေတသိက်၊ ရုပ်၊ နိဗ္ဗာန်)' },
            { term: 'Paṭiccasamuppāda (ပဋိစ္စသမုပ္ပါဒ)', meaning: 'အကြောင်းတရားများအပေါ် အမှီသဟဲပြု၍ အကျိုးတရားများ ဆက်စပ်ဖြစ်ပေါ်လာခြင်း သဘော' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Paṭisandhi (ပဋိသန္ဓေ)', meaning: 'ဘဝဟောင်းနှင့် ဘဝသစ်ကို ဆက်စပ်ပေးသော၊ ဘဝသစ်၏ ပထမဆုံး စိတ်' , links: [{ name: 'ဝီထိမုတ်ပိုင်း (Vīthimutta)', url: 'vithimutta_sangaha.html' }] },
            { term: 'Paṭṭhāna (ပဋ္ဌာန / ပဋ္ဌာန်း)', meaning: 'အကြောင်းအကျိုး ဆက်စပ်မှုတို့ကို အထူး၊ အပြားအားဖြင့် ပြဆိုထားသော ကျမ်း (ပစ္စည်း ၂၄ ပါး)' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Phala (ဖလ / ဖိုလ်)', meaning: 'မဂ်၏ အကျိုးဆက်အဖြစ် ဖြစ်ပေါ်လာသော သဘော' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Phassa (ဖဿ)', meaning: 'အာရုံနှင့် ဒွါရ တွေ့ဆုံထိခိုက်ခြင်း (စေတသိက်)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }, { name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Pīti (ပီတိ)', meaning: 'အာရုံကို နှစ်သက်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Rūpa (ရူပ)', meaning: 'ဖောက်ပြန်တတ်သော သဘော (ရုပ်တရား)' , links: [{ name: 'ရုပ်ပိုင်း (Rūpa)', url: 'rupa_sangaha.html' }] },
            { term: 'Sabba-cittasādhāraṇa (သဗ္ဗစိတ္တသာဓာရဏ)', meaning: 'စိတ်အားလုံးနှင့် ဆက်ဆံသော စေတသိက် (၇) ပါး' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Sacca (သစ္စ / သစ္စာ)', meaning: 'ဖောက်ပြန်လွဲမှားမှု မရှိသော အမှန်တရား (ဥပမာ - ဒုက္ခသစ္စာ၊ သမုဒယသစ္စာ စသည်)' , links: [{ name: 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', url: 'sabba_sangaha.html' }] },
            { term: 'Saddhā (သဒ္ဓါ)', meaning: 'ယုံကြည်သင့်သည်ကို ယုံကြည်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Sahetuka (သဟေတုက)', meaning: 'ဟေတု ပါဝင်သော စိတ်' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Samatha (သမထ)', meaning: 'စိတ်ကို ငြိမ်းအေး တည်ငြိမ်စေသော အကျင့်' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Sammappadhāna (သမ္မပ္ပဓာန)', meaning: 'ကောင်းစွာ အားထုတ်ခြင်း (ဝီရိယ ၄ မျိုး)' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Sampayutta (သမ္ပယုတ္တ)', meaning: 'ယှဉ်တွဲခြင်း၊ အတူတကွ ဖြစ်ပေါ်ခြင်း (ဥပမာ - ဉာဏသမ္ပယုတ်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Sasaṅkhārika (သသင်္ခါရိက)', meaning: 'မိမိ/သူတစ်ပါး၏ တိုက်တွန်းမှုကြောင့် နှေးကွေးစွာ ဖြစ်ပေါ်သော စိတ်' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Sati (သတိ)', meaning: 'အာရုံကို မမေ့လျော့ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Satipaṭṭhāna (သတိပဋ္ဌာန / သတိပဋ္ဌာန်)', meaning: 'သတိကို စွဲမြဲစွာ တည်ထားခြင်း (ကာယ၊ ဝေဒနာ၊ စိတ္တ၊ ဓမ္မ)' , links: [{ name: 'ဗောဓိပက္ခိယ (Bodhipakkhiya)', url: 'bodhipakkhiya_dhamma.html' }] },
            { term: 'Saḷāyatana (သဠာယတန)', meaning: 'အာယတန ၆ ပါး (စက္ခု၊ သောတ၊ ဃာန၊ ဇိဝှာ၊ ကာယ၊ မန)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Saṅkhāra (သင်္ခါရ)', meaning: 'အကြောင်းတရားတို့က ပြုပြင်စီရင်ထားသော တရား၊ ပြုပြင်တတ်သော စေတနာ' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Sobhana (သောဘဏ)', meaning: 'တင့်တယ်ကောင်းမွန်သော (ကုသိုလ်၊ ဝိပါက်၊ ကြိယာ တချို့)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Somanassa (သောမနဿ)', meaning: 'စိတ်ချမ်းသာခြင်း (ဝေဒနာ)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Taṇhā (တဏှာ)', meaning: 'အာရုံကို တပ်မက်ခြင်း၊ လိုချင်ခြင်း (လောဘ)' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }, { name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Thīna (ထိန)', meaning: 'စိတ်၏ ထိုင်းမှိုင်းခြင်း၊ လေးလံခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Uddhacca (ဥဒ္ဓစ္စ)', meaning: 'စိတ် ပျံ့လွင့်ခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Uppāda (ဥပါဒ်)', meaning: 'စတင်ဖြစ်ပေါ်ခြင်း ခဏ' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Upādāna (ဥပါဒါန / ဥပါဒါန်)', meaning: 'အာရုံကို ပြင်းစွာ စွဲလမ်းခြင်း' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }] },
            { term: 'Upādārūpa (ဥပါဒါရူပ / ဥပါဒါရုပ်)', meaning: 'မဟာဘုတ် ၄ ပါးကို မှီ၍ ဖြစ်သော ရုပ် (၂၄ ပါး)' , links: [{ name: 'ရုပ်ပိုင်း (Rūpa)', url: 'rupa_sangaha.html' }] },
            { term: 'Upekkhā (ဥပေက္ခာ)', meaning: 'အလယ်အလတ် ခံစားမှု၊ လျစ်လျူရှုခြင်း (ဝေဒနာ)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vatthu (ဝတ္ထု)', meaning: 'စိတ် မှီရာ ရုပ်အခြေခံ (ဝတ္ထုရုပ် ၆ ပါး)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vedanā (ဝေဒနာ)', meaning: 'အာရုံ၏ အရသာကို ခံစားခြင်း' , links: [{ name: 'ပဋိစ္စသမုပ္ပါဒ် (Paṭiccasamuppāda)', url: 'paticcasamuppada.html' }, { name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vicāra (ဝိစာရ)', meaning: 'အာရုံကို ထပ်ခါထပ်ခါ သုံးသပ်ခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vicikicchā (ဝိစိကိစ္ဆာ)', meaning: 'ယုံမှား သံသယဖြစ်ခြင်း' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Vipassanā (ဝိပဿနာ)', meaning: 'ရုပ်နာမ်တို့၏ အနိစ္စ၊ ဒုက္ခ၊ အနတ္တ သဘောကို အထူး သိမြင်အောင် ရှုပွားသော အကျင့်' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Vippayutta (ဝိပ္ပယုတ္တ)', meaning: 'မယှဉ်တွဲခြင်း၊ ကင်းကွာခြင်း (ဥပမာ - ဉာဏဝိပ္ပယုတ်)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vipāka (ဝိပါက)', meaning: 'ကံ၏ အကျိုးဆက်အဖြစ် ဖြစ်ပေါ်လာသော သဘော (ဝိပါက်)' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Viriya (ဝီရိယ)', meaning: 'အားထုတ်ခြင်း၊ ကြိုးစားခြင်း' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vitakka (ဝိတက္က)', meaning: 'အာရုံသို့ စိတ်ကို တင်ပေးခြင်း (ကြံစည်ခြင်း)' , links: [{ name: 'စေတသိက်ပိုင်း (Cetasika)', url: 'citta_cetasikas_visual_guide.html' }] },
            { term: 'Vīthi (ဝီထိ)', class: 'text-sky-700 dark:text-sky-300', meaning: 'အာရုံကို သိရှိရန် အစဉ်အတိုင်း ဖြစ်ပေါ်သော စိတ်အစဉ်' , links: [{ name: 'ဝီထိပိုင်း (Vīthi)', url: 'vithi_sangaha.html' }] },
            { term: 'Ārammaṇa (အာရမ္မဏ)', meaning: 'စိတ်၏ မှီတွယ်ရာ/သိစရာ (အာရုံ ၆ ပါး)' , links: [{ name: 'ပကိဏ္ဏကပိုင်း (Pakiṇṇaka)', url: 'pakinnaka_sangaha.html' }] },
            { term: 'Āsava (အာသဝ / အာသဝေါ)', meaning: 'ယိုစီးတတ်သော၊ ယစ်မူးစေတတ်သော တရား ၄ ပါး (ကာမ၊ ဘဝ၊ ဒိဋ္ဌိ၊ အဝိဇ္ဇာ)' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Āyatana (အာယတန)', meaning: 'စိတ်နှင့် စေတသိက်တို့ ဖြစ်ပေါ်ကျယ်ပြန့်ရာ အကြောင်း (ဥပမာ - စက္ခာယတန၊ ရူပါယတန စသည်)' , links: [{ name: 'သဗ္ဗသင်္ဂဟ (Sabba Saṅgaha)', url: 'sabba_sangaha.html' }] },
            { term: 'Ṭhiti (ဌီ)', meaning: 'တည်နေခြင်း ခဏ' , links: [{ name: 'စိတ်ပိုင်း (Citta)', url: 'citta_cetasikas_visual_guide.html' }] },

            { term: 'Asubha (အသုဘ)', meaning: 'မတင့်တယ်ခြင်း၊ စက်ဆုပ်ဖွယ် (ကမ္မဋ္ဌာန်း ၄၀ တွင် ပါဝင်သည်)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Adhipati (အဓိပတိ)', meaning: 'အကြီးအမှူးဖြစ်သော အကြောင်းတရား (ဆန္ဒ၊ ဝီရိယ၊ စိတ္တ၊ ဝီမံသ)' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Anantaram (အနန္တရ)', meaning: 'ခြားနားမှုမရှိဘဲ အကျိုးပေးသော ပစ္စည်း' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Anussati (အနုဿတိ)', meaning: 'အဖန်ဖန် အောက်မေ့ခြင်း (ဗုဒ္ဓါနုဿတိ စသော ကမ္မဋ္ဌာန်းများ)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Brahmavihāra (ဗြဟ္မဝိဟာရ)', meaning: 'မြတ်သော နေထိုင်ခြင်း (မေတ္တာ၊ ကရုဏာ၊ မုဒိတာ၊ ဥပေက္ခာ)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Carita (စရိုက်)', meaning: 'လေ့လာကျက်စားလေ့ရှိသော အမူအကျင့် (ရာဂစရိုက် စသည်)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Gantha (ဂန္ထ)', meaning: 'ခန္ဓာကိုယ်နှင့် အာရုံကို နှောင်ဖွဲ့တတ်သော တရား' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Kasiṇa (ကသိုဏ်း)', meaning: 'အလုံးစုံကို ဖြန့်ကြက်၍ ရှုရသော အာရုံ (ဥပမာ - ပထဝီကသိုဏ်း)' , links: [{ name: 'ကမ္မဋ္ဌာန်းပိုင်း (Kammaṭṭhāna)', url: 'kammatthana_sangaha.html' }] },
            { term: 'Nīvaraṇa (နီဝရဏ)', meaning: 'ကုသိုလ်တရားတို့ကို တားဆီးပိတ်ပင်တတ်သော တရား' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] },
            { term: 'Paccuppanna (ပစ္စုပ္ပန်)', meaning: 'ယခုဖြစ်ဆဲ အချိန် (ပစ္စုပ္ပန်အာရုံ)' , links: [{ name: 'ပကိဏ္ဏကပိုင်း (Pakiṇṇaka)', url: 'pakinnaka_sangaha.html' }] },
            { term: 'Sahajāta (သဟဇာတ)', meaning: 'အတူတကွ ဖြစ်ပေါ်လာသော ပစ္စည်း' , links: [{ name: 'ပစ္စည်းပိုင်း (Paccaya)', url: 'paccaya_sangaha.html' }] },
            { term: 'Yoga (ယောဂ)', meaning: 'ယှဉ်စေတတ်သော၊ ဆက်စပ်ပေးတတ်သော တရား ၄ ပါး' , links: [{ name: 'ကိလေသာပိုင်း (Kilesa)', url: 'kilesa_sangaha.html' }] }

];
        
        // Add ID and Categories
        let terms = originalTerms.map(t => {
            // Generate simple ID
            const id = 'term_' + t.term.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
            t.id = id;
            
            // Auto Categorize based on links or keywords
            let cat = 'misc';
            const linksStr = JSON.stringify(t.links || []).toLowerCase();
            const textStr = (t.term + ' ' + t.meaning).toLowerCase();
            
            if (linksStr.includes('citta') || textStr.includes('စိတ်')) cat = 'citta';
            else if (linksStr.includes('cetasika') || textStr.includes('စေတသိက်')) cat = 'cetasika';
            else if (linksStr.includes('rūpa') || textStr.includes('ရုပ်')) cat = 'rupa';
            else if (linksStr.includes('paccaya') || linksStr.includes('paṭiccasamuppāda')) cat = 'paccaya';
            else if (linksStr.includes('kammaṭṭhāna')) cat = 'kammatthana';
            else if (linksStr.includes('kilesa') || textStr.includes('ကိလေသာ')) cat = 'kilesa';
            
            t.category = cat;
            return t;
        });

        // Add related terms dynamically based on category and shared keywords
        terms.forEach(t => {
            t.related = terms
                .filter(other => other.id !== t.id && (other.category === t.category || t.meaning.includes(other.term.split(' ')[0])))
                .slice(0, 3)
                .map(other => other.id);
        });

        // State
        let currentView = 'list'; // list, grid, flashcard
        let currentCategory = 'all';
        let searchQuery = '';
        let flashcardIndex = 0;
        let filteredTerms = [...terms];
        
        // Bookmarks
        let bookmarks = JSON.parse(localStorage.getItem('abhidhamma_bookmarks') || '[]');

        // DOM Elements
        const searchInput = document.getElementById('searchInput');
        const clearBtn = document.getElementById('clearSearch');
        const listEl = document.getElementById('glossaryList');
        const countEl = document.getElementById('resultCount');
        const alphabetIndexEl = document.getElementById('alphabetIndex');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const viewBtns = document.querySelectorAll('.view-btn');

        function toggleBookmark(id, event) {
            if(event) {
                event.stopPropagation();
                event.preventDefault();
            }
            if (bookmarks.includes(id)) {
                bookmarks = bookmarks.filter(b => b !== id);
            } else {
                bookmarks.push(id);
            }
            localStorage.setItem('abhidhamma_bookmarks', JSON.stringify(bookmarks));
            render(); // Re-render to update UI
        }

        function getBaseLetter(str) {
            const firstChar = str.trim().charAt(0).toUpperCase();
            const map = { 'Ā': 'A', 'Ī': 'I', 'Ū': 'U', 'Ṭ': 'T', 'Ḍ': 'D', 'Ṇ': 'N', 'Ḷ': 'L', 'Ṁ': 'M', 'Ṅ': 'N', 'Ñ': 'N' };
            return map[firstChar] || firstChar;
        }

        // Fuzzy match function
        function fuzzyMatch(str, pattern) {
            if (!pattern) return true;
            pattern = pattern.toLowerCase().replace(/\s+/g, '');
            str = str.toLowerCase().replace(/\s+/g, '');
            
            // Exact match
            if (str.includes(pattern)) return true;
            
            // Simple subset character match for slight typos (e.g. ဉာဏ် vs ညဏ်)
            // Just checks if letters appear in order
            let patternIdx = 0;
            for (let i = 0; i < str.length && patternIdx < pattern.length; i++) {
                if (str[i] === pattern[patternIdx]) {
                    patternIdx++;
                }
            }
            return patternIdx === pattern.length;
        }

        function highlight(text, query) {
            if (!query) return text;
            const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
            return text.replace(regex, '<mark>$1</mark>');
        }

        function renderCard(t, q) {
            let linksHtml = '';
            if (t.links && t.links.length > 0) {
                linksHtml = '<div class="mt-3 flex flex-wrap gap-2">' + t.links.map(l => 
                    `<a href="${l.url}" class="inline-flex items-center gap-1 text-[11px] font-medium px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-700 hover:bg-emerald-100 dark:bg-emerald-500/10 dark:text-emerald-300 dark:hover:bg-emerald-500/20 transition-colors border border-emerald-200/50 dark:border-emerald-500/20"><i class="fa-solid fa-link text-[9px] opacity-70"></i> ${l.name}</a>`
                ).join('') + '</div>';
            }
            
            let relatedHtml = '';
            if (t.related && t.related.length > 0) {
                const relTerms = t.related.map(rid => terms.find(x => x.id === rid)).filter(Boolean);
                relatedHtml = '<div class="mt-3 flex flex-wrap gap-1.5 items-center"><span class="text-[10px] text-slate-400 uppercase font-bold tracking-wider">Related:</span> ' + 
                    relTerms.map(rt => `<span class="inline-flex items-center text-[11px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 cursor-help" title="${rt.meaning}">${rt.term.split(' ')[0]}</span>`).join('') + '</div>';
            }
            
            const isBookmarked = bookmarks.includes(t.id);
            const bkmIcon = isBookmarked ? 'fa-solid text-amber-500' : 'fa-regular text-slate-300 dark:text-slate-600';
            
            return `
                <div class="glass-card p-4 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-emerald-400 dark:border-emerald-500/30 transition flex flex-col md:flex-row md:items-start gap-2 md:gap-4 relative group">
                    <button onclick="toggleBookmark('${t.id}', event)" class="bookmark-btn absolute top-4 right-4 text-lg ${bkmIcon} hover:text-amber-500 z-10" title="Bookmark">
                        <i class="fa-star"></i>
                    </button>
                    <div class="md:w-1/3 pt-1 pr-6">
                        <div class="font-bold text-emerald-700 dark:text-emerald-300 text-lg">${highlight(t.term, q)}</div>
                        <span class="inline-block mt-1 text-[10px] uppercase tracking-wider font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">${t.category}</span>
                    </div>
                    <div class="md:w-2/3 flex flex-col justify-center min-h-[2rem]">
                        <div class="text-slate-700 dark:text-slate-300 text-sm md:text-base leading-relaxed pr-6">
                            ${highlight(t.meaning, q)}
                        </div>
                        ${linksHtml}
                        ${relatedHtml}
                    </div>
                </div>
            `;
        }
        
        function renderFlashcard() {
            if (filteredTerms.length === 0) {
                listEl.innerHTML = `<div class="text-center text-slate-500 py-12">No terms found for studying in this category/search.</div>`;
                return;
            }
            if (flashcardIndex >= filteredTerms.length) flashcardIndex = 0;
            if (flashcardIndex < 0) flashcardIndex = filteredTerms.length - 1;
            
            const t = filteredTerms[flashcardIndex];
            const isBookmarked = bookmarks.includes(t.id);
            const bkmIcon = isBookmarked ? 'fa-solid text-amber-500' : 'fa-regular text-slate-300 dark:text-slate-600';
            
            listEl.innerHTML = `
                <div class="flex flex-col items-center">
                    <div class="text-sm text-slate-500 font-medium mb-2">Card ${flashcardIndex + 1} of ${filteredTerms.length}</div>
                    
                    <div class="flashcard-container" onclick="this.querySelector('.flashcard').classList.toggle('is-flipped')">
                        <div class="flashcard shadow-lg rounded-2xl">
                            <!-- Front -->
                            <div class="flashcard-face">
                                <button onclick="toggleBookmark('${t.id}', event)" class="bookmark-btn absolute top-6 right-6 text-2xl ${bkmIcon} hover:text-amber-500 z-10" title="Bookmark">
                                    <i class="fa-star"></i>
                                </button>
                                <span class="absolute top-6 left-6 text-xs uppercase tracking-widest font-bold text-emerald-600/50 dark:text-emerald-400/50 bg-emerald-50 dark:bg-emerald-900/20 px-3 py-1 rounded-full">${t.category}</span>
                                
                                <h2 class="text-3xl md:text-4xl font-bold text-emerald-800 dark:text-emerald-300 leading-tight">${t.term}</h2>
                                <p class="text-sm text-slate-400 mt-6"><i class="fa-solid fa-hand-pointer animate-pulse"></i> Click to flip</p>
                            </div>
                            
                            <!-- Back -->
                            <div class="flashcard-face flashcard-back">
                                <h3 class="text-xl md:text-2xl font-bold text-slate-800 dark:text-slate-100 mb-6 leading-relaxed px-4">${t.meaning}</h3>
                                <div class="w-12 h-1 bg-emerald-500/30 rounded-full mx-auto mb-6"></div>
                                <p class="text-sm text-slate-400"><i class="fa-solid fa-hand-pointer animate-pulse"></i> Click to flip back</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex items-center gap-4 mt-6">
                        <button onclick="flashcardIndex--; renderCore();" class="w-12 h-12 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow flex items-center justify-center hover:bg-slate-50 dark:hover:bg-slate-700 transition">
                            <i class="fa-solid fa-arrow-left"></i>
                        </button>
                        <button onclick="flashcardIndex = Math.floor(Math.random() * filteredTerms.length); renderCore();" class="w-12 h-12 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow flex items-center justify-center hover:text-emerald-500 transition" title="Random Card">
                            <i class="fa-solid fa-shuffle"></i>
                        </button>
                        <button onclick="flashcardIndex++; renderCore();" class="w-12 h-12 rounded-full bg-emerald-500 hover:bg-emerald-600 text-white shadow-md flex items-center justify-center transition">
                            <i class="fa-solid fa-arrow-right"></i>
                        </button>
                    </div>
                </div>
            `;
            if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
        }

        function filterData() {
            filteredTerms = terms.filter(t => {
                // Category Filter
                if (currentCategory === 'favorites' && !bookmarks.includes(t.id)) return false;
                if (currentCategory !== 'all' && currentCategory !== 'favorites' && t.category !== currentCategory) return false;
                
                // Search Filter
                if (searchQuery) {
                    return fuzzyMatch(t.term, searchQuery) || fuzzyMatch(t.meaning, searchQuery);
                }
                return true;
            });
        }

        function renderCore() {
            if (currentView === 'flashcard') {
                renderFlashcard();
            } else {
                if (filteredTerms.length === 0) {
                    listEl.innerHTML = `<div class="text-center text-slate-500 dark:text-slate-500 py-12 flex flex-col items-center"><i class="fa-solid fa-ghost text-4xl mb-4 opacity-50"></i><span>ရှာဖွေမှု ရလဒ် မတွေ့ရှိပါ</span></div>`;
                    if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
                } else {
                    let html = `<div class="${currentView === 'grid' ? 'layout-grid' : 'space-y-4'} w-full">`;
                    
                    if (searchQuery === '' && currentCategory === 'all' && currentView === 'list') {
                        // Group by letter for default view
                        const groups = {};
                        filteredTerms.forEach(t => {
                            const letter = getBaseLetter(t.term);
                            if (!groups[letter]) groups[letter] = [];
                            groups[letter].push(t);
                        });
                        
                        // Render Index
                        const sortedLetters = Object.keys(groups).sort();
                        if(alphabetIndexEl) {
                            alphabetIndexEl.innerHTML = sortedLetters.map(letter => 
                                `<a href="#letter-${letter}" class="w-9 h-9 flex items-center justify-center rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-emerald-50 hover:border-emerald-300 hover:text-emerald-700 dark:hover:bg-emerald-900/30 dark:hover:border-emerald-700 dark:hover:text-emerald-400 text-sm font-bold transition shadow-sm">${letter}</a>`
                            ).join('');
                        }

                        // Render List
                        sortedLetters.forEach(letter => {
                            html += `<h3 id="letter-${letter}" class="text-2xl font-bold text-slate-800 dark:text-slate-200 mt-10 mb-4 border-b-2 border-emerald-500/20 dark:border-emerald-500/10 pb-2 scroll-mt-24 pl-2">${letter}</h3>`;
                            html += '<div class="space-y-4">';
                            html += groups[letter].map(t => renderCard(t, searchQuery)).join('');
                            html += '</div>';
                        });
                    } else {
                        if(alphabetIndexEl) alphabetIndexEl.innerHTML = '';
                        html += filteredTerms.map(t => renderCard(t, searchQuery)).join('');
                    }
                    html += `</div>`;
                    listEl.innerHTML = html;
                }
            }
            
            countEl.textContent = `စုစုပေါင်း ဝေါဟာရ (${filteredTerms.length}) ခု ပြသထားပါသည်`;
            clearBtn.classList.toggle('hidden', searchQuery === '');
        }

        function render(query = searchQuery) {
            searchQuery = query.toLowerCase().trim();
            filterData();
            renderCore();
        }

        // Event Listeners
        searchInput.addEventListener('input', (e) => render(e.target.value));
        
        clearBtn.addEventListener('click', () => {
            searchInput.value = '';
            render('');
            searchInput.focus();
        });

        filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                filterBtns.forEach(b => b.classList.remove('active', 'bg-emerald-500', 'text-white'));
                e.currentTarget.classList.add('active');
                currentCategory = e.currentTarget.dataset.cat;
                flashcardIndex = 0; // reset
                render();
            });
        });

        viewBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                viewBtns.forEach(b => b.classList.remove('active'));
                const targetBtn = e.currentTarget.closest('.view-btn');
                targetBtn.classList.add('active');
                currentView = targetBtn.dataset.view;
                renderCore();
            });
        });

        // Initialize Bookmarks state in filter UI
        const favBtn = document.querySelector('[data-cat="favorites"]');
        if (favBtn) {
            setInterval(() => {
                const favCount = bookmarks.length;
                if (favCount > 0 && currentCategory !== 'favorites') {
                    favBtn.innerHTML = `<i class="fa-solid fa-star"></i> Favorites (${favCount})`;
                } else {
                    favBtn.innerHTML = `<i class="fa-solid fa-star"></i> Favorites`;
                }
            }, 1000);
        }

        // Init
        render();
    