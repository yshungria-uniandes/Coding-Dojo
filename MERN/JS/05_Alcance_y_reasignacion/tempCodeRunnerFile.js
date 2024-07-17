// Variable global para contar las visitas
let visitas = 0;

// Función para mostrar el número de visitas
function mostrarVisitas() {
  console.log(`Número de visitas: ${visitas}`);
}

// Función para registrar una nueva visita
function nuevaVisita() {
  visitas++;
}

// Simulación de visitas
nuevaVisita(); // Se registra una nueva visita
mostrarVisitas(); // Contar visitas registradas
