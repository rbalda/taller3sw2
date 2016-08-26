import unittest
from programa import *

class SimpleTestCase(unittest.TestCase):
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
