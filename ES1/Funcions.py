import User as U

U.User.__init__.
class Funcions:
    def Info_User(Nom, DNI, DirPos, NumTlfn, Email):
        if((Nom or DNI or DirPos or NumTlfn or Email)==[]):    
            incorrectos = True
            continuar = False
                
            while((incorrectos) or (continuar==False)):
                print ("Introducir Nombre, DNI, direccion postal, numero de telefono, email: ")
                Nom = input()
                DNI = input()
                DirPos = input()
                NumTlfn = input()
                Email = input()
                    
                    
                #4. La aplicación valida los datos de facturación
                if((Nom or DNI or DirPos or NumTlfn or Email)==[]):
                    #Sub flujo 1 (S1): datos de facturación incorrectos o incompletos
                    print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                    incorrectos = True
                else:
                    incorrectos = False
                    continuar = True
            
            
        return continuar 
    
    
    ###############################################################################################################################
    def metodo_pago(metodo_pago):
        #print ("Selecciona metodo de pago: VISA o MasterCard")
        
        if ((metodo_pago == 'VISA') or (metodo_pago == 'MasterCard')):
            #print ("El metodo de pago para realizar el pago es el siguiente: " , metodo_pago)
            return metodo_pago
        else:
            #print ("Ha selecionado un metodo de pago erronio")
            print ("Error")
            
            
        def datos_realizar_pago(TiTarj, NumTarj, CodSeg):
            
            if((TiTarj or NumTarj or CodSeg)==[]):
                error = True
                while(error):
                    # 7. La aplicación solicita al usuario que introduzca los datos para realizar el pago
                    
                    if((TiTarj or NumTarj or CodSeg)==[]):
                        # 8. La aplicación valida los datos de pago
                        print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
                        error = True
                    else:
                        error = False 
        
        
        
    def suma_preu_vols(preu_vols):
        preu_volst = 0
        for i in preu_vols:
            preu_volst = preu_volst + i 
            
        #print ("El preu total del viatge es de: " , preu_total)
        
        return preu_volst
    
    
    def suma_preu_vehi(preu_vehi):
        preu_vehit = 0
        for i in preu_vehi:
            preu_vehit = preu_vehit + i 
            
        #print ("El preu total del viatge es de: " , preu_total)
        
        return preu_vehit
    
    def suma_preu_aloja(preu_aloja):
        preu_alojat = 0
        for i in preu_aloja:
            preu_alojat = preu_alojat + i 
            
        #print ("El preu total del viatge es de: " , preu_total)
        
        return preu_alojat
    
    
    def suma_preu_total(preu_vols, preu_vehi, preu_aloja):
        preu_total = suma_preu_vols(preu_vols) + suma_preu_vehi(preu_vehi) + suma_preu_aloja(preu_aloja)
        
        return preu_total
    
    def suma_preu_persona(num_persones, preu_vols, preu_vehi, preu_aloja):
        preu_total = suma_preu_total(preu_vols, preu_vehi, preu_aloja)
        preu_dividit = preu_total/num_persones 
        print ("El preu per persones es de: " , preu_dividit)
        
    def realitza_pagament():
        
        #pagament_correcte = B.do_payment(User, PaymentData)
        
        
        pagament_correcte = True 
        
        if (pagament_correcte == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                    
                #pagament_correcte = confirm_reserve(User, Flights)
                pagament_correcte=True   
                if (pagament_correcte):
                    pagamentOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (pagamentOk == False):
                    
                # cancelamos cargo realizado 
                    
                print ("Ha habido un problema durante el proceso de confirmacion del pagament, no se ha efectuado ningun cargo")
                    
                # 13
                # proceso de pago termina 
        else:
            pagamentOk = True
            
            
        return pagamentOk
    
    ###########################################################################################################################
    def comprovacioaloja(destinos, Preu_alojas):
        Preu_aloja = pd.suma_preu_aloja(Preu_alojas)
        
        if (len(destinos)==0):
            print ("Lista de destinos vacia")
            if (len(Preu_aloja)==0):
                print ("Lista de preu vehicles vacia")
        else:
            print ("Destinaciones:" ,destinos)
            print ("Precio:" ,Preu_aloja)
            
        return destinos, Preu_aloja
        
    def add_alojamiento(add_desti, add_preu, destinos, Preu_aloja):
        
        if((add_preu != None) and (add_desti != None)):
            destinos.append(add_desti)
            Preu_aloja = Preu_aloja + add_preu
        else:
            print ('No hi ha destinacio a afegir.')
            print('No hi ha preu a afegir.')
        
        #return cada lista que editamos
        return destinos, Preu_aloja
        
    def dele_alojamiento(dele_desti, dele_preu, destinos, Preu_aloja):
        if((dele_preu != None) and (dele_desti != None)):
            destinos.remove(dele_desti)
            Preu_aloja = Preu_aloja - dele_preu
        else:
            print ('No hi ha destinacio a eliminar.')
            print('No hi ha preu a eliminar.')
        
        #return cada lista que editamos
        return destinos, Preu_aloja
    
        
    def con_reservaaloja(add_desti, add_preu,dele_desti, dele_preu, destinos, Preu_aloja, Preu_alojas):
        
        #llamar funcion de Booking està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #AppAloja = B.confirm_reserve(User, Hotels)
        
        AlojaOk = False
        AppAloja=True
        add_aloja = False
        dele_aloja = False
        
        while (add_aloja):
            add_alojamiento(add_desti, add_preu, destinos, Preu_aloja)
            
        while (dele_aloja):
            dele_alojamiento(dele_desti, dele_preu, destinos, Preu_aloja)
            
        print (comprovacio(destinos, Preu_alojas))
        
        if (AppAloja == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                    
                #AppVuelo = confirm_reserve(User, Flights)
                AppAloja=True   
                if (AppAloja):
                    AlojaOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (AlojaOk == False):
                    
                # cancelamos cargo realizado 
                    
                print ("Ha habido un problema durante el proceso de confirmacion del alojamiento, no se ha efectuado ningun cargo")
                    
                # 13
                # proceso de pago termina 
        else:
            AlojaOk = True
            
            
        return AlojaOk
######################################################################################################################
        
    
    def comprovaciocar(self):
        #Preu_vehi = pd.suma_preu_vehi(Preu_vehis)
        
        if (len(self.codi_cotxe)==0):
            print ("Lista de codi cotxes vacia")
            if (len(self.marca)==0):
                print ("Lista marca de vehicles vacia")
            else:
                print ("Error: hay marcas selecionadas cuando no deberia")
                
            if (len(self.dies)==0):
                print ("Lista dias de vehicles vacia")
            else:
                print ("Error: hay dias selecionadas cuando no deberia")
                
            if (len(self.recollida)==0):
                print ("Lista recollida de vehicles vacia")
            else:
                print ("Error: hay recollidas selecionadas cuando no deberia")
                
            if (len(self.Preu_vehi)==0):
                print ("Lista precio de vehicles vacia")
            else:
                print ("Error: hay precios selecionadas cuando no deberia")
        else:
            print ("Codi cotxes:" ,self.codi_cotxe)
            print ("Marca:" ,self.marca)
            print ("Dies de reserva:" ,self.dies)
            print ("Destinaciones:" ,self.recollida)
            print ("Precio:" ,self.Preu_vehi)
        
        print ("Assegurat que tot es correcte i prem el boto continuar")
        
    def add_vehiculo(add_desti, add_preu, destinos, Preu_vehi):
        
        if((add_preu != None) and (add_desti != None)):
            destinos.append(add_desti)
            Preu_vehi = Preu_vehi + add_preu
        else:
            print ('No hi ha destinacio a afegir.')
            print('No hi ha preu a afegir.')
        
        #return cada lista que editamos
        return destinos, Preu_vehi
        
        
        
    def delete_vehiculo(dele_desti, dele_preu, destinos, Preu_vehi):
        if((dele_preu != None) and (dele_desti != None)):
            destinos.remove(dele_desti)
            Preu_vehi = Preu_vehi - dele_preu
        else:
            print ('No hi ha destinacio a eliminar.')
            print('No hi ha preu a eliminar.')
        
        #return cada lista que editamos
        return destinos, Preu_vehi
        
    def con_reservacar(add_desti, add_preu,dele_desti, dele_preu, destinos, Preu_vehis, Preu_vehi):
        
        #llamar funcion de Rentalcars està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #AppVuelo = R.confirm_reserve(User, Cars)
        
        VehiOk = False
        AppVehi=True
        add_vehi = False
        dele_vehi = False
        
        while (add_vehi):
            add_vehiculo(add_desti, add_preu, destinos, Preu_vehi)
            
        while (dele_vehi):
            delete_vehiculo(dele_desti, dele_preu, destinos, Preu_vehi)
            
        print (comprovacio(destinos, Preu_vehis))
        
        if (AppVehi == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                    
                #AppVuelo = confirm_reserve(User, Flights)
                AppVehi=True   
                if (AppVehi):
                    VehiOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (VehiOk == False):
                    
                # cancelamos cargo realizado 
                    
                print ("Ha habido un problema durante el proceso de confirmacion del vehiculo, no se ha efectuado ningun cargo")
                    
                # 13
                # proceso de pago termina 
        else:
            VehiOk = True
            
            
        return VehiOk
    
#######################################################################################################################################
        
    
    def comprovacion(self):
        #Llamar la funcion suma_preu para que nos diga el precio total del viaje 
        #Preu_Vol = pd.suma_preu_vols(self.Preu_Vols)
        
        print ("Numero viajeros:" ,self.num_Passatgers)
            
        if (len(self.Destination)==0):
            self.Destination = []
            print ("Destinaciones: No hay destino y la lista esta vacia.") 
                
            if (len(self.Codi_Vol)==0):
                self.Codi_Vol = []
                print ("Lista de vuelos: No hay vuelo, no hay destinos.")
                    
            if (self.Preu_Vol == 0):
                self.Preu_Vol = 0
                print ("Precio: El precio del vuelo es 0, no hay destinos")
                    
        else:
            print ("Destinaciones:" ,self.Destination)
            print ("Lista de vuelos:" ,self.Codi_Vol)
            print ("Precio:" ,self.Preu_Vol)
            
        #return self.num_Passatgers, self.Destination, self.Codi_Vol, self.Preu_Vol
        
    def append_desti(self, append_destinacion, append_codi_vol, append_preu):
            #delete_destinacion no pot ser una llista, ha de ser un unic string
            #haurem de fer el mateix pel codi vol i preu
        
        app_dest = False  
        app_codi = False
        
        #Llamar la funcion suma_preu para que nos diga el precio total del viaje 
        #Preu_Vol = pd.suma_preu_vols(Preu_Vols)
        
        if (append_destinacion != None):
            app_dest = True
            
            
        if (append_codi_vol != None):
            app_codi = True
            
            
        #PARA AÑADIR UNA TIENES QUE AÑADIR TODAS
        #suposem que els preus no varien, i hi ha rembolso total del preu.
        if((append_preu != None) and app_dest and app_codi):
            self.Destination.append(append_destinacion)
            self.Codi_Vol.append(append_codi_vol)
            self.Preu_Vol = self.Preu_Vol + append_preu
        else:
            print ('No hi ha destinacio a afegir.')
            print ('No hi ha codide vol a afegir.')
            print('No hi ha preu a afegir.')
        
        #return cada lista que editamos
        return self.Destination, self.Codi_Vol, self.Preu_Vol
        
        
    def delete_desti(self, delete_destinacion, delete_codi_vol, delete_preu):
        #delete_destinacion no pot ser una llista, ha de ser un unic string
        #haurem de fer el mateix pel codi vol i preu
        dest_del = False
        codi_del = False
        
        if delete_destinacion in self.Destination: 
            dest_del = True
            
            
        if (delete_codi_vol in self.Codi_Vol):
                codi_del = True
        
        #PARA ELIMINAR UNA TIENES QUE ELIMINAR TODAS 
        
        #suposem que els preus no varien, i hi ha rembolso total del preu.
        if(delete_preu!=0 and codi_del and dest_del):
            self.Destination.remove(delete_destinacion)
            self.Codi_Vol.remove(delete_codi_vol)
            self.Preu_Vol = self.Preu_Vol - delete_preu
        else:
            print ('No hi ha destinacio a eliminar.')
            print ('No hi ha codi de vol per eliminar.')
            print('No hi ha preu a eliminar.')
            
                
        #return cada lista que editamos
        return self.Destination, self.Codi_Vol, self.Preu_Vol
        
        
    def con_reserva(self, append_destinacion, append_codi_vol, append_preu, delete_destinacion, delete_codi_vol, delete_preu):
        
        
        #llamar funcion de Skyscanner està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #AppVuelo = S.confirm_reserve(User, Flights)
        
        VueloOk = False
        AppVuelo=True
        add_desti = False
        dele_desti = False
        
        while (add_desti):
            self.Destination, self.Codi_Vol, self.Preu_Vol = append_desti(self, append_destinacion, append_codi_vol, append_preu)
            
        while (dele_desti):
            self.Destination, self.Codi_Vol, self.Preu_Vol = delete_desti(self, delete_destinacion, delete_codi_vol, delete_preu)
            
        print (comprovacion(self))
        
        if (AppVuelo == False):
                
            # Reintentamos confirmar la reserva de vuelos... suponemos que no 
                
            confirmacion = 1
            while(confirmacion <= 3):
                    
                #AppVuelo = confirm_reserve(User, Flights)
                AppVuelo=True   
                if (AppVuelo):
                    VueloOk = True
                    break
                else:
                    confirmacion = confirmacion + 1
                        
            if (VueloOk == False):
                    
                # cancelamos cargo realizado 
                    
                print ("Ha habido un problema durante el proceso de confirmacion del vuelo, no se ha efectuado ningun cargo")
                    
                # 13
                # proceso de pago termina 
        else:
            VueloOk = True
            
            
        return VueloOk