from models.perro import Perro
from models.gato import Gato
from models.huron import Huron
from models.boaConstrictor import Boa_Constrictor


perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3, 8)
perro_2 = Perro("Nala", "Golden R.", 8.5, 0, 9)
perro_3 = Perro("Atila", "Alabai", 58.9, 5, 7)

print(perro_3.obtener_edad())
print(perro_1.obtener_nombre())
print(perro_2.obtener_kilos_comidos())
print(perro_2.hacer_sonido())

gato_1 = Gato("Mishi", 7, 4, "Negro", 7)
print(gato_1.hacer_sonido())
print(gato_1.obtener_color())

huron_1 = Huron("Jorge", 2, 4, 5, "Francia", 4.5)
print(huron_1.hacer_sonido())

boa_1 = Boa_Constrictor("Jen", 60, 2, 38, "Brasil", 4.7, 7)
print(boa_1.contar_ratonescomidos())

print(boa_1.calcular_flete())
