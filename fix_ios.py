import re

with open('accessibility.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace playMettaAudio
old_play = """    function playMettaAudio() {
        mettaAudio.play().then(() => {
            updateAudioUI(true);
            saveAudioState(true);
        }).catch(() => {
            // Autoplay blocked by the browser — wait for a user gesture to resume
            updateAudioUI(false);
        });
    }"""

new_play = """    function playMettaAudio(isInitialResume = false) {
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
    }"""

content = content.replace(old_play, new_play)

# 2. Replace init block
old_init = """    // Resume playback (and position) left over from the previous page
    const initialAudioState = getAudioState();
    if (initialAudioState.playing) {
        // Change preload to metadata so Safari allows seeking
        mettaAudio.preload = "metadata";
        
        // Wait for loadedmetadata to set currentTime reliably on Safari
        const setTimeHandler = () => {
            mettaAudio.currentTime = initialAudioState.time || 0;
        };
        
        if (mettaAudio.readyState >= 1) { // HAVE_METADATA
            mettaAudio.currentTime = initialAudioState.time || 0;
        } else {
            mettaAudio.addEventListener('loadedmetadata', setTimeHandler, { once: true });
        }

        playMettaAudio();

        // If the browser blocked autoplay, resume on the first user interaction with the new page
        const resumeOnInteraction = () => {
            if (mettaAudio.paused && getAudioState().playing) {
                // Ensure time is set correctly again before playing just in case
                if (mettaAudio.readyState >= 1) {
                    mettaAudio.currentTime = initialAudioState.time || 0;
                } else {
                    mettaAudio.addEventListener('loadedmetadata', () => {
                        mettaAudio.currentTime = initialAudioState.time || 0;
                    }, { once: true });
                }
                mettaAudio.play().then(() => updateAudioUI(true)).catch(() => {});
            }
        };
        document.addEventListener('click', resumeOnInteraction, { once: true });
        document.addEventListener('touchstart', resumeOnInteraction, { once: true });
    }"""

new_init = """    // Resume playback (and position) left over from the previous page
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
    }"""

content = content.replace(old_init, new_init)

with open('accessibility.js', 'w', encoding='utf-8') as f:
    f.write(content)

