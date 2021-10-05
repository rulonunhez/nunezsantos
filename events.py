'''

Fichero de eventos generales

'''
import var, sys


class Eventos():
    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('Error en módulo "Salir"', error)