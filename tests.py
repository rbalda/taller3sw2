'''
Autor: Jorge Ayala
Taller 3
'''
import unittest
import datetime

from programa import Tarjeta
from programa import Libro
from programa import Biblioteca
from programa import Bus
from programa import Edificio


class ProbarSistemaPuerta(unittest.TestCase):
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

    def test_escenario_pasaje_trabajador(self):
        bus = Bus()
        tarjeta = Tarjeta("Jore","Ayala","0012345",0.20)
        res = bus.cobrar_pasaje(tarjeta,4)
        self.assertEqual(res,0b1)

    def test_escenario_pasaje_estudiante_1(self):
        bus = Bus()
        tarjeta = Tarjeta("Jore","Ayala","1234567",0.20)
        res = bus.cobrar_pasaje(tarjeta,4)
        self.assertEqual(res,0b0)

    def test_escenario_pasaje_estudiante_2(self):
        bus = Bus()
        tarjeta = Tarjeta("Jore","Ayala","1234567",0.40)
        res = bus.cobrar_pasaje(tarjeta,4)
        self.assertEqual(res,0b1)

    def test_biblioteca_esc_1(self):
        libro = Libro(0b0, 'CE')
        tarjeta = Tarjeta("Jore","Ayala","123rO567",0.40)
        fecha = datetime.date.today()
        biblio = Biblioteca(libro,tarjeta,fecha)
        res = biblio.prestar_libro()
        self.assertEqual(res,None)

    def test_biblioteca_esc_2(self):
        libro = Libro(0b1, 'CE')
        tarjeta = Tarjeta("Jore","Ayala","1234567",0.40)
        fecha = datetime.date.today()
        biblio = Biblioteca(libro,tarjeta,fecha)
        res = biblio.prestar_libro()
        self.assertEqual(res,None)

    def test_biblioteca_esc_3(self):
        libro = Libro(0b0, 'CE')
        tarjeta = Tarjeta("Jore","Ayala","1234567",0.40)
        fecha = datetime.date.today()
        biblio = Biblioteca(libro,tarjeta,fecha)
        res = biblio.prestar_libro()
        fechaLim = datetime.date(2016,8,23)
        self.assertEqual(res,fechaLim)

    def test_biblioteca_esc_4(self):
        libro = Libro(0b0, 'CN')
        tarjeta = Tarjeta("Jore","Ayala","1234567",0.40)
        fecha = datetime.date.today()
        biblio = Biblioteca(libro,tarjeta,fecha)
        res = biblio.prestar_libro()
        fechaLim = datetime.date(2016,8,30)
        self.assertEqual(res,fechaLim)


if __name__ == '__main__':
    unittest.main()
