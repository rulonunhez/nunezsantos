'''

Fichero de eventos generales

'''
import os.path
import zipfile

import conexion
import var, sys, shutil
from windowaviso import *
from datetime import date, datetime
from zipfile import ZipFile

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
            for i in range(5):
               header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
               if i == 0 or i == 3:
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
            var.ui.txtDni.setStyleSheet('QLabel {color: white;}')

        except Exception as error:
            print('Error en módulo limpiar el formulario,', error)

    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir ciadro dialogo,', error)

    def crearBackup(self):
        try:
            fecha = datetime.today().strftime('%Y,%m,%d,%H,%M,%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options = option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))

        except Exception as error:
            print('Error en crear backup', error)

    def recuperarBackup(self):
        try:
            dirpro = os.getcwd()
            print(dirpro)
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getSaveFileName(None, 'Restaurar Copia', var.copia, '.zip', options=option)
            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall()
                bbdd.close()
                shutil.move('bbdd.sqlite', str(dirpro))
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarProv()

        except Exception as error:
            print('Error en crear backup', error)