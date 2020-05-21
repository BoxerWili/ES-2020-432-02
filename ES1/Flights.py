from . import Skyscanner
#import User
import PaymentData as pd
#import Skyscanner as S

class Flights:

    def __init__(self, n, d, c, p):
        self.num_Passtgers = n 
        
        #llista
        self.Destination = d
        
        #llista
        self.Codi_Vol = c
        
        #llista
        self.Preu_Vols = p
        
        self.Preu_Vol = pd.suma_preu_vols(p)
    
    
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
        