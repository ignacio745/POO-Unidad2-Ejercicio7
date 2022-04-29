class ViajeroFrecuente:
    __num__viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    def __init__(self, num_viajero:int, dni:str, nombre:str, apellido:str, millas:int=0):
        self.__num__viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas
    
    def __str__(self):
        cadena = "Numero: {0}\nDNI: {1}\nNombre: {2}\nApellido: {3}\nMillas: {4}".format(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getMillas())
        return cadena

    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, millas:int):
        band = False
        if isinstance(millas, int):
            self.__millas_acum += millas
            band = True
        else:
            print("[ERROR] Las millas deben ser del tipo 'int'")
        return band
    
    
    def canjearMillas(self, millas:int):
        if isinstance(millas, int):
            if millas <= self.__millas_acum:
                self.__millas_acum -= millas
                print("Millas canjeadas")
            else:
                print("[ERROR] No puede canjear más millas de las que tiene")
        else:
            print("[ERROR] Las millas deben ser del tipo 'int'")

    
    def getNumero(self):
        return self.__num__viajero
    
    def getMillas(self):
        return self.__millas_acum
    
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    

    def __gt__(self, otro):
        resultado = None
        if isinstance(otro, ViajeroFrecuente):
            resultado = self.getMillas() > otro.getMillas()
        elif isinstance(otro, int):
            resultado = self.getMillas() > otro
        else:
            print("[ERROR] No se puede comparar un viajero con un {0}".format(type(otro)))
        return resultado

    
    def __eq__(self, otro):
        resultado = None
        if isinstance(otro, ViajeroFrecuente):
            resultado = self.getMillas() == otro.getMillas()
        elif isinstance(otro, int):
            resultado = self.getMillas() == otro
        else:
            print("[ERROR] No se puede comparar un viajero con un {0}".format(type(otro)))
        return resultado
    

    def __add__(self, millas):
        unViajero = None
        if isinstance(millas, int):
            unViajero = ViajeroFrecuente(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getMillas()+millas)
        else:
            print("[ERROR] No se puede sumar una instancia de la clase viajero con un {0}".format(type(millas)))
        return unViajero
    
    def __radd__(self, millas):
        return self + millas
    

    def __sub__(self, millas):
        unViajero = self
        if isinstance(millas, int) and millas <= self.getMillas():
            unViajero = ViajeroFrecuente(self.getNumero(), self.getDNI(), self.getNombre(), self.getApellido(), self.getMillas() - millas)
        else:
            print("[ERROR] No se pudo efectuar la resta")
        return unViajero
    
    def __rsub__(self, millas):
        return self - millas