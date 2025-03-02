from CuentaCorriente import CuentaCorriente

cuentas = []

def create():
    nombre = input("Ingrese el nombre del titular: ")
    saldo = float(input("Ingrese el saldo inicial: "))
    nueva_cuenta = CuentaCorriente(nombre, saldo)
    cuentas.append(nueva_cuenta)
    print(f"\nCuenta creada con éxito! Número de cuenta: {nueva_cuenta.numero_cuenta}")

def review():
    numero_cuenta = int(input("Ingrese el número de la cuenta a revisar: "))
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            print(cuenta.get_datos_cuenta())
            return
    print("Cuenta no encontrada.")

def review_balance():
    numero_cuenta = int(input("Ingrese el número de la cuenta a revisar el saldo: "))
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            print(f"Saldo de la cuenta {numero_cuenta}: ${cuenta.get_saldo()}")
            return
    print("Cuenta no encontrada.")

def takeout():
    numero_cuenta = int(input("Ingrese el número de la cuenta desde la cual desea retirar: "))
    cantidad = float(input("Ingrese el monto a retirar: "))
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            cuenta.set_retiro(cantidad)
            return
    print("Cuenta no encontrada.")

def consign():
    numero_cuenta = int(input("Ingrese el número de la cuenta desde la cual desea consignar: "))
    cantidad = float(input("Ingrese el monto a consignar: "))
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            cuenta.set_deposito(cantidad)
            return
    print("Cuenta no encontrada.")

def transfer():
    numero_cuenta_origen = int(input("Ingrese el numero de la cuenta origen: "))
    numero_cuenta_destino = int(input("Ingrese el numero de la cuenta destino: "))
    cantidad = float(input("Ingrese el monto a transferir: "))
    cuenta_origen = None
    cuenta_destino = None
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta_origen:
            cuenta_origen = cuenta
        elif cuenta.numero_cuenta == numero_cuenta_destino:
            cuenta_destino = cuenta
    if cuenta_origen and cuenta_destino:
        CuentaCorriente.transferir(cuenta_origen, cuenta_destino, cantidad)
    else:
        print("Una o ambas cuentas no fueron encontradas.")

sesion = True
while sesion:
    print("\nMenu de opciones:\n1. Crear cuenta\n2. Ver cuenta\n3. Ver saldo\n4. Retirar dinero\n5. Consignar dinero\n6. Transferir dinero\n7. Salir")
    
    opcion = int(input("\nIngrese una opcion: "))
    
    if opcion == 1:
        create()
    elif opcion == 2:
        review()
    elif opcion == 3:
        review_balance()
    elif opcion == 4:
        takeout()
    elif opcion == 5:
        consign()
    elif opcion == 6:
        transfer()
    elif opcion == 7:
        print("Gracias por usar el sistema.")
        sesion = False
    else:
        print("Opcion no valida. Por favor, intente nuevamente.")
