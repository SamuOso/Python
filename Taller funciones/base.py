from funciones import *
def Actividad():
    _catalogo=input("Ingrese un numero para ver la actividad:")
    match _catalogo:
        case "0":
            return False
        case "1":
            print("Actividad 1: Desarrollar una función que reciba tres números y devuelva la suma de ellos.")
            Actividad1()
        case "2":
            print("Actividad 2: Desarrollar una función que reciba tres números ingresados por el cliente y devuelva la suma de ellos.")
            Actividad2()
        case "3":
            print("Actividad 3: Desarrollar una función en Python que recibe los gastos de pasajes de los 6 días de la semana y calcular el total gastado.")
            Actividad3()
        case "4":
            print("Actividad 4: Crear una función que toma el precio unitario, la cantidad vendida y devuelve el total de la venta.")
            Actividad4()
        case "5":
            print("Actividad 5: Crear una función que tome el costo unitario, el precio de venta y devuelve la ganancia obtenida.")
            Actividad5()
        case "6":
            print("Actividad 6: función en Python que calcula el total a pagar de una nómina, dado el valor por hora, la cantidad de horas trabajadas, las deducciones de fondo de empleados, otras deducciones, mientras el empleado esté activo:")
            Actividad6()
        case "7":
            print("Actividad 7: Crear una función que tome el precio original y el porcentaje de descuento y devuelve el precio con descuento.")
            Actividad7()
        case "8":
            print("Actividad 8: Desarrolle una función que calcule el saldo final del inventario teniendo en cuenta esta recibe 4 parámetros y que saldo final inventario= Saldo inicialmes + cantidadesCompradas- cantidades vendidas y cantDadaDeBaja.")
            Actividad8()
        case _:
            print(f"\nERROR: Atributo no reconocido:{_catalogo} \nSolo hay 8 actividades ingrese un numero del 1 al 8 para continuar o 0 para salir")
_apertura = True
print("Taller Python Funciones para resolver\nPara ver la solucion de cada actividad se requiere que ingrese el numero correspondiente a la actividad, en caso de querer salir ingrese 0\n")
while _apertura != False:
    _apertura = Actividad()
else:
    print("Gracias por usar mi programa")