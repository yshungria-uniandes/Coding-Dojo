// // Variable ES5
// var saludo = "Hola";

// // Función ES5
// function saludar(nombre) {
//   console.log(saludo + ", " + nombre + "!");
// }

// // Ejecución:
// saludar("Pianola");

// Literal de objeto ES5
// var ironMan = {
//   nombre: "Tony",
//   apellido: "Stark",
//   edad: 50,
// };

// // Asignación de propiedades de literales de objeto a variables en ES5
// var nombre = ironMan.nombre;
// var apellido = ironMan.apellido;
// var edad = ironMan.edad;

// // Mostrando propiedades de literales de objeto en ES5
// console.log(nombre, apellido, edad);

// // Variable ES6
// const saludo = "Hola";

// // Función ES6
// const saludarMundo = (a) => {
//   console.log(`${saludo} ${a}`);
// };

// // Para ejecutar:
// saludarMundo("Pianola!");
// // Literal de objeto ES6
// const tonyStark = {
//   nombre: "Tony",
//   apellido: "Stark",
//   edad: 50,
// };

// // ES6 Asignando propiedades de literales de objeto a variables
// const { nombre, apellido, edad } = tonyStark;

// // ES6 Mostrando propiedades de literales de objeto
// console.log(nombre, apellido, edad);

// const jugador = {
//   nombre: "Lionel Messi",
//   equipo: "Paris Saint-Germain",
//   posicion: "Delantero",
// };

// console.log(jugador);
// console.log(jugador.nombre); // Devuelve "Lionel Messi"

// Al desestructurar, se vería de esta manera:

// const jugador = {
//     nombre: "Lionel Messi",
//     equipo: "Paris Saint-Germain",
//     posicion: "Delantero"
// };

// const { nombre, equipo, posicion } = jugador;
// console.log(nombre); // Devuelve "Lionel Messi"
// console.log(equipo); // Devuelve "Paris Saint-Germain"
// console.log(posicion); // Devuelve "Delantero"

// Veamos otro ejemplo:

// // Sin desestructurar
// const auto = {
//     marca: "Toyota",
//     modelo: "Corolla",
//     año: 2022
// };

// console.log(auto.marca); // "Toyota"
// console.log(auto.modelo); // "Corolla"
// console.log(auto.año); // 2022

// // Desestructurando
// const auto = {
//     marca: "Toyota",
//     modelo: "Corolla",
//     año: 2022
// };

// const { marca, modelo, año } = auto;

// console.log(marca); // "Toyota"
// console.log(modelo); // "Corolla"
// console.log(año); // 2022
