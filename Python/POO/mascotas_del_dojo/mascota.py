class Mascota:
    def __init__(self, nombre, tipo, golosinas, salud, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia

    def dormir(self):
        self.energia += 25
        print("durmiendo")
        return self

    def comer(self):
        self.salud += 10
        self.energia += 5
        print("comiendo")
        return self

    def jugar(self):
        self.salud += 5
        print("jugando")
        return self

    def sonido(self):
        if self.tipo == "perro":
            return "guau guau"
        elif self.tipo == "gato":
            return "miau miau"
        elif self.tipo == "canario":
            return "pio pio"
        else:
            return "no se que sonido hace"
