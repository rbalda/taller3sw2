import unittest
import datetime


# Create your tests
'''
from ingreso_pacientes.models import Paciente


class CrearPaciente(TestCase):

def crear_paciente(self):
    self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555')

def test_crear_paciente(self):
    self.crear_paciente()
    self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')
'''
from programa import Biblioteca
from programa import Libro
from programa import Tarjeta
from programa import Edificio
from programa import Bus


class ProbarSistemaAcceso(unittest.TestCase):
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

    def test_escenario1(self):
        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="CE", estado=0)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado,"01/08/2003")

    def test_escenario2(self):

        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="CE", estado=1)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado, 0)

    def test_escenario3(self):

        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="CH", estado=0)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado,"01/08/2003")

    def test_escenario4(self):

        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="CS", estado=0)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado,"01/08/2003")

    def test_escenario5a(self):

        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="CN", estado=0)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado,"01/08/2003")

    def test_escenario5b(self):

        tarj1 = Tarjeta(nombres="Carlos", apellidos="Piguabe", codigo=0012345, saldo_inicial=20)
        libr1 = Libro(titulo="Diferencial", categoria="ABC", estado=0)
        biblio1 = Biblioteca()
        resultado = biblio1.hacer_prestamo(libro =libr1, tarjeta=tarj1, fecha="01/01/2003")
        self.assertEqual(resultado,"01/08/2003")

if __name__ == '__main__':
    unittest.main()
