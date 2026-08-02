import re

with open('emotion_analyzer.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update filter tabs and add search bar
filter_html = """        <!-- Filter Tabs -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 mb-4">
            <div class="flex justify-center gap-2 flex-wrap">
                <button onclick="filterEmotions('all')" id="filter-all" class="filter-btn active px-4 py-1.5 rounded-full border border-slate-300 dark:border-slate-600 text-sm font-medium transition-all hover:bg-slate-200 dark:hover:bg-slate-700">အားလုံး (All)</button>
                <button onclick="filterEmotions('akusala')" id="filter-akusala" class="filter-btn px-4 py-1.5 rounded-full border border-slate-300 dark:border-slate-600 text-sm font-medium transition-all hover:bg-slate-200 dark:hover:bg-slate-700 text-rose-600 dark:text-rose-400">အကုသိုလ် (Problems)</button>
                <button onclick="filterEmotions('kusala')" id="filter-kusala" class="filter-btn px-4 py-1.5 rounded-full border border-slate-300 dark:border-slate-600 text-sm font-medium transition-all hover:bg-slate-200 dark:hover:bg-slate-700 text-emerald-600 dark:text-emerald-400">ကုသိုလ် (Positive)</button>
            </div>
            <div class="relative w-full sm:w-64">
                <input type="text" id="search-emotion" onkeyup="searchEmotions()" placeholder="ခံစားချက် ရှာရန်..." class="w-full pl-9 pr-4 py-2 rounded-full border border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-800 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-amber-500 text-sm">
                <i class="fa-solid fa-search absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            </div>
        </div>"""

content = re.sub(r'<!-- Filter Tabs -->.*?</div>', filter_html, content, flags=re.DOTALL)


# 2. Add new emotions to emotionData
new_emotions = """
            "alobha": {
                id: "alobha",
                name: "ဒါန / စွန့်လွှတ်ခြင်း (Generosity / Non-attachment)",
                icon: "fa-hand-holding", color: "emerald", type: "kusala",
                cittaName: "မဟာကုသိုလ်စိတ် (၈) ပါး",
                desc: "ပေးကမ်းလိုခြင်း၊ စွန့်လွှတ်လိုခြင်း၊ အာရုံများအပေါ် မတွယ်တာမတပ်မက်ခြင်း (အလောဘ) ဖြစ်ပါသည်။ လောဘ၏ ဆန့်ကျင်ဘက်ဖြစ်ပါသည်။",
                remedy: "ဤစိတ်သည် မွန်မြတ်သော ကုသိုလ်စိတ်ဖြစ်ပါသည်။ ပေးကမ်းစွန့်ကြဲမှု (ဒါန) ပြုလုပ်ခြင်းဖြင့် ပိုမိုအားကောင်းလာစေနိုင်ပါသည်။",
                cetasikaCount: "အများဆုံး ၃၈ ပါး",
                cetasikasGroups: [
                    { groupName: "သောဘဏ စေတသိက်များ", items: [ 
                        { name: "အလောဘ (Alobha)", desc: "မတပ်မက်ခြင်း၊ စွန့်လွှတ်ခြင်း (အဓိက)" }, 
                        { name: "အဒေါသ (Adosa)", desc: "မကြမ်းတမ်းခြင်း" }, 
                        { name: "အမောဟ/ပညာ (Amoha)", desc: "အမှန်သိခြင်း" },
                        { name: "သဒ္ဓါ (Saddha)", desc: "ယုံကြည်ခြင်း" },
                        { name: "သတိ (Sati)", desc: "အောက်မေ့ခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၃)", items: [ 
                        { name: "သဗ္ဗစိတ္တသာဓာရဏ (၇)", desc: "ဖဿ၊ ဝေဒနာ စသည်" },
                        { name: "ပကိဏ္ဏက (၆)", desc: "ဝိတက်၊ ဝိစာရ၊ အဓိမောက္ခ၊ ဝီရိယ၊ ပီတိ၊ ဆန္ဒ" }
                    ]}
                ]
            },
            "panna": {
                id: "panna",
                name: "ပညာ / ဆင်ခြင်တုံတရား (Wisdom / Clarity)",
                icon: "fa-lightbulb", color: "amber", type: "kusala",
                cittaName: "ဉာဏသမ္ပယုတ် မဟာကုသိုလ်စိတ် (၄) ပါး",
                desc: "အကြောင်းအကျိုး၊ အဆိုးအကောင်း၊ အမှားအမှန်ကို ရှင်းလင်းစွာ ခွဲခြားသိမြင်သော အသိဉာဏ် (အမောဟ/ပညာ) ဖြစ်ပါသည်။ မောဟ၏ ဆန့်ကျင်ဘက်ဖြစ်ပါသည်။",
                remedy: "ဤစိတ်သည် အမြင့်မြတ်ဆုံးသော ကုသိုလ်ဖြစ်ပါသည်။ ဝိပဿနာတရား အားထုတ်ခြင်း၊ တရားဓမ္မ လေ့လာဆွေးနွေးခြင်းတို့ဖြင့် ပညာကို ရင့်သန်စေနိုင်ပါသည်။",
                cetasikaCount: "အများဆုံး ၃၈ ပါး",
                cetasikasGroups: [
                    { groupName: "သောဘဏ စေတသိက်များ", items: [ 
                        { name: "ပညိန္ဒြေ (Paññā)", desc: "အမှန်ကို သိမြင်ခြင်း (အဓိက)" }, 
                        { name: "အလောဘ (Alobha)", desc: "မတပ်မက်ခြင်း" }, 
                        { name: "အဒေါသ (Adosa)", desc: "မကြမ်းတမ်းခြင်း" }, 
                        { name: "သဒ္ဓါ (Saddha)", desc: "ယုံကြည်ခြင်း" },
                        { name: "သတိ (Sati)", desc: "အောက်မေ့ခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၃)", items: [ 
                        { name: "သဗ္ဗစိတ္တသာဓာရဏ (၇)", desc: "ဖဿ၊ ဝေဒနာ စသည်" },
                        { name: "ပကိဏ္ဏက (၆)", desc: "ဝိတက်၊ ဝိစာရ၊ အဓိမောက္ခ၊ ဝီရိယ၊ ပီတိ၊ ဆန္ဒ" }
                    ]}
                ]
            },
            "sati": {
                id: "sati",
                name: "သတိ / အသိကပ်ခြင်း (Mindfulness)",
                icon: "fa-eye", color: "sky", type: "kusala",
                cittaName: "မဟာကုသိုလ်စိတ် (၈) ပါး",
                desc: "ပစ္စုပ္ပန်တည့်တည့်၌ ဖြစ်ပေါ်နေသော ရုပ်နာမ်အာရုံတို့အပေါ် အသိကပ်နေခြင်း၊ မေ့လျော့မှုကင်းခြင်း (သတိ) ဖြစ်ပါသည်။",
                remedy: "သတိသည် ကုသိုလ်တိုင်းတွင် မပါမဖြစ် လိုအပ်သော တရားဖြစ်ပါသည်။ ကာယ၊ ဝေဒနာ၊ စိတ္တ၊ ဓမ္မ ဟူသော သတိပဋ္ဌာန်လေးပါးကို အမြဲပွားများပါ။",
                cetasikaCount: "အများဆုံး ၃၈ ပါး",
                cetasikasGroups: [
                    { groupName: "သောဘဏ စေတသိက်များ", items: [ 
                        { name: "သတိ (Sati)", desc: "အောက်မေ့ခြင်း၊ အသိကပ်ခြင်း (အဓိက)" }, 
                        { name: "အလောဘ (Alobha)", desc: "မတပ်မက်ခြင်း" }, 
                        { name: "အဒေါသ (Adosa)", desc: "မကြမ်းတမ်းခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၃)", items: [ 
                        { name: "သဗ္ဗစိတ္တသာဓာရဏ (၇)", desc: "ဖဿ၊ ဝေဒနာ စသည်" },
                        { name: "ပကိဏ္ဏက (၆)", desc: "ဝိတက်၊ ဝိစာရ၊ အဓိမောက္ခ၊ ဝီရိယ၊ ပီတိ၊ ဆန္ဒ" }
                    ]}
                ]
            },
            "piti": {
                id: "piti",
                name: "ပီတိ / ဝမ်းသာအားရဖြစ်ခြင်း (Joy / Rapture)",
                icon: "fa-face-laugh-beam", color: "pink", type: "kusala",
                cittaName: "သောမနဿသဟဂုတ်စိတ်များ",
                desc: "ကုသိုလ်ကောင်းမှု ပြုလုပ်ရသဖြင့် ဝမ်းသာအားရဖြစ်ခြင်း၊ နှစ်သက်ခြင်း၊ ပီတိဖြစ်ခြင်း အခြေအနေဖြစ်ပါသည်။ (ပီတိသည် အကုသိုလ်နှင့်လည်း ယှဉ်နိုင်သော်လည်း ဤနေရာတွင် ကုသိုလ်ပီတိကို ဆိုလိုသည်)",
                remedy: "ကုသိုလ်ကောင်းမှု ပြုပြီးတိုင်း မိမိလုပ်ရပ်ကို ပြန်လည်အောက်မေ့၍ ဝမ်းမြောက်ပါ။ သို့သော် ပီတိလွန်ကဲ၍ ပျံ့လွင့်မှု (ဥဒ္ဓစ္စ) မဖြစ်စေရန် သတိဖြင့် ထိန်းကျောင်းပါ။",
                cetasikaCount: "စိတ်ပေါ်မူတည်၍ အပြောင်းအလဲရှိ",
                cetasikasGroups: [
                    { groupName: "အညသမာန်း စေတသိက်များ", items: [ 
                        { name: "ပီတိ (Pīti)", desc: "နှစ်သက်ခြင်း (အဓိက)" }, 
                        { name: "ဝေဒနာ (Vedanā)", desc: "သောမနဿ (ဝမ်းသာခြင်း)" }
                    ]},
                    { groupName: "သောဘဏ စေတသိက်များ", items: [ 
                        { name: "သဒ္ဓါ၊ သတိ စသော", desc: "ကုသိုလ်အဖွဲ့ဝင်များ" }
                    ]}
                ]
            },
            "upekkha": {
                id: "upekkha",
                name: "ဥပေက္ခာ / လျစ်လျူရှုနိုင်ခြင်း (Equanimity)",
                icon: "fa-scale-balanced", color: "indigo", type: "kusala",
                cittaName: "ဥပေက္ခာသဟဂုတ် မဟာကုသိုလ်စိတ်များ",
                desc: "ဝမ်းသာလွန်းခြင်း (သောမနဿ)၊ ဝမ်းနည်းလွန်းခြင်း (ဒေါမနဿ) မရှိဘဲ အလယ်အလတ် မျှတတည်ငြိမ်သော၊ ဘက်မလိုက်သော စိတ်အခြေအနေ (တတြမဇ္ဈတ္တတာ) ဖြစ်ပါသည်။",
                remedy: "သတ္တဝါတို့သည် ကံသာလျှင် ကိုယ်ပိုင်ဥစ္စာရှိသည် (ကမ္မဿကတာဉာဏ်) ကို ဆင်ခြင်ခြင်းဖြင့် ဥပေက္ခာကို ပွားများနိုင်ပါသည်။ လောကဓံနှင့် ကြုံတွေ့ရချိန်တွင် အကောင်းဆုံး လက်နက်ဖြစ်ပါသည်။",
                cetasikaCount: "အများဆုံး ၃၇ ပါး (ပီတိမပါ)",
                cetasikasGroups: [
                    { groupName: "သောဘဏ စေတသိက်များ", items: [ 
                        { name: "တတြမဇ္ဈတ္တတာ", desc: "အလယ်အလတ် မျှတခြင်း (အဓိက)" }, 
                        { name: "အလောဘ (Alobha)", desc: "မတပ်မက်ခြင်း" }, 
                        { name: "အဒေါသ (Adosa)", desc: "မကြမ်းတမ်းခြင်း" },
                        { name: "အမောဟ (Amoha)", desc: "အမှန်သိခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၂)", items: [ 
                        { name: "ဝေဒနာ (Vedanā)", desc: "ဥပေက္ခာ (အလယ်အလတ် ခံစားမှု)" },
                        { name: "ပီတိ (Pīti)", desc: "မပါဝင်ပါ" }
                    ]}
                ]
            },
            "macchariya": {
                id: "macchariya",
                name: "မစ္ဆရိယ / နှမြောဝန်တိုခြင်း (Stinginess)",
                icon: "fa-box-archive", color: "red", type: "akusala",
                cittaName: "ဒေါသမူလစိတ် (၂) ပါး",
                desc: "မိမိပိုင်ဆိုင်သော ပစ္စည်းဥစ္စာ၊ အသိပညာ စသည်တို့ကို သူတစ်ပါးနှင့် မမျှဝေလိုခြင်း၊ သူတစ်ပါး သုံးစွဲမည်ကို စိုးရိမ်နှမြောခြင်း ဖြစ်ပါသည်။ ဒေါသအုပ်စုဝင် ဖြစ်သည်။",
                remedy: "ပစ္စည်းဥစ္စာတို့သည် မမြဲသောသဘောရှိကြောင်း ဆင်ခြင်ပါ။ ပေးကမ်းစွန့်ကြဲမှု (ဒါန) ကို အနည်းငယ်မှစ၍ လေ့ကျင့်ပါ။ သူတစ်ပါးကို ကူညီခြင်းဖြင့် ရရှိသော ပီတိကို ခံစားကြည့်ပါ။",
                cetasikaCount: "အများဆုံး ၂၀ ပါး",
                cetasikasGroups: [
                    { groupName: "အကုသိုလ် စေတသိက်များ", items: [ 
                        { name: "မစ္ဆရိယ (Macchariya)", desc: "ဝန်တိုခြင်း (အဓိက)" }, 
                        { name: "ဒေါသ (Dosa)", desc: "ကြမ်းတမ်းခြင်း၊ စိတ်မချမ်းသာခြင်း" }, 
                        { name: "မောဟ (Moha)", desc: "တွေဝေခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၂)", items: [ 
                        { name: "ဝေဒနာ (Vedanā)", desc: "ဒေါမနဿ" }
                    ]}
                ]
            },
            "kukkucca": {
                id: "kukkucca",
                name: "ကုက္ကုစ္စ / နောင်တရခြင်း (Guilt / Remorse)",
                icon: "fa-person-praying", color: "purple", type: "akusala",
                cittaName: "ဒေါသမူလစိတ် (၂) ပါး",
                desc: "မိမိပြုလုပ်ခဲ့မိသော အမှားများ (သို့) မပြုလုပ်ခဲ့ရသော အကောင်းများအတွက် နောင်တရ ပူပန်နေခြင်း ဖြစ်ပါသည်။ ဒေါသအုပ်စုဝင် ဖြစ်သည်။",
                remedy: "ပြီးခဲ့သောအရာများကို ပြန်ပြင်၍မရကြောင်း လက်ခံပါ။ နောင်တသည် အကုသိုလ်ဖြစ်၍ မိမိကိုယ်ကို ခွင့်လွှတ်ပါ။ ရှေ့ဆက်၍ ကုသိုလ်တရားများကိုသာ ကြိုးစားပြုလုပ်မည်ဟု ဆုံးဖြတ်ပါ။",
                cetasikaCount: "အများဆုံး ၂၀ ပါး",
                cetasikasGroups: [
                    { groupName: "အကုသိုလ် စေတသိက်များ", items: [ 
                        { name: "ကုက္ကုစ္စ (Kukkucca)", desc: "နောင်တပူပန်ခြင်း (အဓိက)" }, 
                        { name: "ဒေါသ (Dosa)", desc: "စိတ်မချမ်းသာခြင်း" }, 
                        { name: "မောဟ (Moha)", desc: "တွေဝေခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၂)", items: [ 
                        { name: "ဝေဒနာ (Vedanā)", desc: "ဒေါမနဿ" }
                    ]}
                ]
            },
            "uddhacca": {
                id: "uddhacca",
                name: "ဥဒ္ဓစ္စ / စိတ်ပျံ့လွင့်ခြင်း (Restlessness)",
                icon: "fa-wind", color: "slate", type: "akusala",
                cittaName: "အကုသိုလ်စိတ်အားလုံး (အထူးသဖြင့် ဥဒ္ဓစ္စသမ္ပယုတ်စိတ်)",
                desc: "စိတ်မငြိမ်သက်ခြင်း၊ ဟိုရောက်ဒီရောက် ပျံ့လွင့်နေခြင်း၊ အာရုံတစ်ခုတည်းတွင် ကြာရှည်မနေနိုင်ခြင်း ဖြစ်ပါသည်။ အကုသိုလ်တိုင်းတွင် ပါဝင်ပါသည်။",
                remedy: "အာနာပါန (ဝင်လေထွက်လေ) မှတ်ခြင်းကဲ့သို့သော သမာဓိဘာဝနာကို ပွားများပါ။ စိတ်ပျံ့လွင့်နေသည်ကို သိသိချင်း ပစ္စုပ္ပန်အာရုံသို့ ချက်ချင်းပြန်ခေါ်ပါ။",
                cetasikaCount: "၁၅ ပါး (ဥဒ္ဓစ္စသမ္ပယုတ်စိတ်၌)",
                cetasikasGroups: [
                    { groupName: "အကုသိုလ် စေတသိက်များ", items: [ 
                        { name: "ဥဒ္ဓစ္စ (Uddhacca)", desc: "ပျံ့လွင့်ခြင်း (အဓိက)" }, 
                        { name: "မောဟ (Moha)", desc: "တွေဝေခြင်း" },
                        { name: "အဟိရိက (Ahirika)", desc: "မရှက်ခြင်း" },
                        { name: "အနောတ္တပ္ပ (Anottappa)", desc: "မကြောက်ခြင်း" }
                    ]},
                    { groupName: "အညသမာန်း စေတသိက်များ (၁၁)", items: [ 
                        { name: "ဝေဒနာ (Vedanā)", desc: "ဥပေက္ခာ (များသောအားဖြင့်)" },
                        { name: "ဧကဂ္ဂတာ (Ekaggatā)", desc: "တည်ကြည်ခြင်း (အားနည်းစွာပါဝင်သည်)" }
                    ]}
                ]
            },"""

content = content.replace('"metta": {', new_emotions + '\n            "metta": {')

# 3. Add search JS
search_js = """
        // Search Logic
        function searchEmotions() {
            const query = document.getElementById('search-emotion').value.toLowerCase();
            const buttons = buttonContainer.querySelectorAll('button');
            
            let found = false;
            buttons.forEach(btn => {
                const emotionId = btn.dataset.id;
                const emotion = emotionData[emotionId];
                
                // Check if matches search
                const matchesSearch = emotion.name.toLowerCase().includes(query) || 
                                      emotion.desc.toLowerCase().includes(query) ||
                                      (emotion.cittaName && emotion.cittaName.toLowerCase().includes(query));
                
                // Check if matches filter
                const matchesFilter = currentFilter === 'all' || emotion.type === currentFilter;
                
                if (matchesSearch && matchesFilter) {
                    btn.style.display = 'flex';
                    found = true;
                } else {
                    btn.style.display = 'none';
                }
            });
            
            // Wait empty state logic could be added if no results found, but buttons area will just be empty.
        }

        // Filter Logic"""

content = content.replace('        // Filter Logic', search_js)

# Save
with open('emotion_analyzer.html', 'w', encoding='utf-8') as f:
    f.write(content)

