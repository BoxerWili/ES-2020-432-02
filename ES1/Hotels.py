import PaymentData as pd

class Hotels:

    def __init__(self, d, p):
        #llista
        self.destinos = d
        
        #llista
        self.Preu_alojas = p
        pass

def comprovacio(destinos, Preu_alojas):
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

    
def con_reserva(add_desti, add_preu,dele_desti, dele_preu, destinos, Preu_aloja, Preu_alojas):
    
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