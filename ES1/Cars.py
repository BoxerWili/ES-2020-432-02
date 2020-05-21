import PaymentData as pd

class Cars:

    def __init__(self,c, m, d, r ,p):
        #llista
        self.codi_cotxe = c
        #llista
        self.marca = m
        #llista
        self.dies = d
        
        #llista
        self.recollida = r
        
        #llista
        self.Preu_vehis = p
        
        self.Preu_vehi = pd.suma_preu_vehi(p)
        pass

def comprovacio(self):
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
    
def con_reserva(add_desti, add_preu,dele_desti, dele_preu, destinos, Preu_vehis, Preu_vehi):
    
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