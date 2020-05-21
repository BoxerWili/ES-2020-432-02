import User as U
import Flights as F
import Cars as C
import Hotels as H
import PaymentData as P
import Funcions as FNC

def main():
    ################################################################################
    num_Passatgers = 4
    destinos = ['BCN', 'CND', 'BRS', 'MAD']
    Codi_Vol = [123, 456, 789, 369]
    Preu_Vols = [15, 20, 10, 10] 
    append_destinacion = 'MAD'
    append_codi_vol = 369
    append_preu = 10
    delete_destinacion = 'MAD'
    delete_codi_vol = 369
    delete_preu = 10

    #faltan los de vehiculo
    #faltan los de alojamiento
    #metodos de pago
    
    #acabar los tests y muhcas cosas mas
    
    
    metodo_pago = "VISA"
    
    
    ################################################################################
    
    ini_user = False
    Pagar = False
    TodoCorrecto = False
    
    #inicializamos al usuario
    ini_user = FNC.Funcions.Info_User(Nom, DNI, DirPos, NumTlfn, Email)
        
    
    if (ini_user == True):
        #reserva vol
        VolOk=FNC.Funcions.con_reserva(num_Passatgers, destinos, Codi_Vol, Preu_Vols, append_destinacion, append_codi_vol, append_preu, delete_destinacion, delete_codi_vol, delete_preu, Preu_Vol)
        
        #reserva vehicle
        VehOk = FNC.Funcions.con_reserva(add_desti, add_preu, dele_desti, dele_preu, destinos, Preu_vehis, Preu_vehi)
        #reserva alojamiento
        AloOk = FNC.Funcions.con_reserva(add_desti, add_preu, dele_desti, dele_preu, destinos, Preu_aloja, Preu_alojas)
        
        if ((VolOk and VehOk and AloOk) == True):
            Pagar = True
        else:
            Pagar = False
    
    if (Pagar == True):
        P.metodo_pago(metodo_pago)
        P.datos_realizar_pago(TiTarj, NumTarj, CodSeg)
        TodoCorrecto = P.realitza_pagament()
        P.suma_preu_total(preu_vols, preu_vehi, preu_aloja)
        
    
    if (TodoCorrecto):
        # 11. La aplicación envía la factura al usuario por email
        """
        Enviamos factura por email...
        """
        # 12. La aplicación confirma al usuario que el pago se ha realizado correctamente, que las reservas están confirmadas, y que se le ha enviado la factura por email
        print ("Pago realizado correctamente, reservas confirmadas, la factura la recibira en el email.")
        # 13. El proceso de pago termina
        """
        CLOSE
        FINISH
        """


