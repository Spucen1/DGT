if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js")
      .then((registration) => {
        console.log("Service worker je zaregistrovaný:", registration.scope);
      })
      .catch((error) => {
        console.error("Registrácia service workera zlyhala:", error);
      });
  });
}
