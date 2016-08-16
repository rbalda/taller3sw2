import programa
from datetime import timedelta
import datetime 

tarjeta = programa.Tarjeta("Gabriel", "Aumala", "2343455", 0.30)
tarjetaEMP = programa.Tarjeta("Gabriel", "Aumala", "0043455", 0.30)

def test_pasaje():
    bus = programa.Bus()
    res = bus.cobrar_pasaje(tarjeta, 6)
    assert(res == 0b0)
    res = bus.cobrar_pasaje(tarjeta, 2)
    assert(res == 0b1)
    res = bus.cobrar_pasaje(tarjeta, 1)
    assert(res == 0b0)
    res = bus.cobrar_pasaje(tarjeta, 5)
    assert(res == 0b1)

    res = bus.cobrar_pasaje(tarjetaEMP, 6)
    assert(res == 0b0)
    res = bus.cobrar_pasaje(tarjetaEMP, 2)
    assert(res == 0b1)
    res = bus.cobrar_pasaje(tarjetaEMP, 3)
    assert(res == 0b1)
    res = bus.cobrar_pasaje(tarjetaEMP, 1)
    assert(res == 0b0)
    res = bus.cobrar_pasaje(tarjetaEMP, 5)
    assert(res == 0b1)

def test_biblioteca():
     fecha = programa.Biblioteca.prestar(programa.Libro("CE"), tarjeta, datetime.date.today())
     assert(fecha == "23/08/2016")
     fecha = programa.Biblioteca.prestar(programa.Libro("CS"), tarjeta, datetime.date.today())
     assert(fecha == "30/08/2016")

    
