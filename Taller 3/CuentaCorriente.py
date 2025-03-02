import random

class CuentaCorriente:
    def __init__(self, nombre_titular, saldo):
        self.nombre_titular = nombre_titular
        self.saldo = float(saldo)
        self.numero_cuenta = random.randint(1000000000, 9999999999)
    
    def get_saldo(self):
        return self.saldo
    def get_datos_cuenta(self):
        return f"Titular: {self.nombre_titular}, #cuenta: {self.numero_cuenta}, Saldo: ${self.saldo}"

    def set_deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingreso de ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Cantidad invalida para deposito.")
    def set_retiro(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Egreso de ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente o cantidad inválida para retiro.")
    
    @staticmethod
    def transferir(cuenta_origen, cuenta_destino, cantidad):
        if cuenta_origen.get_saldo() >= cantidad:
            cuenta_origen.set_retiro(cantidad)
            cuenta_destino.set_deposito(cantidad)
            print(f"Transferencia exitosa de ${cantidad} de la cuenta {cuenta_origen.numero_cuenta} a la cuenta {cuenta_destino.numero_cuenta}.")
        else:
            print(f"Transferencia fallida. La cuenta {cuenta_origen.numero_cuenta} no tiene saldo suficiente para transferir ${cantidad}.")