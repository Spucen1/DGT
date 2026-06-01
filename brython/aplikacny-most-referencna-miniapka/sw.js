const CACHE_VERSION = "v4.2.0";
const STATIC_CACHE = `aplikacny-most-static-${CACHE_VERSION}`;
const OFFLINE_URL = "./offline.html";

const PRECACHE_ASSETS = [
  "./",
  "./index.html",
  "./normalize.css",
  "./style.css",
  "./app.py",
  "./manifest.json",
  "./navigator.js",
  "./sw.js",
  "./offline.html",
  "./brython.min.js",
  "./brython_stdlib.js",
  "./android-chrome-192x192.png",
  "./android-chrome-512x512.png",
  "./apple-touch-icon.png",
  "./favicon.ico",
  "./favicon-16x16.png",
  "./favicon-32x32.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(STATIC_CACHE);
    await cache.addAll(PRECACHE_ASSETS);
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys
        .filter((key) => key.startsWith("aplikacny-most-static-") && key !== STATIC_CACHE)
        .map((key) => caches.delete(key))
    );
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") {
    return;
  }

  const url = new URL(request.url);

  if (request.mode === "navigate") {
    event.respondWith((async () => {
      const cache = await caches.open(STATIC_CACHE);
      try {
        const response = await fetch(request);
        if (response && response.ok) {
          cache.put("./index.html", response.clone());
        }
        return response;
      } catch (error) {
        return (
          (await cache.match(request)) ||
          (await cache.match("./")) ||
          (await cache.match("./index.html")) ||
          (await cache.match(OFFLINE_URL)) ||
          new Response("Aplikácia nie je dostupná offline.", { status: 503 })
        );
      }
    })());
    return;
  }

  if (url.origin === self.location.origin) {
    event.respondWith((async () => {
      const cache = await caches.open(STATIC_CACHE);
      const cached = await cache.match(request);
      if (cached) {
        return cached;
      }

      try {
        const response = await fetch(request);
        if (response && response.ok) {
          cache.put(request, response.clone());
        }
        return response;
      } catch (error) {
        return new Response("Súbor nie je dostupný offline.", { status: 503 });
      }
    })());
  }
});
