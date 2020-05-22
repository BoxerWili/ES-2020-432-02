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
    
    ##Coches a flights
    
    
    Josep.Vols[1].afegirCar(C.Cars('456', 'BMW', 4, 'CND', 20))
    Josep.Vols[2].afegirCar(C.Cars('246', 'KIA', 4, 'BRS', 10))
    
    
    Josep.Vols[0].afegirHotels(H.Hotels('1234','IMPERIAL', 4, 2, 5, 40))
    Josep.Vols[1].afegirHotels(H.Hotels('2869','GRAN HOTEL', 4, 1, 4, 50))
    Josep.Vols[2].afegirHotels(H.Hotels('5820','FRANCISCO', 4, 2, 4, 40))


    
    ##Coches = C.Cars(['456','246'], ['BMW', 'KIA'], [4,4], ['CND', 'BRS'], [20, 10])
    ##Hoteles = H.Hotels(['1234', '2869', '5820'], ['IMPERIAL', 'GRAN HOTEL', 'FRANCISCO'], [4, 4, 4], [2, 1, 2], [5, 4, 4], [40, 50, 40] )
    
    Josep.afegirMetodePagament(P.PaymentData('VISA', 'Josep', 44443333, 987))
    
    print(Principio_tests.test_comprovacion(Josep))
    
    
    
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
    
    
    
   

    
    ################################################################################
    

    Pagar = False
    TodoCorrecto = False
    
    
    ini_user = F.Funcions.Info_User(Josep)
        
    
    if (ini_user == True):
        #reserva vol
        """
        add_desti = False
        dele_desti = False
        print ("Añadimos destinos:")
        while (add_desti):
            F.Flights.Destination, F.Flights.Codi_Vol, Preu_Vol = F.Funcions.append_desti(append_destinacion, append_codi_vol, append_preu)
        print ("Eliminamos destinos:")
        while (dele_desti):
            F.Flights.Destination, F.Flights.Codi_Vol, Preu_Vol = F.Funcions.delete_desti(delete_destinacion, delete_codi_vol, delete_preu)
        """  
        
        Josep.afegirFlights(Fl.Flights(4, append_destinacion, append_codi_vol, append_preu))
        
        Josep.DeleteVol(delete_destinacion)
        
        VolOk=F.Funcions.con_reserva(Josep)
        
        #reserva vehicle
        """
        add_vehi = False
        dele_vehi = False
        print ("Añadir coche:")
        while (add_vehi):
            C.Cars.codi_cotxe, C.Cars.marca, C.Cars.recollida, C.Cars.dies, Preu_vehi = F.Funcions.add_vehiculo(add_codiC, add_marcaC, add_diesC, add_recollidaC, add_preuC)
        print ("Eliminar coche:")
        while (dele_vehi):
            C.Cars.codi_cotxe, C.Cars.marca, C.Cars.recollida, C.Cars.dies, Preu_vehi = F.Funcions.delete_vehiculo(dele_codiC, dele_marcaC, dele_diesC, dele_recollidaC, dele_preuC)
        """  
        
        Josep.Vols[2].deleteCar()
        
        Josep.Vols[3].afegirCar(C.Cars(add_codiC, add_marcaC, add_diesC, add_recollidaC, add_preuC))
        VehOk = F.Funcions.con_reservacar(Josep)
        
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
        
        Josep.Vols[2].deleteHotel()
        Josep.Vols[3].afegirHotels(H.Hotels( add_codiA,add_nomA, add_numpers, add_habA, add_diesA, add_preuA))
        AloOk = F.Funcions.con_reservaaloja()
        
        if ((VolOk and VehOk and AloOk) == True):
            Pagar = True
        else:
            Pagar = False
    
    if (Pagar == True):
        
        
        F.Funcions.metodo_pago()
        F.Funcions.datos_realizar_pago()
        F.Funcions.suma_preu_total()
        
        TodoCorrecto = F.Funcions.realitza_pagament
        
        
    
    if (TodoCorrecto):
        #Enviamos factura por email...
        print ("Pago realizado correctamente, reservas confirmadas, la factura la recibira en el email.")
        #FINALIZAMOS 
    else:
        print ("Ha habido un error")
        #VOLVEMOS A EMPEZAR

print (main())
