'''

Fichero de eventos generales

'''
import var, sys
from windowaviso import *

class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en módulo "Salir"', error)