import unittest
from programa import Tarjeta,Bus,Edificio,Validador,Biblioteca,Libro

class TestTarjeta(unittest.TestCase):


    def test_prueba1(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",2345,5.00)
        #fecha
        libro = Libro("CE",0)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, 1)

    def test_prueba2(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",2345,4.00)
        #fecha
        libro = Libro("CS",0)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, 1)

    def test_prueba3(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",1015,3.00)
        #fecha
        libro = Libro("CH",0)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, 1)

    def test_prueba4(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",1015,4.00)
        #fecha
        libro = Libro("CN",1)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, None)

    #pruebas para estudiantes
    def test_prueba5(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",2345,4.00)
        t.inicio="21"
        #fecha
        libro = Libro("CS",0)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, 1)

    def test_prueba6(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",1015,3.00)
        t.inicio="14"
        #fecha
        libro = Libro("CH",0)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, 1)

    def test_prueba7(self):

        #tarjeta
        t = Tarjeta( "Julio", "Aguirre",1015,4.00)
        t.inicio="11"
        #fecha
        libro = Libro("CN",1)
        #prestar_libro(self,libro,tarjeta,fecha)
        p = Biblioteca.prestar_libro(libro, t, "12/10/2012")
        print(p)
        self.assertEqual(p, None)

if __name__ == '__main__':
    unittest.main()
