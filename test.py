import unittest
from programa import Libro,Tarjeta,Edificio,Validador,Bus,Fecha

#taller
class AddTest(unittest.TestCase):
   def setUp(self):
       self.tarjeta = Tarjeta('Adriano','Pinargote','1234567',1)
       self.tarjetat = Tarjeta('jose','velez','0034567',1)
       self.bus= Bus()
       self.edificio=Edificio()

   def tearDown(self):
      pass


   def test_estudiante_Laborables(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,3,12),1)
   def test_estudiante_NoLaborables(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,12),0)
   def test_estudiante_hMenor10(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,9),1)
   def test_estudiante_hPasada(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,19),0)
   def test_estudiante_hPermit(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,13),1)
   def test_empleado_finDeSemanaHoraMenor10(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,8),0)
   def test_empleado_finDeSemanaHoraMayor15(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,16),0)
   def test_empleado_finDeSemanaHoraPermitida(self):
       self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,13),0)
   def test_diaGratis_Bus(self):
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjeta,5),1)
   def test_diaCobrado_Bus(self):
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjeta,3),1)
   def test_diaFinDeSemana_Bus(self):
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjeta,6),0)

   def test_saldoMayor30ctvs_Bus(self):
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjeta,1),1)
   def test_saldoMenor30ctvs_Bus(self):
       self.tarjeta.saldo=0.15
       self.bus.saldo=.30
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjeta,1),0)
       def test_saldoMenor15ctvs_Bus(self):
           self.tarjeta.saldo=0.15
           self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjetat,1),0)

if __name__=='__main__':
    unittest.main()
