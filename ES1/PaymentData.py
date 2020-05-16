#import Bank as B
#import User

class PaymentData:

    def __init__(self, np, pv):
        self.num_persones = np 
        self.preu_vols = pv
        pass
    
def metodo_pago(metodo_pago):
    #print ("Selecciona metodo de pago: VISA o MasterCard")
    
    if ((metodo_pago == 'VISA') or (metodo_pago == 'MasterCard')):
        #print ("El metodo de pago para realizar el pago es el siguiente: " , metodo_pago)
        return metodo_pago
    else:
        #print ("Ha selecionado un metodo de pago erronio")
        print ("Error")
    
def suma_preu_total(preu_vols):
    preu_total = 0
    for i in preu_vols:
        preu_total = preu_total + i 
        
    #print ("El preu total del viatge es de: " , preu_total)
    
    return preu_total

def suma_preu_persona(num_persones, preu_vols):
    preu_total = suma_preu_total(preu_vols)
    preu_dividit = preu_total/num_persones 
    print ("El preu per persones es de: " , preu_dividit)
    
def realitza_pagament():
    #pagament_correcte = B.do_payment(User, PaymentData)
    pagament_correcte = True
    """
    if (pagament_correcte == True):
        print ("Se ha realizado correctamente el pago")
    else:
        print ("No se ha podido realizar el pago")
    """
    return pagament_correcte
    