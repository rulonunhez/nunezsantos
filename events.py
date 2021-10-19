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

    def abrircal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error al abrir el calendario, ',error)

    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(4):
               header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
               if i == 2:
                   header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print('Eror en módulo redimensionar tabla clientes')

    def limpiaForm(self):
        var.ui.txtDni
        try:
            cajas = [var.ui.txtDni, var.ui.txtApel, var.ui.txtDir, var.ui.txtNome, var.ui.txtFechaAlta]
            for i in cajas:
                i.setText("")
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMun.setCurrentIndex(0)
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.chkTransfer.setChecked(False)
        except Exception as error:
            print('Error en módulo limpiar el formulario')