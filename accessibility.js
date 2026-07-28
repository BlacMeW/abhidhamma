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
                
                <div class="space-y-4">
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
                            <button id="a11y-audio-playpause" class="flex-1 py-1.5 rounded-md text-sm font-medium flex items-center justify-center gap-2 transition-colors bg-white dark:bg-slate-700 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-600">
                                <i class="fa-solid fa-play" id="a11y-audio-icon"></i> <span id="a11y-audio-label">ဖွင့်မည်</span>
                            </button>
                            <button id="a11y-audio-stop" class="w-10 h-8 rounded-md bg-white dark:bg-slate-800 text-rose-500 shadow-sm border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition" aria-label="Stop background audio" title="ရပ်မည်">
                                <i class="fa-solid fa-stop"></i>
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

    function playMettaAudio() {
        mettaAudio.play().then(() => {
            updateAudioUI(true);
            saveAudioState(true);
        }).catch(() => {
            // Autoplay blocked by the browser — wait for a user gesture to resume
            updateAudioUI(false);
        });
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
    }

    audioPlayPauseBtn.addEventListener('click', () => {
        if (mettaAudio.paused) {
            playMettaAudio();
        } else {
            pauseMettaAudio();
        }
    });

    audioStopBtn.addEventListener('click', stopMettaAudio);

    mettaAudio.addEventListener('timeupdate', () => {
        if (!mettaAudio.paused) saveAudioState(true);
    });

    window.addEventListener('pagehide', () => {
        if (!mettaAudio.paused) saveAudioState(true);
    });

    // Resume playback (and position) left over from the previous page
    const initialAudioState = getAudioState();
    if (initialAudioState.playing) {
        mettaAudio.currentTime = initialAudioState.time || 0;
        playMettaAudio();

        // If the browser blocked autoplay, resume on the first user interaction with the new page
        const resumeOnInteraction = () => {
            if (mettaAudio.paused && getAudioState().playing) {
                mettaAudio.play().then(() => updateAudioUI(true)).catch(() => {});
            }
        };
        document.addEventListener('click', resumeOnInteraction, { once: true });
        document.addEventListener('touchstart', resumeOnInteraction, { once: true });
    }

    // Exposed so other page scripts (e.g. metta_prompter.html's own guided timer) can
    // pause this background player instead of overlapping it with their own audio.
    window.abhidhammaMettaAudio = {
        play: playMettaAudio,
        pause: pauseMettaAudio,
        stop: stopMettaAudio,
        isPlaying: () => !mettaAudio.paused
    };
})();

