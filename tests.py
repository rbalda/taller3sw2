from programa import Biblioteca, Libro, Validador, Tarjeta
from datetime import date, timedelta

import unittest

class Test_System(unittest.TestCase):
    def setUp(self):
        pass

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
        prestamo_libro = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta)
        fecha_esperada_devolucion = (date.today() + timedelta(days=7)).strftime('%d/%m/%Y')
        self.assertEqual(prestamo_libro,fecha_esperada_devolucion)

    def test_prestamo_libro_valido_14_dias(self):
        libro = Libro(categoria="CH")
        tarjeta = Tarjeta(nombres="Daniel",apellidos="Izquierdo",codigo="1234567",saldo_inicial=0.5)
        prestamo_libro = Biblioteca.prestar_libro(libro=libro,tarjeta=tarjeta)
        fecha_esperada_devolucion = (date.today() + timedelta(days=14)).strftime('%d/%m/%Y')
        self.assertEqual(prestamo_libro,fecha_esperada_devolucion)

if __name__ == '__main__':
    unittest.main()