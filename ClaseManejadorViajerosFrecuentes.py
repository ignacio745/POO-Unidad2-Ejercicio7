from numpy import indices
from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class ManejadorViajerosFrecuentes:
    __viajeros = []
    def __init__(self):
        self.__viajeros = []
    
    def agregarViajeroFrecuente(self, unViajeroFrecuente:ViajeroFrecuente):
        band = False
        if isinstance(unViajeroFrecuente, ViajeroFrecuente):
            self.__viajeros.append(unViajeroFrecuente)
            band = True
        return band


    def leerCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo)
        self.__viajeros = []
        agregados = 0
        total = 0
        for fila in reader:
            if fila[0].isnumeric() and fila[1].isnumeric() and fila[4].isnumeric():
                unViajeroFrecuente = ViajeroFrecuente(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
                self.agregarViajeroFrecuente(unViajeroFrecuente)
                agregados +=1
            else:
                print("[ERROR] No se pudo agregar un viajero")
            total +=1
        print("Se cargaron {0} de {1} viajeros".format(agregados, total))
        archivo.close()

    
    def listarViajeros(self):
        print("{0:<10}{1:<9}{2:<15}{3:<15}{4}".format("Numero", "DNI", "Nombre", "Apellido", "Millas"))
        for unViajero in self.__viajeros:
            if isinstance(unViajero, ViajeroFrecuente):
                print("{0:<10}{1:<9}{2:<15}{3:<15}{4}".format(unViajero.getNumero(), unViajero.getDNI(), unViajero.getNombre(), unViajero.getApellido(), unViajero.getMillas()))


    def buscarViajeroPorNumero(self, numero:int):

        i = 0
        while (i < len(self.__viajeros) and self.__viajeros[i].getNumero() != numero):
            i += 1
        if i == len(self.__viajeros):
            i = -1
        return i


    def consultarCantidadMillas(self):
        numeroViajero = int(input("Ingrese el numero de viajero: "))
        indice = self.buscarViajeroPorNumero(numeroViajero)

        if indice != -1:
            unViajero = self.__viajeros[indice]
            millas = unViajero.getMillas()
            print ("La cantidad de millas del viajero {0} es {1}".format(numeroViajero, millas))
        else:
            print("[ERROR] No se encuentra el viajero")
    

    def acumularMillas(self):
        numeroViajero = int(input("Ingrese el numero de viajero: "))

        indice = self.buscarViajeroPorNumero(numeroViajero)
        
        if indice != -1:
            millas = int(input("Ingrese el numero de millas a acumular: "))
            self.__viajeros[indice] = millas + self.__viajeros[indice]
        else:
            print ("[ERROR] No se encuentra el viajero")
        

    def canjearMillas(self):

        numeroViajero = int(input("Ingrese el numero de viajero: "))
        indice = self.buscarViajeroPorNumero(numeroViajero)
        if indice != -1:
            millas = int(input("Ingrese el numero de millas a canjear: "))
            self.__viajeros[indice] = millas - self.__viajeros[indice]
        else:
            print("[ERROR] No se encuentra el viajero")
    
    
    def guardarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo)
        for unViajero in self.__viajeros:
            if isinstance(unViajero, ViajeroFrecuente):
                datos = [unViajero.getNumero(), unViajero.getDNI(), unViajero.getNombre(), unViajero.getApellido(), unViajero.getMillas()]
                writer.writerow(datos)
        archivo.close()
    
    
    def mostrarViajerosMayorCantidadDeMillasAcumuladas(self):
        unViajero = self.__viajeros[0]
        for otroViajero in self.__viajeros:
            if unViajero < otroViajero:
                unViajero = otroViajero

        print("Los viajeros con mas millas son: ")
        print("{0:^8}{1:^11}{2:^15}{3:^15}{4:^8}".format("Numero", "DNI", "Nombre", "Apellido", "Millas"))
        for otroViajero in self.__viajeros:
            if unViajero == otroViajero:
                print("{0:^8}{1:^11}{2:^15}{3:^15}{4:^8}".format(otroViajero.getNumero(), otroViajero.getDNI(), otroViajero.getNombre(), otroViajero.getApellido(), otroViajero.getMillas()))