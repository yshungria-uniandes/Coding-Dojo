// const superheroe = {
//     nombre: 'Wonder Woman',
//     alias: 'Diana Prince',
//     poderes: ['super fuerza', 'velocidad', 'durabilidad'],
//     habilidades: ['combate cuerpo a cuerpo', 'uso del lazo mágico', 'vuelo'],
//     creadaPor: 'William Moulton Marston',
//     primeraAparicion: 'All Star Comics #8 (1941)',
//     codigoSecreto: '12345' // ¿Muy fácil el código de nuestra super amiga, no crees?
// };

// const armas = ['Espada de Athena', 'Escudo', 'Lazo de la Verdad', 'Brazaletes indestructibles'];
// const codigoSecreto = 'ABCDE'; // Acá está el conflicto

// const { nombre, alias, poderes, habilidades, creadaPor, primeraAparicion, codigoSecreto: codigoEncriptado } = superheroe; // Acá corregimos el conflicto

// console.log(codigoEncriptado) // Salida: 12345

// const alterego = {
//   nombre: "Diana",
//   apellido: "Prince",
//   email: "diana.prince@themyscira.com",
//   contraseña: "Am@z0nW@rri0r",
//   usuario: "wonderwoman",
//   direcciones: [
//     {
//       direccion: "Themyscira Palace",
//       ciudad: "Themyscira",
//       codigoPostal: "0001",
//     },
//     {
//       direccion: "7000 Hollywood Blvd",
//       ciudad: "Los Angeles",
//       codigoPostal: "90028",
//     },
//   ],
//   creadoEn: 1714866113353,
// };
// // const { direcciones } = alterego;
// // const [primeraDireccion, segundaDireccion] = direcciones;

// // console.log(primeraDireccion);
// // console.log(segundaDireccion);

// const { direcciones } = alterego;
// const [, segundaDireccion] = direcciones;

// console.log("Segunda Dirección:", segundaDireccion);

let cantidad = 10;

const manejarCantidad = [
  // Índice 0; Una Función Getter
  function () {
    console.log("Cantidad actual: " + cantidad);
    return cantidad;
  },
  // Índice 1; Una Función Setter
  function (nuevaCantidad) {
    console.log("Cantidad actualizada: " + nuevaCantidad);
    cantidad = nuevaCantidad;
    return cantidad;
  },
];

// Acá desestructuramos getter (getCantidad) y setter (setCantidad)
const [getCantidad, setCantidad] = manejarCantidad;

getCantidad(); // Salida: Cantidad actual: 10
setCantidad(20); // Salida: Cantidad actualizada: 20
getCantidad(); // Salida: Cantidad actual: 20
