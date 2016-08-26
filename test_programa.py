import programa
from datetime import timedelta
import datetime
import unittest
from programa import Edificio,Tarjeta,Bus

tarjeta = programa.Tarjeta("Gabriel", "Aumala", "2343455", 0.30)
tarjetaEMP = programa.Tarjeta("Gabriel", "Aumala", "0043455", 0.30)

class PruebaPrograma(unittest.TestCase):

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

    def test_pasaje1(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjeta, 6)
        assert(res == 0b0)

    def test_pasaje2(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjeta, 2)
        assert(res == 0b1)

    def test_pasaje3(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjeta, 1)
        assert(res == 0b0)

    def test_pasaje4(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjeta, 5)
        assert(res == 0b1)

    def test_pasajeemp1(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjetaEMP, 6)
        assert(res == 0b0)

    def test_pasajeemp2(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjetaEMP, 2)
        assert(res == 0b1)

    def test_pasajeemp3(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjetaEMP, 3)
        assert(res == 0b1)

    def test_pasajeemp4(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjetaEMP, 1)
        assert(res == 0b0)

    def test_pasajeemp5(self):
        bus = programa.Bus()
        res = bus.cobrar_pasaje(tarjetaEMP, 5)
        assert(res == 0b1)

    def test_biblioteca(self):
        fecha = programa.Biblioteca.prestar(programa.Libro("CE"), tarjeta, datetime.datetime.strptime("16/08/2016","%d/%m/%Y"))
        assert(fecha == "23/08/2016")

    def test_biblioteca1(self):
        fecha = programa.Biblioteca.prestar(programa.Libro("CS"), tarjeta, datetime.datetime.strptime("16/08/2016","%d/%m/%Y"))
        assert(fecha == "30/08/2016")


# def test_pasaje():
#     bus = programa.Bus()
#     res = bus.cobrar_pasaje(tarjeta, 6)
#     assert(res == 0b0)
#     res = bus.cobrar_pasaje(tarjeta, 2)
#     assert(res == 0b1)
#     res = bus.cobrar_pasaje(tarjeta, 1)
#     assert(res == 0b0)
#     res = bus.cobrar_pasaje(tarjeta, 5)
#     assert(res == 0b1)
#
#     res = bus.cobrar_pasaje(tarjetaEMP, 6)
#     assert(res == 0b0)
#     res = bus.cobrar_pasaje(tarjetaEMP, 2)
#     assert(res == 0b1)
#     res = bus.cobrar_pasaje(tarjetaEMP, 3)
#     assert(res == 0b1)
#     res = bus.cobrar_pasaje(tarjetaEMP, 1)
#     assert(res == 0b0)
#     res = bus.cobrar_pasaje(tarjetaEMP, 5)
#     assert(res == 0b1)

# def test_biblioteca():
#      fecha = programa.Biblioteca.prestar(programa.Libro("CE"), tarjeta, datetime.date.today())
#      assert(fecha == "23/08/2016")
#      fecha = programa.Biblioteca.prestar(programa.Libro("CS"), tarjeta, datetime.date.today())
#      assert(fecha == "30/08/2016")
if __name__ == '__main__':
    unittest.main()
