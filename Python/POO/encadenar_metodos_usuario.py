class Usuario:
    def __init__(self, nombre, edad, cuenta=0):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = cuenta

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años y deseo hacer un deposito')

    def hacer_deposito(self, cantidad):
        self.cuenta += cantidad
        print(f'{self.nombre} ha depositado {cantidad} pesos')
        print(f'Saldo actual: {self.cuenta}')
        return self
    
    def hacer_retiro(self, cantidad):
        if cantidad > self.cuenta:
            print(f'Saldo insuficiente')
        else:
            self.cuenta -= cantidad
            print(f'{self.nombre} ha retirado {cantidad} pesos')
            print(f'Saldo actual: {self.cuenta}')
        return self

    def mostrar_balance_usuario(self):
        print(f'El saldo actual de {self.nombre} es de {self.cuenta} pesos')
        return self
    
    def transferencia(self, usuario, cantidad):
        if cantidad > self.cuenta:
            print(f'Saldo insuficiente')
        else:
            self.cuenta -= cantidad
            usuario.cuenta += cantidad
            print(f'{self.nombre} ha transferido {cantidad} pesos a {usuario.nombre}')
            print(f'Saldo actual de {self.nombre}: {self.cuenta}')
            print(f'Saldo actual de {usuario.nombre}: {usuario.cuenta}')
        return self


yojan = Usuario('Yojan', 25)
carlos = Usuario('Carlos', 30)
lina = Usuario('Lina', 28)

yojan.hacer_deposito(100).hacer_deposito(200).hacer_deposito(300).hacer_retiro(50).mostrar_balance_usuario()

carlos.hacer_deposito(100).hacer_deposito(200).hacer_retiro(50).hacer_retiro(100).mostrar_balance_usuario()

lina.hacer_deposito(100).hacer_retiro(50).hacer_retiro(100).hacer_retiro(200).mostrar_balance_usuario()

yojan.transferencia(lina, 50).mostrar_balance_usuario()

lina.mostrar_balance_usuario()