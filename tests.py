from programa import Biblioteca, Libro, Validador, Tarjeta,Edificio,Bus
from datetime import date, timedelta,datetime

import unittest

class Test_System(unittest.TestCase):
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

    def test_categoria_valida(self):
        libro = Libro(categoria="CS")
        self.assertTrue(libro.validar_categoria())

    def test_categoria_invalida(self):
        libro = Libro(categoria="CNN")
        self.assertFalse(libro.validar_categoria())

    def test_estado_libro_valido(self):
        libro = Libro(categoria="CS")
        self.assertIn(libro.prestado,[0,1])

    def test_estado_libro_invalido(self):
        libro = Libro(categoria="CS")
        libro.prestado = 4
        self.assertNotIn(libro.prestado,[0,1])

    def test_prestamo_libro_valido_7_dias(self):
        libro = Libro(categoria="CE")
        tarjeta = Tarjeta(nombres="Daniel",apellidos="Izquierdo",codigo="1234567",saldo_inicial=0.5)
        prestamo_libro = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta,fecha_actual=datetime.strptime("16/08/2016","%d/%m/%Y"))
        fecha_esperada_devolucion = (datetime.strptime("16/08/2016","%d/%m/%Y") + timedelta(days=7)).strftime('%d/%m/%Y')
        self.assertEqual(prestamo_libro,fecha_esperada_devolucion)

    def test_prestamo_libro_valido_14_dias(self):
        libro = Libro(categoria="CH")
        tarjeta = Tarjeta(nombres="Daniel",apellidos="Izquierdo",codigo="1234567",saldo_inicial=0.5)
        prestamo_libro = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta,fecha_actual=datetime.strptime("16/08/2016","%d/%m/%Y"))
        fecha_esperada_devolucion = (datetime.strptime("16/08/2016","%d/%m/%Y") + timedelta(days=14)).strftime('%d/%m/%Y')
        self.assertEqual(prestamo_libro,fecha_esperada_devolucion)

if __name__ == '__main__':
    unittest.main()
