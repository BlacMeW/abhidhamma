const CACHE_NAME = 'abhidhamma-guide-v3';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './matika.html',
  './citta_cetasikas_visual_guide.html',
  './rupa_sangaha.html',
  './vithimutta_sangaha.html',
  './kilesa_sangaha.html',
  './bodhipakkhiya_dhamma.html',
  './sabba_sangaha.html',
  './paccaya_sangaha.html',
  './paticcasamuppada.html',
  './kammatthana_sangaha.html',
  './manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
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
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        return response;
      })
      .catch(() => caches.match(event.request).then((cached) => cached || caches.match('./index.html')))
  );
});
