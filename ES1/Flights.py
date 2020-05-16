#from Skyscanner import *
#import User
import PaymentData as pd
import Skyscanner as S

class Flights:

    def __init__(self, n, d, c, p):
        self.num_Passtgers = n 
        
        #llista
        self.Destination = d
        
        #llista
        self.Codi_Vol = c
        
        #llista
        self.Preu_Vols = p
        
    
    
def comprovacion(num_Passatgers, Destination, Codi_Vol, Preu_Vols):
    #Llamar la funcion suma_preu para que nos diga el precio total del viaje 
    Preu_Vol = pd.suma_preu_total(Preu_Vols)
    
    #print ("Numero viajeros:" ,num_Passatgers)
        
    if (len(Destination)==0):
        Destination = []
        #print ("Destinaciones: No hay destino y la lista esta vacia.") 
            
        if (len(Codi_Vol)==0):
            Codi_Vol = []
            #print ("Lista de vuelos: No hay vuelo, no hay destinos.")
                
        if (Preu_Vol == 0):
            Preu_Vol = 0
            #print ("Precio: El precio del vuelo es 0, no hay destinos")
                
    #else:
        #print ("Destinaciones:" ,Destination)
        #print ("Lista de vuelos:" ,Codi_Vol)
        #print ("Precio:" ,Preu_Vol)
        
    return num_Passatgers, Destination, Codi_Vol, Preu_Vol
    
def append_desti(append_destinacion, append_codi_vol, append_preu, Destination, Codi_Vol, Preu_Vols):
        #delete_destinacion no pot ser una llista, ha de ser un unic string
        #haurem de fer el mateix pel codi vol i preu
    
    app_dest = False  
    app_codi = False
    
    #Llamar la funcion suma_preu para que nos diga el precio total del viaje 
    Preu_Vol = pd.suma_preu_total(Preu_Vols)
    
    if (append_destinacion != None):
        app_dest = True
        
        
    if (append_codi_vol != None):
        app_codi = True
        
        
    #PARA AÑADIR UNA TIENES QUE AÑADIR TODAS
    #suposem que els preus no varien, i hi ha rembolso total del preu.
    if((append_preu != None) and app_dest and app_codi):
        Destination.append(append_destinacion)
        Codi_Vol.append(append_codi_vol)
        Preu_Vol = Preu_Vol + append_preu
    else:
        print ('No hi ha destinacio a afegir.')
        print ('No hi ha codide vol a afegir.')
        print('No hi ha preu a afegir.')
    
    #return cada lista que editamos
    return Destination, Codi_Vol, Preu_Vol
    
    
def delete_desti(delete_destinacion, delete_codi_vol, delete_preu, Destination, Codi_Vol, Preu_Vol):
    #delete_destinacion no pot ser una llista, ha de ser un unic string
    #haurem de fer el mateix pel codi vol i preu
    dest_del = False
    codi_del = False
    
    if delete_destinacion in Destination: 
        dest_del = True
        
        
    if (delete_codi_vol in Codi_Vol):
            codi_del = True
    
    #PARA ELIMINAR UNA TIENES QUE ELIMINAR TODAS 
    
    #suposem que els preus no varien, i hi ha rembolso total del preu.
    if(delete_preu!=0 and codi_del and dest_del):
        Destination.remove(delete_destinacion)
        Codi_Vol.remove(delete_codi_vol)
        Preu_Vol = Preu_Vol - delete_preu
    else:
        print ('No hi ha destinacio a eliminar.')
        print ('No hi ha codi de vol per eliminar.')
        print('No hi ha preu a eliminar.')
        
            
    #return cada lista que editamos
    return Destination, Codi_Vol, Preu_Vol
    
    
def con_reserva(User, Flights):
    
    #llamar funcion de Skyscanner està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #VueloOk = False
    AppVuelo = S.confirm_reserve(User, Flights)
    #AppVuelo=True
        
    if (AppVuelo == False):
        """    
        # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            
        confirmacion = 1
        while(confirmacion <= 3):
                
            #AppVuelo = confirm_reserve(User, Flights)
            AppVuelo=True   
            if (AppVuelo):
                VueloOk = True
                break
            else:
                confirmacion=confirmacion + 1
                    
        if (confirmacion != 1):
                
            # cancelamos cargo realizado 
                
            print ("Ha habido un problema durante el proceso de confirmacion, no se ha efectuado ningun cargo")
                
            # 13
            # proceso de pago termina 
        """
        print ("Ha habido un problema durante el proceso de confirmacion, no se ha efectuado ningun cargo")

    else:
        print ("Se ha realizado correctamente el pago")
        
    
        