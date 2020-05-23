



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
    
    def afegirHotel(self, vol, Hotel):
        
        for i in self.Vols:
            if i.Destination == vol:
                i.afegirHotels(Hotel)
        
        pass
    
    def deleteHotel(self, vol):
        for i in self.Vols:
            if i.Destination == vol:
                i.deleteHotel()
        pass
    
    
    def afegirCar(self, vol, car):
        
        
        for i in self.Vols:
            if i.Destination == vol:
                i.afegirCar(car)
        
        
        pass
    
    
    def deleteCar(self, vol):
        for i in self.Vols:
            if i.Destination == vol:
                i.deleteCar()
        
        
        pass
    
    
        
    def afegirMetodePagament(self, pago):
        self.Pagament=pago
        pass