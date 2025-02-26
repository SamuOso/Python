import random

class cuentacorriente:
    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.Ncuenta = random.randrange(0,999999999)
    def set_ingreso(self, num):
        self.saldo =+ num
    def set_retiro(self, num):
        self.saldo =- num
    def get_saldo(self):
        return print(f"Su saldo es de: {self.saldo}")
    def get_datos_cuenta(self):
        return print(f"# de cuenta: {self.Ncuenta}\nNombre: {self.nombre}\n{self.get_saldo}")
    @staticmethod
    def transferencia(self,dinero):
        self.saldo =+ dinero
        

