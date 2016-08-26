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

    def setUp(self):
        self.edificio= Edificio()
        self.bus = Bus()

    def test_accede_trabajador_horario_normal(self):
        trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
        assert self.edificio.conceder_acceso(trabajador,5,0) == 0b1

    def test_accede_trabajador_fin_semana(self):
        trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
        assert self.edificio.conceder_acceso(trabajador,6,15) == 0b1

    def test_trabajador_no_accede(self):
        trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
        assert self.edificio.conceder_acceso(trabajador,6,16) == 0b0

    def test_accede_estudiante(self):
        estudiante = Tarjeta("Manuel","Torres","1112345",1)
        assert self.edificio.conceder_acceso(estudiante,5,18)==0b1

    def test_estudiante_no_accede(self):
        estudiante = Tarjeta("Manuel","Torres","1112345",1)
        assert self.edificio.conceder_acceso(estudiante,5,19)==0b0

    def test_tarjeta_invalida(self):
        tarjeta = Tarjeta("Manuel","Torres","11123a5",1)
        assert self.edificio.conceder_acceso(tarjeta,5,19)==0b0

    def test_tarjeta_none(self):
        assert self.edificio.conceder_acceso(None,5,19) == 0b0

if __name__ == '__main__':
    unittest.main()
