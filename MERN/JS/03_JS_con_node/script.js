// Usamos Invoked Function Expression (IIFE) para mantener el código limpio
(function () {
  // Se mostrará un mensaje en la consola cuando el DOM esté completamente cargado
  document.addEventListener("DOMContentLoaded", function () {
    console.info("¡El script se ha cargado correctamente!");
    console.log("¡La página está completamente cargada!");

    // Cambiamos algo en el HTML
    document.body.style.backgroundColor = "lightblue";

    // Y mostramos un mensaje de alerta
    alert("¡Bienvenido a nuestro sitio web!");
  });
})();

button = document.getElementById("prueba");
button.addEventListener("click", function () {
  document.getElementById("prueba").innerHTML = "Prueba yojan";
  alert("¡Has pulsado el botón!");
});

h1 = document.querySelector("h1");
h1.addEventListener("click", function () {
  h1.innerHTML = "Prueba yojan";
  alert("¡Has pulsado el h1!");
});
