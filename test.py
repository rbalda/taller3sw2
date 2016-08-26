import unittest
from programa import *

class BibliotecaTest(unittest.TestCase):
    """
    Clase de prueba para el nuevo modulo de Biblioteca
    """
    def setUp(self):
        self.tarjeta = Tarjeta(nombres="Israel", apellidos="Fernandez", codigo="1234567", saldo_inicial=10)
        self.libro = Libro(categoria="CE", estado=0)
        self.dia = 16
        self.mes = 8
        self.anio = 2016
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

    def test1(self):
        """
        Prueba libro de Ciencias Exactas disponible
        fecha de prestamo 16/08/2016
        estado libro = disponible
        categoria = CE
        resultado esperado = "23/8/2016"
        """
        result = Biblioteca.prestamo_libros(tarjeta= self.tarjeta, libro = self.libro, dia = self.dia, mes = self.mes, anio = self.anio)
        assert result == "23/8/2016"

    def test2(self):
        """
        Prueba libro de Ciencias Sociales disponible
        fecha de prestamo 16/08/2016
        estado libro = disponible
        categoria = CS
        resultado esperado = "30/8/2016"
        """
        self.libro.categoria = "CS"
        result = Biblioteca.prestamo_libros(tarjeta= self.tarjeta, libro = self.libro, dia = self.dia, mes = self.mes, anio = self.anio)
        assert result == "30/8/2016"

    def test3(self):
        """
        Prueba libro de Ciencias Exactas prestado
        fecha de prestamo 16/08/2016
        estado libro = prestado
        categoria = CE
        resultado esperado = "El libro ya ha sido prestado"
        """
        self.libro.estado = 1
        result = Biblioteca.prestamo_libros(tarjeta= self.tarjeta, libro = self.libro, dia = self.dia, mes = self.mes, anio = self.anio)
        assert result == "El libro ya ha sido prestado"

    def test4(self):
        """
        Prueba libro de Ciencias Exactas prestado
        fecha de prestamo 16/08/2016
        estado libro = prestado
        categoria = CE
        resultado esperado ="Tarjeta invalida"
        """
        self.tarjeta.codigo = "holi"
        result = Biblioteca.prestamo_libros(tarjeta= self.tarjeta, libro = self.libro, dia = self.dia, mes = self.mes, anio = self.anio)
        assert result == "Tarjeta invalida"

class BusTest(unittest.TestCase):
    """
    Clase de prueba para los cambios en cobrar pasaje
    """
    def setUp(self):
        self.tarjeta = Tarjeta(nombres="Israel", apellidos="Fernandez", codigo="1234567", saldo_inicial=10)
        self.bus = Bus()

    def test5(self):
        """
        Prueba tarjeta codigo de ESTUDIANTE
        dia Lunes (1)
        resultado esperado 1 binario (0b1)
        saldo 10 debitado 30 ctvs
        saldo total = 9.70
        """
        result = self.bus.cobrar_pasaje(tarjeta=self.tarjeta,dia=1)
        assert result == 0b1 and self.tarjeta.saldo == 9.7

    def test6(self):
        """
        Prueba tarjeta codigo de ESTUDIANTE
        dia Viernes (5)
        resultado esperado 1 binario (0b1)
        saldo 10 sin debito porque el viernes es gratis
        """
        result = self.bus.cobrar_pasaje(tarjeta=self.tarjeta,dia=5)
        assert result == 0b1 and self.tarjeta.saldo == 10

    def test8(self):
        """
        Prueba tarjeta codigo de TRABAJADOR
        dia Lunes(1)
        resultado esperado 1 binario (0b1)
        saldo 10 debitado 15 ctvs
        saldo total = 9.85
        """
        self.tarjeta.codigo = "0012345"
        result = self.bus.cobrar_pasaje(tarjeta=self.tarjeta,dia=1)
        assert result == 0b1 and self.tarjeta.saldo == 9.85

    def test9(self):
        """
        Prueba tarjeta codigo de TRABAJADOR
        dia Viernes (5)
        resultado esperado 1 binario (0b1)
        saldo 10 sin debito porque el viernes es gratis
        """
        self.tarjeta.codigo = "0012345"
        result = self.bus.cobrar_pasaje(tarjeta=self.tarjeta,dia=5)
        assert result == 0b1 and self.tarjeta.saldo == 10



if __name__ == "__main__":
    unittest.main() # run all tests
