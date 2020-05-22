



class User:

    def __init__(self, Nom, DNI, DirPos, NumTlfn, Email):
        self.Nom = Nom
        self.DNI = DNI
        self.DirPos = DirPos
        self.NumTlfn = NumTlfn
        self.Email = Email
        self.Vols=[]
        
        pass
    
    def afegirFlights(self, Vol):
        
        self.Vols.append(Vol)
        
        pass
    
    def DeleteVol(self, Vol):
        Lista_aux=[]
        for i in self.Vols:
            if i.Destination !=Vol:
                Lista_aux.append(i)
                
        self.Vols=Lista_aux
        
        
        
        pass
    
    
        
    def afegirMetodePagament(self, pago):
        self.Pagament=pago
        pass