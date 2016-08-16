import unittest
from programa import *


class ProgramaTest(unittest.TestCase):
    def test_function_1(self):
        tarjeta = Tarjeta("AAA", "AAA", "0012345", 1.0)

        valor1 = Bus.cobrar_pasaje(tarjeta, 5)
        valor2 = 0b1
        self.assertEqual(valor1, valor2)

    def test_function_2(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 1.0)
        valor1 = Bus.cobrar_pasaje(tarjeta, 2)
        valor2 = 0b1
        self.assertEqual(valor1, valor2)

    def test_function_3(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 'a')
        valor1 = Bus.cobrar_pasaje(tarjeta, 2)
        valor2 = 0b0
        self.assertEqual(valor1, valor2)

    def test_function_4(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 0)
        valor1 = Bus.cobrar_pasaje(tarjeta, 2)
        valor2 = 0b0
        self.assertEqual(valor1, valor2)

    def test_function_5(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 0)
        valor1 = Bus.cobrar_pasaje(tarjeta, 5)
        valor2 = 0b1
        self.assertEqual(valor1, valor2)

    def test_function_6(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 1)
        valor1 = Bus.cobrar_pasaje(tarjeta, 6)
        valor2 = 0b0
        self.assertEqual(valor1, valor2)

    def test_function_7(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 1)
        valor1 = Bus.cobrar_pasaje(tarjeta, 'a')
        valor2 = 0b0
        self.assertEqual(valor1, valor2)

    def test_function_8(self):
        tarjeta = Tarjeta("AAA", "AAA", "2212345", 1)
        valor1 = Bus.cobrar_pasaje(tarjeta, 'a')
        valor2 = 0b0
    def test_function_9(self):

    def test_function_10(self):

    def test_function_11(self):

    def test_function_12(self):
    #Pruebas para las funcionalidades de la biblioteca
    def test_biblio_1(self):
        tarjeta =