
import datetime

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
            if Validador.validar_tarjeta(tarjeta) != "INVALIDA":
                if dia == 5:
                    return 0b1
                else:
                    if tarjeta.saldo >= self.pasaje:
                        if Validador.validar_tarjeta(tarjeta) == "TRABAJADOR":
                            tarjeta.debitar(self.pasaje/2)
                        else:
                            tarjeta.debitar(self.pasaje)
                        return 0b1
        return 0b0

class Biblioteca(object):

    def prestar_libro(self, libro=None, tarjeta=None, fecha=None):
        if Validador.validar_tarjeta(tarjeta) != "INVALIDA":
            fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            if libro.esta_disponible():
                fecha_limite = fecha_obj + + datetime.timedelta(days=libro.get_fecha_limite())
                return "Fecha límite: " + fecha_limite.strftime("%d/%m/%Y")
        return 0b0


class Libro(object):
    """
    Modulo de libro
    """
    def __init__(self, nombre=None, categoria=None, estado=0):
        """
        Constructor de la clase libro que recibe parametros para inicializarla
        :param nombre: Nombres del libro
        :param categoria: Categoría adjunta del libro
        :param estado: Estado en el que se encuentra el libro
        """
        self.nombre=nombre
        if self.categoria_valida(categoria):
            self.categoria=categoria
        else:
            self.categoria=None            
        self.estado=estado

    def get_categoria(self):
        return self.categoria

    def get_fecha_limite(self):
        categoria = self.get_categoria()
        if categoria != None:
            if categoria == "CE":
                return 7
            return 14

    def esta_disponible(self):
        if self.categoria_valida(self.get_categoria()):
            return self.estado==0
        return False

    def categoria_valida(self, categoria=None):
        if categoria != None:
            if (categoria == "CE" or categoria == "CN" or categoria == "CS" or categoria == "CH"):
                return True
        return False


tarjeta = Tarjeta("AA", "BB", "0034567", 10)
libro = Libro("","CN",0)
biblioteca = Biblioteca()
print(biblioteca.prestar_libro(libro,tarjeta,"16/08/2016"))
