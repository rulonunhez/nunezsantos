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
            nFilas = clientes.nrows
            nColumnas = clientes.ncols
            print(nFilas)
            print(nColumnas)
            i = 1
            while i <= nFilas:
                dni = clientes.cell_value(i, 0)
                apellidos = clientes.cell_value(i, 1)
                nome = clientes.cell_value(i, 2)
                direccion = clientes.cell_value(i, 3)
                provincia = clientes.cell_value(i, 4)
                sexo = clientes.cell_value(i, 5)
                query = QtSql.QSqlQuery()
                query.prepare(
                    'insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo) values (:dni, :apellidos, :nombre, :direccion, :provincia, :sexo)')
                query.bindValue(':dni', dni)
                query.bindValue(':apellidos', apellidos)
                query.bindValue(':nombre', nome)
                query.bindValue(':direccion', direccion)
                query.bindValue(':provincia', provincia)
                query.bindValue(':sexo', sexo)
                query.exec()
                i += 1
                conexion.Conexion.cargaTabCli()

        except Exception as error:
            print('Error en cargar el excel', error)

    def exportExcel(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '(*.xls);;All files (*.*)',
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
