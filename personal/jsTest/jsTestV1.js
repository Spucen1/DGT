console.log("Výpočet obsahu obdĺžnika");
let button = document.getElementById("button");
button.addEventListener("click", function () {
  let a = parseFloat(document.getElementById("a").value);
  let b = parseFloat(document.getElementById("b").value);
  let obsah = a * b;
  button.innerText = obsah;
});