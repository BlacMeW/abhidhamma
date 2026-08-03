import re

html_content = """<!DOCTYPE html>
<html lang="my" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>အဘိဓမ္မာ ဆက်စပ်မှု မြေပုံကြီး (Mind Map) - Visual Guide</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Pyidaungsu"', '"Myanmar Text"', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Pyidaungsu', 'Myanmar Text', sans-serif; overflow: hidden; margin: 0; padding: 0; }
        .glass-nav {
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .light .glass-nav {
            background: rgba(255, 255, 255, 0.8);
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        #markmap-container {
            width: 100vw;
            height: calc(100vh - 64px);
            position: relative;
            background: transparent;
        }
        
        /* Force SVG to fill container */
        #markmap {
            width: 100%;
            height: 100%;
            display: block;
        }
        
        /* Dark mode overrides for Markmap SVG elements */
        .dark .markmap-node text {
            fill: #e2e8f0 !important;
            font-family: 'Pyidaungsu', sans-serif !important;
        }
        .light .markmap-node text {
            fill: #1e293b !important;
            font-family: 'Pyidaungsu', sans-serif !important;
        }
        .dark .markmap-link {
            stroke: #475569 !important;
        }
        
        .map-controls {
            position: absolute;
            bottom: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 10;
        }
        .map-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: inherit;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }
        .dark .map-btn { background: rgba(30, 41, 59, 0.6); }
        .light .map-btn { background: rgba(255, 255, 255, 0.8); border: 1px solid rgba(0, 0, 0, 0.1); }
        .map-btn:hover { background: rgba(99, 102, 241, 0.8); color: white; border-color: transparent; }
    </style>
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 min-h-screen flex flex-col">

    <!-- Navigation -->
    <nav class="glass-nav sticky top-0 z-50 transition-colors duration-300 h-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full">
            <div class="flex items-center justify-between h-full">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-sky-500 to-indigo-500 flex items-center justify-center shadow-lg">
                        <i class="fa-solid fa-project-diagram text-white text-sm"></i>
                    </div>
                    <a href="index.html" class="font-bold text-lg md:text-xl tracking-wide bg-clip-text text-transparent bg-gradient-to-r from-sky-600 to-indigo-600 dark:from-sky-400 dark:to-indigo-400">
                        Concept Map (Interactive)
                    </a>
                </div>
                <div class="flex items-center gap-4">
                    <a href="index.html" class="text-sm font-semibold text-slate-600 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 transition flex items-center gap-2">
                        <i class="fa-solid fa-home"></i> <span class="hidden md:inline">ပင်မစာမျက်နှာ</span>
                    </a>
                    <button id="theme-toggle" class="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-800 transition">
                        <i class="fa-solid fa-moon dark:hidden text-lg"></i>
                        <i class="fa-solid fa-sun hidden dark:block text-lg"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Interactive Map Section -->
    <main id="markmap-container" class="bg-slate-50 dark:bg-slate-900">
        
        <!-- Instruction Overlay -->
        <div class="absolute top-4 right-4 z-10 pointer-events-none text-right">
            <div class="bg-white/80 dark:bg-slate-800/80 backdrop-blur px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-700 shadow-lg inline-block text-left">
                <h3 class="font-bold text-sm text-indigo-600 dark:text-indigo-400 mb-1"><i class="fa-solid fa-hand-pointer mr-1"></i> Interactive Map</h3>
                <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                    • <b>Click</b> on nodes to expand/collapse them.<br>
                    • <b>Drag</b> anywhere to move the map.<br>
                    • <b>Scroll</b> or pinch to zoom in/out.
                </p>
            </div>
        </div>

        <svg id="markmap"></svg>
        
        <!-- Controls -->
        <div class="map-controls">
            <button class="map-btn shadow-md" onclick="zoomIn()" title="Zoom In"><i class="fa-solid fa-plus"></i></button>
            <button class="map-btn shadow-md" onclick="zoomOut()" title="Zoom Out"><i class="fa-solid fa-minus"></i></button>
            <button class="map-btn shadow-md" onclick="fitMap()" title="Fit to screen"><i class="fa-solid fa-expand"></i></button>
        </div>
    </main>

    <!-- Markmap Libraries -->
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.17.0"></script>
    <script src="https://cdn.jsdelivr.net/npm/markmap-view@0.17.0"></script>

    <script>
        // Theme Toggle Logic
        const themeToggleBtn = document.getElementById('theme-toggle');
        const htmlElement = document.documentElement;
        
        if (localStorage.getItem('theme') === 'light' || (!('theme' in localStorage) && !window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            htmlElement.classList.remove('dark');
            htmlElement.classList.add('light');
        } else {
            htmlElement.classList.add('dark');
            htmlElement.classList.remove('light');
        }

        themeToggleBtn.addEventListener('click', () => {
            const isDark = htmlElement.classList.contains('dark');
            htmlElement.classList.toggle('dark', !isDark);
            htmlElement.classList.toggle('light', isDark);
            localStorage.setItem('theme', !isDark ? 'dark' : 'light');
        });

        // Markdown Data for Mind Map
        const markdown = `
# အဘိဓမ္မာ ၉ ပိုင်း
## စိတ် (၈၉ / ၁၂၁)
### ကာမစိတ် (၅၄)
#### အကုသိုလ်စိတ် (၁၂)
- လောဘမူ (၈)
- ဒေါသမူ (၂)
- မောဟမူ (၂)
#### အဟိတ်စိတ် (၁၈)
- အကုသလဝိပါက် (၇)
- အဟိတ်ကုသလဝိပါက် (၈)
- အဟိတ်ကြိယာ (၃)
#### ကာမသောဘဏစိတ် (၂၄)
- မဟာကုသိုလ် (၈)
- မဟာဝိပါက် (၈)
- မဟာကြိယာ (၈)
### မဟဂ္ဂုတ်စိတ် (၂၇)
#### ရူပစိတ် (၁၅)
#### အရူပစိတ် (၁၂)
### လောကုတ္တရာစိတ် (၈ / ၄၀)
#### မဂ်စိတ် (၄ / ၂၀)
#### ဖိုလ်စိတ် (၄ / ၂၀)

## စေတသိက် (၅၂)
### အညသမာန်း (၁၃)
- သဗ္ဗစိတ္တက (၇)
- ပကိဏ္ဏက (၆)
### အကုသိုလ် (၁၄)
- မောစတုက္က (၄)
- လောတိက (၃)
- ဒေါစတုက္က (၄)
- ထီသိတ် (၂)
- ဝိစိကိစ္ဆာ (၁)
### သောဘဏ (၂၅)
- သောဘဏသာဓာရဏ (၁၉)
- ဝိရတီ (၃)
- အပ္ပမညာ (၂)
- ပညိန္ဒြေ (၁)

## ရုပ် (၂၈)
### မဟာဘုတ် (၄)
### ဥပါဒါရုပ် (၂၄)
- ပသာဒရုပ် (၅)
- ဂေါစရရုပ် (၄)
- ဘာဝရုပ် (၂)
- ဟဒယရုပ် (၁)
- ဇီဝိတရုပ် (၁)
- အာဟာရရုပ် (၁)
- အနိပ္ဖန္နရုပ် (၁၀)

## နိဗ္ဗာန်
- သဥပါဒိသေသ နိဗ္ဗာန်
- အနုပါဒိသေသ နိဗ္ဗာန်

## ဝီထိ (ဖြစ်စဉ်)
- ပဉ္စဒွါရဝီထိ
- မနောဒွါရဝီထိ
- အပ္ပနာဝီထိ (ဈာန်/မဂ်/ဖိုလ်)

## ဝီထိမုတ္တ
### ဘုံ (၃၁)
- ကာမဘုံ (၁၁)
- ရူပဘုံ (၁၆)
- အရူပဘုံ (၄)
### ပဋိသန္ဓေစိတ် (၁၉)
### ကံ (၁၆)
### မရဏုပ္ပတ္တိ (၄)

## သမုစ္စည်း
- အကုသလ သင်္ဂဟ (၉)
- ဗောဓိပက္ခိယ (၇)
- သဗ္ဗ သင်္ဂဟ (၅)
- မိဿက သင်္ဂဟ (၇)

## ပစ္စည်း
- ပဋိစ္စသမုပ္ပါဒ် (အင်္ဂါ ၁၂ ပါး)
- ပဋ္ဌာန်း (ပစ္စည်း ၂၄ ပါး)

## ကမ္မဋ္ဌာန်း
### သမထ (၄၀)
- ကသိုဏ်း (၁၀)
- အသုဘ (၁၀)
- အနုဿတိ (၁၀)
- အပ္ပမညာ (၄)
- အာရုပ္ပ (၄)
- သညာ (၁)
- ဝဝတ္ထာန် (၁)
### ဝိပဿနာ
- ဝိသုဒ္ဓိ (၇) ပါး
- ဉာဏ်စဉ် (၁၀) ပါး
`;

        let mm;
        
        // Ensure DOM is fully loaded and container has dimensions
        window.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                const { Transformer } = window.markmap;
                const { Markmap } = window.markmap;

                const transformer = new Transformer();
                const { root } = transformer.transform(markdown);
                
                mm = Markmap.create('#markmap', {
                    autoFit: true,
                    fitRatio: 0.9,
                    duration: 500,
                    paddingX: 80,
                }, root);
            }, 100);
        });

        // Control functions
        function zoomIn() { if(mm) mm.rescale(1.2); }
        function zoomOut() { if(mm) mm.rescale(0.8); }
        function fitMap() { if(mm) mm.fit(); }
    </script>
</body>
</html>"""

with open('concept_map.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("concept_map.html fixed using explicit markmap initialization and proper SVG sizing.")
