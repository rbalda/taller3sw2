import unittest
# import Tarjeta
from programa import Tarjeta
from programa import Bus
from programa import Libro
from programa import Biblioteca

class TestStringMethods(unittest.TestCase):
    # def test_Tarjeta1(self):
    #     # t = Tarjeta()
    #     self.assertEqual(Tarjeta.isValid("0012345"), True)
    # def test_Tarjeta2(self):
    #     # t = Tarjeta()
    #     self.assertEqual(Tarjeta.isValid("001234567890"), False)
    # def test_Tarjeta3(self):
    #     # t = Tarjeta()
    #     self.assertEqual(Tarjeta.isValid("1234567"), True)
    # def test_Tarjeta4(self):
    #     # t = Tarjeta()
    #     self.assertEqual(Tarjeta.isValid("0012345"), True)

    t_est = Tarjeta("Branny", "Chito", "1234567", 3.50)
    t_est2 = Tarjeta("Branny", "Chito", "1234567", .10)
    t_emp = Tarjeta("Ariana", "Palma", "0034567", 0.20)
    t_emp2 = Tarjeta("Ariana", "Palma", "0034567", .05)
    t_invalida = Tarjeta("Branny", "Chito", "0012345xx", 3.50)

    def test_Bus_dia1(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_est, -1), 0)
    def test_Bus_dia2(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_est, 5), 1)
    def test_Bus_dia3(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_emp, 5), 1)

    def test_Bus_Estudiante(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_est, 1), 1)
    def test_Bus_Estudiante2(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_est2, 1), 0)

    def test_Bus_Empleado(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_emp, 1), 1)
    def test_Bus_Empleado2(self):
        bus = Bus()
        self.assertEqual(bus.cobrar_pasaje(self.t_emp2, 1), 0)

    def test_Libro_Prestar(self):
        l = Libro("CH")
        self.assertEqual(Biblioteca.prestar(l, self.t_est, '01/09/2016'), '15/09/2016')
    def test_Libro_Prestar2(self):
        l = Libro("CE")
        self.assertEqual(Biblioteca.prestar(l, self.t_est, '01/09/2016'), '08/09/2016')




    # student
    # def test_Acceso1(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('8812345', 1, 18), '01')
    # def test_Acceso2(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('8812345', 1, 19), '00')
    # def test_Acceso3(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('8812345', 7, 18), '00')

    # employed
    # def test_Acceso4(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('0012345', 1, 23), '01')
    # def test_Acceso5(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('0012345', 6, 10), '01')
    # def test_Acceso6(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('0012345', 6, 9), '00')
    #
    # def test_Acceso7(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('0012345', 8, 9), '00')
    # def test_Acceso8(self):
    #     acc = Access()
    #     self.assertEqual(acc.getAccess('0012345', 8, 25), '00')


if __name__ == '__main__':
    unittest.main()
