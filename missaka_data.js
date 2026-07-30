const msData = [
            // Hetu (6)
            { id: 1, key: 'h-lobha', name: 'လောဘ', group: 'hetu', icon: 'fa-magnet', desc: 'အာရုံကို တွယ်တာတပ်မက်သော အကုသိုလ်ဟေတု။' },
            { id: 2, key: 'h-dosa', name: 'ဒေါသ', group: 'hetu', icon: 'fa-fire', desc: 'အာရုံကို ကြမ်းတမ်းစွာ ဖျက်ဆီးလိုသော အကုသိုလ်ဟေတု။' },
            { id: 3, key: 'h-moha', name: 'မောဟ', group: 'hetu', icon: 'fa-cloud', desc: 'အာရုံ၏ သဘောမှန်ကို ဖုံးကွယ်ထားသော အကုသိုလ်ဟေတု။' },
            { id: 4, key: 'h-alobha', name: 'အလောဘ', group: 'hetu', icon: 'fa-hand-holding-heart', desc: 'အာရုံ၌ မတွယ်တာဘဲ စွန့်လွှတ်သော သောဘဏဟေတု။' },
            { id: 5, key: 'h-adosa', name: 'အဒေါသ', group: 'hetu', icon: 'fa-dove', desc: 'အာရုံ၌ မကြမ်းတမ်းဘဲ မေတ္တာထားသော သောဘဏဟေတု။' },
            { id: 6, key: 'h-amoha', name: 'အမောဟ (ပညာ)', group: 'hetu', icon: 'fa-lightbulb', desc: 'အာရုံ၏ သဘောမှန်ကို ခွဲခြားသိမြင်သော သောဘဏဟေတု။' },

            // Jhananga (7)
            { id: 7, key: 'j-vitakka', name: 'ဝိတက်', group: 'jhananga', icon: 'fa-arrow-pointer', desc: 'အာရုံပေါ်သို့ စိတ်ကို တင်ပေးခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 8, key: 'j-vicara', name: 'ဝိစာရ', group: 'jhananga', icon: 'fa-magnifying-glass', desc: 'အာရုံကို ထပ်ခါထပ်ခါ သုံးသပ်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 9, key: 'j-piti', name: 'ပီတိ', group: 'jhananga', icon: 'fa-face-smile', desc: 'အာရုံကို နှစ်သက်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 10, key: 'j-ekaggata', name: 'ဧကဂ္ဂတာ', group: 'jhananga', icon: 'fa-bullseye', desc: 'အာရုံတစ်ခုတည်း၌ စူးစိုက်တည်ငြိမ်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 11, key: 'j-somanassa', name: 'သောမနဿ', group: 'jhananga', icon: 'fa-face-laugh', desc: 'စိတ်ချမ်းသာခြင်း ဝေဒနာ (ကု/အကု ရောပြွမ်း)။' },
            { id: 12, key: 'j-domanassa', name: 'ဒေါမနဿ', group: 'jhananga', icon: 'fa-face-frown', desc: 'စိတ်ဆင်းရဲခြင်း ဝေဒနာ (အကုသိုလ်သက်သက်)။' },
            { id: 13, key: 'j-upekkha', name: 'ဥပေက္ခာ', group: 'jhananga', icon: 'fa-scale-balanced', desc: 'အလယ်အလတ် ခံစားမှု ဝေဒနာ (ကု/အကု ရောပြွမ်း)။' },

            // Magganga (12)
            { id: 14, key: 'm-sammaditthi', name: 'သမ္မာဒိဋ္ဌိ (ပညာ)', group: 'magganga', icon: 'fa-eye', desc: 'မှန်ကန်သော အမြင် (ကုသိုလ်)။' },
            { id: 15, key: 'm-sammavitakka', name: 'သမ္မာသင်္ကပ္ပ (ဝိတက်)', group: 'magganga', icon: 'fa-brain', desc: 'မှန်ကန်သော ကြံစည်မှု (ကုသိုလ်)။' },
            { id: 16, key: 'm-sammavaca', name: 'သမ္မာဝါစာ', group: 'magganga', icon: 'fa-comment', desc: 'မှန်ကန်သော စကား (ကုသိုလ်)။' },
            { id: 17, key: 'm-sammakammanta', name: 'သမ္မာကမ္မန္တ', group: 'magganga', icon: 'fa-hand', desc: 'မှန်ကန်သော အလုပ် (ကုသိုလ်)။' },
            { id: 18, key: 'm-sammaajiva', name: 'သမ္မာအာဇီဝ', group: 'magganga', icon: 'fa-shop', desc: 'မှန်ကန်သော အသက်မွေးဝမ်းကျောင်း (ကုသိုလ်)။' },
            { id: 19, key: 'm-sammavayama', name: 'သမ္မာဝါယာမ (ဝီရိယ)', group: 'magganga', icon: 'fa-person-running', desc: 'မှန်ကန်သော အားထုတ်မှု (ကုသိုလ်)။' },
            { id: 20, key: 'm-sammasati', name: 'သမ္မာသတိ', group: 'magganga', icon: 'fa-bell', desc: 'မှန်ကန်သော အောက်မေ့မှု (ကုသိုလ်)။' },
            { id: 21, key: 'm-sammasamadhi', name: 'သမ္မာသမာဓိ (ဧကဂ္ဂတာ)', group: 'magganga', icon: 'fa-bullseye', desc: 'မှန်ကန်သော တည်ကြည်မှု (ကုသိုလ်)။' },
            { id: 22, key: 'm-micchaditthi', name: 'မိစ္ဆာဒိဋ္ဌိ', group: 'magganga', icon: 'fa-eye-slash', desc: 'မှားယွင်းသော အမြင် (အကုသိုလ်)။' },
            { id: 23, key: 'm-micchasankappa', name: 'မိစ္ဆာသင်္ကပ္ပ (ဝိတက်)', group: 'magganga', icon: 'fa-brain', desc: 'မှားယွင်းသော ကြံစည်မှု (အကုသိုလ်)။' },
            { id: 24, key: 'm-micchavayama', name: 'မိစ္ဆာဝါယာမ (ဝီရိယ)', group: 'magganga', icon: 'fa-person-running', desc: 'မှားယွင်းသော အားထုတ်မှု (အကုသိုလ်)။' },
            { id: 25, key: 'm-micchasamadhi', name: 'မိစ္ဆာသမာဓိ (ဧကဂ္ဂတာ)', group: 'magganga', icon: 'fa-bullseye', desc: 'မှားယွင်းသော တည်ကြည်မှု (အကုသိုလ်)။' },

            // Indriya (22)
            { id: 26, key: 'i-cakkhu', name: 'စက္ခုန္ဒြေ', group: 'indriya', icon: 'fa-eye', desc: 'မြင်ခြင်း၌ အစိုးရသော မျက်စိအကြည်ရုပ်။' },
            { id: 27, key: 'i-sota', name: 'သောတိန္ဒြေ', group: 'indriya', icon: 'fa-ear-listen', desc: 'ကြားခြင်း၌ အစိုးရသော နားအကြည်ရုပ်။' },
            { id: 28, key: 'i-ghana', name: 'ဃာနိန္ဒြေ', group: 'indriya', icon: 'fa-nose', desc: 'နံခြင်း၌ အစိုးရသော နှာခေါင်းအကြည်ရုပ်။' },
            { id: 29, key: 'i-jivha', name: 'ဇိဝှိန္ဒြေ', group: 'indriya', icon: 'fa-tongue', desc: 'အရသာသိခြင်း၌ အစိုးရသော လျှာအကြည်ရုပ်။' },
            { id: 30, key: 'i-kaya', name: 'ကာယိန္ဒြေ', group: 'indriya', icon: 'fa-hand', desc: 'ထိတွေ့ခြင်း၌ အစိုးရသော ကိုယ်အကြည်ရုပ်။' },
            { id: 31, key: 'i-itthi', name: 'ဣတ္ထိန္ဒြေ', group: 'indriya', icon: 'fa-venus', desc: 'မိန်းမဟန် အသွင်အပြင်၌ အစိုးရသော ဘာဝရုပ်။' },
            { id: 32, key: 'i-purisa', name: 'ပုရိသိန္ဒြေ', group: 'indriya', icon: 'fa-mars', desc: 'ယောက်ျားဟန် အသွင်အပြင်၌ အစိုးရသော ဘာဝရုပ်။' },
            { id: 33, key: 'i-jivita', name: 'ဇီဝိတိန္ဒြေ', group: 'indriya', icon: 'fa-heart-pulse', desc: 'အသက်ရှင်ခြင်း၌ အစိုးရသော ရုပ်/နာမ် ဇီဝိတ။' },
            { id: 34, key: 'i-mano', name: 'မနိန္ဒြေ', group: 'indriya', icon: 'fa-brain', desc: 'အာရုံကို သိခြင်း၌ အစိုးရသော စိတ် ၈၉ ပါး။' },
            { id: 35, key: 'i-sukha', name: 'သုခိန္ဒြေ', group: 'indriya', icon: 'fa-face-laugh', desc: 'ကိုယ်ချမ်းသာခြင်း၌ အစိုးရသော ဝေဒနာ။' },
            { id: 36, key: 'i-dukkha', name: 'ဒုက္ခိန္ဒြေ', group: 'indriya', icon: 'fa-face-frown', desc: 'ကိုယ်ဆင်းရဲခြင်း၌ အစိုးရသော ဝေဒနာ။' },
            { id: 37, key: 'i-somanassa', name: 'သောမနဿိန္ဒြေ', group: 'indriya', icon: 'fa-face-smile', desc: 'စိတ်ချမ်းသာခြင်း၌ အစိုးရသော ဝေဒနာ။' },
            { id: 38, key: 'i-domanassa', name: 'ဒေါမနဿိန္ဒြေ', group: 'indriya', icon: 'fa-face-sad-cry', desc: 'စိတ်ဆင်းရဲခြင်း၌ အစိုးရသော ဝေဒနာ။' },
            { id: 39, key: 'i-upekkha', name: 'ဥပေက္ခိန္ဒြေ', group: 'indriya', icon: 'fa-scale-balanced', desc: 'အလယ်အလတ်ဖြစ်ခြင်း၌ အစိုးရသော ဝေဒနာ။' },
            { id: 40, key: 'i-saddha', name: 'သဒ္ဓိန္ဒြေ', group: 'indriya', icon: 'fa-hands-praying', desc: 'ယုံကြည်ခြင်း၌ အစိုးရသော သဒ္ဓါစေတသိက်။' },
            { id: 41, key: 'i-viriya', name: 'ဝီရိယိန္ဒြေ', group: 'indriya', icon: 'fa-bolt', desc: 'အားထုတ်ခြင်း၌ အစိုးရသော ဝီရိယစေတသိက်။' },
            { id: 42, key: 'i-sati', name: 'သတိန္ဒြေ', group: 'indriya', icon: 'fa-bell', desc: 'အောက်မေ့ခြင်း၌ အစိုးရသော သတိစေတသိက်။' },
            { id: 43, key: 'i-samadhi', name: 'သမာဓိန္ဒြေ', group: 'indriya', icon: 'fa-bullseye', desc: 'တည်ကြည်ခြင်း၌ အစိုးရသော ဧကဂ္ဂတာစေတသိက်။' },
            { id: 44, key: 'i-panna', name: 'ပညိန္ဒြေ', group: 'indriya', icon: 'fa-lightbulb', desc: 'သိမြင်ခြင်း၌ အစိုးရသော ပညာစေတသိက်။' },
            { id: 45, key: 'i-anannata', name: 'အနညတညဿာမီတိန္ဒြေ', group: 'indriya', icon: 'fa-eye', desc: 'မသိသေးသည်ကို သိအောင်လုပ်ခြင်း၌ အစိုးရသော (သောတာပတ္တိမဂ် ပညာ)။' },
            { id: 46, key: 'i-annita', name: 'အညိန္ဒြေ', group: 'indriya', icon: 'fa-eye', desc: 'သိပြီးသည်ကို ပို၍သိခြင်း၌ အစိုးရသော (အလယ် မဂ် ၃ ဖိုလ် ၃ ပညာ)။' },
            { id: 47, key: 'i-annatavi', name: 'အညာတာဝိန္ဒြေ', group: 'indriya', icon: 'fa-eye', desc: 'အကုန်အစင် သိပြီးသူ၏ အဖြစ်၌ အစိုးရသော (အရဟတ္တဖိုလ် ပညာ)။' },

            // Bala (9)
            { id: 48, key: 'b-saddha', name: 'သဒ္ဓါဗလ', group: 'bala', icon: 'fa-hands-praying', desc: 'မယုံကြည်မှု (အဿဒ္ဓိယ) ကို တွန်းလှန်နိုင်စွမ်းသော ခွန်အား။' },
            { id: 49, key: 'b-viriya', name: 'ဝီရိယဗလ', group: 'bala', icon: 'fa-bolt', desc: 'ပျင်းရိမှု (ကောသဇ္ဇ) ကို တွန်းလှန်နိုင်စွမ်းသော ခွန်အား (ကု/အကု ရောပြွမ်း)။' },
            { id: 50, key: 'b-sati', name: 'သတိဗလ', group: 'bala', icon: 'fa-bell', desc: 'မေ့လျော့မှု (မုဋ္ဌသစ္စ) ကို တွန်းလှန်နိုင်စွမ်းသော ခွန်အား။' },
            { id: 51, key: 'b-samadhi', name: 'သမာဓိဗလ', group: 'bala', icon: 'fa-bullseye', desc: 'ပျံ့လွင့်မှု (ဥဒ္ဓစ္စ) ကို တွန်းလှန်နိုင်စွမ်းသော ခွန်အား (ကု/အကု ရောပြွမ်း)။' },
            { id: 52, key: 'b-panna', name: 'ပညာဗလ', group: 'bala', icon: 'fa-lightbulb', desc: 'မသိမှု (အဝိဇ္ဇာ) ကို တွန်းလှန်နိုင်စွမ်းသော ခွန်အား။' },
            { id: 53, key: 'b-hiri', name: 'ဟိရီဗလ', group: 'bala', icon: 'fa-shield-heart', desc: 'မရှက်မှု (အဟိရိက) ကို တွန်းလှန်နိုင်စွမ်းသော ရှက်ခြင်းခွန်အား။' },
            { id: 54, key: 'b-ottappa', name: 'ဩတ္တပ္ပဗလ', group: 'bala', icon: 'fa-shield-halved', desc: 'မကြောက်မှု (အနောတ္တပ္ပ) ကို တွန်းလှန်နိုင်စွမ်းသော ကြောက်ခြင်းခွန်အား။' },
            { id: 55, key: 'b-ahiri', name: 'အဟိရိကဗလ', group: 'bala', icon: 'fa-xmark', desc: 'ရှက်ခြင်း (ဟိရီ) ကို တွန်းလှန်နိုင်စွမ်းသော မရှက်ခြင်းခွန်အား (အကုသိုလ်)။' },
            { id: 56, key: 'b-anottappa', name: 'အနောတ္တပ္ပဗလ', group: 'bala', icon: 'fa-xmark', desc: 'ကြောက်ခြင်း (ဩတ္တပ္ပ) ကို တွန်းလှန်နိုင်စွမ်းသော မကြောက်ခြင်းခွန်အား (အကုသိုလ်)။' },

            // Adhipati (4)
            { id: 57, key: 'a-chanda', name: 'ဆန္ဒာဓိပတိ', group: 'adhipati', icon: 'fa-fire', desc: 'ပြင်းပြသော ဆန္ဒဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 58, key: 'a-viriya', name: 'ဝီရိယာဓိပတိ', group: 'adhipati', icon: 'fa-bolt', desc: 'ပြင်းပြသော အားထုတ်မှုဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 59, key: 'a-citta', name: 'စိတ္တာဓိပတိ', group: 'adhipati', icon: 'fa-brain', desc: 'ပြင်းပြသော စိတ်စွမ်းအင်ဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း (ကု/အကု ရောပြွမ်း)။' },
            { id: 60, key: 'a-vimamsa', name: 'ဝီမံသာဓိပတိ (ပညာ)', group: 'adhipati', icon: 'fa-lightbulb', desc: 'ပြင်းပြသော စူးစမ်းဆင်ခြင်မှုဖြင့် အကြီးအကဲ ပြုလုပ်ခြင်း (ပညာ - ကုသိုလ်)။' },

            // Ahara (4)
            { id: 61, key: 'ah-kabalikara', name: 'ကဗဠီကာရာဟာရ', group: 'ahara', icon: 'fa-bowl-food', desc: 'ခန္ဓာကိုယ်ကို ထောက်ပံ့သော ရုပ်အစာ (ဩဇာရုပ်)။' },
            { id: 62, key: 'ah-phassa', name: 'ဖဿာဟာရ', group: 'ahara', icon: 'fa-hand-pointer', desc: 'ဝေဒနာ (ခံစားမှု) သုံးပါးကို ဖြစ်စေသော ထိတွေ့မှု အစာ (ဖဿ)။' },
            { id: 63, key: 'ah-manosancetana', name: 'မနောသဉ္စေတနာဟာရ', group: 'ahara', icon: 'fa-gears', desc: 'ဘဝသစ်ကို ဖြစ်စေသော ကံတရား အစာ (စေတနာ)။' },
            { id: 64, key: 'ah-vinnana', name: 'ဝိညာဏာဟာရ', group: 'ahara', icon: 'fa-brain', desc: 'နာမ်ရုပ်ကို ဖြစ်စေသော စိတ်အစာ (ဝိညာဉ်)။' }
        ];

