from models.animalExotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre:str, peso:int, edad:int, kilos_comidos:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, kilos_comidos, pais_origen, impuestos)

    def hacer_sonido(self):
        return "¡Eek Eek!"
    