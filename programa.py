import time
from datetime import date, timedelta,datetime


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

    def getCodigo(self):
        return self.codigo

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
        #inicializa el valor del pasaje general
        self.pasaje = 0.30
        self.porcentajeDescuento = 1

    def cobrar_pasaje(self,tarjeta=None,dia=0):
        """
        Funcion que verifica que el pasaje haya sido pagado exitosamente
        :param tarjeta: Tarjeta del usuario que paga el pasaje
        :param dia: dia de la senama en el que cobra el pasaje
        :return: 1 en binario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            tarjetaStatus = Validador.validar_tarjeta(tarjeta)
            if tarjetaStatus != "INVALIDA":
                if tarjetaStatus == "TRABAJADOR":
                    self.porcentajeDescuento = 0.5
                if dia == 5:
                    return 0b1
                else:
                    if tarjeta.saldo >= (self.pasaje * self.porcentajeDescuento):
                        tarjeta.debitar(self.pasaje * self.porcentajeDescuento)
                        return 0b1
        return 0b0


class Categoria(object):
    def __init__(self,label=None,tiempoPrestamo=14):
        self.label = label
        self.tiempoPrestamo = tiempoPrestamo
        if label=='CE':
            self.tiempoPrestamo = 7
        
    def getTiempoPrestamo(self):
        return self.tiempoPrestamo


class Libro(object):
    def __init__(self,nombre=None,categoria=None,estado=0):
        self.nombre = nombre
        self.categoria =categoria
        self.estado = estado
        self.numeroTarjeta = None #para guardar el dato de quien ha prestado el libro

    def estaDisponible(self):
        if self.estado==0:
            return True
        return False

    def prestar(self,codigoTarjeta,fechaPrestamo):
        #La funcion se encarga de evaluar el periodo del prestamo segun la categoria
        #y cambia el estado del libro. 
        #Devuelve un Objeto con el parametro resultado y otro mensaje
        
        if self.estado==0:
            self.estado==1
            self.numeroTarjeta = codigoTarjeta
            tiempo = self.categoria.getTiempoPrestamo()
            fechaObj = datetime.strptime(fechaPrestamo, '%d/%m/%Y') + timedelta(days=tiempo)
            return {
                'resultado':True,
                'mensaje': "Puede prestar el libro. La fecha de entrega es el "+fechaObj.strftime("%d/%m/%Y")
            }
        else:
            return {
                'resultado':False,
                'mensaje': "El libro no esta disponible"
            }

    
    
class Biblioteca(object):

    @classmethod
    def prestar_libro(cls,libro=None,tarjeta=None,fechaActual=time.strftime("%d/%m/%Y")):
        #validar tarjeta
        if Validador.validar_tarjeta(tarjeta) == "INVALIDA":
            return {
                'resultado':False,
                'mensaje': "La tarjeta es invalida"
            }
        return libro.prestar(tarjeta.getCodigo(),fechaActual)
            

    




