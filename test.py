import unittest
from programa import *


class Test(unittest.TestCase):
    def test1(self):
        l = Libro('CE', 0)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), '17/12/2016')

    def test2(self):
        l = Libro('CS', 0)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), '24/12/2016')

    def test3(self):
        l = Libro('CX', 0)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), 'No permitido')

    def test4(self):
        l = Libro('CE', 1)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), 'No permitido')

    def test5(self):
        l = Libro('CS', 1)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), 'No permitido')

    def test6(self):
        l = Libro('CX', 1)
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        b = Biblioteca()
        self.assertEquals(b.prestar_libro(t,l, '10/12/2016'), 'No permitido')

    def test7(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '0012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,1), 0b1)

    def test8(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '0012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,5), 0b1)

    def test9(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,2), 0b1)

    def test10(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,5), 0b1)

    def test11(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '1012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,6), 0b0)

    def test12(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '0012345', 1)
        self.assertEquals(b.cobrar_pasaje(t,6), 0b0)

    def test13(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '1012345', 0.20)
        self.assertEquals(b.cobrar_pasaje(t,2), 0b0)

    def test14(self):
        b = Bus()
        t = Tarjeta('Angely', 'Oyola', '0012345', 0.10)
        self.assertEquals(b.cobrar_pasaje(t,2), 0b0)

if __name__ == '__main__':
    unittest.main()