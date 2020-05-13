# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:28:04 2020

@author: alexp
"""
def Programa():
    #empiezo con el codigo que no se si es correcto pero por hacer algo 
    
    #Botón "Realizar pago de la reserva"
    rreserva = False
    
    #para introducir los datos
    pago = False
    
    #boton continuar
    continuar = False
    
    #continuar de la tarjeta
    seleccioncontinuar = False
    
    # Sub flujo 3 (S3): no se puede realizar el pago
    NoPosible = True
    
    VueloOk = False
    #Ha reservado vehiculos?
    RVehi = False
    VehiOk = False
    #Ha reservado alojamiento?
    RAloja = False
    AlojaOk = False
    
    #Para finalizar el programa...
    TodoCorrecto = False
    
    # 1. El usuario pulsa el botón “Realizar pago de la reserva”
    while(rreserva==False):
        """
        Imaginamos que clica el boton...
        """
        rreserva = True
        
        if (rreserva):
            pago = True
            
    """
    incorrectos = True
    continuar = False
    
    # 2. La aplicación solicita al usuario que introduzca sus datos de facturación
    if(pago):
        while((incorrectos) or (continuar==False)):
            print ("Introducir Nombre, DNI, direccion postal, numero de telefono, email: ")
            Nom = input()
            DNI = input()
            DirPos = input()
            NumTlfn = input()
            Email = input()
            
            botoncontinuar = True
        
            # 3. El usuario introduce los datos de facturación y pulsa el botón “Continuar”
            if (botoncontinuar):
                continuar = True
            
            #4. La aplicación valida los datos de facturación
            if((Nom or DNI or DirPos or NumTlfn or Email)==[]):
                #Sub flujo 1 (S1): datos de facturación incorrectos o incompletos
                print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                incorrectos = True
            else:
                incorrectos = False 
    """
    
    if (incorrectos==False):
        # 5. La aplicación solicita al usuario que seleccione el método de pago
        print ("Selecciona metodo de pago: VISA o MasterCard")
        # 6. El usuario selecciona el método de pago y pulsa el botón “Continuar”
        metodopago = input()
        seleccioncontinuar = True
    
    if (seleccioncontinuar):
        
        while(NoPosible):
            # Sub flujo 2 (S2): datos para el pago incorrectos o incompletos
            error = True
            while(error):
                # 7. La aplicación solicita al usuario que introduzca los datos para realizar el pago
                print("Introducir--> Titular tarjeta, numero tarjeta y codigo de seguridad: ")
                TiTarj = input()
                NumTarj = input()
                CodSeg = input()
                if((TiTarj or NumTarj or CodSeg)==[]):
                    # 8. La aplicación valida los datos de pago
                    print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                    error = True
                else:
                    error = False 
                    
            """
            imaginemos que no hay ningun error... fallopago = False
            """
            fallopago = False
            if(fallopago):
                NoPosible = True
            else:
                # 9. La aplicación inicia el proceso de pago usando la plataforma asociada al método de pago
                """
                Se hace automaticamente??
                """
                NoPosible = False
    
    # 10. La aplicación inicia el proceso de confirmación de las reservas
    if (NoPosible==False):
        # a. Se continúa con el S4
        """
        Aplicación confirma la reserva de vuelos... suponemos que si
        """
        AppVuelo = True
        if (AppVuelo == False):
            """
            Reintentamos confirmar la reserva de vuelos... suponemos que no 
            """
            confirmacion = 1
            while(confirmacion <= 3):
                ReinVuelo = False
                if (ReinVuelo):
                    VueloOk = True
                    break
                else:
                    confirmacion=confirmacion + 1
                    
            if (confirmacion != 1):
                """
                cancelamos cargo realizado 
                """
                print ("Ha habido un problema durante el proceso de confirmacion, no se ha efectuado ningun cargo")
                # 13
                """
                proceso de pago termina 
                """
        else:
            VueloOk = True
        
        # b. Si el usuario había reservado vehículos se continúa con el S5
        if (RVehi):
            """
            Aplicación confirma la reserva de vehiculos... suponemos que si
            """
            AppVehi = True
            if (AppVehi == False):
                """
                Reintentamos confirmar la reserva de vehiculos... suponemos que no 
                """
                confirVehi = 1
                while(confirVehi <= 3):
                    ReinVehi = False
                    if (ReinVehi):
                        VehiOk = True
                        break
                    else:
                        confirVehi=confirVehi + 1
                        
                if (confirVehi != 1):
                    """
                    cancelamos cargo realizado 
                    """
                    print ("Ha habido un problema durante el proceso de confirmacion, no se ha efectuado ningun cargo")
                    # 13
                    """
                    proceso de pago termina 
                    """
            else:
                VehiOk = True
            
        # c. Si el usuario había reservado alojamientos se continúa con el S6
        if (RAloja):
            
            """
            Aplicación confirma la reserva de alojamiento... suponemos que si
            """
            AppAloja = True
            if (AppAloja == False):
                """
                Reintentamos confirmar la reserva de alojamiento... suponemos que no 
                """
                confirAloja = 1
                while(confirAloja <= 3):
                    ReinAloja = False
                    if (ReinAloja):
                        AlojaOk = True
                        break
                    else:
                        confirAloja = confirAloja + 1
                        
                if (confirAloja != 1):
                    """
                    cancelamos cargo realizado 
                    """
                    print ("Ha habido un problema durante el proceso de confirmacion, no se ha efectuado ningun cargo")
                    # 13
                    """
                    proceso de pago termina 
                    """
            else:
                AlojaOk = True
    
        if (VueloOk and (RVehi and VehiOk) and (RAloja and AlojaOk)):
            TodoCorrecto=True
        
        if (VueloOk and (RVehi and VehiOk) and (RAloja == False and AlojaOk ==False)):
            TodoCorrecto=True
        
        if (VueloOk and (RVehi == False and VehiOk == False) and (RAloja and AlojaOk)):
            TodoCorrecto=True
    
        if (VueloOk and (RVehi == False and VehiOk == False) and (RAloja == False and AlojaOk == False)):
            TodoCorrecto=True
    
    
    
    
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

        
        
    
    
    
    
    
    
    
    
