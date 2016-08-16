import unittest
from programa import *

class TestPrograma(unittest.TestCase):
    # def setUp(self):
    #     #self.biblioteca = Biblioteca()

    def test_1(self):
        categoria = Categoria(label='CE')
        libro =Libro("Caperucita",categoria=categoria)
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1234567",saldo_inicial=100.0)
        prestamo = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta)
        self.assertEqual(prestamo['resultado'],True)
        print prestamo['mensaje']

    def test_2(self):
        categoria = Categoria(label='CS')
        libro =Libro("Caperucita",categoria=categoria)
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1234567",saldo_inicial=100.0)
        prestamo = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta,fechaActual = '10/11/2016')
        self.assertEqual(prestamo['resultado'],True)
        print prestamo['mensaje']

    def test_3(self):
        categoria = Categoria(label='SH')
        libro =Libro("Caperucita",categoria=categoria)
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1234567",saldo_inicial=100.0)
        prestamo = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta,fechaActual = '30/12/2016')
        self.assertEqual(prestamo['resultado'],True)
        print prestamo['mensaje']

    def test_4(self):
        categoria = Categoria(label='CN')
        libro =Libro("Caperucita",categoria=categoria)
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1234567",saldo_inicial=100.0)
        prestamo = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta,fechaActual = '05/10/2016')
        self.assertEqual(prestamo['resultado'],True)
        print prestamo['mensaje']

if __name__ == '__main__':
	unittest.main()