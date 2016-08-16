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
        :return: 1 en nario si el pasaje es pagado, 0 si este no se pudo cobrar
        """
        if dia > 0 and dia <= 5:
            if Validador.validar_tarjeta(tarjeta) != "INVALIDA":
                if dia == 5:
                    return 0b1
                else:
                    if Validator.validar_tarjeta(tarjeta) == "TRABAJADOR" and tarjeta.saldo >= self.pasaje/2:
                        tarjeta.debitar(self.pasaje/2)
                        return 0b1
                    elif tarjeta.saldo >= self.pasaje and  Validator.validar_tarjeta(tarjeta) == "ESTUDIANTE":
                        tarjeta.debitar(self.pasaje)
                        return 0b1
        return 0b0

class Biblioteca:
    def __init__(self, categoria, estado):
        self.estado = estado
        self.categoria = categoria

    def prestar_libro(self, tarjeta = None, fecha_actual= datetime.date.today()): #fecha es un datetime        today = 
    #   delta_prestamo = fecha - today # fecha limite menos el dia de hoy
     #   d = delta_prestamo.days        
      #  format_today = '{0:%Y/%m/%d}'.format(today)
      #  print(format_today)
      #  print(d)
        if(self.validarEstado() == False):
            print("Estado invalido")
            return 0b0
        if(self.validarCategoria() == False):
            print("Categoria invalida")            
            return 0b0

        if(self.estado == 1): # si ya esta prestado
            return 0b0
        if(self.categoria == "CE"):
            end_date = fecha_actual + datetime.timedelta(days=7) #tiempo limite de 7 dias 
        else:
            end_date = fecha_actual + datetime.timedelta(days=14) #tiempo limite de 14 dias 

        self.presentarFechaLimite(end_date)
        return 0b1

    def presentarFechaLimite(self, dia):
        format_today = '{0:%Y/%m/%d}'.format(dia)
        print("La fecha maxima es: " + format_today)

    #validar el estado ingresado
    def validarEstado(self):
        return(self.estado == 1 or self.estado == 0)

    # validar la categoria ingresado
    def validarCategoria(self):
        return(self.categoria in ["CE","CH","CN","CS"] )

def main():
    b = Biblioteca("EC", 0)
    b.prestar_libro()

if __name__ == "__main__":
    main()