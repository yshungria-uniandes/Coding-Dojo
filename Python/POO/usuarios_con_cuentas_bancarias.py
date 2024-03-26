class CuentaBancaria:
    cantidad_cuentas = 0
    def __init__(self, balance=0, tasa_interes=0.01):
        self.balance = balance
        self.tasa_interes = tasa_interes
        CuentaBancaria.cantidad_cuentas += 1
    
    def depositar(self, cantidad):
        self.balance += cantidad
        return self
    
    def retirar(self, cantidad):
        self.balance -= cantidad
        return self

    def mostrar_info_cuenta(self):
        print(f'Saldo: {self.balance}')
        return self
    
    def calcular_interes(self):
        self.balance += self.balance * self.tasa_interes
        return self
    
    @classmethod
    def mostrar_cantidad_cuentas(cls):
        print(f'Cantidad de cuentas: {cls.cantidad_cuentas}')
    
    @staticmethod
    def calcular_interes_estatico(balance, tasa_interes):
        return balance * tasa_interes
    
# class Usuario:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
#         self.cuenta = CuentaBancaria( balance=0, tasa_interes=0.02 )

#     def hacer_deposito(self, cantidad):
#         self.cuenta.depositar(cantidad)
#         print(f'{self.nombre} ha depositado {cantidad} pesos')
#         print(f'Saldo actual: {self.cuenta.balance}')

#     def hacer_retiro(self, cantidad):
#         if cantidad > self.cuenta.balance:
#             print(f'Saldo insuficiente')
#         else:
#             self.cuenta.retirar(cantidad)
#             print(f'{self.nombre} ha retirado {cantidad} pesos')
#             print(f'Saldo actual: {self.cuenta.balance}')
    
#     def mostrar_balance_usuario(self):
#         print(f'El saldo actual de {self.nombre} es de {self.cuenta.balance} pesos')

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuentas = [CuentaBancaria( balance=0, tasa_interes=0.02 )]

    def hacer_deposito(self, cuenta, cantidad):
        self.cuentas[cuenta].depositar(cantidad)
        print(f'{self.nombre} ha depositado {cantidad} pesos')
        print(f'Saldo actual: {self.cuentas[cuenta].balance}')
        return self

    def hacer_retiro(self, cuenta, cantidad):
        if cantidad > self.cuentas[cuenta].balance:
            print(f'Saldo insuficiente')
        else:
            self.cuentas[cuenta].retirar(cantidad)
            print(f'{self.nombre} ha retirado {cantidad} pesos')
            print(f'Saldo actual: {self.cuentas[cuenta].balance}')
        return self
    
    def mostrar_balance_usuario(self, cuenta):
        print(f'El saldo actual de {self.nombre} es de {self.cuentas[cuenta].balance} pesos')
        return self
    
    def transferencia(self, usuario, cantidad):
        if cantidad > self.cuentas[0].balance:
            print(f'Saldo insuficiente')
        else:
            self.cuentas[0].retirar(cantidad)
            usuario.cuentas[0].depositar(cantidad)
            print(f'{self.nombre} ha transferido {cantidad} pesos a {usuario.nombre}')
            print(f'Saldo actual de {self.nombre}: {self.cuentas[0].balance}')
            print(f'Saldo actual de {usuario.nombre}: {usuario.cuentas[0].balance}')
        return self

    def ver_cuentas(self):
        print(f'Áquí tienes el listados de cuentas de {self.nombre}')
        for i in range(len(self.cuentas)):
            print(f'Cuenta {i+1}: Saldo: {self.cuentas[i].balance}')
        


yojan = Usuario('Yojan', 'yshungriaœgmail.com')
yojan.hacer_deposito(0, 100).hacer_deposito(0, 200).hacer_deposito(0, 300).hacer_retiro(0, 50).mostrar_balance_usuario(0)

CuentaBancaria.mostrar_cantidad_cuentas()
print(CuentaBancaria.calcular_interes_estatico(1000, 0.05))


yojan.ver_cuentas()

