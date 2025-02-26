from CuentaCorriente import cuentacorriente

def create():
    for i in range(cuenta):
        nombre = (input(f"\nIngrese el nombre de la cuenta #{i+1}: "))
        saldo = (input(f"\nIngrese el saldo de la cuenta #{i+1}: "))
        cuenta.append(cuentacorriente(nombre,saldo))

def review():
    buscador = input("Ingrese el numero de la cuenta")
    for i in cuenta:
        if i == buscador:
            cuenta[i].get_datos_cuenta()

sesion= True
cuenta = []
while sesion:
    buscador = int(input("Ingrese 1 para crear\nIngrese 2 para ver la cuenta\nIngrese 3 para ver su saldo\nIngrese 4 para retirar\nIngrese 5 para consignar\nIngrese 6 para tansferir"))
