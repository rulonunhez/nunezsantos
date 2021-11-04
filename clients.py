import conexion
import events
from window import *
import var
from PyQt5 import QtSql


class Clientes():

    def validarDni():
        try:
            dni = var.ui.txtDni.text()
            dnivalido = False
            var.ui.txtDni.setText(dni.upper())
            table = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and table[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblValidoDNI.setText('V')
                    var.ui.txtDni.setStyleSheet('background-color: lime;')
                    dnivalido = True

                else:
                    var.ui.lblValidoDNI.setStyleSheet('QLabel {color: red;}')
                    var.ui.lblValidoDNI.setText('F')
                    var.ui.txtDni.setStyleSheet('background-color: pink;')
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidoDNI.setText('F')
                var.ui.txtDni.setStyleSheet('background-color: pink;')

            return dnivalido
        except Exception as error:
            print('Error en módulo validarDni')

    def cargaProv(self):
        try:
            provincias = conexion.Conexion.cargarProv(self)
            nombres = provincias.values()
            var.ui.cmbProv.clear()
            for i in nombres:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print('Eror en módulo cargaProv, ', error)

    def cargaMun(self):
        try:
            var.ui.cmbMun.clear()
            mun = conexion.Conexion.cargarMun()
            for i in mun:
                var.ui.cmbMun.addItem(i)
        except Exception as error:
            print('Eror en módulo cargaProv, ', error)

    def selMun(mun):
        try:
            print('Has seleccionado el municipio de', mun)
            return mun
        except Exception as error:
            print('Error en módulo selProv, ', error)

    def selFechaAlta(fecha):
        try:
            print('La fecha seleccionada es', fecha)
        except Exception as error:
            print('Error en módulo selFechaAlta', error)

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error en módulo cargarFecha ', error)

    def cambiarAMayuscula():
        texto = var.ui.txtNome.text()
        var.ui.txtNome.setText(texto.title())
        texto = var.ui.txtApel.text()
        var.ui.txtApel.setText(texto.title())
        texto = var.ui.txtDir.text()
        var.ui.txtDir.setText(texto.title())

    def guardaCli(self):
        try:
            # Preparamos el registro
            dniValido = Clientes.validarDni()

            newCli = []  # para la base de datos
            cliente = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            tabCli = []  # para tablewidget
            client = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAlta]  # para la TableView
            for i in client:
                tabCli.append(i.text())
            for i in cliente:
                newCli.append(i.text())

            newCli.append(var.ui.cmbProv.currentText())
            newCli.append(var.ui.cmbMun.currentText())

            if var.ui.rbtHom.isChecked():
                newCli.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                newCli.append('Mujer')

            pagos = []

            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo cuenta')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTransfer.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')

            pagos = set(pagos)
            tabCli.append('; '.join(pagos))
            newCli.append('; '.join(pagos))

            print(newCli)

            # Cargamos en la tabla
            if dniValido:
                conexion.Conexion.altaCli(newCli) #graba en la tabla de la bbdd
                conexion.Conexion.cargaTabCli() #recarga la tabla

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('DNI no válido. Introduzca otro')
                msg.exec()


        except Exception as error:
            print('Error en módulo guardar clientes', error)

    def cargaCli(self):
        try:
            events.Eventos.limpiaForm(self)
            fila = var.ui.tabClientes.selectedItems()
            datos = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAlta]

            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            dni = var.ui.txtDni.text

            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in row[4]:
                var.ui.chkTransfer.setChecked(True)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Cargo cuenta' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)

            registro = conexion.Conexion.cargaCli2(row[0])
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMun.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            if str(registro[3]) == 'Mujer':
                var.ui.rbtFem.setChecked(True)

        except Exception as error:
            print('Error en módulo cargar cliente ', error)

    def bajaCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargaTabCli()
        except Exception as error:
            print('Error en baja cliente', error)

    # Módulos gestión base datos cliente