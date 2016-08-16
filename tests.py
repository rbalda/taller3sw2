import unittest

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


class ProbarSistemaAcceso(unittest.TestCase):

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
