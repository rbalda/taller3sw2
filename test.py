import unittest
from programa import Libro,Biblioteca,Tarjeta,Bus,Edificio

#taller 3
class Test(unittest.TestCase):
    def setUp(self):
        self.edificio = Edificio()
        self.biblioteca = Biblioteca()
        self.matematicas = Libro("Matematicas","CE")
        self.sociales = Libro("Sociales","CS")
        self.humanas = Libro("Ciencias Humanas","CH")
        self.humanas.estado=1

        self.tarjetaEstudiante= Tarjeta("","","1479863",0.3)
        self.tarjetaTrabajador= Tarjeta("","","0069876",0.15)
        self.bus=Bus()
    def tearDown(self):
        pass


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

    def test_libroCienciasExactasFechaIncorrecta(self):
        print("Libro de ciencias exactas con fecha mayor a 7 dias")
        self.assertEqual(self.biblioteca.prestar(self.matematicas,"09/09/2016"),0)

    def test_libroCienciasExactasFechaCorrecta(self):
        print("Libro de ciencias exactas con fecha menor a 7 dias")
        self.assertEqual(self.biblioteca.prestar(self.matematicas,"30/08/2016"),1)

    def test_libroCienciasNoExactasFechaCorrecta(self):
        print("Libro de ciencias sociales con fecha menor a 14 dias")
        self.assertEqual(self.biblioteca.prestar(self.sociales,"09/09/2016"),1)

    def test_libroCienciasNoExactasFechaIncorrecta(self):
        print("Libro de ciencias sociales con fecha mayor a 14 dias")
        self.assertEqual(self.biblioteca.prestar(self.sociales,"12/09/2016"),0)

    def test_libroCienciasNoExactasPrestado(self):
        print("Libro Prestado")
        self.assertEqual(self.biblioteca.prestar(self.humanas,"20/08/2016"),0)

    def test_CobrarPasaje_Estudiante_Saldo_DiaDeCobro(self):
        print("Cobro del pasaje de un estudiante con saldo dispobible en dias de cobro")
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaEstudiante,3),0b1)

    def test_CobrarPasaje_Estudiante_SinSaldo_DiaDeCobro(self):
        print("Cobro del pasaje de un estudiante sin saldo en dias de cobro")
        self.tarjetaEstudiante.saldo=0.00
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaEstudiante,3),0b0)
    def test_CobrarPasaje_Estudiante_SinSaldo_DiaDeNoCobro(self):
        print("Cobro del pasaje de un estudiante sin saldo en dia gratis")
        self.tarjetaEstudiante.saldo=0.00
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaEstudiante,5),0b1)
    def test_CobrarPasaje_Trabajador_Saldo_DiaDeCobro(self):
        print("Cobro del pasaje de un trabajador con saldo dispobible en dias de cobro")
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaTrabajador,3),0b1)
    def test_CobrarPasaje_Trabajador_SinSaldo_DiaDeCobro(self):
        print("Cobro del pasaje de un trabajdor sin saldo en dias de cobro")
        self.tarjetaTrabajador.saldo=0.00
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaTrabajador,3),0b0)
    def test_CobrarPasaje_Trabajador_SinSaldo_DiaDeNoCobro(self):
        print("Cobro del pasaje de un trabajador sin saldo en dia gratis")
        self.tarjetaTrabajador.saldo=0.00
        self.assertEqual(self.bus.cobrar_pasaje(self.tarjetaTrabajador,5),0b1)

if __name__=='__main__':
    unittest.main()
