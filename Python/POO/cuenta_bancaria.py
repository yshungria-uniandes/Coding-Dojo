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


cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria(1000, 0.05)

cuenta1.depositar(100).depositar(200).depositar(300).retirar(50).calcular_interes().mostrar_info_cuenta()
cuenta2.depositar(100).depositar(200).retirar(50).retirar(50).retirar(50).retirar(50).calcular_interes().mostrar_info_cuenta()

CuentaBancaria.mostrar_cantidad_cuentas()
print(CuentaBancaria.calcular_interes_estatico(1000, 0.05))