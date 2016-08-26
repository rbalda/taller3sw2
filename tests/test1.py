import unittest
from programa import Biblioteca,Edificio,Tarjeta,Bus

class BibliotecaTestCase(unittest.TestCase):
	def setUp(self):
		"""se la llama antes de cada test"""
		self.edificio= Edificio()
		self.bus = Bus()

	def test_accede_trabajador_horario_normal(self):
		trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
		assert self.edificio.conceder_acceso(trabajador,5,0) == 0b1

	def test_accede_trabajador_fin_semana(self):
		trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
		assert self.edificio.conceder_acceso(trabajador,6,15) == 0b1

	def test_trabajador_no_accede(self):
		trabajador = Tarjeta("Juan","De la Cruz","0012345",0.50)
		assert self.edificio.conceder_acceso(trabajador,6,16) == 0b0

	def test_accede_estudiante(self):
		estudiante = Tarjeta("Manuel","Torres","1112345",1)
		assert self.edificio.conceder_acceso(estudiante,5,18)==0b1

	def test_estudiante_no_accede(self):
		estudiante = Tarjeta("Manuel","Torres","1112345",1)
		assert self.edificio.conceder_acceso(estudiante,5,19)==0b0

	def test_tarjeta_invalida(self):
		tarjeta = Tarjeta("Manuel","Torres","11123a5",1)
		assert self.edificio.conceder_acceso(tarjeta,5,19)==0b0

	def test_tarjeta_none(self):
		assert self.edificio.conceder_acceso(None,5,19) == 0b0

	def tearDown(self):
		"""llamar luego de cada test"""
		print("termino test")

	def testCategoriaInvalido(self):
		self.biblioteca = Biblioteca("CENN",0)
		assert self.biblioteca.prestar_libro() == 0b0

	def testACategoriaValidoCE(self):
	    self.biblioteca = Biblioteca("CE",0)
	    assert self.biblioteca.prestar_libro() == 0b1

	def testACategoriaValidoCH(self):
		self.biblioteca = Biblioteca("CH",0)
		assert self.biblioteca.prestar_libro() == 0b1

	def testEstadoInvalido(self):
		self.biblioteca = Biblioteca("CE",2)
		assert self.biblioteca.prestar_libro() == 0b0

	def testAEstadoValidoCE(self):
		self.biblioteca = Biblioteca("CE",0)
		assert self.biblioteca.prestar_libro() == 0b1
if __name__ == "__main__":
	unittest.main()   # run all tests
