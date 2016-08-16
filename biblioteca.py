from tarjeta import Tarjeta
from libro import Libro
from acceso import Acceso
from datetime import datetime
from datetime import timedelta

class Biblioteca():
	def prestar_libro(self, libro, tarjeta, fecha):
		acceso = Acceso()
		if(acceso.codigo_valido(tarjeta.codigo) and fecha > datetime(2016, 10, 1, 00, 00)):	
			if(libro.categoria == "CE" and libro.estado == 0):
				print ("Fecha limite: " + str(fecha + timedelta(days=7)))
				libro.estado = 1
				return 1
			elif((libro.categoria == "CN" or libro.categoria == "CS" or libro.categoria == "CH") and libro.estado == 0):
				print ("Fecha limite: " + str(fecha + timedelta(days=14)))
				libro.estado = 1
				return 2
			else:
				print ("Libro no disponible")
				return 0
		elif(acceso.codigo_valido(tarjeta.codigo) and fecha < datetime(2016, 10, 1, 00, 00)):
			print ("Fecha invalida. Sistema todavia no puede prestar libros")
			return 0
		elif(acceso.codigo_valido(tarjeta.codigo) == 0):
			print ("Codigo invalido, no se puede prestar")
			return 0