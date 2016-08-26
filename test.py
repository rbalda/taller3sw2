import unittest
from programa import Tarjeta
from programa import Biblioteca
from programa import Libro
from programa import Bus
from programa import Edificio

class pruebas(unittest.TestCase):
    """ Todos los datos correctos, Libro tiene categoria CN,
          la fecha tiene que sumarse 14 dias """

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

    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "0034567", 10)
        libro = Libro("","CN",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = "Fecha límite: 30/08/2016"
        self.assertEqual(valor1, valor2)

    """ Todos los datos correctos, Libro tiene categoria CE,
          la fecha tiene que sumarse 7 dias """
    def test_function_2(self):
        tarjeta = Tarjeta("AA", "BB", "1234567", 10)
        libro = Libro("","CE",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = "Fecha límite: 23/08/2016"
        self.assertEqual(valor1, valor2)

    """ Tarjeta inválida, retorna 0"""
    def test_function_3(self):
        tarjeta = Tarjeta("AA", "BB", "003456", 10)
        libro = Libro("","CE",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

    """ Categoŕía del libro inválida, retorna 0"""
    def test_function_4(self):
        tarjeta = Tarjeta("AA", "BB", "003456", 10)
        libro = Libro("","CEN",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

    """ Libro no disponible, retorna 0"""
    def test_function_5(self):
        tarjeta = Tarjeta("AA", "BB", "0034567", 10)
        libro = Libro("","CE",1)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

    """ Pagar bus todo correcto"""
    def test_function_6(self):
        tarjeta = Tarjeta("AA", "BB", "0034567", 10)
        bus = Bus()
        valor1 = bus.cobrar_pasaje(tarjeta,1)
        valor2 = 1
        self.assertEqual(valor1, valor2)

    """ Pagar bus dia 5"""
    def test_function_7(self):
        tarjeta = Tarjeta("AA", "BB", "0034567", 10)
        bus = Bus()
        valor1 = bus.cobrar_pasaje(tarjeta,5)
        valor2 = 1
        self.assertEqual(valor1, valor2)

if __name__ == '__main__':
    unittest.main()
