import datetime
import unittest
class Tarjeta(object):
    """
    Clase que modela la tarjeta para acceso a edificio y pago de bus
    """
    def __init__(self,nombres=None,apellidos=None,codigo=None,saldo_inicial=0.0):
        """
        Construntor de la clase que recibe parametros para inicializarla
        :param nombres: Nombres de la persona a quien pertenece la tarjeta
        :param apellidos: Apellidos de la persona a quien pertenece la tarjeta
        :param codigo: Codigo de siete digitos numericos para identificar la tarjeta
        :param saldo_inicial: Saldo inicial que contiene la tarjeta
        """
        self.digitos_max=7
        self.inicio="00"
        self.nombres=nombres
        self.apellidos=apellidos
        self.codigo=codigo
        self.saldo=saldo_inicial

    def debitar(self,valor=0.0):
        """
        Funcion que debita el valor del pasaje que se pase como parametro
        :param valor: valor del pasaje
        :return:
        """
        self.saldo=self.saldo-valor

class Validador(object):
    """
    Modulo que valida la tarjeta
    """
    @classmethod
    def validar_tarjeta(cls,tarjeta=None):
        """
        Funcion que valida que la tarjeta sea valida o de un tipo estudiante o trabajador
        :param tarjeta: Trajeta que contiene un codigo numerico
        :return: Retirna el tipo de tarjeta o si es invalida
        """
        try:
            if len(tarjeta.codigo)== tarjeta.digitos_max and tarjeta.codigo.isdigit():
                if tarjeta.codigo[:2]== tarjeta.inicio:
                    return "TRABAJADOR"
                else:
                    return "ESTUDIANTE"
            return "INVALIDA"
        except:
            return "INVALIDA"


class Edificio(object):
    """
    Modulo que verifica accesos al edificio
    """
    def conceder_acceso(self,tarjeta=None,dia=0,hora=0):
        """
        Funcion que verifica si el acceso se concedio o no
        :param tarjeta: Tarjeta del usuario a ingresar
        :param dia: dia de la semana en entero lunes=1,martes=2...domingo=7
        :param hora: hora del dia en formato 24, este valor sera solo un entero
        :return: 1 binario si el acceso es concedido, 0 si el acceso es denegado
        """
        if dia > 0 and dia < 8:
            if Validador.validar_tarjeta(tarjeta)=="TRABAJADOR":
                if dia <= 5:
                    return 0b1
                else:
                    if hora >=10 and hora <=15:
                        return 0b1
            elif Validador.validar_tarjeta(tarjeta)=="ESTUDIANTE":
                if dia <= 5:
                    if hora >= 8 and hora <=18:
                        return 0b1
            else:
                return 0b0
        return 0b0


class Bus(object):
    """
    Modulo que verifica el pago del bus
    """
    def __init__(self):
        self.pasaje = 0.30
        self.pasaje_trabajador = 0.15

    def cobrar_pasaje(self,tarjeta=None,dia=0):
        """
        Funcion que verifica que el pasaje haya sido pagado exitosamente
        :param tarjeta: Tarjeta del usuario que paga el pasaje
        :param dia: dia de la senama en el que cobra el pasaje
        :return: 1 en binario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            if Validador.validar_tarjeta(tarjeta) != "INVALIDA":
                if dia == 5:
                    return 0b1
                elif Validador.validar_tarjeta(tarjeta)=="TRABAJADOR":
                    tarjeta.debitar(self.pasaje_trabajador)
                    return 0b1
                else:
                    if tarjeta.saldo >= self.pasaje:
                        tarjeta.debitar(self.pasaje)
                        return 0b1
        return 0b0

class Libro(object):
    """
    Clase que modela al libro
    """
    def __init__(self, nombre=None, categoria=None, estado=0):
        """
        Construntor de la clase que recibe parametros para inicializarla
        :param nombre: Nombre del libro
        :param categoria: Categoria a la que pertenece el libro
        :param estado: Estado del libro
        """
        self.nombre=nombre
        self.categoria=categoria
        self.estado=estado

class Biblioteca(object):
    """
    Modulo que permite prestar libros
    """
    def prestar_libro(self, libro, tarjeta, fecha_actual):
        if Validador.validar_tarjeta(tarjeta) != "INVALIDA" and libro.estado == 0:
            fecha_entrada = datetime.datetime.strptime(fecha_actual, "%d/%m/%Y")
            if libro.categoria == "CE":
                fecha_cierre = fecha_entrada + datetime.timedelta(days=7)
            elif libro.categoria == "CN" or libro.categoria == "CH" or libro.categoria == "CS":
                fecha_cierre = fecha_entrada + datetime.timedelta(days=14)

            fecha_cierre = datetime.datetime.strftime(fecha_cierre, "%d/%m/%Y")
            print(fecha_cierre)
            return fecha_cierre

        print("No se puede prestar el libro")
        return None


# Creando casos de prueba
class Pruebas(unittest.TestCase):
    def test_prestar_libro_CE(self):
        biblioteca = Biblioteca()
        prestamo = biblioteca.prestar_libro(Libro("Prueba","CE", 0), Tarjeta("a","b","0012345",1), "20/03/2015")
        self.assertEqual(prestamo, "27/03/2015", "27/03/2015")

    def test_prestar_libro_CS(self):
        biblioteca = Biblioteca()
        prestamo = biblioteca.prestar_libro(Libro("Prueba","CS", 0), Tarjeta("a","b","0012345",1), "22/08/2016")
        self.assertEqual(prestamo, "05/09/2016", "05/09/2016")

    def test_prestar_libro_invalido(self):
        biblioteca = Biblioteca()
        prestamo = biblioteca.prestar_libro(Libro("Prueba","CS", 0), Tarjeta("a","b","02012345",1), "22/08/2016")
        self.assertEqual(prestamo, None, "No se puede prestar el libro")

    def test_codigo_empleado_valido(self):
        validar = Validador.validar_tarjeta(Tarjeta("f","e", "0099999", 3))
        self.assertEqual(validar, "TRABAJADOR", None)

    def test_codigo_estudiante_valido(self):
        validar = Validador.validar_tarjeta(Tarjeta("f","e", "9999999", 3))
        self.assertEqual(validar, "ESTUDIANTE", None)

    def test_codigo_invalido1(self):
        validar = Validador.validar_tarjeta(Tarjeta("f","e", "99999999", 3))
        self.assertEqual(validar, "INVALIDA", None)

    def test_codigo_invalido(self):
        validar = Validador.validar_tarjeta(Tarjeta("f","e", None, 3))
        self.assertEqual(validar, "INVALIDA", None)

    def test_acceso_estudiante_dia_laboral(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "9999999", 3), 1, 8)
        self.assertEqual(acceso, 0b1, None)

    def test_hora_invalida_estudiante_dia_laboral(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "9999999", 3), 5, 19)
        self.assertEqual(acceso, 0b0, None)

    def test_dia_invalido_estudiante_dia_laboral(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "9999999", 3), 6, 18)
        self.assertEqual(acceso, 0b0, None)

    def test_empleado_dia_laboral(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "0099999", 3), 2, 23)
        self.assertEqual(acceso, 0b1, None)

    def test_hora_invalida_empleado_dia_laboral(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "0099999", 3), 3, 24)
        self.assertEqual(acceso, 0b1, None)

    def test_empleado_fin_semana_dia_invalido(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "0099999", 3), 6, 15)
        self.assertEqual(acceso, 0b1, None)

    def test_dia_invalido1(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "0099999", 3), 8, 15)
        self.assertEqual(acceso, 0b0, None)

    def test_dia_invalido(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "0099999", 3), 8, 15)
        self.assertEqual(acceso, 0b0, None)

    def test_permiso_invalido(self):
        acceso = Edificio().conceder_acceso(Tarjeta("f","e", "02099999", 3), 5, 15)
        self.assertEqual(acceso, 0b0, None)


    def test_dia_gratis(self):
        bus = Bus().cobrar_pasaje(Tarjeta("f","e", "0099999", 3), 5)
        self.assertEqual(bus, 0b1, None)

    def test_empleadoMitadPrecio(self):
        bus = Bus().cobrar_pasaje(Tarjeta("f","e", "0099999", 0.15), 2)
        self.assertEqual(bus, 0b1, None)

    def test_estudiantePaga(self):
        bus = Bus().cobrar_pasaje(Tarjeta("f","e", "9999999", 0.30), 2)
        self.assertEqual(bus, 0b1, None)

    def test_diaBusinvalido(self):
        bus = Bus().cobrar_pasaje(Tarjeta("f","e", "9999999", 0.30), 8)
        self.assertEqual(bus, 0b0, None)
    #def test_pasaje_insuficiente(self):
    #    Bus().cobrar_pasaje(self,Tarjeta(),dia=0)
    #    self.assertEqual(prestamo, "INVALIDA", None)


if __name__ == "__main__":
    unittest.main()