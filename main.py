import Funcions as F
import User as U
import Flights as Fl
import Cars as C
import Hotels as H
import PaymentData as P

import Principio_tests

def main():
    ################################################################################
    Josep = U.User('Josep', '123456Q', 'Barcelona', 4567890, 'josepbcn@gmail.com')
    ###Vuelos = Fl.Flights(4, ['BCN', 'CND', 'BRS', 'MAD'], [123, 456, 789, 369], [15, 20, 10, 10])
    ###Josep.afegirFlights(Fl.Flights(4, ['BCN', 'CND', 'BRS', 'MAD'], [123, 456, 789, 369], [15, 20, 10, 10]))
    Josep.afegirFlights(Fl.Flights(4, 'BCN', 123, 15))
    Josep.afegirFlights(Fl.Flights(4,'CND', 456, 20))
    Josep.afegirFlights(Fl.Flights(4, 'BRS', 789, 10))
    Josep.afegirFlights(Fl.Flights(4, 'MAD', 369, 10))
    
   
    
    
    Josep.Vols[1].afegirCar(C.Cars('456', 'BMW', 4, 'CND', 20))
    Josep.Vols[2].afegirCar(C.Cars('246', 'KIA', 4, 'BRS', 10))
    
    
    Josep.Vols[0].afegirHotels(H.Hotels('1234','IMPERIAL', 4, 2, 5, 40))
    Josep.Vols[1].afegirHotels(H.Hotels('2869','GRAN HOTEL', 4, 1, 4, 50))
    Josep.Vols[2].afegirHotels(H.Hotels('5820','FRANCISCO', 4, 2, 4, 40))


    
    ##Coches = C.Cars(['456','246'], ['BMW', 'KIA'], [4,4], ['CND', 'BRS'], [20, 10])
    ##Hoteles = H.Hotels(['1234', '2869', '5820'], ['IMPERIAL', 'GRAN HOTEL', 'FRANCISCO'], [4, 4, 4], [2, 1, 2], [5, 4, 4], [40, 50, 40] )
    
    Josep.afegirMetodePagament(P.PaymentData('VISA', 'Josep', 44443333, 987))
    
    
    
    ###Test principio, inicialización######## 
    print ("############################################")
    print("Test 1: Inicio")
    print ("############################################")

    Principio_tests.test_comprovacion(Josep)
    #########################################
    
    
    append_destinacion = 'FRA'
    append_codi_vol = 667
    append_preu = 15
    
    
    
    delete_destinacion = 'MAD'
   
    
    
    
    add_codiC = '791'
    add_marcaC = 'AUDI'
    add_diesC = 3
    add_recollidaC = 'MAD'
    add_preuC = 15
    
    
    
    
    
  
    
    add_codiA = '9731'
    add_nomA = 'EUROPA'
    add_numpers = 4
    add_habA = 3
    add_diesA = 4
    add_preuA = 50
    
    
    ##Utils=F.Funcions
   

    
    ################################################################################
    

    Pagar = False
    TodoCorrecto = False
    
    
    ini_user = F.Funcions.Info_User(Josep)
        
    
    if (ini_user == True):
        #reserva vol  
        
        ###Añadimos vuelo###
        
        Josep.afegirFlights(Fl.Flights(4, append_destinacion, append_codi_vol, append_preu))
        
        print ("############################################")
        print("Test 2: Añadir vuelo")
        print ("############################################")
        
        Principio_tests.test_append_desti(Josep)
        
        
        Josep.DeleteVol(delete_destinacion)
        
        print ("############################################")
        print("Test 3: Quitamos vuelo")
        print ("############################################")
               
        Principio_tests.test_delete_desti(Josep)
        
        VolOk=F.Funcions.con_reserva(F,Josep)
        
        #reserva vehicle
        
        
        
        Josep.afegirCar('FRA', C.Cars(add_codiC, add_marcaC, add_diesC, add_recollidaC, add_preuC))
        
        print ("############################################")
        print("Test 4: Añadimos Coche")
        print ("############################################")
               
               

        Principio_tests.test_add_vehicle(Josep)
        ###Josep.Vols[3].afegirCar(C.Cars(add_codiC, add_marcaC, add_diesC, add_recollidaC, add_preuC))
        
        
        Josep.deleteCar('BRS')
        print ("############################################")
        print("Test 5: Quitamos Coche")
        print ("############################################")
        Principio_tests.test_delevehicle(Josep)
        
        ###Josep.Vols[2].deleteCar()
        
        VehOk = F.Funcions.con_reservacar(F, Josep)
        
        """
        add_aloja = False
        dele_aloja = False
        print ("Afageix alojamiento:")
        while (add_aloja):
            H.Hotels.codi_hotel, H.Hotels.nom_hotel, H.Hotels.num_habitacions, H.Hotels.dies, Preu_aloja = F.Funcions.add_alojamiento(add_codiA, add_nomA, add_numpers, add_habA, add_diesA, add_preuA)
        print ("Elimina alojamiento:")
        while (dele_aloja):
            H.Hotels.codi_hotel, H.Hotels.nom_hotel, H.Hotels.num_habitacions, H.Hotels.dies, Preu_aloja = F.Funcions.dele_alojamiento(dele_codiA, dele_nomA, dele_numpers, dele_habA, dele_diesA, dele_preuA)
        """  
    
    
    
        Josep.afegirHotel('FRA', H.Hotels( add_codiA,add_nomA, add_numpers, add_habA, add_diesA, add_preuA))
        ###Josep.Vols[3].afegirHotels(H.Hotels( add_codiA,add_nomA, add_numpers, add_habA, add_diesA, add_preuA))
        
        
        print ("############################################")
        print("Test 6: Añadimos Hotel")
        print ("############################################")
        
        
        Principio_tests.test_addaloja(Josep)
        
        
        print ("############################################")
        print("Test 7: Quitamos Hotel")
        print ("############################################")
        
        Josep.deleteHotel('BRS')
        ###Josep.Vols[2].deleteHotel()
        
        Principio_tests.test_delealoja(Josep)
        
        
        AloOk = F.Funcions.con_reservaaloja(F, Josep)
        
        if ((VolOk and VehOk and AloOk) == True):
            Pagar = True
        else:
            Pagar = False
    
    if (Pagar == True):
        
        
        Metode_P, tarjeta = F.Funcions.metodo_pago(Josep.Pagament)
        
        Principio_tests.test_metodo_pago(Josep)
        
        if Metode_P:
            Pago = F.Funcions.datos_realizar_pago(Josep.Pagament)
            
            
            ##Principio_tests.test_realitza_pagament(Josep)
            
            ##Principio_tests.test_realitza_pagamentV2(Josep)
            ##Principio_tests.test_realitza_pagamentV3(Josep)
            
            if not Pago:
                
                Preu_personal= F.Funcions.suma_preu_vols_persona(F, Josep) + F.Funcions.suma_preu_aloja_persona(F, Josep) + F.Funcions.suma_preu_vehi_persona(F, Josep)
                
                #Preu_personal = F.Funcions.suma_preu_persona(F, Josep)
                
                print ("############################################")
                print("Preus")
                print ("############################################")
                
                print("Preu personal: ", Preu_personal)
                
                Preu_total = F.Funcions.suma_preu_vols_total(F, Josep) + F.Funcions.suma_preu_aloja(F, Josep) + F.Funcions.suma_preu_vehi(F, Josep)
                
                print ("Preu total: ", Preu_total)
                
        
                TodoCorrecto = F.Funcions.realitza_pagament(Josep)
        
        
    
    if (TodoCorrecto):
        #Enviamos factura por email...
        print ("Pago realizado correctamente, reservas confirmadas, la factura la recibira en el email.")
        #FINALIZAMOS 
    else:
        print ("Ha habido un error")
        #VOLVEMOS A EMPEZAR
        
    #print(F.Funcions.comprovacion(Josep))

print(main())