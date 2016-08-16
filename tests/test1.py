import unittest
from programa import Biblioteca

class BibliotecaTestCase(unittest.TestCase):
	def setUp(self):
		"""se la llama antes de cada test"""
		pass

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