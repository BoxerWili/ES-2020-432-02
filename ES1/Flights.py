from Skyscanner import confirm_reserve

class Flights:

    def __init__(self, n, d, c, p):
        self.num_Passtgers = n
        
        #llista
        self.Destination = d
        
        #llista
        self.Codi_Vol = c
        
        self.Preu_Vol = p
        
    
    
def comprovacion(num_Passatgers, Destination, Codi_Vol, Preu_Vol):
    print ("Numero viajeros:" ,num_Passatgers)
        
    if (len(Destination)==0):
        print ("Destinaciones: No hay destino y la lista esta vacia.") 
            
        if (len(Codi_Vol)==0):
            print ("Lista de vuelos: No hay vuelo, no hay destinos.")
                
        if (Preu_Vol == 0):
            print ("Precio: El precio del vuelo es 0, no hay destinos")
                
    else:
        print ("Destinaciones:" ,Destination)
        print ("Lista de vuelos:" ,Codi_Vol)
        print ("Precio:" ,Preu_Vol)
    
    
def append_desti(append_destinacion, append_codi_vol, append_preu, Destination, Codi_Vol, Preu_Vol):
        #delete_destinacion no pot ser una llista, ha de ser un unic string
        #haurem de fer el mateix pel codi vol i preu
        
    if (append_destinacion != None):
        Destination.append(append_destinacion)
    else:
        print ('No hi ha destinacio a afegir.')
        
        
    if (append_codi_vol != None):
        Codi_Vol.append(append_codi_vol)
    else:
        print ('No hi ha codide vol a afegir.')
        
        
    #suposem que els preus no varien, i hi ha rembolso total del preu.
    if(append_preu != None):
        Preu_Vol = Preu_Vol + append_preu
    else:
        print('No hi ha preu a afegir.')
    
    #return cada lista que editamos
    return Destination, Codi_Vol, Preu_Vol
    
    
def delete_desti(delete_destinacion, delete_codi_vol, delete_preu, Destination, Codi_Vol, Preu_Vol):
    #delete_destinacion no pot ser una llista, ha de ser un unic string
    #haurem de fer el mateix pel codi vol i preu
    if delete_destinacion in Destination: Destination.remove(delete_destinacion)
    else:
        print ('No hi ha destinacio a eliminar.')
        
        
    if delete_codi_vol in Codi_Vol: Codi_Vol.remove(delete_codi_vol)
    else:
        print ('No hi ha codi de vol per eliminar.')
        
            
    #suposem que els preus no varien, i hi ha rembolso total del preu.
    if(delete_preu!=0):
        Preu_Vol = Preu_Vol - delete_preu
    else:
        print('No hi ha preu a eliminar.')
            
    #return cada lista que editamos
    return Destination, Codi_Vol, Preu_Vol
    
    
def con_reserva(User, Flights):
    #llamar funcion de Skyscanner està malament!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    VueloOk = False
    AppVuelo = confirm_reserve(User, Flights)
        
        
    if (AppVuelo == False):
            
        # Reintentamos confirmar la reserva de vuelos... suponemos que no 
            
        confirmacion = 1
        while(confirmacion <= 3):
                
            AppVuelo = confirm_reserve(User, Flights)
                
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
                
    else:
        VueloOk = True
        
    return VueloOk
        