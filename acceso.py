class Acceso():

	def validar_acceso(self, codigo, hora, dia):
		def validar_codigo(codigo):
			if(len(codigo) == 7 and codigo[:2] == "00" and codigo.isdigit()):
				print ("empleado")
				return 1
			elif(len(codigo) == 7 and codigo[:2] != "00" and codigo.isdigit()):
				print ("estudiante")
				return 2
			else:
				print ("codigo invalido")
				return 0

		valido = validar_codigo(codigo)

		if(valido == 1 and hora >= 0 and hora <= 24 and dia >= 1 and dia <= 5):
			print ("acceso")
			return 1
		elif(valido == 1 and hora >= 10 and hora <= 15 and dia >= 6 and dia <= 7):
			print ("acceso")
			return 1
		elif(valido == 2 and hora >= 8 and hora <= 18 and dia >= 1 and dia <= 5):
			print ("acceso")
			return 1
		else:
			print ("no acceso")
			return 0

	def codigo_valido(self, codigo):
		if(len(codigo) == 7 and codigo[:2] == "00" and codigo.isdigit()):
			return 1
		elif(len(codigo) == 7 and codigo[:2] != "00" and codigo.isdigit()):
			return 1
		else:
			return 0