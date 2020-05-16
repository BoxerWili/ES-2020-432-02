import pytest
import Flights 
"""
VERSION 1
"""
import PaymentData as pd
import Flights as fly

num_persones = 4
llista_destins = ['BCN', 'CND', 'BRS']
llista_codis = [123, 456, 789]
preu_vols = [15, 20, 10] 

def test_comprovacion(num_persones, llista_destins, llista_codis, preu_vols):
    pers, destinos, codigos, precios = fly.comprovacion(num_persones, llista_destins, llista_codis, preu_vols)
    assert pers == 4
    assert destinos == ['BCN', 'CND', 'BRS']
    assert codigos == [123, 456, 789]
    assert precios == 45 


aff_desti = 'MAD'
aff_codi = 369
aff_preu = 10
def test_append_desti(aff_desti, aff_codi, aff_preu, llista_destins, llista_codis, preu_vols):
    destinos, codigos, precio = fly.append_desti(aff_desti, aff_codi, aff_preu, llista_destins, llista_codis, preu_vols)
    assert destinos == ['BCN', 'CND', 'BRS', 'MAD']
    assert codigos == [123, 456, 789, 369]
    assert precio == 55


del_desti = 'MAD'
del_codi = 369
del_preu = 10
destinos =['BCN', 'CND', 'BRS', 'MAD']
codigos = [123, 456, 789, 369]
precio = 55
def test_delete_desti(del_desti, del_codi, del_preu, destinos, codigos, precio):
    destinos, codigos, precio = fly.delete_desti(del_desti, del_codi, del_preu, destinos, codigos, precio)
    assert destinos == ['BCN', 'CND', 'BRS']
    assert codigos == [123, 456, 789]
    assert precio == 45

    #destinos, codigos, precio = fly.delete_desti('BCN', 369, 10,destinos, codigos, precio)
    #print (destinos, codigos, precio)

preu_vols = [15, 20, 10]
def test_suma_preu_total(preu_vols):
    preu_final = pd.suma_preu_total(preu_vols)
    assert preu_final == 45
    
    
def test_realitza_pagament():
    pagament = pd.realitza_pagament()
    assert pagament == True


def test_con_reserva(User, Flights):
    reserva = fly.con_reserva(User, Flights)
    assert reserva == True
    
#print (test_con_reserva(User, Flights))

"""
VERSION 2
"""
metodo_pago = "VISA"
def test_metodo_pago(metodo_pago):
    pago=pd.metodo_pago(metodo_pago)
    assert pago == "VISA"
    
#dos tests iguales que en la version 1, comentados porque ya los realizamos anteriormente.
"""
def test_realitza_pagament():
    pagament = pd.realitza_pagament()
    print (pagament)


def test_con_reserva():
    reserva = fly.con_reserva()
    print (reserva)
"""
    
"""
VERSIÓN 3
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    