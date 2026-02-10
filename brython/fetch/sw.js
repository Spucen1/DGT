// sw.js — školský štandard (PWA + offline)
// Založené na pracovnom liste VERZIA A: install → activate → fetch fileciteturn0file1
//
// DNEŠNÝ CIEĽ (1 hodina): aby fungovalo fetch rozhodovanie + offline fallback.
// Budúci týždeň môžete dotiahnuť update flow (skipWaiting/clients.claim) podľa potreby.

const CACHE_VERSION = "v1.0.0";            // keď meníš precache zoznam, zvýš verziu
const STATIC_CACHE  = `static-${CACHE_VERSION}`;
const OFFLINE_URL   = "./offline.html";

const PRECACHE_ASSETS = [
  "./",
  "./index.html",
  "./style.css",
  "./app.py",           // ak máte Brython appku (inak vymaž)
  "./manifest.json",
  "./sw.js",
  OFFLINE_URL,

  // Voliteľné (ak existujú v projekte):
  // "./icons/icon-192.png",
  // "./icons/icon-512.png",
  // "./brython/brython.min.js",
  // "./brython/brython_stdlib.js",
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(STATIC_CACHE);
    await cache.addAll(PRECACHE_ASSETS);
    // Voliteľne (na budúci týždeň): self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys
        .filter(k => k.startsWith("static-") && k !== STATIC_CACHE)
        .map(k => caches.delete(k))
    );
    // Voliteľne (na budúci týždeň): await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const req = event.request;

  // Pre jednoduchosť riešime len GET
  if (req.method !== "GET") return;

  const url = new URL(req.url);

  // 1) NAVIGÁCIA (HTML): network-first + offline fallback
  if (req.mode === "navigate") {
    event.respondWith((async () => {
      try {
        const resp = await fetch(req);
        // voliteľné: ulož aktuálny index do cache (pomáha pri návrate online)
        const cache = await caches.open(STATIC_CACHE);
        cache.put("./index.html", resp.clone());
        return resp;
      } catch (e) {
        const cache = await caches.open(STATIC_CACHE);
        return (await cache.match(OFFLINE_URL)) || new Response("Offline", { status: 503 });
      }
    })());
    return;
  }

  // 2) ASSETY (CSS/JS/obrázky/py): cache-first (iba rovnaký origin)
  if (url.origin === self.location.origin) {
    event.respondWith((async () => {
      const cache = await caches.open(STATIC_CACHE);
      const cached = await cache.match(req);
      if (cached) return cached;

      try {
        const resp = await fetch(req);
        cache.put(req, resp.clone());
        return resp;
      } catch (e) {
        return new Response("Resource unavailable offline.", { status: 503 });
      }
    })());
  }
});
