/**
 * Accessibility features for Abhidhamma Visual Guide
 * Handles Light/Dark mode toggling, Text size adjustments, and Draggable positioning.
 */

(function() {
    // Inject the widget HTML
    const widgetHTML = `
        <div id="a11y-widget" class="fixed z-50 font-sans select-none" style="bottom: 16px; right: 16px; touch-action: none;">
            <button id="a11y-toggle" class="relative w-12 h-12 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white shadow-xl flex items-center justify-center text-xl transition-transform hover:scale-110 focus:outline-none focus:ring-2 focus:ring-emerald-400 focus:ring-offset-2 dark:focus:ring-offset-slate-900 cursor-move active:scale-95" title="နေရာရွှေ့ရန် ဖိဆွဲနိုင်သည် (Drag to move) / ဖွင့်ရန် နှိပ်ပါ" aria-label="Accessibility Settings">
                <i class="fa-solid fa-universal-access pointer-events-none"></i>
                <span id="a11y-audio-badge" class="hidden absolute -top-1 -right-1 w-3.5 h-3.5 bg-rose-500 rounded-full ring-2 ring-white dark:ring-slate-900 animate-pulse pointer-events-none"></span>
            </button>
            <audio id="a11y-metta-audio" src="assets/mp3/Metta.mp3" loop preload="none"></audio>

            <div id="a11y-panel" class="absolute bottom-16 right-0 mb-2 w-64 bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 p-4 transition-all duration-200 origin-bottom-right scale-0 opacity-0 pointer-events-none">
                <h3 class="font-bold text-slate-800 dark:text-slate-200 text-sm mb-3 border-b border-slate-100 dark:border-slate-700 pb-2 flex items-center justify-between">
                    <span class="flex items-center gap-1.5"><i class="fa-solid fa-universal-access text-emerald-500"></i> ဖတ်ရှုမှု အထောက်အကူ</span>
                    <button id="a11y-close" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"><i class="fa-solid fa-xmark"></i></button>
                </h3>
                
                    <!-- Quick Global Search -->
                    <div>
                        <button id="a11y-global-search-btn" class="w-full py-2 px-3 rounded-xl text-xs font-semibold flex items-center justify-between bg-sky-50 dark:bg-slate-700 text-sky-700 dark:text-sky-300 hover:bg-sky-100 dark:hover:bg-slate-600 transition border border-sky-200 dark:border-slate-600 shadow-sm" aria-label="တစ်ဆိုက်လုံး ရှာဖွေရန် (Global Search)">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-magnifying-glass text-sky-500"></i> ရှာဖွေရန် (Search)</span>
                            <kbd class="text-[10px] px-1.5 py-0.5 rounded bg-white dark:bg-slate-800 text-slate-500 font-mono shadow-xs">Ctrl+K</kbd>
                        </button>
                    </div>

                    <!-- Theme Toggle -->
                    <div>
                        <span class="text-xs text-slate-500 dark:text-slate-400 block mb-2 font-semibold uppercase tracking-wider">အလင်း/အမှောင် (Theme)</span>
                        <div class="flex items-center bg-slate-100 dark:bg-slate-900 rounded-lg p-1">
                            <button id="theme-light" class="flex-1 py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors text-slate-600 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">
                                <i class="fa-solid fa-sun text-amber-500"></i> Light
                            </button>
                            <button id="theme-dark" class="flex-1 py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors text-slate-600 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">
                                <i class="fa-solid fa-moon text-sky-400"></i> Dark
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

                    <!-- Background Metta Chant Audio -->
                    <div class="pt-2 border-t border-slate-100 dark:border-slate-700">
                        <span class="text-xs text-slate-500 dark:text-slate-400 block mb-2 font-semibold uppercase tracking-wider">မေတ္တာရွတ်သံ (Background Audio)</span>
                        <div class="flex items-center gap-2">
                            <button id="a11y-audio-playpause" class="flex-[2] py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors bg-white dark:bg-slate-700 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-600">
                                <i class="fa-solid fa-play" id="a11y-audio-icon"></i> <span id="a11y-audio-label">ဖွင့်မည်</span>
                            </button>
                            <button id="a11y-audio-stop" class="flex-1 py-1.5 rounded-md bg-white dark:bg-slate-800 text-rose-500 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition" aria-label="Stop background audio" title="ရပ်မည်">
                                <i class="fa-solid fa-stop"></i>
                            </button>
                            <button id="a11y-lyrics-btn" class="flex-1 py-1.5 rounded-md bg-white dark:bg-slate-800 text-sky-500 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition" aria-label="View Lyrics" title="ရွတ်စဉ်ဖတ်မည်">
                                <i class="fa-solid fa-music"></i>
                            </button>
                        </div>
                        <span class="text-[10px] text-slate-400 dark:text-slate-500 block mt-1.5"><i class="fa-solid fa-circle-info mr-1"></i> စာမျက်နှာ ပြောင်းလဲသည့်တိုင် ဆက်လက် ဖွင့်ထားနိုင်သည်</span>
                    </div>

                    <!-- Reset Position -->
                    <div class="pt-2 border-t border-slate-100 dark:border-slate-700 flex justify-between items-center">
                        <span class="text-[10px] text-slate-400 dark:text-slate-500"><i class="fa-solid fa-arrows-up-down-left-right mr-1"></i> ဖိဆွဲ၍ ရွှေ့နိုင်သည်</span>
                        <button id="a11y-reset-pos" class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 hover:underline flex items-center gap-1">
                            <i class="fa-solid fa-rotate-left"></i> မူလနေရာထားမည်
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', widgetHTML);

    const widget = document.getElementById('a11y-widget');
    const toggleBtn = document.getElementById('a11y-toggle');
    const panel = document.getElementById('a11y-panel');
    const closeBtn = document.getElementById('a11y-close');
    const resetPosBtn = document.getElementById('a11y-reset-pos');
    
    let isPanelOpen = false;

    // Position & Orientation Management
    function updatePanelOrientation(x, y) {
        // Automatically flip panel open direction so it never overflows off screen
        if (y < 280) {
            panel.classList.remove('bottom-16', 'origin-bottom-right', 'origin-bottom-left', 'mb-2');
            panel.classList.add('top-16', 'mt-2');
        } else {
            panel.classList.remove('top-16', 'origin-top-right', 'origin-top-left', 'mt-2');
            panel.classList.add('bottom-16', 'mb-2');
        }

        if (x < window.innerWidth / 2) {
            panel.classList.remove('right-0', 'origin-bottom-right', 'origin-top-right');
            panel.classList.add('left-0', y < 280 ? 'origin-top-left' : 'origin-bottom-left');
        } else {
            panel.classList.remove('left-0', 'origin-bottom-left', 'origin-top-left');
            panel.classList.add('right-0', y < 280 ? 'origin-top-right' : 'origin-bottom-right');
        }
    }

    function setDefaultPosition(forceReset = false) {
        const isMobile = window.innerWidth < 768;
        // On mobile, default bottom to 80px so it sits ABOVE the bottom navigation bar (which is ~60px tall)
        const defaultBottom = isMobile ? '80px' : '16px';
        const defaultRight = '16px';

        if (!forceReset) {
            const savedPos = localStorage.getItem('abhidhamma_a11y_pos');
            if (savedPos) {
                try {
                    const pos = JSON.parse(savedPos);
                    const x = Math.max(8, Math.min(window.innerWidth - 56, pos.x));
                    const y = Math.max(8, Math.min(window.innerHeight - 56, pos.y));
                    widget.style.left = `${x}px`;
                    widget.style.top = `${y}px`;
                    widget.style.right = 'auto';
                    widget.style.bottom = 'auto';
                    updatePanelOrientation(x, y);
                    return;
                } catch(e) {}
            }
        }

        widget.style.bottom = defaultBottom;
        widget.style.right = defaultRight;
        widget.style.left = 'auto';
        widget.style.top = 'auto';
        updatePanelOrientation(window.innerWidth - 64, window.innerHeight - (isMobile ? 130 : 64));
    }

    setDefaultPosition();
    window.addEventListener('resize', () => setDefaultPosition(false));

    resetPosBtn.addEventListener('click', () => {
        localStorage.removeItem('abhidhamma_a11y_pos');
        widget.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        setDefaultPosition(true);
        setTimeout(() => { widget.style.transition = ''; }, 300);
    });

    // Drag & Drop Functionality using Pointer Events (Touch + Mouse)
    let isDragging = false;
    let startX = 0, startY = 0;
    let initialLeft = 0, initialTop = 0;

    toggleBtn.addEventListener('pointerdown', (e) => {
        toggleBtn.setPointerCapture(e.pointerId);
        startX = e.clientX;
        startY = e.clientY;
        const rect = widget.getBoundingClientRect();
        initialLeft = rect.left;
        initialTop = rect.top;
        isDragging = false;
        widget.style.transition = 'none';
    });

    toggleBtn.addEventListener('pointermove', (e) => {
        if (!toggleBtn.hasPointerCapture(e.pointerId)) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        
        if (Math.hypot(dx, dy) > 5) {
            isDragging = true;
            let newLeft = Math.max(8, Math.min(window.innerWidth - 56, initialLeft + dx));
            let newTop = Math.max(8, Math.min(window.innerHeight - 56, initialTop + dy));
            
            widget.style.left = `${newLeft}px`;
            widget.style.top = `${newTop}px`;
            widget.style.right = 'auto';
            widget.style.bottom = 'auto';
            updatePanelOrientation(newLeft, newTop);
        }
    });

    function onPointerEnd(e) {
        if (!toggleBtn.hasPointerCapture(e.pointerId)) return;
        toggleBtn.releasePointerCapture(e.pointerId);
        widget.style.transition = '';
        
        if (isDragging) {
            const rect = widget.getBoundingClientRect();
            localStorage.setItem('abhidhamma_a11y_pos', JSON.stringify({ x: Math.round(rect.left), y: Math.round(rect.top) }));
            setTimeout(() => { isDragging = false; }, 50);
        }
    }

    toggleBtn.addEventListener('pointerup', onPointerEnd);
    toggleBtn.addEventListener('pointercancel', onPointerEnd);

    function togglePanel() {
        if (isDragging) return; // Prevent panel toggle if user just dragged the button
        isPanelOpen = !isPanelOpen;
        if (isPanelOpen) {
            const rect = widget.getBoundingClientRect();
            updatePanelOrientation(rect.left, rect.top);
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
            document.body.style.removeProperty('background-color');
            btnDark.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-slate-900', 'dark:text-white');
            btnDark.classList.remove('text-slate-600', 'dark:text-slate-400');
            
            btnLight.classList.remove('bg-white', 'shadow-sm', 'text-slate-900');
            btnLight.classList.add('text-slate-600', 'dark:text-slate-400');
        } else {
            htmlEl.classList.remove('dark');
            document.body.style.setProperty('background-color', '#f8fafc', 'important');
            btnLight.classList.add('bg-white', 'shadow-sm', 'text-slate-900');
            btnLight.classList.remove('text-slate-600', 'dark:text-slate-400');
            
            btnDark.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-slate-900', 'dark:text-white');
            btnDark.classList.add('text-slate-600', 'dark:text-slate-400');
        }
        localStorage.setItem('abhidhamma_theme', theme);
    }

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

    applyTextSize();

    // Background Metta Chant Audio (persists play position across page navigation)
    const mettaAudio = document.getElementById('a11y-metta-audio');
    const audioPlayPauseBtn = document.getElementById('a11y-audio-playpause');
    const audioIcon = document.getElementById('a11y-audio-icon');
    const audioLabel = document.getElementById('a11y-audio-label');
    const audioStopBtn = document.getElementById('a11y-audio-stop');
    const audioBadge = document.getElementById('a11y-audio-badge');
    const AUDIO_STATE_KEY = 'abhidhamma_metta_audio_state';

    function getAudioState() {
        try {
            return JSON.parse(localStorage.getItem(AUDIO_STATE_KEY)) || { playing: false, time: 0 };
        } catch (e) {
            return { playing: false, time: 0 };
        }
    }

    function saveAudioState(playing) {
        localStorage.setItem(AUDIO_STATE_KEY, JSON.stringify({
            playing: playing,
            time: mettaAudio.currentTime || 0
        }));
    }

    function updateAudioUI(playing) {
        audioIcon.className = playing ? 'fa-solid fa-pause' : 'fa-solid fa-play';
        audioLabel.textContent = playing ? 'ခေတ္တရပ်မည်' : 'ဖွင့်မည်';
        audioBadge.classList.toggle('hidden', !playing);
    }

    function playMettaAudio(isInitialResume = false) {
        const playPromise = mettaAudio.play();
        if (playPromise !== undefined) {
            playPromise.then(() => {
                updateAudioUI(true);
                
                // Safari iOS FIX: Safari often ignores currentTime assignments before play() resolves.
                // So we set the time exactly here, right after it is unlocked by the user gesture.
                if (isInitialResume && !window._audioTimeRestored) {
                    const state = getAudioState();
                    if (state.playing && state.time > 0 && mettaAudio.currentTime < 1) {
                        mettaAudio.currentTime = state.time;
                    }
                    window._audioTimeRestored = true;
                }
                saveAudioState(true);
            }).catch(() => {
                // Autoplay blocked by the browser — wait for a user gesture to resume
                updateAudioUI(false);
            });
        }
    }

    function pauseMettaAudio() {
        mettaAudio.pause();
        updateAudioUI(false);
        saveAudioState(false);
    }

    function stopMettaAudio() {
        mettaAudio.pause();
        mettaAudio.currentTime = 0;
        updateAudioUI(false);
        localStorage.removeItem(AUDIO_STATE_KEY);
        const marqueeContainer = document.getElementById('a11y-marquee-container');
        if (marqueeContainer) {
            marqueeContainer.classList.add('hidden');
        }
    }

    audioPlayPauseBtn.addEventListener('click', () => {
        if (mettaAudio.paused) {
            playMettaAudio();
        } else {
            pauseMettaAudio();
        }
    });

    audioStopBtn.addEventListener('click', stopMettaAudio);

    let lastSaveTime = 0;
    mettaAudio.addEventListener('timeupdate', () => {
        if (!mettaAudio.paused) {
            const now = Date.now();
            if (now - lastSaveTime > 1000) { // save every 1 second to avoid performance issues
                saveAudioState(true);
                lastSaveTime = now;
            }
        }
    });

    window.addEventListener('pagehide', () => {
        if (!mettaAudio.paused) saveAudioState(true);
    });
    
    // Also use visibilitychange for better iOS support
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden' && !mettaAudio.paused) {
            saveAudioState(true);
        }
    });

    // Resume playback (and position) left over from the previous page
    const initialAudioState = getAudioState();
    if (initialAudioState.playing) {
        // Change preload to encourage metadata loading
        mettaAudio.preload = "auto";
        window._audioTimeRestored = false;
        
        // Desktop/Android: try to set time as soon as possible
        const setTimeHandler = () => {
            if (!window._audioTimeRestored && initialAudioState.time > 0) {
                mettaAudio.currentTime = initialAudioState.time;
                window._audioTimeRestored = true;
            }
        };
        
        if (mettaAudio.readyState >= 1) { // HAVE_METADATA
            setTimeHandler();
        } else {
            mettaAudio.addEventListener('loadedmetadata', setTimeHandler, { once: true });
        }

        // playMettaAudio will handle the iOS fallback inside its .then()
        playMettaAudio(true);

        // If the browser blocked autoplay, resume on the first user interaction
        const resumeOnInteraction = () => {
            if (mettaAudio.paused && getAudioState().playing) {
                playMettaAudio(true);
            }
        };
        // Add to both document and the play button specifically to ensure it catches gestures
        document.addEventListener('click', resumeOnInteraction, { once: true });
        document.addEventListener('touchstart', resumeOnInteraction, { once: true });
    }

    const lyricsString = "အဟံ အဝေရော ဟောမိ ☸ အဗျာပဇ္ဇော ဟောမိ ☸ အနီဃော ဟောမိ ☸ သုခီ အတ္တာနံ ပရိဟရာမိ ☸ မမ မာတာပိတု ☸ အာစရိယ စ ဉာတိမိတ္တ စ ☸ သဗြဟ္မစာရိနော စ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ ဣမသ္မိံ အာရာမေ သဗ္ဗေ ယောဂိနော ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ ဣမသ္မိံ အာရာမေ သဗ္ဗေ ဘိက္ခူ ☸ သာမဏေရာ စ ☸ ဥပါသကာ ဥပါသိကာယ စ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ အမှာကံ စတုပစ္စယ ဒါယကာ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ အမှာကံ အာရက္ခဒေဝတာ ☸ ဣမသ္မိံ ဝိဟာရေ ☸ ဣမသ္မိံ အာဝါသေ ☸ ဣမသ္မိံ အာရာမေ ☸ အာရက္ခဒေဝတာ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ သဗ္ဗေ သတ္တာ ☸ သဗ္ဗေ ပါဏာ ☸ သဗ္ဗေ ဘူတာ ☸ သဗ္ဗေ ပုဂ္ဂလာ ☸ သဗ္ဗေ အတ္တဘာဝ ပရိယာပန္နာ ☸ သဗ္ဗာ ဣတ္ထိယော ☸ သဗ္ဗေ ပုရိသာ ☸ သဗ္ဗေ အရိယာ ☸ သဗ္ဗေ အနရိယာ ☸ သဗ္ဗေ ဒေဝါ ☸ သဗ္ဗေ မနုဿာ ☸ သဗ္ဗေ ဝိနိပါတိကာ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ ဒုက္ခာ မုစ္စန္တု ☸ ယထာလဒ္ဓသမ္ပတ္တိတော မာ ဝိဂစ္ဆန္တု ☸ ကမ္မဿကာ ☸ ပုရတ္ထိမာယ ဒိသာယ ☸ ပစ္ဆိမာယ ဒိသာယ ☸ ဥတ္တရာယ ဒိသာယ ☸ ဒက္ခိဏာယ ဒိသာယ ☸ ပုရတ္ထိမာယ အနုဒိသာယ ☸ ပစ္ဆိမာယ အနုဒိသာယ ☸ ဥတ္တရာယ အနုဒိသာယ ☸ ဒက္ခိဏာယ အနုဒိသာယ ☸ ဟေဋ္ဌိမာယ ဒိသာယ ☸ ဥပရိမာယ ဒိသာယ ☸ သဗ္ဗေ သတ္တာ ☸ သဗ္ဗေ ပါဏာ ☸ သဗ္ဗေ ဘူတာ ☸ သဗ္ဗေ ပုဂ္ဂလာ ☸ သဗ္ဗေ အတ္တဘာဝ ပရိယာပန္နာ ☸ သဗ္ဗာ ဣတ္ထိယော ☸ သဗ္ဗေ ပုရိသာ ☸ သဗ္ဗေ အရိယာ ☸ သဗ္ဗေ အနရိယာ ☸ သဗ္ဗေ ဒေဝါ ☸ သဗ္ဗေ မနုဿာ ☸ သဗ္ဗေ ဝိနိပါတိကာ ☸ အဝေရာ ဟောန္တု ☸ အဗျာပဇ္ဇာ ဟောန္တု ☸ အနီဃာ ဟောန္တု ☸ သုခီ အတ္တာနံ ပရိဟရန္တု ☸ ဒုက္ခာ မုစ္စန္တု ☸ ယထာလဒ္ဓသမ္ပတ္တိတော မာ ဝိဂစ္ဆန္တု ☸ ကမ္မဿကာ ☸ ဥဒ္ဓံ ယာဝ ဘဝဂ္ဂါ စ ☸ အဓော ယာဝ အဝီစိတော ☸ သမန္တာ စက္ကဝါဠေသု ☸ ယေ သတ္တာ ပထဝီစရာ ☸ အဗျာပဇ္ဇာ နိဝေရာ စ ☸ နိဒုက္ခာ စ နုပဒ္ဒဝါ ☸ ဥဒ္ဓံ ယာဝ ဘဝဂ္ဂါ စ ☸ အဓော ယာဝ အဝီစိတော ☸ သမန္တာ စက္ကဝါဠေသု ☸ ယေ သတ္တာ ဥဒကေစရာ ☸ အဗျာပဇ္ဇာ နိဝေရာ စ ☸ နိဒုက္ခာ စ နုပဒ္ဒဝါ ☸ ဥဒ္ဓံ ယာဝ ဘဝဂ္ဂါ စ ☸ အဓော ယာဝ အဝီစိတော ☸ သမန္တာ စက္ကဝါဠေသု ☸ ယေ သတ္တာ အာကာသေစရာ ☸ အဗျာပဇ္ဇာ နိဝေရာ စ ☸ နိဒုက္ခာ စ နုပဒ္ဒဝါ";


    const lyricsMarqueeHTML = `
    <style>
        .a11y-marquee-text {
            display: inline-block;
            white-space: nowrap;
            padding-left: 50vw;
            padding-right: 50vw;
            will-change: transform;
        }
    </style>
    <div id="a11y-marquee-container" class="fixed bottom-0 left-0 right-0 h-14 bg-slate-900/90 text-amber-400 text-lg sm:text-xl font-bold z-[60] hidden flex items-center overflow-hidden backdrop-blur-sm border-t border-amber-500/30 font-sans">
        <div class="a11y-marquee-text tracking-wider shadow-black drop-shadow-md">
            ${lyricsString}
        </div>
        <button id="a11y-marquee-close" class="absolute right-2 top-1/2 -translate-y-1/2 w-8 h-8 flex items-center justify-center rounded-full bg-slate-800 text-slate-300 hover:bg-rose-500 hover:text-white transition shadow-md z-[61] focus:outline-none ring-2 ring-slate-700/50">
            <i class="fa-solid fa-xmark"></i>
        </button>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', lyricsMarqueeHTML);

    const a11yLyricsBtn = document.getElementById('a11y-lyrics-btn');
    const a11yMarqueeContainer = document.getElementById('a11y-marquee-container');
    const a11yMarqueeClose = document.getElementById('a11y-marquee-close');

    let lyricsVisible = localStorage.getItem('abhidhamma_a11y_lyrics') !== 'false';
    let marqueeAnimationFrame = null;

    function updateMarqueePosition() {
        const audioEl = document.getElementById('a11y-metta-audio');
        const marqueeTextEl = a11yMarqueeContainer.querySelector('.a11y-marquee-text');
        
        if (!audioEl || !marqueeTextEl || isNaN(audioEl.duration) || audioEl.duration <= 0) {
            return;
        }

        const introDelay = 29; // စစချင်း တီးလုံးစောင့်မည့် အချိန် (စက္ကန့်)
        const outroDelay = 20; // အဆုံးသတ် တီးလုံး/အသံတိတ် ချိန် (စာသားကို ပိုမြန်မြန် ပြီးစေရန် ချိန်ညှိနိုင်သည်)
        const chantDuration = audioEl.duration - introDelay - outroDelay;
        let elapsed = audioEl.currentTime - introDelay;
        
        let percentage = 0;
        if (elapsed > 0 && chantDuration > 0) {
            percentage = elapsed / chantDuration;
        }
        if (percentage > 1) percentage = 1;
        
        marqueeTextEl.style.transform = `translateX(calc(-${percentage * 100}% + ${percentage * 100}vw))`;
        
        if (!audioEl.paused && lyricsVisible) {
            marqueeAnimationFrame = requestAnimationFrame(updateMarqueePosition);
        }
    }

    const bgAudioEl = document.getElementById('a11y-metta-audio');
    if (bgAudioEl) {
        bgAudioEl.addEventListener('play', () => {
            if (lyricsVisible) {
                a11yMarqueeContainer.classList.remove('hidden');
                if (marqueeAnimationFrame) cancelAnimationFrame(marqueeAnimationFrame);
                marqueeAnimationFrame = requestAnimationFrame(updateMarqueePosition);
            }
        });
        bgAudioEl.addEventListener('pause', () => {
            if (marqueeAnimationFrame) cancelAnimationFrame(marqueeAnimationFrame);
            updateMarqueePosition();
        });
        bgAudioEl.addEventListener('seeked', updateMarqueePosition);
        // Also update once metadata is loaded so it doesn't stay hidden or unset
        bgAudioEl.addEventListener('loadedmetadata', updateMarqueePosition);
    }

    function applyLyricsVisibility() {
        if (lyricsVisible) {
            a11yMarqueeContainer.classList.remove('hidden');
            updateMarqueePosition();
            
            const audioEl = document.getElementById('a11y-metta-audio');
            if (audioEl && !audioEl.paused) {
                if (marqueeAnimationFrame) cancelAnimationFrame(marqueeAnimationFrame);
                marqueeAnimationFrame = requestAnimationFrame(updateMarqueePosition);
            }
        } else {
            a11yMarqueeContainer.classList.add('hidden');
            if (marqueeAnimationFrame) cancelAnimationFrame(marqueeAnimationFrame);
        }
    }

    function toggleMarquee() {
        lyricsVisible = !lyricsVisible;
        localStorage.setItem('abhidhamma_a11y_lyrics', lyricsVisible);
        applyLyricsVisibility();
    }

    if (a11yLyricsBtn) a11yLyricsBtn.addEventListener('click', toggleMarquee);
    if (a11yMarqueeClose) a11yMarqueeClose.addEventListener('click', () => {
        lyricsVisible = false;
        localStorage.setItem('abhidhamma_a11y_lyrics', 'false');
        applyLyricsVisibility();
    });

    // Apply initial state
    applyLyricsVisibility();

    // ==========================================
    // Universal Global Search System
    // ==========================================
    const universalSearchDb = [
        { name: 'စိတ် (၈၉ / ၁၂၁)', category: 'ပရိစ္ဆေဒ ၁ - စိတ္တသင်္ဂဟ', link: 'citta_cetasikas_visual_guide.html#citta89', icon: 'fa-brain' },
        { name: 'စေတသိက် (၅၂)', category: 'ပရိစ္ဆေဒ ၂ - စေတသိကသင်္ဂဟ', link: 'citta_cetasikas_visual_guide.html#cetasika', icon: 'fa-heart' },
        { name: 'ပကိဏ္ဏကသင်္ဂဟ (ဝေဒနာ၊ ဟိတ်၊ ကိစ္စ၊ ဒွါရ၊ အာရုံ၊ ဝတ္ထု)', category: 'ပရိစ္ဆေဒ ၃ - ပကိဏ္ဏကသင်္ဂဟ', link: 'pakinnaka_sangaha.html', icon: 'fa-layer-group' },
        { name: 'ဝီထိစိတ်ဖြစ်စဉ် (Citta Vithi)', category: 'ပရိစ္ဆေဒ ၄ - ဝီထိသင်္ဂဟ', link: 'vithi_sangaha.html', icon: 'fa-diagram-project' },
        { name: 'ဘုံ (၃၁) ပါး၊ ပဋိသန္ဓေ၊ ကံ ၄၊ မရဏုပ္ပတ္တိ', category: 'ပရိစ္ဆေဒ ၅ - ဝီထိမုတ္တသင်္ဂဟ', link: 'vithimutta_sangaha.html', icon: 'fa-arrows-split-up-and-left' },
        { name: 'ရုပ် (၂၈) ပါး နှင့် နိဗ္ဗာန်', category: 'ပရိစ္ဆေဒ ၆ - ရူပသင်္ဂဟ', link: 'rupa_sangaha.html', icon: 'fa-cube' },
        { name: 'သမုစ္စယသင်္ဂဟ (ကိလေသာ ၄၃ ပါး)', category: 'ပရိစ္ဆေဒ ၇ - သမုစ္စယသင်္ဂဟ', link: 'kilesa_sangaha.html', icon: 'fa-link-slash' },
        { name: 'မိဿကသင်္ဂဟ (ရောပြွမ်း ၇ အုပ်စု)', category: 'ပရိစ္ဆေဒ ၇ - သမုစ္စယသင်္ဂဟ', link: 'missaka_sangaha.html', icon: 'fa-shuffle' },
        { name: 'ဗောဓိပက္ခိယဓမ္မာ (၃၇ ပါး)', category: 'ပရိစ္ဆေဒ ၇ - သမုစ္စယသင်္ဂဟ', link: 'bodhipakkhiya_dhamma.html', icon: 'fa-seedling' },
        { name: 'သဗ္ဗသင်္ဂဟ (ခန္ဓာ၊ အာယတန၊ ဓာတ်၊ သစ္စာ)', category: 'ပရိစ္ဆေဒ ၇ - သမုစ္စယသင်္ဂဟ', link: 'sabba_sangaha.html', icon: 'fa-atom' },
        { name: 'ပစ္စယသင်္ဂဟ (ပဋ္ဌာန်း ၂၄ ပစ္စည်း)', category: 'ပရိစ္ဆေဒ ၈ - ပစ္စယသင်္ဂဟ', link: 'paccaya_sangaha.html', icon: 'fa-link' },
        { name: 'ပဋိစ္စသမုပ္ပါဒ် (၁၂ အင်္ဂါ၊ ဝဋ် ၃ ပါး)', category: 'ပရိစ္ဆေဒ ၈ - ပစ္စယသင်္ဂဟ', link: 'paticcasamuppada.html', icon: 'fa-circle-notch' },
        { name: 'ပညတ် (Paññatti)', category: 'ပရိစ္ဆေဒ ၈ - ပစ္စယသင်္ဂဟ', link: 'pannatti.html', icon: 'fa-font' },
        { name: 'ကမ္မဋ္ဌာနသင်္ဂဟ (သမထ ၄၀၊ ဝိသုဒ္ဓိ ၇၊ ဉာဏ်စဉ် ၁၆)', category: 'ပရိစ္ဆေဒ ၉ - ကမ္မဋ္ဌာနသင်္ဂဟ', link: 'kammatthana_sangaha.html', icon: 'fa-spa' },
        { name: 'အဘိဓမ္မာ အဘိဓာန် (Abhidhamma Glossary)', category: 'အဘိဓာန်နှင့် ဝေါဟာရ', link: 'glossary.html', icon: 'fa-spell-check' },
        { name: 'အဘိဓမ္မာ သဘောတရား ဆက်စပ်မှုပြ Concept Map', category: 'သဘောတရားမြေပုံ', link: 'concept_map.html', icon: 'fa-project-diagram' },
        { name: 'စိတ်သရုပ်ခွဲစက် (Emotion Analyzer)', category: 'လက်တွေ့လေ့လာရေး Tool', link: 'emotion_analyzer.html', icon: 'fa-microscope' },
        { name: 'တရားထိုင် အချိန်မှတ်စနစ် (Meditation Timer)', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'meditation_timer.html', icon: 'fa-bell' },
        { name: 'အာနာပါန Visualizer', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'anapana_visualizer.html', icon: 'fa-wind' },
        { name: 'အာနာပါန ရေတွက်ကိရိယာ (Breath Counter)', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'anapana_counter.html', icon: 'fa-hashtag' },
        { name: 'ကသိုဏ်းဝန်း Simulator (၁၀ ပါး)', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'kasina_simulator.html', icon: 'fa-circle-dot' },
        { name: 'ကသိုဏ်း (၁၀) ပါး လမ်းညွှန်', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'kasina_guide.html', icon: 'fa-book-open' },
        { name: 'မေတ္တာပို့ Prompter', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'metta_prompter.html', icon: 'fa-heart' },
        { name: 'မေတ္တာဘာဝနာ လမ်းညွှန် (၅၂၈ မေတ္တာ)', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'metta_bhavana_guide.html', icon: 'fa-hands-holding-heart' },
        { name: 'သတိပဋ္ဌာန် Prompter', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'satipatthana_prompter.html', icon: 'fa-person-walking' },
        { name: 'သတိပဋ္ဌာန် လမ်းညွှန် (ကာယ၊ ဝေဒနာ၊ စိတ္တ၊ ဓမ္မ)', category: 'တရားလက်တွေ့ကျင့်စဉ်', link: 'satipatthana_guide.html', icon: 'fa-mountain-sun' },
        { name: 'ကျမ်းကိုးစာအုပ်များ (Reference Library)', category: 'စာကြည့်တိုက်', link: 'library.html', icon: 'fa-book' }
    ];

    function openUniversalSearch() {
        if (typeof window.openGlobalSearch === 'function' && document.getElementById('search-modal')) {
            window.openGlobalSearch();
            return;
        }

        let modal = document.getElementById('a11y-universal-search-modal');
        if (!modal) {
            const modalHTML = `
                <div id="a11y-universal-search-modal" class="fixed inset-0 z-[100] flex items-start justify-center pt-16 sm:pt-24 px-4 bg-slate-900/60 backdrop-blur-sm transition-opacity" role="dialog" aria-modal="true" aria-label="Global Search">
                    <div class="w-full max-w-xl bg-white dark:bg-slate-800 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-700 overflow-hidden flex flex-col max-h-[80vh]">
                        <div class="p-4 border-b border-slate-200 dark:border-slate-700 flex items-center gap-3">
                            <i class="fa-solid fa-magnifying-glass text-sky-500 text-lg"></i>
                            <input type="text" id="a11y-universal-search-input" placeholder="တရားအမည် သို့မဟုတ် ပရိစ္ဆေဒ ရှာရန်..." class="w-full bg-transparent text-slate-800 dark:text-slate-100 placeholder-slate-400 focus:outline-none text-base" aria-label="ရှာဖွေရန် စာသား">
                            <button id="a11y-universal-search-close" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-lg p-1" aria-label="ပိတ်ရန်">
                                <i class="fa-solid fa-xmark"></i>
                            </button>
                        </div>
                        <div id="a11y-universal-search-results" class="p-3 overflow-y-auto space-y-2 flex-1">
                            <!-- Results will be dynamically populated -->
                        </div>
                        <div class="p-2.5 bg-slate-50 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-700 flex justify-between items-center text-[11px] text-slate-500 dark:text-slate-400">
                            <span><kbd class="px-1.5 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-600 font-mono">ESC</kbd> ဖြင့် ပိတ်ပါ</span>
                            <span>ပရိစ္ဆေဒ (၉) ခန်းလုံးနှင့် Tools များ စုံလင်စွာ ရှာဖွေနိုင်ပါသည်</span>
                        </div>
                    </div>
                </div>
            `;
            document.body.insertAdjacentHTML('beforeend', modalHTML);
            modal = document.getElementById('a11y-universal-search-modal');

            const searchInput = document.getElementById('a11y-universal-search-input');
            const searchResults = document.getElementById('a11y-universal-search-results');
            const closeBtn = document.getElementById('a11y-universal-search-close');

            function renderResults(q) {
                const query = q.trim().toLowerCase();
                const filtered = query ? universalSearchDb.filter(item => 
                    item.name.toLowerCase().includes(query) || 
                    item.category.toLowerCase().includes(query)
                ) : universalSearchDb.slice(0, 10);

                if (filtered.length === 0) {
                    searchResults.innerHTML = '<p class="text-center text-slate-400 dark:text-slate-500 py-6 text-sm">ရှာဖွေမှု မတွေ့ရှိပါ။ အခြားစာလုံးဖြင့် ထပ်မံ ရှာဖွေပါ</p>';
                    return;
                }

                searchResults.innerHTML = filtered.map(item => `
                    <a href="${item.link}" class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900/60 hover:bg-sky-50 dark:hover:bg-slate-700 border border-slate-200/80 dark:border-slate-700/80 transition flex items-center justify-between group">
                        <div class="flex items-center gap-3">
                            <div class="w-8 h-8 rounded-lg bg-sky-100 dark:bg-sky-950 text-sky-600 dark:text-sky-400 flex items-center justify-center text-sm shrink-0">
                                <i class="fa-solid ${item.icon}"></i>
                            </div>
                            <div>
                                <div class="font-bold text-slate-800 dark:text-slate-200 text-sm group-hover:text-sky-600 dark:group-hover:text-sky-400 transition">${item.name}</div>
                                <div class="text-[11px] text-slate-500 dark:text-slate-400">${item.category}</div>
                            </div>
                        </div>
                        <i class="fa-solid fa-arrow-right text-xs text-slate-400 group-hover:text-sky-500 transform group-hover:translate-x-1 transition"></i>
                    </a>
                `).join('');
            }

            searchInput.addEventListener('input', (e) => renderResults(e.target.value));
            closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.classList.add('hidden');
            });

            renderResults('');
        }

        modal.classList.remove('hidden');
        const input = document.getElementById('a11y-universal-search-input');
        if (input) {
            input.value = '';
            input.focus();
            const results = document.getElementById('a11y-universal-search-results');
            if (results) {
                results.innerHTML = universalSearchDb.slice(0, 10).map(item => `
                    <a href="${item.link}" class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900/60 hover:bg-sky-50 dark:hover:bg-slate-700 border border-slate-200/80 dark:border-slate-700/80 transition flex items-center justify-between group">
                        <div class="flex items-center gap-3">
                            <div class="w-8 h-8 rounded-lg bg-sky-100 dark:bg-sky-950 text-sky-600 dark:text-sky-400 flex items-center justify-center text-sm shrink-0">
                                <i class="fa-solid ${item.icon}"></i>
                            </div>
                            <div>
                                <div class="font-bold text-slate-800 dark:text-slate-200 text-sm group-hover:text-sky-600 dark:group-hover:text-sky-400 transition">${item.name}</div>
                                <div class="text-[11px] text-slate-500 dark:text-slate-400">${item.category}</div>
                            </div>
                        </div>
                        <i class="fa-solid fa-arrow-right text-xs text-slate-400 group-hover:text-sky-500 transform group-hover:translate-x-1 transition"></i>
                    </a>
                `).join('');
            }
        }
    }

    const a11yGlobalSearchBtn = document.getElementById('a11y-global-search-btn');
    if (a11yGlobalSearchBtn) {
        a11yGlobalSearchBtn.addEventListener('click', () => {
            closePanel();
            openUniversalSearch();
        });
    }

    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            openUniversalSearch();
        } else if (e.key === 'Escape') {
            const modal = document.getElementById('a11y-universal-search-modal');
            if (modal && !modal.classList.contains('hidden')) {
                modal.classList.add('hidden');
            }
        }
    });

    // Exposed so other scripts can access
    window.abhidhammaMettaAudio = {
        play: playMettaAudio,
        pause: pauseMettaAudio,
        stop: stopMettaAudio,
        isPlaying: () => !mettaAudio.paused
    };
    window.openUniversalSearch = openUniversalSearch;
})();


