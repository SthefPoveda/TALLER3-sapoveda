import unittest
from models.boaConstrictor import Boa_Constrictor
from models.guarderia import Guarderia

boa_1 = Boa_Constrictor(nombre="Jen", peso=60, edad=2, kilos_comidos=38, pais_origen="Brasil", impuestos=4.7, ratonescomidos=8)
boas_2 = Guarderia(animales=["Boa1", "Boa2"], es_boa=True, ratonescomidos=90)

class TestBoa_Constrictor(unittest.TestCase):
    def test_hacer_sonido (self):   
        self.assertEqual(boa_1.hacer_sonido(), "¡Tsss!")
    
    def test_calcular_flete (self):
        self.assertEqual(boa_1.calcular_flete(), 282)

    def test_contar_ratonescomidos(self):
        try: 
            resultado = boa_1.contar_ratonescomidos()
            print(f"Cantidad de ratones comidos: {resultado}")
        except ValueError as e:
            print(f"Error al realizar la operación: {e}")
    
    def test_alimentar_boa(self):
        try:
            comer_ratones= boas_2.alimentar_boa()
            print(f"Cantidad de ratones comidos: {comer_ratones}")
        except ValueError as i:
            print(f"Error al realizar la operación: {i}")