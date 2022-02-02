'''

Fichero de eventos generales

'''
import os.path
import zipfile
# from __future__ import print_function
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
import xlwt as xlwt
from PyQt5.QtWidgets import QMessageBox

import conexion
import var, sys, shutil
from windowaviso import *
from datetime import date, datetime
from zipfile import ZipFile
from PyQt5 import QtPrintSupport, QtSql
import xlrd


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
            print('Error al abrir el calendario, ', error)

    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print('Eror en módulo redimensionar tabla clientes')

    def resizeTabArts(self):
        try:
            header = var.ui.tabArts.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
                if i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        except Exception as error:
            print('Eror en módulo redimensionar tabla clientes')

    def resizeTabFacturas(self):
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print('Eror en módulo redimensionar tabla clientes')

    def resizeTabVentas(self):
        try:
            header = var.ui.tabVentas.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
                if i == 1 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print('Eror en módulo redimensionar tabla ventas')

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
            var.ui.spinEnvio.setValue(0)
            var.ui.txtDni.setStyleSheet('QLabel {color: white;}')

        except Exception as error:
            print('Error en módulo limpiar el formulario,', error)

    def limpiaFormArt(self):
        try:
            cajas = [var.ui.lblResulCodigo, var.ui.txtNombreArt, var.ui.txtPrecioArt]
            for i in cajas:
                i.setText("")

        except Exception as error:
            print('Error en módulo limpiar el formulario,', error)

    def limpiaFormFac(self):
        try:
            cajas = [var.ui.txtDniFac, var.ui.txtClienteFac, var.ui.txtCodFac, var.ui.txtFechaFac]
            for i in cajas:
                i.setText("")
            conexion.Conexion.cargarLineasVenta(0)

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
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip',
                                                                options=option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))

        except Exception as error:
            print('Error en crear backup', error)

    def recuperarBackup(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia', '', '*.zip;;ALL', options=option)
            if var.dlgabrir.Accepted and filename != '':
                file = filename[0]
                print(file)
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargaTabCli()
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('AViso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Copia de seguridad creada')
            msg.exec()

        except Exception as error:
            print('Error en crear backup', error)

    def imprimir(self):
        try:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec():
                printDialog.show()
        except Exception as error:
            print('Error en impresión', error)

    def cargarExcel(self):
        try:
            documento = xlrd.open_workbook("DATOSCLIENTES.xls")
            clientes = documento.sheet_by_index(0)
            filas_clientes = clientes.nrows
            columnas_clientes = clientes.ncols
            print("Filas: " + str(filas_clientes) + ". Columnas: " + str(columnas_clientes))

            dirpro = os.getcwd()
            print(dirpro)
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, 'Cargar datos desde Excel', "", '*.xls;;All ',
                                                    options=option)
            if var.dlgabrir.Accepted and filename != "":
                dnis = []
                query = QtSql.QSqlQuery()
                query.prepare('select dni from clientes')
                if query.exec_():
                    while query.next():
                        dnis.append(query.value(0))

                for i in range(clientes.nrows - 1):
                    c1 = clientes.cell_value(i + 1, 0)
                    c2 = clientes.cell_value(i + 1, 1)
                    c3 = clientes.cell_value(i + 1, 2)
                    c4 = clientes.cell_value(i + 1, 3)
                    c5 = clientes.cell_value(i + 1, 4)
                    c6 = clientes.cell_value(i + 1, 5)

                    if c1 in dnis:
                        query.prepare('update clientes set apellidos = :apellidos, nombre = :nombre, '
                                      'direccion = :direccion, provincia = :provincia, sexo = :sexo '
                                      'where dni = :dni')
                        query.bindValue(':dni', c1)
                        query.bindValue(':apellidos', c2)
                        query.bindValue(':nombre', c3)
                        query.bindValue(':direccion', c4)
                        query.bindValue(':provincia', c5)
                        query.bindValue(':sexo', c6)
                        query.exec()
                    else:
                        query.prepare(
                            'insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo)'
                            'VALUES (:dni, :apellidos, :nombre, :direccion,:provincia, :sexo)')
                        query.bindValue(':dni', c1)
                        query.bindValue(':apellidos', c2)
                        query.bindValue(':nombre', c3)
                        query.bindValue(':direccion', c4)
                        query.bindValue(':provincia', c5)
                        query.bindValue(':sexo', c6)
                        query.exec()

            conexion.Conexion.cargaTabCli()
            Eventos.limpiaForm(self)

        except Exception as error:
            print('Error al cargar datos del excel ', error)


    def exportExcel(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia,
                                                                '(*.xls);;All files (*.*)',
                                                                options=option)
            wb = xlwt.Workbook()
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'APELIDOS')
            sheet1.write(0, 2, 'NOME')
            sheet1.write(0, 3, 'DIRECCION')
            sheet1.write(0, 4, 'PROVINCIA')
            sheet1.write(0, 5, 'SEXO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    sheet1.write(f, 0, query.value(0))
                    sheet1.write(f, 1, query.value(2))
                    sheet1.write(f, 2, query.value(3))
                    sheet1.write(f, 3, query.value(4))
                    sheet1.write(f, 4, query.value(5))
                    sheet1.write(f, 5, query.value(7))
                    f += 1
            wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ', error)

    def cambiaGestion(self):
        if var.ui.tabPrograma.currentIndex() == 0:
            var.ui.lblClientes.setText("XESTIÓN CLIENTES")
        elif var.ui.tabPrograma.currentIndex() == 1:
            var.ui.txtFechaFac.setText("FACTURACIÓN")
        elif var.ui.tabPrograma.currentIndex() == 2:
            var.ui.txtFechaFac.setText("XESTIÓN ARTÍCULOS")

# def copiaDrive(self):
#     """Shows basic usage of the Drive v3 API.
#         Prints the names and ids of the first 10 files the user has access to.
#         """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     service = build('drive', 'v3', credentials=creds)
#
#     # Call the Drive v3 API
#     results = service.files().list(
#         pageSize=10, fields="nextPageToken, files(id, name)").execute()
#     items = results.get('files', [])
#
#     if not items:
#         print('No files found.')
#     else:
#         print('Files:')
#         for item in items:
#             print(u'{0} ({1})'.format(item['name'], item['id']))
