import unittest
from programa import *

class TestPrograma(unittest.TestCase):
    # def setUp(self):
    #     #self.biblioteca = Biblioteca()
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

    def test_5(self):
        bus = Bus()
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1234567",saldo_inicial=100.0)
        self.assertEqual(bus.cobrar_pasaje(tarjeta=tarjeta,dia=1),0b1)

    def test_6(self):
        bus = Bus()
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="0034567",saldo_inicial=0.15)
        self.assertEqual(bus.cobrar_pasaje(tarjeta=tarjeta,dia=4),0b1)

    def test_7(self):
        bus = Bus()
        tarjeta = Tarjeta(nombres="Yamil",apellidos="Nunez",codigo="1134567",saldo_inicial=0.25)
        self.assertEqual(bus.cobrar_pasaje(tarjeta=tarjeta,dia=4),0b0)

if __name__ == '__main__':
	unittest.main()
