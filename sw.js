const CACHE_NAME = 'abhidhamma-guide-v5';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './citta_cetasikas_visual_guide.html',
  './concept_map.html',
  './vithi_sangaha.html',
  './vithimutta_sangaha.html',
  './rupa_sangaha.html',
  './kilesa_sangaha.html',
  './bodhipakkhiya_dhamma.html',
  './sabba_sangaha.html',
  './paccaya_sangaha.html',
  './paticcasamuppada.html',
  './kammatthana_sangaha.html',
  './missaka_sangaha.html',
  './pakinnaka_sangaha.html',
  './pannatti.html',
  './glossary.html',
  './library.html',
  './emotion_analyzer.html',
  './meditation_timer.html',
  './anapana_counter.html',
  './anapana_visualizer.html',
  './kasina_guide.html',
  './kasina_simulator.html',
  './metta_bhavana_guide.html',
  './metta_prompter.html',
  './satipatthana_guide.html',
  './satipatthana_prompter.html',
  './404.html',
  './output.css',
  './accessibility.js',
  './firebase_tracker.js',
  './manifest.json',
  './assets/images/icon-192.png',
  './assets/images/icon-512.png',
  './assets/images/apple-touch-icon.png',
  './assets/mp3/Metta.mp3'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Cache each asset individually so one missing/404 file can't abort the
      // whole install (cache.addAll rejects atomically if any single request fails).
      return Promise.all(
        ASSETS_TO_CACHE.map((url) =>
          cache.add(url).catch((err) => console.warn('SW: skip caching', url, err))
        )
      );
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Network-first: always try to fetch the latest version and refresh the cache with it,
// only falling back to whatever's cached when the network request genuinely fails (offline).
// The previous cache-first strategy served stale HTML forever once a page was cached once,
// since nothing ever re-checked the network unless the cache had no entry at all.
self.addEventListener('fetch', (event) => {
  const request = event.request;

  // cache.put throws on non-GET requests (e.g. the Firebase tracker's POSTs),
  // so leave anything that isn't a GET entirely alone.
  if (request.method !== 'GET') {
    return;
  }

  const isSameOrigin = new URL(request.url).origin === self.location.origin;

  if (isSameOrigin) {
    // Same-origin (our HTML/CSS/JS): network-first so users always get the
    // latest deploy, falling back to cache (or index.html) when offline.
    event.respondWith(
      fetch(request)
        .then((response) => {
          if (response && response.ok && response.type === 'basic') {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          }
          return response;
        })
        .catch(() => caches.match(request).then((cached) => cached || caches.match('./index.html')))
    );
    return;
  }

  // Cross-origin (CDN fonts / Font Awesome / Google Fonts): cache-first so the
  // page still renders with its fonts and icons while offline. These come back
  // as opaque responses (status 0), so we can't check response.ok — just cache
  // whatever we successfully fetched.
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;
      return fetch(request).then((response) => {
        if (response) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone).catch(() => {}));
        }
        return response;
      });
    })
  );
});
