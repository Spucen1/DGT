const CACHE_VERSION = "v3";
const CACHE_NAME = `app-shell-${CACHE_VERSION}`;

const PRECACHE_ASSETS = ["/", "index.html", "offline.html", "style.css"];

self.addEventListener("install", (event) => {
    event.waitUntil(
        cacheSignal.open(CACHE_NAME).then((cache) => {
            return cache.addAll(PRECACHE_ASSETS);
        }),
    );
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) return caches.delete(key);
                }),
            );
        }),
    );
});

self.addEventListener("fetch", (event) => {
    if (event.request.mode === "navigate") {
        event.respondWith(fetch(event.request).catch(() => caches.match("offline.html")));
        return;
    }

    event.respondWith(
        caches.match(event.request).then((cached) => {
            return cached || fetch(event.request);
        }),
    );
});
