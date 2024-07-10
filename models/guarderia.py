from models.boaConstrictor import Boa_Constrictor

class Guarderia:
    def __init__(self, animales:list, es_boa:bool, ratonescomidos:int):
        self.animales = [animales]
        self.es_boa = es_boa
        self._ratonescomidos = ratonescomidos

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        for animal in self.animales:
            print(animal)
    
    def alimentar_boa(self):
        if self.es_boa == True:
            return Boa_Constrictor.comer_raton(self)
        else:
            return "Esta Boa no existe!"



