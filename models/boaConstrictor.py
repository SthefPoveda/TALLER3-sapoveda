from models.animalExotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre:str, peso:int, edad:int, kilos_comidos:int, pais_origen:str, impuestos:float, ratonescomidos:int):
        super().__init__(nombre, peso, edad, kilos_comidos, pais_origen, impuestos)
        self._ratonescomidos = ratonescomidos

    def hacer_sonido(self):
        return "¡Tsss!"
    
    def contar_ratonescomidos(self):
        if self._ratonescomidos >= 20:
            raise ValueError("Demasiados Ratones!")
        return self._ratonescomidos + 1
    
    def comer_raton(self):
        if self._ratonescomidos >= 20:
            raise ValueError(f"La boa está llena! ratones comidos: {self._ratonescomidos}")
        elif self._ratonescomidos< 20:
            return self._ratonescomidos + 1
        else:
            return "Esta Boa no existe!"
    
    
    
    