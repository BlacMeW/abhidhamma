/**
 * Accessibility features for Abhidhamma Visual Guide
 * Handles Light/Dark mode toggling and Text size adjustments.
 */

(function() {
    // Inject the widget HTML
    const widgetHTML = `
        <div id="a11y-widget" class="fixed bottom-4 right-4 z-50 font-sans">
            <button id="a11y-toggle" class="w-12 h-12 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white shadow-lg flex items-center justify-center text-xl transition-transform hover:scale-110 focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:ring-offset-2 dark:focus:ring-offset-slate-900" aria-label="Accessibility Settings">
                <i class="fa-solid fa-universal-access"></i>
            </button>
            
            <div id="a11y-panel" class="absolute bottom-16 right-0 mb-2 w-64 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 p-4 transition-all duration-200 origin-bottom-right scale-0 opacity-0 pointer-events-none">
                <h3 class="font-bold text-slate-800 dark:text-slate-200 text-sm mb-3 border-b border-slate-100 dark:border-slate-700 pb-2 flex items-center justify-between">
                    <span>ဖတ်ရှုမှု အထောက်အကူ</span>
                    <button id="a11y-close" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"><i class="fa-solid fa-xmark"></i></button>
                </h3>
                
                <div class="space-y-4">
                    <!-- Theme Toggle -->
                    <div>
                        <span class="text-xs text-slate-500 dark:text-slate-400 block mb-2 font-semibold uppercase tracking-wider">အလင်း/အမှောင် (Theme)</span>
                        <div class="flex items-center bg-slate-100 dark:bg-slate-900 rounded-lg p-1">
                            <button id="theme-light" class="flex-1 py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors text-slate-600 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">
                                <i class="fa-solid fa-sun"></i> Light
                            </button>
                            <button id="theme-dark" class="flex-1 py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors text-slate-600 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">
                                <i class="fa-solid fa-moon"></i> Dark
                            </button>
                        </div>
                    </div>
                    
                    <!-- Text Size -->
                    <div>
                        <span class="text-xs text-slate-500 dark:text-slate-400 block mb-2 font-semibold uppercase tracking-wider">စာလုံးအရွယ်အစား (Text Size)</span>
                        <div class="flex items-center justify-between bg-slate-100 dark:bg-slate-900 rounded-lg p-1">
                            <button id="text-decrease" class="w-10 h-8 rounded-md bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition font-bold" aria-label="Decrease text size">A-</button>
                            <span id="text-size-display" class="text-sm font-bold text-slate-700 dark:text-slate-300 w-12 text-center">100%</span>
                            <button id="text-increase" class="w-10 h-8 rounded-md bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition font-bold" aria-label="Increase text size">A+</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', widgetHTML);

    const toggleBtn = document.getElementById('a11y-toggle');
    const panel = document.getElementById('a11y-panel');
    const closeBtn = document.getElementById('a11y-close');
    
    let isPanelOpen = false;

    function togglePanel() {
        isPanelOpen = !isPanelOpen;
        if (isPanelOpen) {
            panel.classList.remove('scale-0', 'opacity-0', 'pointer-events-none');
            panel.classList.add('scale-100', 'opacity-100');
        } else {
            panel.classList.add('scale-0', 'opacity-0', 'pointer-events-none');
            panel.classList.remove('scale-100', 'opacity-100');
        }
    }

    toggleBtn.addEventListener('click', togglePanel);
    closeBtn.addEventListener('click', togglePanel);

    // Close when clicking outside
    document.addEventListener('click', (e) => {
        if (isPanelOpen && !document.getElementById('a11y-widget').contains(e.target)) {
            togglePanel();
        }
    });

    // Theme Management
    const htmlEl = document.documentElement;
    const btnLight = document.getElementById('theme-light');
    const btnDark = document.getElementById('theme-dark');

    function setTheme(theme) {
        if (theme === 'dark') {
            htmlEl.classList.add('dark');
            btnDark.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-slate-900', 'dark:text-white');
            btnDark.classList.remove('text-slate-600', 'dark:text-slate-400');
            
            btnLight.classList.remove('bg-white', 'shadow-sm', 'text-slate-900');
            btnLight.classList.add('text-slate-600', 'dark:text-slate-400');
        } else {
            htmlEl.classList.remove('dark');
            btnLight.classList.add('bg-white', 'shadow-sm', 'text-slate-900');
            btnLight.classList.remove('text-slate-600', 'dark:text-slate-400');
            
            btnDark.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-slate-900', 'dark:text-white');
            btnDark.classList.add('text-slate-600', 'dark:text-slate-400');
        }
        localStorage.setItem('abhidhamma_theme', theme);
    }

    // Initialize Theme (Default to dark for this app)
    const savedTheme = localStorage.getItem('abhidhamma_theme') || 'dark';
    setTheme(savedTheme);

    btnLight.addEventListener('click', () => setTheme('light'));
    btnDark.addEventListener('click', () => setTheme('dark'));

    // Text Size Management
    let currentSize = parseInt(localStorage.getItem('abhidhamma_text_size') || '100', 10);
    const sizeDisplay = document.getElementById('text-size-display');
    const btnIncrease = document.getElementById('text-increase');
    const btnDecrease = document.getElementById('text-decrease');

    function applyTextSize() {
        // We adjust the font-size of html element. Tailwind uses rem based on this.
        // Base is usually 16px (100%).
        htmlEl.style.fontSize = `${(currentSize / 100) * 16}px`;
        sizeDisplay.textContent = `${currentSize}%`;
        localStorage.setItem('abhidhamma_text_size', currentSize.toString());
    }

    btnIncrease.addEventListener('click', () => {
        if (currentSize < 150) {
            currentSize += 10;
            applyTextSize();
        }
    });

    btnDecrease.addEventListener('click', () => {
        if (currentSize > 80) {
            currentSize -= 10;
            applyTextSize();
        }
    });

    // Init text size
    applyTextSize();
})();
