from ClaseManejadorViajerosFrecuentes import ManejadorViajerosFrecuentes
from ClaseViajeroFrecuente import ViajeroFrecuente
from claseMenu import Menu

unManejadorViajeros = ManejadorViajerosFrecuentes()
unManejadorViajeros.leerCSV("viajeros.csv")

unMenu = Menu()

opcion = "0"

unMenu.ejecutarMenu(unManejadorViajeros)