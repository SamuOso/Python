from validaciones import *

def Actividad1():
    _Numeros=[1,2,3]
    _Acomulador=0
    print("La suma del número:")
    for i in _Numeros:
        print(i)
        _Acomulador += float(i)
    else:
        print(f'da un total de: {_Acomulador}\n')

def Actividad2():
    _Acomulador=0
    _Numeros=[]
    _Lista=["primer","segundo","tercer"]
    for i in _Lista:
        validador=True
        while validador == True:
            numero = input(f'Ingrese el {i} número:\n')
            validacion= [numero,validador] = validarFloat(numero,validador)
        _Numeros.append(numero)
    else:
        for x in _Numeros:
            _Acomulador += x
        else:
            print(f'La suma es de:{_Acomulador}\n')

def Actividad3():
    _Acomulador=0
    _Pasajediario =[]
    for i in range (6):
        validador=True
        while validador == True:
            numero = input(f'ingrese el gasto del dia {i+1}:\n')
            validacion= [numero,validador] = validarFloat(numero,validador)
        _Pasajediario.append(numero)
    else:
        for x in _Pasajediario:
            _Acomulador += x
        else:
            print(f'gastaste un total de: {_Acomulador}')

def Actividad4():
    _preciounitario = 0
    _cantidadventas = 0
    
    validador = True
    while validador == True:
        _preciounitario = input("Ingrese el precio de la unidad: ")
        validacion= [_preciounitario,validador] = validarFloat(_preciounitario,validador)
    validador=True
    while validador == True:
        _cantidadventas = input("Ingrese la cantidad de unidades: ")
        validacion= [_cantidadventas,validador] = validarFloat(_cantidadventas,validador)
    
    total = _cantidadventas*_preciounitario
    print(f'total de la venta: {total}')
    
def Actividad5():
    _costounidad=0
    _precioventa=0
    validador=True
    while validador == True:
        _costounidad = input("ingrese el costo unitario: ")
        validacion = [_costounidad,validador] = validarFloat(_costounidad,validador)
    validador=True
    while validador == True:
        _precioventa = input("ingrese el precio: ")
        validacion = [_precioventa,validador] = validarFloat(_precioventa,validador)
    total = _precioventa-_costounidad
    print(f'La ganancia es de {total}')
    
def Actividad6():
    _valorxhora=0
    _cantidadhoras=0
    _pagoneto=0
    _deduccionesfondo=0
    _otrasdeducciones=0
    _deducciontotal= _deduccionesfondo
    validacion = True
    validacion2 = True
    validador=True
    while validacion == True:
        _validar = input("¿El empleado esta activo?\nIngrese Y si es el caso N, en caso contrario: ")
        if _validar.upper() == "Y":
            validador=True
            while validador == True:
                _valorxhora = input("Ingrese el valor de las horas: ")
                validacion = [_valorxhora,validador] = validarFloat(_valorxhora,validador)
            validador=True
            while validador == True:
                _cantidadhoras= input("Ingrese la cantidad de horas trabajadas: ")
                validacion = [_cantidadhoras,validador] = validarFloat(_cantidadhoras,validador)
            validador=True
            while validador == True:
                _deduccionesfondo= input("ingrese la cantidad de deducciones del fondo: ")
                validacion = [_deduccionesfondo,validador] = validarFloat(_deduccionesfondo,validador) 
            while validacion2 == True:
                _validar = input("¿cuenta con otras deducciones?\nIngrese Y si es el caso N, en caso contrario: ")
                if _validar.upper() == "Y":
                    validador=True
                    while validador == True:
                        _otrasdeducciones= input("ingrese las deducciones: ")
                        validacion = [_otrasdeducciones,validador] = validarFloat(_otrasdeducciones,validador) 
                    _deducciontotal = _otrasdeducciones + _deduccionesfondo
                    _pagoneto=(_valorxhora*_cantidadhoras)-_deducciontotal
                    print(f"El pago del empleado es de: {_pagoneto}")
                    validacion2 = False
                elif _validar.upper() == "N":
                    _pagoneto=(_valorxhora*_cantidadhoras)-_deduccionesfondo
                    print(f"El pago del empleado es de: {_pagoneto}")
                    validacion2 = False
                else:
                    print("ingreso un caracter no valido")
            validacion = False
        elif _validar.upper() == "N":
            validacion = False
            print("No se puede hacer un proceso a un empleado inactivo")
        else:
            print("ingreso un caracter no valido")

def Actividad7():
    _precio=0
    _descuento=0
    validador = True
    while validador == True:
        _precio=input("ingrese el precio del producto: ")
        validacion = [_precio,validador] = validarFloat(_precio,validador)
    validador = True
    while validador == True:
        _descuento=input("ingrese el descuento: ")
        validacion = [_descuento,validador] = validarFloat(_descuento,validador)
    descuento=(_precio*_descuento)/100
    preciocondescuento= _precio-descuento
    print(f"el precio del producto con el descuento es de: {preciocondescuento}")

def Actividad8():
    _saldofinal=0
    _saldomensual=0
    _cantidadcompra=0
    _cantidadesvendidas=0
    _cantidadesdebaja=0
    validador=True
    while validador == True:
        _saldomensual = input("Ingrese el saldo mensual: ")
        validacion = [_saldomensual,validador] = validarFloat(_saldomensual,validador)
    validador=True
    while validador == True:
        _cantidadcompra = input("ingrese la cantidad comprada: ")
        validacion = [_cantidadcompra,validador] = validarFloat(_cantidadcompra,validador)
    validador=True
    while validador == True:    
        _precio = input("Ingrese el precio del producto: ")
        validacion = [_precio,validador] = validarFloat(_precio,validador)
    validador=True
    while validador == True:
        _cantidadesvendidas = input("cantidad vendida: ")
        validacion = [_cantidadesvendidas,validador] = validarFloat(_cantidadesvendidas,validador)
    validador=True
    while validador == True:
        _cantidadesdebaja = input("cantidad descartadas: ")
        validacion = [_cantidadesdebaja,validador] = validarFloat(_cantidadesdebaja,validador)
    totalcomprada = _cantidadcompra * _precio
    total = totalcomprada - (_cantidadesdebaja+_cantidadesvendidas)
    _saldofinal=  _saldomensual - total
    print(f'Saldo final: {_saldofinal} \nunidades restantes:{(_cantidadcompra-(_cantidadesvendidas + _cantidadesdebaja))}')