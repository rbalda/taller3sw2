from datetime import datetime
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
        self.pasaje = 0.30 #cambio de valor de pasaje de 0.25 a 0.30
        self.pasajeDiferenciado= 0.15 #cambio de valor al pasaje de trabajadores
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
                    if Validador.validar_tarjeta(tarjeta)== "ESTUDIANTE":  #verificala tarjeta para debitar el saldo de estudiante
                        if tarjeta.saldo >= self.pasaje:
                            tarjeta.debitar(self.pasaje)
                            return 0b1
                    elif Validador.validar_tarjeta(tarjeta)== "TRABAJADOR": #verifica la tarjeta para debitar el saldo de trabajador
                         if tarjeta.saldo >= self.pasajeDiferenciado:
                            tarjeta.debitar(self.pasajeDiferenciado)
                            return 0b1
        return 0b0

class Libro(object):
        """
        Estructura de datos que representa un libro de una biblioteca
        """
        def __init__(self,nombre,categoria):
            """
            Constructor de la clase libro
            :param nombre: Nombre del libro
            :param categoria: Categoria del libro ciencias naturales CN,ciencias exactas CE, ciencias sociales CS
            :estado: 1 en binario si el libro esta prestado, 0 si esta disponible
            """
            self.nombre=nombre
            self.categoria=categoria
            self.estado=0
class Biblioteca(object):
        """
        Estructura de datos que verifica un prestamo de un libro
        """
        def __init__(self):
            pass

        def prestar(self,libro=None,fecha=''):
            self.dias=  int((datetime.strptime(fecha, '%d/%m/%Y').date()-datetime.now().date()).days)
            if libro.estado==0:
                if libro.categoria=="CE" and self.dias<=7:
                    libro.estado=1
                    print("Se realizo el prestamo correctamente del libro ", libro.nombre)
                    return 1
                elif libro.categoria!="CE" and self.dias<=14:
                    libro.estado=1
                    print("Se realizo el prestamo correctamente del libro ", libro.nombre)
                    return 1
                else:
                    print("La fecha del prestamo no es correcta")
                    return 0
            print ("El libro ",libro.nombre, " se encuentra prestado")
            return 0
