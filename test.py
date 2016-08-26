import unittest
from programa import Libro,Tarjeta,Edificio,Validador,Bus,Fecha,Prestamo

#taller
class AddTest(unittest.TestCase):
   def setUp(self):
       self.tarjeta = Tarjeta('Adriano','Pinargote','1234567',1)
       self.tarjetat = Tarjeta('jose','velez','0034567',1)
       self.bus= Bus()
       self.edificio=Edificio()
       self.libro=Libro()
       self.fecha=Fecha()
       self.prestamo=Prestamo()

   def tearDown(self):
       pass

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

   # def test_estudiante_Laborables(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,3,12),1)
   # def test_estudiante_NoLaborables(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,12),0)
   # def test_estudiante_hMenor10(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,9),1)
   # def test_estudiante_hPasada(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,19),0)
   # def test_estudiante_hPermit(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,2,13),1)
   # def test_empleado_finDeSemanaHoraMenor10(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,8),0)
   # def test_empleado_finDeSemanaHoraMayor15(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,16),0)
   # def test_empleado_finDeSemanaHoraPermitida(self):
   #     self.assertEqual(Edificio.conceder_acceso(self.edificio,self.tarjeta,6,13),0)
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
   def test_saldo15ctvs_Bus_Trabajador(self):
       self.tarjeta.saldo=0.15
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjetat,1),1)
   def test_saldoMenor15ctvs_Bus_Trabajador(self):
       self.tarjetat.saldo=0.12
       self.assertEqual(Bus.cobrar_pasaje(self.bus,self.tarjetat,1),0)
   def test_prestamo(self):
       self.libro.tipo='CE'
       self.libro.estado=0
       self.fecha.anio=2016
       self.fecha.mes=11
       self.fecha.dia=20
       self.assertEqual(Prestamo.realizar_prestamo(self.prestamo,self.tarjeta, self.libro, self.fecha),1)



if __name__=='__main__':
    unittest.main()
