class Person:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def GetterEdad(self):
        return self.__edad
    def GetterName(self):
        return self.__nombre