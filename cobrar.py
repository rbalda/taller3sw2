from tarjeta import Tarjeta

class Cobrar():
	def cobrar_pasaje(self, tarjeta, dia):
		if (1 <= dia <= 4):
			if(len(tarjeta.codigo) == 7 and tarjeta.codigo[:2] == "00" and tarjeta.codigo.isdigit() and tarjeta.saldo >= 0.15):
				tarjeta.saldo -= 0.15
				print ("Empleado: cobrado 0.15, saldo total: "+str(tarjeta.saldo))
				return 1
			elif(len(tarjeta.codigo) == 7 and tarjeta.codigo[:2] == "00" and tarjeta.codigo.isdigit() and tarjeta.saldo < 0.15):
				print ("Saldo insuficiente, saldo total: "+str(tarjeta.saldo))
				return 0
			elif(tarjeta.saldo >= 0.3):
				tarjeta.saldo -= 0.3
				print ("Estudiante: cobrado 0.30, saldo total: "+str(tarjeta.saldo))
				return 1
			elif (0.0 <= tarjeta.saldo < 0.3):
				print ("Saldo insuficiente, saldo total: "+str(tarjeta.saldo))
				return 0
			elif (tarjeta.saldo < 0.0):
				print ("Saldo invalido")
				return 0
		elif (dia == 5 and tarjeta.saldo >= 0.0):
			print ("Viernes (gratuito): Cobrado 0.0, saldo total: "+str(tarjeta.saldo))
			return 1
		elif (dia > 5 or dia < 1):
			print ("Error dia invalido: solo lunes a viernes")
			return 0