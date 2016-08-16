import unittest
from programa import *

class SimpleTestCase(unittest.TestCase):
    def testPasajeEstudianteLunesAJueves(self):
        bus=Bus()
        tarjeta=Tarjeta("Leo","Eras","0987654",2.0)
        bus.cobrar_pasaje(tarjeta,1)
        assert tarjeta.saldo == 1.7

    def testPasajeTrabajadorLunesAJueves(self):
        bus=Bus()
        tarjeta=Tarjeta("Holguer","Jose","0087654",2.0)
        bus.cobrar_pasaje(tarjeta,1)
        assert tarjeta.saldo == 1.85

    def testPasajeEstudianteViernes(self):
        bus=Bus()
        tarjeta=Tarjeta("Leo","Eras","0987654",2.0)
        bus.cobrar_pasaje(tarjeta,5)
        assert tarjeta.saldo == 2.0

    def testPasajeTrabajadorViernes(self):
        bus=Bus()
        tarjeta=Tarjeta("Holguer","Jose","0087654",2.0)
        bus.cobrar_pasaje(tarjeta,5)
        assert tarjeta.saldo == 2.0
        
    def testLibroValidoDisponible7Dias(self):
        libro=Libro("CE", 0)
        assert libro.prestamo("10/02/2015") == "17/02/2015"

    def testLibroValidoDisponible14Dias(self):
        libro=Libro("CH", 0)
        assert libro.prestamo("10/02/2015") == "24/02/2015"

    def testLibroValidoPrestado(self):
        libro = Libro("CE", 1)
        assert libro.prestamo("10/02/2015") == 0

    def testLibroValidoPrestado(self):
        libro = Libro("CN", 1)
        assert libro.prestamo("10/02/2015") == 0

    def testLibroInvalido(self):
        libro = Libro("AD", 1)
        assert libro.prestamo("10/02/2015") == None
        
if __name__ == "__main__":
    unittest.main()
