from datetime import date
from datetime import timedelta
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

    def cobrar_pasaje(self,tarjeta=None,dia=0):
        """
        Funcion que verifica que el pasaje haya sido pagado exitosamente
        :param tarjeta: Tarjeta del usuario que paga el pasaje
        :param dia: dia de la senama en el que cobra el pasaje
        :return: 1 en binario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            tarjeta_tipo = Validador.validar_tarjeta(tarjeta)
            if tarjeta_tipo != "INVALIDA":
                if dia == 5:
                    return 0b1
                else:
                    if tarjeta_tipo == "TRABAJADOR":
                        self.pasaje = 0.15
                    if tarjeta.saldo >= self.pasaje:
                        tarjeta.debitar(self.pasaje)
                        return 0b1
        return 0b0

class Biblioteca(object):
    """
    modulo Biblioteca, sirve para el prestamo de libros
	"""
    tiempo_prestamo = 14

    @classmethod
    def prestar_libro(self,libro=None, tarjeta=None, fecha_actual=date.today()):
        tarjeta_valida = Validador.validar_tarjeta(tarjeta) != "INVALIDA"
        categoria_libro_valida = libro.validar_categoria()

        if tarjeta_valida:
            if not libro.prestado and categoria_libro_valida:
                if libro.categoria == "CE":
                    self.tiempo_prestamo = 7

                libro.prestado = 1
                fecha_devolucion = fecha_actual + timedelta(days=self.tiempo_prestamo)
                fecha_devolucion = fecha_devolucion.strftime('%d/%m/%Y') #devuelve fecha en formato dd/mm/aa
                return fecha_devolucion

        return 0b0

class Libro(object):
    """
    clase que modela el libro para poder prestarlo a un estudiante o trabajador
    """
    def __init__(self, categoria):
        self.categoria = categoria
        self.prestado = 0

    def validar_categoria(self):
        return self.categoria in ["CE", "CN", "CS", "CH"]