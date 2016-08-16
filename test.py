import unittest
from datetime import datetime, date, time, timedelta

import programa

class TestAcceso (unittest.TestCase):
    def setUp (self):
        self.validador = programa.Validador()
        self.edificio = programa.Edificio()
        self.bus = programa.Bus()
        pass

    def tearDown (self):
        pass
    
#Parte 1
    def test_codigoMenosCaracteres (self):
        self.assertEqual(self.validador.esTarjetaValida (programa.Tarjeta("","","123456",0)), False)

    def test_codigoMasCaracteres (self):
        self.assertEqual(self.validador.esTarjetaValida (programa.Tarjeta("","","123456789", 0)),False)

    def test_codigoAlfanumerico (self):
        self.assertEqual(self.validador.esTarjetaValida (programa.Tarjeta("","","A4df33", 0)),False)

    def test_codigoAlfabetico (self):
        self.assertEqual(self.validador.esTarjetaValida (programa.Tarjeta("","","ABCDEFG", 0)),False)

    def test_codigoEstudianteFechaHoraOK (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","1234567", 0), 2,time(12,0,0)),0b1)

    def test_codigoEstudianteFechaHoraMayor (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","1234567", 0), 2,time(20,0,0)),0b0)    

    def test_codigoEstudianteFechaHoraMenor (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","1234567", 0), 2,time(5,0,0)),0b0)    

    def test_codigoEstudianteFechaFinde (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","1234567", 0), 6,time(12,0,0)),0b0)    


    def test_codigoEmpleadoFechaOK (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","0034567", 0), 2,time(12,0,0)),0b1)    


    def test_codigoEmpleadoFechaFindeOK (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","0034567", 0),7,time(13,0,0)),0b1)    


    def test_codigoEmpleadoFechaFindeMenor (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","0034567", 0),6,time(8,0,0)),0b0)    

    def test_codigoEmpleadoFechaFindeMayor (self):
        self.assertEqual(self.edificio.conceder_acceso (programa.Tarjeta("","","0034567", 0),6,time(17,0,0)),0b0)

#parte 2/3

    def test_codigoInvalido (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","FG@#123",5),5),0)

    def test_codigoOKLunesJuevesConSaldoEst (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","1234567",5), 2),1)

    def test_codigoOKLunesJuevesSinSaldoEst (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","1234567",0), 0),0)

    def test_codigoOKViernesConSaldo (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","1234567",5), 5),1)

    def test_codigoOKViernesSinSaldo (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","1234567",0), 5),1)

    def test_codigoOKFinde (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","1234567",5), 6),0)

    def test_codigoOKLunesJuevesConSaldoEmp (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","0034567",5), 2),1)

    def test_codigoOKLunesJuevesSinSaldoEmp (self):
        self.assertEqual (self.bus.cobrar_pasaje(programa.Tarjeta("","AA","0034567",0), 0),0)
        
    #Parte 3

if __name__=='__main__':
    unittest.main()
