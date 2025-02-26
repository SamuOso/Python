from person import *

class AccesoPersona:
    def show_info_person(self, Person):
        print(f'Nombre: {Person.GetterName()}.\nEdad: {Person.GetterEdad()} años.')

if __name__ == "__main__":
    persona1 = Person("Samuel",20)
    acceso = AccesoPersona()
    acceso.show_info_person(persona1)