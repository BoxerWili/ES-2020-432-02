##import Funcions as F



class Flights:

    def __init__(self, n, d, c, p):
        self.num_Passtgers = n 
        
        #llista
        self.Destination = d
        
        #llista
        self.Codi_Vol = c
        
        #llista
        self.Preu_Vols = p
        
        #self.Preu_Vol = F.Funcions.suma_preu_vols(self.Preu_Vols)
        
        self.coche=None
        
        pass
    
    def afegirCar(self, car):
        self.coche=car
        pass
    
    
    def deleteCar(self):
        self.coche = None
    
    def afegirHotels(self, Hotel):
        
        self.Hotel=Hotel
    
        pass
    
    def deleteHotel(self):
        
        self.Hotel=None
        
        