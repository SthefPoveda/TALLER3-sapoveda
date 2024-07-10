import unittest
from models.perro import Perro

class TestPerro(unittest.TestCase):
    def test_hacer_sonido (self):   
        perro_1 = Perro(nombre="Zeus", raza="Rottweiler", peso=45.8, edad=3, kilos_comidos=8)
        self.assertEqual(perro_1.hacer_sonido(), "¡Guau, guau!")




