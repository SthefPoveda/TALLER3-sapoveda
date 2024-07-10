from models.animal import Animal

class Perro(Animal):
    def __init__(self, nombre:str, raza:str, peso:float, edad:int, kilos_comidos:int):
        super().__init__(nombre, peso, edad, kilos_comidos)
        self.raza   = raza

    def hacer_sonido(self):
        return "¡Guau, guau!"
    
    def modificar_peso(self, nuevo_peso):
        self._peso = nuevo_peso

    def obtener_raza(self):
        return self.raza

