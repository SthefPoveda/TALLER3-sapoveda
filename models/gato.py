from models.animal import Animal

class Gato(Animal):
    def __init__(self, nombre:str, peso:float, edad:int, color:str, kilos_comidos:int):
        super().__init__(nombre, peso, edad, kilos_comidos)
        self.color   = color

    def hacer_sonido(self):
        return "¡Miau, miau!"
    
    def obtener_color(self):
        return self.color
