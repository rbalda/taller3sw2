import unittest
from programa import Tarjeta
from programa import Biblioteca
from programa import Libro

class pruebas(unittest.TestCase):
    """ Todos los datos correctos, Libro tiene categoria CN,
          la fecha tiene que sumarse 14 dias """
    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "0034567", 10)
        libro = Libro("","CN",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = "Fecha límite: 30/08/2016"
        self.assertEqual(valor1, valor2)

    """ Todos los datos correctos, Libro tiene categoria CE,
          la fecha tiene que sumarse 7 dias """
    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "1234567", 10)
        libro = Libro("","CE",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = "Fecha límite: 23/08/2016"
        self.assertEqual(valor1, valor2)
   
    """ Tarjeta inválida, retorna 0"""
    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "003456", 10)
        libro = Libro("","CE",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

    """ Categoŕía del libro inválida, retorna 0"""
    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "003456", 10)
        libro = Libro("","CEN",0)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

    """ Libro no disponible, retorna 0"""
    def test_function_1(self):
        tarjeta = Tarjeta("AA", "BB", "003456", 10)
        libro = Libro("","CE",1)
        biblioteca = Biblioteca()
        valor1 = biblioteca.prestar_libro(libro,tarjeta,"16/08/2016")
        valor2 = 0
        self.assertEqual(valor1, valor2)

if __name__ == '__main__':
    unittest.main()
