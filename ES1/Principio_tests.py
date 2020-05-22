from Funcions import Funcions
"""
VERSION 1
"""
def test_comprovacion(Usuario):
    pers, destinos, codigos, precios = Funcions.comprovacion(Usuario)
    
    assert pers == [4,4,4,4]
    assert destinos == ['BCN', 'CND', 'BRS', 'MAD']
    assert codigos == [123, 456, 789, 369]
    assert precios == [15, 20, 10, 10] 
    
"""    
aff_desti = 'FRA'
aff_codi = 667
aff_preu = 15
def test_append_desti():
    destinos, codigos, precio = F.Funcions.append_desti(aff_desti, aff_codi, aff_preu)
    assert destinos == ['BCN', 'CND', 'BRS', 'MAD', 'FRA']
    assert codigos == [123, 456, 789, 369, 667]
    assert precio == 70


del_desti = 'MAD'
del_codi = 369
del_preu = 10
def test_delete_desti():
    destinos, codigos, precio = F.Funcions.delete_desti(del_desti, del_codi, del_preu)
    assert destinos == ['BCN', 'CND', 'BRS', 'FRA']
    assert codigos == [123, 456, 789, 667]
    assert precio == 60

    #destinos, codigos, precio = fly.delete_desti('BCN', 369, 10,destinos, codigos, precio)
    #print (destinos, codigos, precio)


def test_suma_vol():
    preu_final = F.Funcions.suma_preu_persona()
    assert preu_final == 60


def test_suma_total():
    preu_total = F.Funcions.suma_preu_total()
    assert preu_total == 240
    
    
def test_realitza_pagament():
    pagament = F.Funcions.realitza_pagament()
    assert pagament == True


def test_con_reserva():
    reserva = F.Funcions.con_reserva()
    assert reserva == True
    

"""
###VERSION 2
"""
def test_metodo_pago():
    pago = F.Funcions.metodo_pago()
    assert pago == "VISA"
    

def test_realitza_pagamentV2():
    pagament = F.Funcions.realitza_pagament()
    assert pagament == False


def test_con_reservaV2():
    reserva = F.Funcions.con_reserva()
    assert reserva == False

    
"""
##VERSIÓN 3
"""
add_codiC = '791'
add_marcaC = 'AUDI'
add_diesC = 3
add_recollidaC = 'MAD'
add_preuC = 15
def test_add_vehicle():
    codi_cotxe, marca, recollida, dies, Preu_vehi = F.Funcions.add_vehiculo(add_codiC, add_marcaC, add_diesC, add_recollidaC, add_preuC)
    assert Preu_vehi == 45
    primer = F.Funcions.suma_preu_persona()
    assert primer == 105


dele_codiC = '246'
dele_marcaC = 'KIA'
dele_diesC = 4
dele_recollidaC = 'BRS'
dele_preuC = 10
def test_delevehicle():
    codi_cotxe, marca, recollida, dies, Preu_vehi = F.Funcions.delete_vehiculo(dele_codiC, dele_marcaC, dele_diesC, dele_recollidaC, dele_preuC)
    assert Preu_vehi == 35
    segon = F.Funcions.suma_preu_persona()
    assert segon == 95
    
    
add_codiA = '9731'
add_nomA = 'EUROPA'
add_numpersA = 4
add_habA = 3
add_diesA = 4
add_preuA = 50
def test_addaloja():
    codi_hotel,nom_hotel, num_habitacions, dies, Preu_aloja = F.Funcions.add_alojamiento(add_codiA, add_nomA, add_numpersA, add_habA, add_diesA, add_preuA)
    assert Preu_aloja == 180
    segon = F.Funcions.suma_preu_persona()
    assert segon == 275


dele_codiA = '5820'
dele_nomA = 'FRANCISCO'
dele_numpersA = 4
dele_habA = 2
dele_diesA = 4
dele_preuA = 40
def test_delealoja():
    codi_hotel,nom_hotel, num_habitacions, dies, Preu_aloja = F.Funcions.dele_alojamiento(dele_codiA, dele_nomA, dele_numpersA, dele_habA, dele_diesA, dele_preuA)
    assert Preu_aloja == 140
    segon = F.Funcions.suma_preu_persona()
    assert segon == 235


def test_confVehi():
    error = F.Funcions.con_reservacar() 
    if(error):
        assert error == True
    else:
        assert error == False
        
        
def test_confAloja():
    error = F.Funcions.con_reservaaloja()
    if(error):
        assert error == True
    else:
        assert error == False
        
        
"""
###VERSIÓN 4
"""
"""










