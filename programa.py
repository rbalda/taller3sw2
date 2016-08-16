from datetime import datetime, date, time, timedelta


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
    def esTarjetaValida(cls, tarjeta):
        """
        Funcion que valida que la tarjeta sea valida o de un tipo estudiante o trabajador
        :param tarjeta: Trajeta que contiene un codigo numerico
        :return: Retirna el tipo de tarjeta o si es invalida
        """
        try:
            if len(tarjeta.codigo)== tarjeta.digitos_max and tarjeta.codigo.isdigit():
                return True
            return False
        except:
            return False

    @classmethod
    def esEmpleado (cls,tarjeta = None):
        if cls.esTarjetaValida(tarjeta) and tarjeta.codigo[:2]== tarjeta.inicio:
            return True
        return False

    @classmethod
    def esEstudiante (cls,tarjeta = None):
        if cls.esTarjetaValida(tarjeta) and tarjeta.codigo[:2]!= tarjeta.inicio:
            return True
        return False  


class Edificio():
    """
    Modulo que verifica accesos al edificio
    """
    horaEstudianteInicio = time(8, 0, 0)  # Asigna 8h 0m 0s
    horaEstudianteFin = time(18, 0, 0)  # Asigna 18h 0m 0s
    horaEmpleadoInicio = time(10, 0, 0)  # Asigna 10h 0m 0s
    horaEmpleadoFin = time(15, 0, 0)  # Asigna 15h 0m 0s        
  
    def conceder_acceso(self, tarjeta, dia, hora):
        """
        Funcion que verifica si el acceso se concedio o no
        :param tarjeta: Tarjeta del usuario a ingresar
        :param dia: dia de la semana en entero lunes=1,martes=2...domingo=7
        :param hora: hora del dia en formato 24, este valor sera solo un entero
        :return: 1 binario si el acceso es concedido, 0 si el acceso es denegado
        """
        print ("dia" )
        print (hora)
        if dia <= 5:
            if Validador.esEmpleado(tarjeta):
                return 0b1
            elif Validador.esEstudiante(tarjeta) and hora >= self.horaEstudianteInicio and hora <=self.horaEstudianteFin:
                return 0b1
        else:
            if Validador.esEmpleado(tarjeta) and hora >= self.horaEmpleadoInicio and hora <=self.horaEmpleadoFin:
                return 0b1
        return 0b0


class Bus(object):
    """
    Modulo que verifica el pago del bus
    """
    def __init__(self):
        self.pasaje = 0.30
        self.descuento = 0

    def cobrar_pasaje(self,tarjeta=None,dia=0):
        """
        Funcion que verifica que el pasaje haya sido pagado exitosamente
        :param tarjeta: Tarjeta del usuario que paga el pasaje
        :param dia: dia de la senama en el que cobra el pasaje
        :return: 1 en binario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            if Validador.esTarjetaValida(tarjeta):
                if dia == 5:
                    return 0b1
                else:
                    if Validador.esEmpleado(tarjeta):
                        self.descuento=0.5                        
                    if tarjeta.saldo >= (self.pasaje*(1-self.descuento)):
                        tarjeta.debitar(self.pasaje * (1-self.descuento))
                        return 0b1
        return 0b0

class Libro (object):
    """
    Clase que modela el libro
    """
    def __init__(self, categoria=None, estado=0):
        self.categoria = categoria
        self.estado=estado

    def prestar (self):
        if estado==0:
            estado=1
            return True
        else:
            return False


class CategoriaLibro (object):
    """
    Modulo que verifica la categoria del libro y obtiene tiempo maximo de prestamo
    """
    @classmethod
    def tiempoPrestamo(cls,libro=None):
        switcher = {
            "CE": 7,
            "CN": 14,
            "CS": 14,
            "CH": 14,
            }
        return switcher.get (libro.categoria, 0)

class Biblioteca (object):

    def __init__(self):
        self.fechaInicio = datetime(2016, 10, 1, 0, 0, 0)

    def prestarLibro (libro = None, tarjeta = None, fechaActual = None):
        if fechaActual >= self.fechaInicio and libro.estado==0 and Validador.esTarjetaValida(tarjeta):
            print("prestado hasta")
            diasPrestamo = CategoriaLibro.tiempoPrestamo (libro)
            fechaDevolucion = datetime (fechaActual.year, fechaActual.month, fechaActual.day + diasPrestamo, 0, 0, 0)
            print (fechaDevolucion)
        else:
            print("No presto")
