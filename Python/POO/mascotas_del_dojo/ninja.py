import mascota

class Ninja(mascota.Mascota):
    def __init__(self, nombre, apellido, mascota, pemio, comida_mascota):
        super().__init__(mascota.nombre, mascota.tipo, mascota.golosinas, mascota.salud, mascota.energia)
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = pemio
        self.comida_mascota = comida_mascota
    

    def caminar(self):
        self.mascota.jugar()
        return self
    
    def alimentar(self):
        self.mascota.comer()
        return self
    
    def bañar(self):
        self.mascota.sonido()
        return self
    

usuario1 = Ninja("Yojan", "Perez", mascota.Mascota("Toby", "perro", 0, 100, 100), "galletas", "croquetas")

print(usuario1.nombre)
print(usuario1.apellido)
print(usuario1.mascota.nombre)
print(usuario1.premio)
print(usuario1.comida_mascota)
print(usuario1.salud)
print(usuario1.energia)
print(usuario1.golosinas)
print(usuario1.tipo)

usuario1.caminar().alimentar().bañar()

