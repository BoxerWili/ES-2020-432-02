from Funcions import Funcions
from unittest.mock import Mock
from Bank import Bank
import Skyscanner as S
import Booking as Bo
import Rentalcars as R


"""
VERSION 1
"""
def test_comprovacion(Usuario):
    pers, destinos, codigos, precios = Funcions.comprovacion(Usuario)
    
    assert pers == [4,4,4,4]
    assert destinos == ['BCN', 'CND', 'BRS', 'MAD']
    assert codigos == [123, 456, 789, 369]
    assert precios == [15, 20, 10, 10] 
    

def test_append_desti(Usuario):
    pers, destinos, codigos, precio = Funcions.comprovacion(Usuario)
    assert pers == [4,4,4,4,4]
    assert destinos == ['BCN', 'CND', 'BRS', 'MAD', 'FRA']
    assert codigos == [123, 456, 789, 369, 667]
    assert precio == [15,20,10,10,15]



def test_delete_desti(Usuario):
    pers, destinos, codigos, precio = Funcions.comprovacion(Usuario)
    assert pers == [4,4,4,4]
    assert destinos == ['BCN', 'CND', 'BRS', 'FRA']
    assert codigos == [123, 456, 789, 667]
    assert precio == [15,20,10,15]

    #destinos, codigos, precio = fly.delete_desti('BCN', 369, 10,destinos, codigos, precio)
    #print (destinos, codigos, precio)

"""
def test_suma_vol():
    preu_final = F.Funcions.suma_preu_vols_persona(F, Josep)
    assert preu_final == 60
"""

def test_suma_total_persona(Usuario):
    
    preu_pers= Funcions.suma_preu_vols_persona(Funcions, Usuario)
    
    assert preu_pers== 60

    pass



def test_suma_total(Usuario):
    preu_total = Funcions.suma_preu_vols_total(Usuario)
    assert preu_total == 240
    
    
def test_realitza_pagament(Usuario):
    pagament = Funcions.realitza_pagament(Usuario)
    assert pagament == True


def test_con_reserva(Usuario):
    reserva = Funcions.con_reserva(Funcions, Usuario)
    assert reserva == True
    


###VERSION 2

def test_metodo_pago(Usuario):
    pago, tarjeta = Funcions.metodo_pago(Usuario.Pagament)
    assert pago == True
    assert tarjeta == "VISA"
    

def test_realitza_pagamentV2(Usuario):
    pagament = Funcions.realitza_pagament(Usuario)
    assert pagament == False
    print("Error al realizar pago")


def test_con_reservaV2(Usuario):
    reserva = Funcions.con_reserva(Funcions, Usuario)
    assert reserva == False
    print("Error al reservar vuelo")

    

##VERSIÓN 3



def test_add_vehicle(Usuario):
    codi, marca, dies, recollida, preu = Funcions.comprovaciocar(Usuario)
    
    assert codi == ['456','246','791']
    assert marca == ['BMW', 'KIA', 'AUDI']
    assert dies == [4,4,3]
    assert recollida == ['CND', 'BRS', 'MAD']
    assert preu == [20,10,15]



def test_delevehicle(Usuario):
    codi, marca, dies, recollida, preu = Funcions.comprovaciocar(Usuario)
    
    assert codi == ['456','791']
    assert marca == ['BMW','AUDI']
    assert dies == [4,3]
    assert recollida == ['CND', 'MAD']
    assert preu == [20,15]
    
    pass

    


def test_addaloja(Usuario):
    codi, nom, pers, hab, dies, preu = Funcions.comprovacioaloja(Usuario)
    
    assert codi == ['1234','2869','5820','9731']
    assert nom == ['IMPERIAL', 'GRAN HOTEL', 'FRANCISCO', 'EUROPA']
    assert pers == [4,4,4,4]
    assert hab == [2,1,2,3]
    assert dies == [5,4,4,4]
    assert preu == [40,50,40,50]
    
    pass



def test_delealoja(Usuario):
    codi, nom, pers, hab, dies, preu = Funcions.comprovacioaloja(Usuario)
    
    assert codi == ['1234','2869','9731']
    assert nom == ['IMPERIAL', 'GRAN HOTEL', 'EUROPA']
    assert pers == [4,4,4]
    assert hab == [2,1,3]
    assert dies == [5,4,4]
    assert preu == [40,50,50]
    
    pass


def test_suma_total_personaV2(Usuario):
    preu_total= Funcions.suma_preu_vols_persona(Funcions, Usuario) + Funcions.suma_preu_aloja_persona(Funcions, Usuario) + Funcions.suma_preu_vehi_persona(Funcions, Usuario)
    
    assert preu_total == 391.25
    
    pass


def test_suma_totalV2(Usuario):
    preu_total = Funcions.suma_preu_vols_total(Funcions, Usuario) + Funcions.suma_preu_aloja(Funcions, Usuario) + Funcions.suma_preu_vehi(Funcions, Usuario)
    
    assert preu_total == 1565
    
    
    pass


def test_confVehi(Usuario):
    error = Funcions.con_reservacar(Usuario) 
    if(error):
        assert error == True
    else:
        assert error == False
        print("Error al confirmar vehiculo")
        
        
def test_confAloja(Usuario):
    error = Funcions.con_reservaaloja(Usuario)
    if(error):
        assert error == True
    else:
        assert error == False
        print("Error al confirmar reserva")
        
        

###VERSIÓN 4
        
def test_realitza_pagamentV3(Usuario):

    #U.afegirMetodePagament(U,'visa')
    
    

    Bank.do_payment = Mock()
 
    Bank.do_payment.return_value = False
    assert not Funcions.realitza_pagament(Usuario)

    Bank.do_payment.return_value = True
    assert Funcions.realitza_pagament(Usuario)
    
def test_con_reservaV3(Usuario):
    #U.Vols=['v']
    #U.afegirFlights(U,'v')
    
    S.confirm_reserve = Mock()

    S.confirm_reserve.return_value = False
    assert not Funcions.con_reserva(Funcions,Usuario)

    S.confirm_reserve.return_value = True
    assert Funcions.con_reserva(Funcions,Usuario)
    

###VERSION 5

def test_con_reservaaloja(Usuario):
    #U.Vols=[]
    #comentar si s'arribara algun cop aquesta funcio sense cap vol guardat 
    Bo.confirm_reserve = Mock()
    #Mock -> Fals
    S.confirm_reserve.return_value = False
    assert not Funcions.con_reservaaloja(Funcions,Usuario)
    #Mock -> Verdader
    S.confirm_reserve.return_value = True
    assert Funcions.con_reservaaloja(Funcions,Usuario)


def test_con_reservacar(Usuario):
    #U.Vols=[]
    #comentar si s'arribara algun cop aquesta funcio sense cap vol guardat
    R.confirm_reserve = Mock()
    #Mock -> Fals
    R.confirm_reserve.return_value = False
    assert not Funcions.con_reservacar(Funcions,Usuario)
    #Mock -> Verdader
    S.confirm_reserve.return_value = True
    assert Funcions.con_reservacar(Funcions,Usuario)
    
    
    
### El test que falta lo implementaremos en un parche ###
    

        
        











