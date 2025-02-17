def validarFloat(_paravalidar,validador):
    try:
        datos = float(_paravalidar)
        validador=False
        return datos, validador
    except:
        print("La entrada es incorrecta: escribe un numero entero")
        return _paravalidar, validador