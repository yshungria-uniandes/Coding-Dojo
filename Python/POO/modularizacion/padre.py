
local_val = "unicornios mágicos"

def square(x):
    return x * x


class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"

# en el mismo archivo, agrega lo siguiente debajo de la clase Usuario
# print(square(5))
# usuario = Usuario("Anna")
# print(usuario.name)
# print(usuario.di_hola())

# print(__name__)
    
if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)
  

#   ¿Cómo es esto útil? Podemos usar esta condicional para evitar que se ejecuten bloques de código a menos que el archivo se esté ejecutando directamente. ¿Por qué querríamos hacer esto? Considera una situación en la que una clase depende de otra, como en la asignación de Usuarios con Cuentas bancarias. En nuestro documento de producto, podríamos crear una gran cantidad de código de prueba para asegurarnos de que podemos crear nuevos productos y ejecutar métodos. Cuando importamos productos al archivo de tienda como un módulo, no queremos que todas esas pruebas se ejecuten cada vez que ejecutamos el archivo tienda, por lo que dentro de nuestro documento de producto, es posible que tengamos algo como a continuación:

# if __name__ == "__main__":
#     producto = Producto([args])
#     print(producto)
#     print(producto.agregar_impuesto(0.18))

