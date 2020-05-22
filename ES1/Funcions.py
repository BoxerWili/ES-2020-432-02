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
        if((User.Nom or User.DNI or User.DirPos or User.NumTlfn or User.Email)==[]):    
            incorrectos = True
            continuar = False
                
            while((incorrectos) or (continuar==False)):
                print ("Introducir Nombre, DNI, direccion postal, numero de telefono, email: ")
                User.Nom = input()
                User.DNI = input()
                User.DirPos = input()
                User.NumTlfn = input()
                User.Email = input()
                        
                        
                #4. La aplicación valida los datos de facturación
                if((User.Nom or User.DNI or User.DirPos or User.NumTlfn or User.Email)==[]):
                    #Sub flujo 1 (S1): datos de facturación incorrectos o incompletos
                    print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                    incorrectos = True
                    continuar = False
                else:
                    incorrectos = False
                    continuar = True
        else:
            continuar = True
            
            
        return continuar #TRUE OR FALSE
    
    #Enteoria correcto
    ###############################################################################################################################
    def metodo_pago(Usuario):
        #print ("Selecciona metodo de pago: VISA o MasterCard")
        
        if ((P.PaymentData.tipus_targeta == 'VISA') or (P.PaymentData.tipus_targeta == 'MasterCard')):
            #print ("El metodo de pago para realizar el pago es el siguiente: " , metodo_pago)
            return P.PaymentData.tipus_targeta
        else:
            #print ("Ha selecionado un metodo de pago erronio")
            print ("Error no has introduit correctament el tipus de targeta.")
            
            
    def datos_realizar_pago():
        if((P.PaymentData.nom_titular or P.PaymentData.num_targeta or P.PaymentData.codi_seguretat)==[]):
            error = True
            while(error):
                print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                P.PaymentData.nom_titular = input()
                P.PaymentData.num_targeta = input()
                P.PaymentData.codi_seguretat = input()
                if((P.PaymentData.nom_titular or P.PaymentData.num_targeta or P.PaymentData.codi_seguretat)==[]):
                    error = True
                else:
                    error = False 
        else:
            error = False
        
        return error #TRUE OR FALSE
    
    def suma_preu_vols():
        preu_volst = 0
        for i in F.Flights.Preu_vol:
            preu_volst = preu_volst + i 

        return preu_volst
    
    
    def suma_preu_vehi():
        preu_vehit = 0
        for i in C.Cars.Preu_vehi:
            preu_vehit = preu_vehit + i 

        return preu_vehit
    
    def suma_preu_aloja():
        preu_alojat = 0
        for i in H.Hotels.Preu_aloja:
            preu_alojat = preu_alojat + i 
            
        return preu_alojat
    
    
    def suma_preu_total(self):
        preu_final = self.suma_preu_persona() 
        preu_total = preu_final*F.Flights.num_Passtgers 
        #print ("El preu per persones es de: " , preu_total)
        return preu_total
    
    def suma_preu_persona(self):
        preu_persona = self.suma_preu_vols() + self.suma_preu_vehi() + self.suma_preu_aloja()
        return preu_persona
        
        
    def realitza_pagament():
        
        pagament_correcte = B.do_payment(U.User, P.PaymentData)
        #pagament_correcte = True 
        if (pagament_correcte == False):
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            confirmacion = 1
            while(confirmacion <= 3):
                    
                pagament_correcte = B.do_payment(U.User, P.PaymentData)
                #pagament_correcte=True   
                if (pagament_correcte):
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
    
    def comprovacioaloja():
        if (len(H.Hotel.codi_hotel)==0):
            print ("Lista de codi hotels vacia")
            if (len(H.Hotels.nom_hotel)==0):
                print ("Lista nom hotels vacia")
            else:
                print ("Error: hay hoteles selecionadas cuando no deberia")
                
            if (len(H.Hotels.num_persones)==0):
                print ("No hay personas")
            else:
                print ("Error: hay numero de personas selecionadas cuando no deberia")
                
            if (len(H.Hotels.num_habitacions)==0):
                print ("Lista habitaciones  vacia")
            else:
                print ("Error: hay habitaciones selecionadas cuando no deberia")
                
            if (len(H.Hotels.dies)==0):
                print ("Lista dias de alojamientos vacia")
            else:
                print ("Error: hay dias de alojamientos selecionadas cuando no deberia")
            if (len(H.Hotels.Preu_alojas)==0):
                print ("Lista precio de alojamientos vacia")
            else:
                print ("Error: hay alojamientos selecionadas cuando no deberia")
        else:
            print ("Codi hotel:" ,H.Hotel.codi_hotel)
            print ("Nombre hotel:" ,H.Hotels.nom_hotel)
            print ("Numero de personas:" ,H.Hotels.num_persones)
            print ("Numero habitaciones:" ,H.Hotels.num_habitacions)
            print ("Dias:" ,H.Hotels.dies)
            print ("Precio:" ,H.Hotels.Preu_alojas)
        
        print ("Assegurat que tot es correcte i prem el boto continuar")
        
       
    def add_alojamiento(self, add_codi, add_nom, add_numpers, add_hab, add_dies, add_preu):
        Preu_aloja = self.suma_preu_aloja()
        if((add_codi != None) and (add_nom != None) and (add_numpers != None) and (add_hab != None) and (add_dies != None) and (add_preu != None)):
            H.Hotels.codi_hotel.append(add_codi)
            H.Hotels.nom_hotel.append(add_nom)
            H.Hotels.num_persones.append(add_numpers)
            H.Hotels.num_habitacions.append(add_hab)
            H.Hotels.dies.append(add_dies)
            Preu_aloja = Preu_aloja + add_preu
        else:
            print ('Te falta llenar alguno de los campos obligatorios')

        #return cada lista que editamos
        return H.Hotels.codi_hotel, H.Hotels.nom_hotel, H.Hotels.num_habitacions, H.Hotels.dies, Preu_aloja
         
    def dele_alojamiento(self, dele_codi, dele_nom, dele_numpers, dele_hab, dele_dies, dele_preu):
        Preu_aloja = self.suma_preu_aloja()
        if((dele_codi != None) and (dele_nom != None) and (dele_numpers != None) and (dele_hab != None) and (dele_dies != None) and (dele_preu != None)):
            H.Hotels.codi_hotel.remove(dele_codi)
            H.Hotels.nom_hotel.remove(dele_nom)
            H.Hotels.num_persones.remove(dele_numpers)
            H.Hotels.num_habitacions.remove(dele_hab)
            H.Hotels.dies.remove(dele_dies)
            Preu_aloja = Preu_aloja - dele_preu
        else:
            print ('Te falta llenar alguno de los campos obligatorios')

        #return cada lista que editamos
        return H.Hotels.codi_hotel, H.Hotels.nom_hotel, H.Hotels.num_habitacions, H.Hotels.dies, Preu_aloja
    
    """
    def con_reservaaloja(self):
        #Preu_aloja = self.suma_preu_aloja()
        #llamar funcion de Booking està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        AppAloja = Bo.Booking.confirm_reserve(U.User, H.Hotels)
        #AppAloja=True
        
        AlojaOk = False
        
        print (self.comprovacioaloja())
        
        if (AppAloja == False):
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            confirmacion = 1
            while(confirmacion <= 3):
                AppAloja = Bo.Booking.confirm_reserve(U.User, H.Hotels)
                #AppAloja=True   
                if (AppAloja):
                    AlojaOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (AlojaOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del alojamiento, no se ha efectuado ningun cargo")
        else:
            AlojaOk = True
            
        return AlojaOk #TRUE OR FALSE
        """    
    
######################################################################################################################
        
    def comprovaciocar():
        
        #Preu_vehi = pd.suma_preu_vehi(Preu_vehis)
        
        if (len(C.Cars.codi_cotxe)==0):
            print ("Lista de codi cotxes vacia")
            if (len(C.Cars.marca)==0):
                print ("Lista marca de vehicles vacia")
            else:
                print ("Error: hay marcas selecionadas cuando no deberia")
                
            if (len(C.Cars.dies)==0):
                print ("Lista dias de vehicles vacia")
            else:
                print ("Error: hay dias selecionadas cuando no deberia")
                
            if (len(C.Cars.recollida)==0):
                print ("Lista recollida de vehicles vacia")
            else:
                print ("Error: hay recollidas selecionadas cuando no deberia")
                
            if (len(C.Cars.Preu_vehi)==0):
                print ("Lista precio de vehicles vacia")
            else:
                print ("Error: hay precios selecionadas cuando no deberia")
        else:
            print ("Codi cotxes:" ,C.Cars.codi_cotxe)
            print ("Marca:" ,C.Cars.marca)
            print ("Dies de reserva:" ,C.Cars.dies)
            print ("Destinaciones:" ,C.Cars.recollida)
            print ("Precio:" ,C.Cars.Preu_vehi)
        
        print ("Assegurat que tot es correcte i prem el boto continuar")
        
  
    def add_vehiculo(self, add_codi, add_marca, add_dies, add_recollida, add_preu):
        Preu_vehi = self.suma_preu_vehi()
        if((add_codi != None) and (add_marca != None) and (add_recollida != None) and (add_dies != None) and (add_preu != None)):
            C.Cars.codi_cotxe.append(add_codi)
            C.Cars.marca.append(add_marca)
            C.Cars.recollida.append(add_recollida)
            C.Cars.dies.append(add_dies)
            Preu_vehi = Preu_vehi + add_preu
        else:
            print ('Te falta llenar alguno de los campos obligatorios')

        #return cada lista que editamos
        return C.Cars.codi_cotxe, C.Cars.marca, C.Cars.recollida, C.Cars.dies, Preu_vehi
        
          
    def delete_vehiculo(self, dele_codi, dele_marca, dele_dies, dele_recollida, dele_preu):
        Preu_vehi = self.suma_preu_vehi()
        if((dele_codi != None) and (dele_marca != None) and (dele_recollida != None) and (dele_dies != None) and (dele_preu != None)):
            C.Cars.codi_cotxe.remove(dele_codi)
            C.Cars.marca.remove(dele_marca)
            C.Cars.recollida.remove(dele_recollida)
            C.Cars.dies.remove(dele_dies)
            Preu_vehi = Preu_vehi - dele_preu
        else:
            print ('Te falta llenar alguno de los campos obligatorios')

        #return cada lista que editamos
        return C.Cars.codi_cotxe, C.Cars.marca, C.Cars.recollida, C.Cars.dies, Preu_vehi
    
    
    def con_reservacar(self, Usuario):
        #Preu_vehi = self.suma_preu_vehi()
        AppVehi = R.Rentalcars.confirm_reserve(Usuario, C.Cars)
        #AppVehi=True
        
        VehiOk = False
        
        ##print (self.comprovaciocar())
        
        if (AppVehi == False):
            confirmacion = 1
            while(confirmacion <= 3):
                AppVehi = R.Rentalcars.confirm_reserve(U.User, C.Cars)
                #AppVehi=True   
                if (AppVehi):
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
                
            
            """ 
            print ("Destinaciones:" ,F.Flights.Destination)
            print ("Lista de vuelos:" ,F.Flights.Codi_Vol)
            print ("Precio:" ,F.Flights.Preu_Vol)
            """
        return Llista_p, Llista_d, Llista_c, Llista_pr
        pass
        
    def append_desti(self, append_destinacion, append_codi_vol, append_preu):
        Preu_Vol = self.suma_preu_vols()
            #delete_destinacion no pot ser una llista, ha de ser un unic string        
        app_dest = False  
        app_codi = False
        
        if (append_destinacion != None):
            app_dest = True

        if (append_codi_vol != None):
            app_codi = True
            
        #PARA AÑADIR UNA TIENES QUE AÑADIR TODAS
        #suposem que els preus no varien, i hi ha rembolso total del preu.
        if((append_preu != None) and app_dest and app_codi):
            F.Flights.Destination.append(append_destinacion)
            F.Flights.Codi_Vol.append(append_codi_vol)
            Preu_Vol = Preu_Vol + append_preu
        else:
            print ('Te falta alguno de los campos obligatorios por llenar.')
        
        #return cada lista que editamos
        return F.Flights.Destination, F.Flights.Codi_Vol, Preu_Vol
        
        
    def delete_desti(self, delete_destinacion, delete_codi_vol, delete_preu):
        Preu_Vol = self.suma_preu_vols()
        #delete_destinacion no pot ser una llista, ha de ser un unic string
        #haurem de fer el mateix pel codi vol i preu
        dest_del = False
        codi_del = False
        
        if delete_destinacion in F.Flights.Destination: 
            dest_del = True
            
        if (delete_codi_vol in F.Flights.Codi_Vol):
                codi_del = True
        
        #PARA ELIMINAR UNA TIENES QUE ELIMINAR TODAS 
        
        #suposem que els preus no varien, i hi ha rembolso total del preu.
        if(delete_preu!=0 and codi_del and dest_del):
            F.Flights.Destination.remove(delete_destinacion)
            F.Flights.Codi_Vol.remove(delete_codi_vol)
            Preu_Vol = Preu_Vol - delete_preu
        else:
            print ('No hi ha destinacio a eliminar.')
            print ('No hi ha codi de vol per eliminar.')
            print('No hi ha preu a eliminar.')
            
                
        #return cada lista que editamos
        return F.Flights.Destination, F.Flights.Codi_Vol, Preu_Vol
        
        
    def con_reserva(self, Usuario):
        #AppVuelo = S.confirm_reserve(Usuario, Usuario.Vols)
        AppVuelo=True
        
        VueloOk = False
        
        """
        print (self.comprovacion())
        """
        self.comprovacion(Usuario)
        
        
        if (AppVuelo == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                #AppVuelo = S.confirm_reserve(U.User, F.Flights)
                AppVuelo=True   
                if (AppVuelo):
                    VueloOk = True
                    break
                else:
                    confirmacion = confirmacion + 1                        
            if (VueloOk == False):
                print ("Ha habido un problema durante el proceso de confirmacion del vuelo, no se ha efectuado ningun cargo")
        else:
            VueloOk = True
            
            
        return VueloOk