from models.ianimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre:str, peso:int, edad:int, kilos_comidos:int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 40

    def comer(self, kilos):
        self._kilos_comidos+=kilos

    def obtener_kilos_comidos (self):
        return self._nombre + " " + str(self._kilos_comidos)

    def obtener_nombre(self):
        return self._nombre
    
    def obtener_peso(self):
        return self._peso
        
    def obtener_edad(self):
        return self._edad
    