const CACHE_NAME = 'abhidhamma-guide-v1';
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

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).catch(() => caches.match('./index.html'));
    })
  );
});
