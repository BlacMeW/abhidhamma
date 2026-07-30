const bhumiData = [
            // Kamabhumi (11) — rose
            { id: 1, key: 'niraya', pali: 'Niraya', name: 'ငရဲဘုံ', group: 'kamabhumi', icon: 'fa-fire', desc: 'အပါယ်ဘုံ (၄) ပါးအနက် ဆင်းရဲဒုက္ခ အပြင်းထန်ဆုံး ဘုံ — အကုသိုလ်ကံ၏ အကျိုးဆက်ဖြင့် ပဋိသန္ဓေယူရသည်။', example: 'သတ္တဝါတို့ အလွန်ပြင်းထန်သော ဝေဒနာများကို ဆက်တိုက် ခံစားနေရသော ဘုံ။' },
            { id: 2, key: 'tiracchana', pali: 'Tiracchāna-yoni', name: 'တိရစ္ဆာန်ဘုံ', group: 'kamabhumi', icon: 'fa-paw', desc: 'တိရစ္ဆာန် သတ္တဝါများ၏ ဘုံ — အကုသိုလ်ကံ၏ အကျိုးဆက်။', example: 'တိရစ္ဆာန်အားလုံးသည် ဤဘုံတွင် ပဋိသန္ဓေယူကြသည်။' },
            { id: 3, key: 'petti', pali: 'Petti-visaya', name: 'ပြိတ္တာဘုံ', group: 'kamabhumi', icon: 'fa-ghost', desc: 'အစာရေစာ ငတ်မွတ်ခေါင်းပါးသော ပြိတ္တာဘုံ — အကုသိုလ်ကံ၏ အကျိုးဆက်။', example: 'အခါခပ်သိမ်း ငတ်ပြတ်နေသော ပြိတ္တာသတ္တဝါများ၏ ဘုံ။' },
            { id: 4, key: 'asurakaya', pali: 'Asurakāya', name: 'အသုရကာယ်ဘုံ', group: 'kamabhumi', icon: 'fa-user-ninja', desc: 'အသုရကာယ် သတ္တဝါများ၏ ဘုံ — အကုသိုလ်ကံ၏ အကျိုးဆက်။', example: 'အပါယ်ဘုံ (၄) ပါးအနက် နောက်ဆုံး ဘုံ။' },
            { id: 5, key: 'manussa', pali: 'Manussa', name: 'လူ့ဘုံ', group: 'kamabhumi', icon: 'fa-person', desc: 'ကုသိုလ်/အကုသိုလ် နှစ်မျိုးစလုံး ရောနှော ခံစားရသော ဘုံ — ဓမ္မအားထုတ်ရန် အသင့်လျော်ဆုံး ဘုံ ဟု ဆိုကြသည်။', example: 'သုခ/ဒုက္ခ နှစ်မျိုးလုံး ရောယှက် ခံစားရသဖြင့် သံဝေဂ ရလွယ်သော ဘုံ။' },
            { id: 6, key: 'catummaharajika', pali: 'Cātumahārājika', name: 'စတုမဟာရာဇ်ဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'ကာမာဝစရ နတ်ဘုံ (၆) ပါးအနက် ပထမဆုံး — မင်းကြီး (၄) ပါး အုပ်ချုပ်သော ဘုံ။', example: 'လူ့ဘုံနှင့် အနီးဆုံး နတ်ဘုံ။' },
            { id: 7, key: 'tavatimsa', pali: 'Tāvatiṃsa', name: 'တာဝတိံသာဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'သိကြားမင်း အုပ်ချုပ်သော ကာမာဝစရ နတ်ဘုံ။', example: 'နတ်မင်းသိကြား နေထိုင်ရာ ဘုံ။' },
            { id: 8, key: 'yama', pali: 'Yāma', name: 'ယာမာဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'ကာမာဝစရ နတ်ဘုံ (၆) ပါးအနက် (၃) ခုမြောက်။', example: 'ယာမာနတ်မင်း အုပ်ချုပ်သော ဘုံ။' },
            { id: 9, key: 'tusita', pali: 'Tusita', name: 'တုသိတာဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'ဘုရားလောင်းများ မှတ်တမ်းတင် ချီးမြှင့်ခံရလေ့ရှိသော ကာမာဝစရ နတ်ဘုံ။', example: 'ဘုရားဖြစ်ခါနီး ဗောဓိသတ္တာများ နေထိုင်လေ့ရှိသော ဘုံ။' },
            { id: 10, key: 'nimmanarati', pali: 'Nimmānarati', name: 'နိမ္မာနရတိဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'မိမိဖန်ဆင်းသော ကာမဂုဏ်ဖြင့် ပျော်မွေ့သော ကာမာဝစရ နတ်ဘုံ။', example: 'လိုချင်သည့်အရာကို မိမိဖန်ဆင်း၍ ခံစားနိုင်သော ဘုံ။' },
            { id: 11, key: 'paranimmitavasavatti', pali: 'Paranimmitavasavatti', name: 'ပရနိမ္မိတဝသဝတ္တီဘုံ', group: 'kamabhumi', icon: 'fa-crown', desc: 'အခြားသူ ဖန်ဆင်းပေးသော ကာမဂုဏ်ဖြင့် ပျော်မွေ့သော ကာမာဝစရ နတ်ဘုံ (၆) ပါးအနက် အမြင့်ဆုံး ဘုံ။', example: 'မာရ်နတ်မင်း နေထိုင်ရာ ဘုံ။' },

            // Rupabhumi (16) — sky
            { id: 12, key: 'brahmaparisajja', pali: 'Brahmapārisajjā', name: 'ဗြဟ္မပါရိသဇ္ဇာဘုံ', group: 'rupabhumi', icon: 'fa-mountain', desc: 'ပဌမဈာန်ဘုံ (၃) ပါးအနက် အနိမ့်ဆုံး — ပဌမဈာန် ပရိတ္တအဆင့်ဖြင့် ရရှိသော ဘုံ။', example: 'ပရိတ္တ ပဌမဈာန် ရရှိသူ ပဋိသန္ဓေယူရာ ဘုံ။' },
            { id: 13, key: 'brahmapurohita', pali: 'Brahmapurohitā', name: 'ဗြဟ္မပုရောဟိတာဘုံ', group: 'rupabhumi', icon: 'fa-mountain', desc: 'ပဌမဈာန် မဇ္ဈိမအဆင့်ဖြင့် ရရှိသော ဘုံ။', example: 'ပဌမဈာန်ဘုံ (၃) ပါးအနက် အလယ်အလတ်။' },
            { id: 14, key: 'mahabrahma', pali: 'Mahābrahmā', name: 'မဟာဗြဟ္မာဘုံ', group: 'rupabhumi', icon: 'fa-mountain', desc: 'ပဌမဈာန် ပဏီတ (အထွဋ်အမြတ်) အဆင့်ဖြင့် ရရှိသော ဘုံ။', example: 'ပဌမဈာန်ဘုံ (၃) ပါးအနက် အမြင့်ဆုံး။' },
            { id: 15, key: 'parittabha', pali: 'Parittābhā', name: 'ပရိတ္တာဘာဘုံ', group: 'rupabhumi', icon: 'fa-mountain-sun', desc: 'ဒုတိယဈာန်ဘုံ (၃) ပါးအနက် အနိမ့်ဆုံး — ရောင်ခြည် အနည်းငယ်သာ ထွန်းလင်းသော ဘုံ။', example: 'ဒုတိယဈာန် ပရိတ္တအဆင့်ဖြင့် ရရှိသော ဘုံ။' },
            { id: 16, key: 'appamanabha', pali: 'Appamāṇābhā', name: 'အပ္ပမာဏာဘာဘုံ', group: 'rupabhumi', icon: 'fa-mountain-sun', desc: 'ဒုတိယဈာန် မဇ္ဈိမအဆင့်ဖြင့် ရရှိသော ဘုံ — ရောင်ခြည် မရေတွက်နိုင်အောင် ထွန်းလင်းသည်။', example: 'ဒုတိယဈာန်ဘုံ (၃) ပါးအနက် အလယ်အလတ်။' },
            { id: 17, key: 'abhassara', pali: 'Ābhassarā', name: 'အာဘဿရာဘုံ', group: 'rupabhumi', icon: 'fa-mountain-sun', desc: 'ဒုတိယဈာန် ပဏီတအဆင့်ဖြင့် ရရှိသော ဘုံ — ရောင်ခြည် တောက်ပစွာ ထွန်းလင်းသည်။', example: 'ကမ္ဘာပျက်ချိန်တွင် သတ္တဝါအများစု ဤဘုံတွင် ခိုလှုံလေ့ရှိသည်ဟု ဆိုသည်။' },
            { id: 18, key: 'parittasubha', pali: 'Parittasubhā', name: 'ပရိတ္တသုဘာဘုံ', group: 'rupabhumi', icon: 'fa-gem', desc: 'တတိယဈာန်ဘုံ (၃) ပါးအနက် အနိမ့်ဆုံး — အလှတန်ဆာ အနည်းငယ်သာ ရှိသော ဘုံ။', example: 'တတိယဈာန် ပရိတ္တအဆင့်ဖြင့် ရရှိသော ဘုံ။' },
            { id: 19, key: 'appamanasubha', pali: 'Appamāṇasubhā', name: 'အပ္ပမာဏသုဘာဘုံ', group: 'rupabhumi', icon: 'fa-gem', desc: 'တတိယဈာန် မဇ္ဈိမအဆင့်ဖြင့် ရရှိသော ဘုံ။', example: 'တတိယဈာန်ဘုံ (၃) ပါးအနက် အလယ်အလတ်။' },
            { id: 20, key: 'subhakinha', pali: 'Subhakiṇhā', name: 'သုဘကိဏှာဘုံ', group: 'rupabhumi', icon: 'fa-gem', desc: 'တတိယဈာန် ပဏီတအဆင့်ဖြင့် ရရှိသော ဘုံ — အလှတန်ဆာ ပြည့်စုံစွာ ရှိသော ဘုံ။', example: 'တတိယဈာန်ဘုံ (၃) ပါးအနက် အမြင့်ဆုံး။' },
            { id: 21, key: 'vehapphala', pali: 'Vehapphalā', name: 'ဝေဟပ္ဖလာဘုံ', group: 'rupabhumi', icon: 'fa-cloud', desc: 'စတုတ္ထဈာန်ဖြင့် ရရှိသော ဘုံ — ဖလကြီးသော ဘုံ ဟု အနက်ရှိသည်။', example: 'ရူပါဝစရဘုံများအနက် တည်ငြိမ်ဆုံးဘုံ ဟု ဆိုကြသည်။' },
            { id: 22, key: 'asannasatta', pali: 'Asaññasatta', name: 'အသညသတ်ဘုံ', group: 'rupabhumi', icon: 'fa-cloud', desc: 'စိတ် (နာမ်ခန္ဓာ) လုံးဝ မရှိဘဲ ရုပ်ခန္ဓာတစ်ခုတည်းဖြင့်သာ တည်ရှိနေသော ထူးခြားသော ဘုံ။', example: 'ဤဘုံတွင် ရုပ်တစ်ခုတည်း (ဇီဝိတနဝကကလာပ်) သာ ဆက်တိုက် တည်ရှိနေသည်။' },
            { id: 23, key: 'aviha', pali: 'Avihā', name: 'အဝိဟာဘုံ', group: 'rupabhumi', icon: 'fa-star', desc: 'သုဒ္ဓါဝါသဘုံ (၅) ပါးအနက် ပထမ — အနာဂါမီပုဂ္ဂိုလ်များသာ ပဋိသန္ဓေယူနိုင်သော ဘုံ။', example: 'ရဟန္တာ မဖြစ်မီ ဤဘုံတွင် နောက်ဆုံးအကြိမ် ပဋိသန္ဓေယူတတ်သည်။' },
            { id: 24, key: 'atappa', pali: 'Atappā', name: 'အတပ္ပာဘုံ', group: 'rupabhumi', icon: 'fa-star', desc: 'သုဒ္ဓါဝါသဘုံ (၅) ပါးအနက် ဒုတိယ — အနာဂါမီပုဂ္ဂိုလ်များသာ ပဋိသန္ဓေယူနိုင်သော ဘုံ။', example: 'သုဒ္ဓါဝါသဘုံငါးခုစလုံးကို အနာဂါမီပုဂ္ဂိုလ်များသာ ပဋိသန္ဓေယူနိုင်သည်။' },
            { id: 25, key: 'sudassa', pali: 'Sudassā', name: 'သုဒဿာဘုံ', group: 'rupabhumi', icon: 'fa-star', desc: 'သုဒ္ဓါဝါသဘုံ (၅) ပါးအနက် တတိယ။', example: 'အနာဂါမီပုဂ္ဂိုလ်များသာ ပဋိသန္ဓေယူနိုင်သော ဘုံ။' },
            { id: 26, key: 'sudassi', pali: 'Sudassī', name: 'သုဒဿီဘုံ', group: 'rupabhumi', icon: 'fa-star', desc: 'သုဒ္ဓါဝါသဘုံ (၅) ပါးအနက် စတုတ္ထ။', example: 'အနာဂါမီပုဂ္ဂိုလ်များသာ ပဋိသန္ဓေယူနိုင်သော ဘုံ။' },
            { id: 27, key: 'akanittha', pali: 'Akaniṭṭhā', name: 'အကနိဋ္ဌာဘုံ', group: 'rupabhumi', icon: 'fa-star', desc: 'သုဒ္ဓါဝါသဘုံ (၅) ပါးအနက် အမြင့်ဆုံး — ရူပါဝစရဘုံများအနက် အမြင့်ဆုံးဘုံလည်း ဖြစ်သည်။', example: 'ဤဘုံမှ အနာဂါမီပုဂ္ဂိုလ်များ ရဟန္တာ ဖြစ်၍ ပရိနိဗ္ဗာန်စံလေ့ရှိသည်။' },

            // Arupabhumi (4) — amber
            { id: 28, key: 'akasanancayatana', pali: 'Ākāsānañcāyatana', name: 'အာကာသာနဉ္စာယတနဘုံ', group: 'arupabhumi', icon: 'fa-expand', desc: 'ပဌမ အရူပဈာန် (အာကာသ-မိုးကောင်းကင် အနန္တသဘောကို အာရုံပြု) ဖြင့် ရရှိသော ဘုံ။', example: 'ရူပစဉ်ဆင်းရဲမှုကို ရှောင်ရှားလို၍ မိုးကောင်းကင်ကို အကန့်အသတ်မရှိ ဟု ရှုမှတ်ခြင်းမှ ဖြစ်သည်။' },
            { id: 29, key: 'vinnanancayatana', pali: 'Viññāṇañcāyatana', name: 'ဝိညာဏဉ္စာယတနဘုံ', group: 'arupabhumi', icon: 'fa-brain', desc: 'ဒုတိယ အရူပဈာန် (ပဌမ အရူပဈာန်ဝိညာဉ်ကို အာရုံပြု) ဖြင့် ရရှိသော ဘုံ။', example: 'ရှေးဈာန်ဝိညာဉ်ကို "အနန္တ" ဟု ရှုမှတ်ခြင်းမှ ဖြစ်သည်။' },
            { id: 30, key: 'akincannayatana', pali: 'Ākiñcaññāyatana', name: 'အာကိဉ္စညာယတနဘုံ', group: 'arupabhumi', icon: 'fa-circle-notch', desc: 'တတိယ အရူပဈာန် (ပဌမ အရူပဈာန်ဝိညာဉ် ကွယ်ပျောက်သွားပြီ ဟူသော "မရှိခြင်း" ကို အာရုံပြု) ဖြင့် ရရှိသော ဘုံ။', example: '"တစ်စုံတစ်ခုမျှ မရှိတော့" ဟူသော သဘောကို အာရုံပြု ရှုမှတ်ခြင်းမှ ဖြစ်သည်။' },
            { id: 31, key: 'nevasannanasannayatana', pali: 'Nevasaññānāsaññāyatana', name: 'နေဝသညာနာသညာယတနဘုံ', group: 'arupabhumi', icon: 'fa-yin-yang', desc: 'စတုတ္ထ အရူပဈာန် (တတိယ အရူပဈာန်ကို အလွန်သိမ်မွေ့စွာ အာရုံပြု) ဖြင့် ရရှိသော ဘုံ — ရူပါဝစရ/အရူပါဝစရဘုံများအနက် အမြင့်ဆုံး၊ သညာ ရှိသည်လည်း မဆို၊ မရှိသည်လည်း မဆိုနိုင်လောက်အောင် သိမ်မွေ့သော ဘုံ။', example: 'သံသရာတွင် ရရှိနိုင်သမျှ အမြင့်ဆုံး ဘဝ ဖြစ်သော်လည်း၊ နိစ္စမမြဲသေးသဖြင့် သံသရာမှ လွတ်မြောက်ခြင်း မဟုတ်သေးပေ။' }
        ];

const patisandhiData = [
            {
                name: '၁။ အပါယပဋိသန္ဓေ', count: '၁ ပါး', color: 'rose', icon: 'fa-fire-flame-curved',
                desc: 'အပါယ် ၄ ဘုံ၌ ပဋိသန္ဓေနေသော စိတ်။',
                detail: 'အကုသလဝိပါက် ဥပေက္ခာသန္တီရဏစိတ် ၁ ပါး ဖြစ်သည်။ ငရဲ၊ တိရစ္ဆာန်၊ ပြိတ္တာ၊ အသုရကာယ် ဘုံတို့၌ ပဋိသန္ဓေကျသည်။'
            },
            {
                name: '၂။ ကာမသုဂတိပဋိသန္ဓေ', count: '၉ ပါး', color: 'emerald', icon: 'fa-hands-holding-child',
                desc: 'လူ့ဘုံ နှင့် ကာမနတ် ၆ ဘုံ၌ ပဋိသန္ဓေနေသော စိတ်များ။',
                detail: 'အဟေတုက ကုသလဝိပါက် ဥပေက္ခာသန္တီရဏ ၁ ပါး (လူအကန္ဓ/မွေးရာပါဆမအကုသိုလ်အကျိုး) + မဟာဝိပါက်စိတ် ၈ ပါး = စုစုပေါင်း ၉ ပါး ဖြစ်သည်။'
            },
            {
                name: '၃။ ရူပါဝစရပဋိသန္ဓေ', count: '၆ မျိုး (နာမ်၅ + ရုပ်၁)', color: 'sky', icon: 'fa-mountain',
                desc: 'ရူပ ၁၆ ဘုံ၌ ပဋိသန္ဓေနေသော နာမ်/ရုပ် တရားများ။',
                detail: 'ရူပါဝစရ ဝိပါက်စိတ် ၅ ပါး (ပထမဈာန် မှ ပဉ္စမဈာန်) + အသညသတ်ဘုံ၌ ရုပ်ပဋိသန္ဓေ ၁ မျိုး (ဇီဝိတနဝကကလာပ်ရုပ်) = စုစုပေါင်း ၆ မျိုး ဖြစ်သည်။'
            },
            {
                name: '၄။ အရူပါဝစရပဋိသန္ဓေ', count: '၄ ပါး', color: 'amber', icon: 'fa-expand',
                desc: 'အရူပ ၄ ဘုံ၌ ပဋိသန္ဓေနေသော စိတ်များ။',
                detail: 'အရူပါဝစရ ဝိပါက်စိတ် ၄ ပါး (အာကာသာနဉ္စာယတန မှ နေဝသညာနာသညာယတန အထိ) ဖြစ်သည်။'
            }
        ];

const yoniData = [
            { key: 'andaja', pali: 'Aṇḍaja', name: 'အဏ္ဍဇယောနိ', desc: 'ဥအဖြစ် ဦးစွာ ဖွားမြင်ပြီးမှ အသက်ဝင်လာသော နည်းလမ်း — ငှက်၊ ကြက်။' },
            { key: 'jalabuja', pali: 'Jalābuja', name: 'ဇလာဗုဇယောနိ', desc: 'အမိဝမ်းတွင်းမှ တိုက်ရိုက် အသက်ရှင်လျက် မွေးဖွားလာသော နည်းလမ်း — လူ၊ နွား။' },
            { key: 'samsedaja', pali: 'Saṃsedaja', name: 'သံသေဒဇယောနိ', desc: 'စွတ်စိုမှု (ချွေးရည်/ပုပ်ရည်) မှ ပေါက်ဖွားလာသော နည်းလမ်း — ပိုးအချို့။' },
            { key: 'opapatika', pali: 'Opapātika', name: 'ဩပပါတိကယောနိ', desc: 'အရွယ်ရောက်ပြီးသား ခန္ဓာကိုယ်ဖြင့် ချက်ချင်း ပေါ်ထွန်းလာသော နည်းလမ်း — နတ်၊ ဗြဟ္မာ၊ ငရဲသား။' }
        ];

const nearDeathData = [
            { key: 'kamma', name: 'ကံ', icon: 'fa-scale-balanced', cls: 'border-rose-400 dark:border-rose-500/30 text-rose-700 dark:text-rose-300', desc: 'ယခင်က ပြုခဲ့ဖူးသော ကုသိုလ်/အကုသိုလ် ကံလုပ်ဆောင်ချက်ကို ပြန်လည် သတိရ ခံစားမိခြင်း' },
            { key: 'kammanimitta', name: 'ကမ္မနိမိတ်', icon: 'fa-image', cls: 'border-amber-400 dark:border-amber-500/30 text-amber-700 dark:text-amber-300', desc: 'ထိုကံနှင့် ဆက်စပ်သော အရာဝတ္ထု/ပုံရိပ် ပေါ်လာခြင်း (ဥပမာ — ဒါနပေးရာ၌ အသုံးပြုခဲ့သော ပစ္စည်း)' },
            { key: 'gatinimitta', name: 'ဂတိနိမိတ်', icon: 'fa-road', cls: 'border-sky-400 dark:border-sky-500/30 text-sky-700 dark:text-sky-300', desc: 'နောင်ဘဝ ရောက်ရှိမည့် ဘုံ၏ ရှေ့အနာဂတ် ပုံရိပ် ကြိုတင် ပေါ်လာခြင်း (ဥပမာ — ငရဲမီးလျှံ၊ နတ်ပြာသာဒ်)' }
        ];

const maranaData = [
            { key: 'ayukkhaya', pali: 'Āyukkhaya', name: 'အာယုက္ခယ', desc: 'သက်တမ်း အပြည့်အဝ ကုန်ဆုံးခြင်း — ထိုဘုံ၏ ပုံမှန် အသက်တမ်း ကုန်ဆုံးသောကြောင့် သေဆုံးခြင်း' },
            { key: 'kammakkhaya', pali: 'Kammakkhaya', name: 'ကမ္မက္ခယ', desc: 'ပဋိသန္ဓေဖြစ်စေသော ဇနကကံ၏ အားထုတ်နိုင်စွမ်း ကုန်ဆုံးခြင်း — သက်တမ်း မကုန်ခင် ကံ အားနည်းသွားသောကြောင့်' },
            { key: 'ubhayakkhaya', pali: 'Ubhayakkhaya', name: 'ဥဘယက္ခယ', desc: 'သက်တမ်းလည်း ကုန်ဆုံး၊ ကံလည်း ကုန်ဆုံး — နှစ်ခုစလုံး တစ်ပြိုင်နက် ဖြစ်ပျက်ခြင်း' },
            { key: 'upacchedaka', pali: 'Upacchedaka', name: 'ဥပစ္ဆေဒက', desc: 'ပြင်းထန်သော အခြားကံတစ်ခု (ဥပဃာတကကံ) က ရုတ်တရက် ဖြတ်တောက်ခြင်း — မတော်တဆမှုကဲ့သို့' }
        ];

