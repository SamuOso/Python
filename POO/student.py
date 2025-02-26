from person import *

class students(Person):
    def __init__ (self,nombre,edad,grado):
        super().__init__(nombre,edad,grado)
        self.grado = grado
    
