import unittest
from models.huron import Huron

huron_1 = Huron(nombre="Jorge", peso=2, edad=4, kilos_comidos=5, pais_origen="Francia", impuestos=4.5)
        
class TestBoa_Huron(unittest.TestCase):
    def test_hacer_sonido (self):   
       self.assertEqual(huron_1.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete (self):
        self.assertEqual(huron_1.calcular_flete(), 9)