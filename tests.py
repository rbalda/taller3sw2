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


class ProbarSistemaPuerta(unittest.TestCase):

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


