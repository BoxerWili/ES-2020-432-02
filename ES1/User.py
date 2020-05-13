class User:

    def __init__(self, Nom, DNI, DirPos, NumTlfn, Email):
        self.Nom = Nom
        self.DNI = DNI
        self.DirPos = DirPos
        self.NumTlfn = NumTlfn
        self.Email = Email
        
        pass
    
    
def Info_User():
        
    incorrectos = True
    continuar = False
        
    while((incorrectos) or (continuar==False)):
        print ("Introducir Nombre, DNI, direccion postal, numero de telefono, email: ")
        Nom = input()
        DNI = input()
        DirPos = input()
        NumTlfn = input()
        Email = input()
            
        #botoncontinuar = True
        
        # 3. El usuario introduce los datos de facturación y pulsa el botón “Continuar”
        #if (botoncontinuar):
        #   continuar = True
            
        #4. La aplicación valida los datos de facturación
        if((Nom or DNI or DirPos or NumTlfn or Email)==[]):
            #Sub flujo 1 (S1): datos de facturación incorrectos o incompletos
            print ("Datos incorrectos o incompletos vuelva a introducir todos los datos: ")
            incorrectos = True
        else:
            incorrectos = False
        
    return continuar 