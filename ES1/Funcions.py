import User as U
import Flights as F
import Cars as C
import Hotels as H
import PaymentData as P
import Bank as B
import Skyscanner as S
import Rentalcars as R
import Booking as Bo

class Funcions:
    
    def Info_User(User):

        continuar = False
                
                        
                        
                #4. La aplicación valida los datos de facturación
        if((User.Nom or User.DNI or User.DirPos or User.NumTlfn or User.Email)==None):
                    #Sub flujo 1 (S1): datos de facturación incorrectos o incompletos
            print ("Datos incorrectos o incompletos vuelva a introducir todos los datos.")
            
            continuar = False
        
        else:
            continuar = True
            
            
        return continuar #TRUE OR FALSE
    
    #Enteoria correcto
    ###############################################################################################################################
    def metodo_pago(Pago):
        #print ("Selecciona metodo de pago: VISA o MasterCard")
        
        if ((Pago.tipus_targeta == 'VISA') or (Pago.tipus_targeta == 'MasterCard')):
            #print ("El metodo de pago para realizar el pago es el siguiente: " , metodo_pago)
            return True, Pago.tipus_targeta
        else:
            #print ("Ha selecionado un metodo de pago erronio")
            print ("Error no has introduit correctament el tipus de targeta.")
            return False
            
    def datos_realizar_pago(Pago):
        if((Pago.nom_titular or Pago.num_targeta or Pago.codi_seguretat)==None):
            error = True
            
            print ("Datos incorrectos o incompletos vuelva a introducir todos los datos.")
            
               
        else:
            error = False
        
        return error #TRUE OR FALSE
    
    def suma_preu_vols_total(self,Usuario):
        preu_volst = 0
        for i in Usuario.Vols:
            preu_volst = preu_volst + i.Preu_Vols*i.num_Passtgers 

        return preu_volst
    
    
    def suma_preu_vols_persona(self,Usuario):
        preu_volst = 0
        for i in Usuario.Vols:
            preu_volst = preu_volst + i.Preu_Vols 

        return preu_volst
    
    def suma_preu_vehi_persona(self,Usuario):
        preu_vehit = 0
        for i in Usuario.Vols:
            if i.coche != None:
                preu_vehit = preu_vehit + (i.coche.Preu_vehis*i.coche.dies/i.num_Passtgers) 
                
        

        return preu_vehit
    
    
    
    def suma_preu_vehi(self,Usuario):
        preu_vehit = 0
        for i in Usuario.Vols:
            if i.coche != None:
                preu_vehit = preu_vehit + i.coche.Preu_vehis*i.coche.dies 
        
        

        return preu_vehit
    
    
    def suma_preu_aloja_persona(self,Usuario):
        preu_alojat = 0
        
        for i in Usuario.Vols:
            if i.Hotel != None:
                
                preu_alojat = preu_alojat + (i.Hotel.Preu_alojas * i.Hotel.num_habitacions * i.Hotel.dies/i.num_Passtgers)
            
        return preu_alojat
    
    
    def suma_preu_aloja(self,Usuario):
        preu_alojat = 0
        
        for i in Usuario.Vols:
            if i.Hotel != None:
                
                preu_alojat = preu_alojat + i.Hotel.Preu_alojas * i.Hotel.num_habitacions * i.Hotel.dies 
            
        return preu_alojat
    
    
    
    
    def suma_preu_persona(self, Usuario):
        preu_persona = self.suma_preu_vols_persona(self, Usuario) + self.suma_preu_vehi_persona(self,Usuario) + self.suma_preu_aloja(self,Usuario)
        return preu_persona
    
    
    
    def suma_preu_total(self, Usuario):
        
        ##preu_personal = self.suma_preu_persona(Usuario) 
        preu_total = self.suma_preu_vols_total(self, Usuario) + self.suma_preu_vehi(self, Usuario) + self.suma_preu_aloja(self, Usuario)
        #print ("El preu per persones es de: " , preu_total)
        return preu_total
    
    
        
        
    def realitza_pagament(Usuario):
        
        pagament_correcte = B.Bank()
        confirm = pagament_correcte.do_payment(Usuario, Usuario.Pagament)
        
        #pagament_correcte = True 
        pagamentOk=False
        if (confirm == False):
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            confirmacion = 1
            while(confirmacion <= 3):
                    
                confirm = pagament_correcte.do_payment(Usuario, Usuario.Pagament)
                #pagament_correcte=True   
                if (confirm):
                    pagamentOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (pagamentOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del pagament, no se ha efectuado ningun cargo")
        else:
            pagamentOk = True
            
        return pagamentOk #TRUE OR FALSE
    
    ###########################################################################################################################
    
    def comprovacioaloja(Usuario):
        
        count = 1
            
        Llista_codi=[]
            
        Llista_nom=[]
            
        Llista_pers=[]
            
        Llista_hab=[]
        
        Llista_dies=[]
        
        Llista_preu=[]
            
        for i in Usuario.Vols:
            
            if i.Hotel != None:
                
                print("Vol ", count, "Hotel:")
                
                print("Codi: ",i.Hotel.codi_hotel)
                Llista_codi.append(i.Hotel.codi_hotel)
                print("Nom: ", i.Hotel.nom_hotel)
                Llista_nom.append(i.Hotel.nom_hotel)
                print("Persones: ", i.Hotel.num_persones)
                Llista_pers.append(i.Hotel.num_persones)
                
                print("Habitacions: ", i.Hotel.num_habitacions)
                Llista_hab.append(i.Hotel.num_habitacions)
                
                print ("Dies: ", i.Hotel.dies)
                Llista_dies.append(i.Hotel.dies)
                
                
                print ("Preu: ", i.Hotel.Preu_alojas)
                Llista_preu.append(i.Hotel.Preu_alojas)
                

                
            count+=1
        
        return Llista_codi, Llista_nom, Llista_pers, Llista_hab, Llista_dies, Llista_preu
        
       
    
    
    
    def con_reservaaloja(self, Usuario):
        #Preu_aloja = self.suma_preu_aloja()
        #llamar funcion de Booking està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        AppAloja = Bo.Booking()
        for i in Usuario.Vols:
            if i.Hotel != None:        
                confirm = AppAloja.confirm_reserve(Usuario, i.Hotel)
        

        #AppAloja=True
        
        AlojaOk = False
        
        ##print (self.comprovacioaloja())
        
        if (confirm == False):
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            confirmacion = 1
            while(confirmacion <= 3):
                for i in Usuario.Vols:
                    if i.Hotel != None:        
                        confirm = AppAloja.confirm_reserve(Usuario, i.Hotel)
                #AppAloja=True   
                if (confirm):
                    AlojaOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (AlojaOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del alojamiento, no se ha efectuado ningun cargo")
        else:
            AlojaOk = True
            
        return AlojaOk #TRUE OR FALSE
          
    
######################################################################################################################
        
    def comprovaciocar(Usuario):
        
        
        count = 1
            
        Llista_codi=[]
            
        Llista_marca=[]
            
        Llista_dies=[]
            
        Llista_recollida=[]
        
        Llista_preu=[]
            
        for i in Usuario.Vols:
            
            if i.coche != None:
                
                print("Vol ", count, "Coche:")
                
                print("Codi: ",i.coche.codi_cotxe)
                Llista_codi.append(i.coche.codi_cotxe)
                print("Marca: ", i.coche.marca)
                Llista_marca.append(i.coche.marca)
                print ("Dies: ", i.coche.dies)
                Llista_dies.append(i.coche.dies)
                
                print("Recollida: ", i.coche.recollida)
                Llista_recollida.append(i.coche.recollida)
                print ("Preu: ", i.coche.Preu_vehis)
                Llista_preu.append(i.coche.Preu_vehis)
                

                
            count+=1
        
        return Llista_codi, Llista_marca, Llista_dies, Llista_recollida, Llista_preu
        

    pass
        
  
    
    
    def con_reservacar(self, Usuario):
        #Preu_vehi = self.suma_preu_vehi()
        AppVehi = R.Rentalcars()
        for i in Usuario.Vols:
            if i.coche != None:
                confirm = AppVehi.confirm_reserve(Usuario, i.coche)
        
        #AppVehi=True
        
        VehiOk = False
        
        ##print (self.comprovaciocar())
        
        if (confirm == False):
            confirmacion = 1
            while(confirmacion <= 3):
                for i in Usuario.Vols:
                    if i.coche != None:
                        confirm = AppVehi.confirm_reserve(Usuario, i.coche)
                #AppVehi=True   
                if (confirm):
                    VehiOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (VehiOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del vehiculo, no se ha efectuado ningun cargo")
        else:
            VehiOk = True
            
            
        return VehiOk

#######################################################################################################################################
        
    
    def comprovacion(Usuario):
        #Llamar la funcion suma_preu para que nos diga el precio total del viaje 
        #Preu_Vol = pd.suma_preu_vols(self.Preu_Vols)
        
        
            
        if (len(Usuario.Vols)==0):
            ###F.Flights.Destination = []
            print ("Destinaciones: No hay destino y la lista esta vacia.") 
            """    
            if (len(F.Flights.Codi_Vol)==0):
                F.Flights.Codi_Vol = []
                print ("Lista de vuelos: No hay vuelo, no hay destinos.")
                    
            if (F.Flights.Preu_Vol == 0):
                F.Flights.Preu_Vol = 0
                print ("Precio: El precio del vuelo es 0, no hay destinos")
              """      
        else:
            
            count = 1
            
            Llista_p=[]
            
            Llista_d=[]
            
            Llista_c=[]
            
            Llista_pr=[]
            
            for i in Usuario.Vols:
                
                print("Vol ", count)
                
                print("Numero de passatgers: ",i.num_Passtgers)
                Llista_p.append(i.num_Passtgers)
                print("Destinació: ", i.Destination)
                Llista_d.append(i.Destination)
                print ("Codi de vol: ", i.Codi_Vol)
                Llista_c.append(i.Codi_Vol)
                print ("Preu: ", i.Preu_Vols)
                Llista_pr.append(i.Preu_Vols)
                count+=1
                
            
        return Llista_p, Llista_d, Llista_c, Llista_pr
        pass
        
        
    def con_reserva(self, Usuario):
        AppVuelo = S.Skyscanner()
        
        if Usuario.Vols != []:
            for i in Usuario.Vols:
                confirm = AppVuelo.confirm_reserve(Usuario, i)
                
        
        ##AppVuelo=True
        
        VueloOk = False
        
        """
        print (self.comprovacion())
        """
        ##self.comprovacion(Usuario)
        
        
        if (confirm == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                #AppVuelo = S.confirm_reserve(U.User, F.Flights)
                ##AppVuelo=True 
                if Usuario.Vols != []:
                    for i in Usuario.Vols:
                        confirm = AppVuelo.confirm_reserve(Usuario, i)
                if (confirm):
                    VueloOk = True
                    break
                else:
                    confirmacion = confirmacion + 1                        
            if (VueloOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del vuelo, no se ha efectuado ningun cargo")
        else:
            VueloOk = True
            
            
        return VueloOk