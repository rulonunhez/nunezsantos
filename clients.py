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
            mun = conexion.Conexion.cargarMun(self)
            var.ui.cmbMun.clear()
            for i in mun:
                var.ui.cmbMun.addItem(i)
        except Exception as error:
            print('Eror en módulo cargaMun, ', error)

    def selFechaAlta(fecha):
        try:
            print('La fecha seleccionada es', fecha)
        except Exception as error:
            print('Error en módulo selFechaAlta', error)

    def cargarFecha(qDate):
        try:
            data = (str(qDate.day()).zfill(2) + '/' + str(qDate.month()).zfill(2) + '/' + str(qDate.year()))
            if var.ui.tabPrograma.currentIndex() == 0:
                var.ui.txtFechaAlta.setText(str(data))
            elif var.ui.tabPrograma.currentIndex() == 1:
                var.ui.txtFechaFac.setText(str(data))
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

            newCli.append(str(var.ui.cmbProv.currentText()))
            newCli.append(str(var.ui.cmbMun.currentText()))

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

            if var.ui.spinEnvio.value() == 0:
                newCli.append(0)
            elif var.ui.spinEnvio.value() == 1:
                newCli.append(1)
            elif var.ui.spinEnvio.value() == 2:
                newCli.append(2)
            elif var.ui.spinEnvio.value() == 3:
                newCli.append(3)

            # Cargamos en la tabla
            if dniValido:
                conexion.Conexion.altaCli(newCli) #graba en la tabla de la bbdd
                conexion.Conexion.cargaTabCli() #recarga la tabla
                events.Eventos.limpiaForm(self) #limpia el formulario

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
                var.ui.txtDniFac.setText(row[0])
                var.ui.txtClienteFac.setText(row[1] + ', ' + row[2])
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

            if registro[4] == 0:
                var.ui.spinEnvio.setValue(0)
            if registro[4] == 1:
                var.ui.spinEnvio.setValue(1)
            if registro[4] == 2:
                var.ui.spinEnvio.setValue(2)
            if registro[4] == 3:
                var.ui.spinEnvio.setValue(3)

        except Exception as error:
            print('Error en módulo cargar cliente ', error)

    def modifCli(self):
        try:
            modcliente = []
            cliente = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbProv.currentText())
            modcliente.append(var.ui.cmbMun.currentText())
            if var.ui.rbtHom.isChecked():
                modcliente.append('Hombre')
            elif var.ui.rbtFem.isChecked():
                modcliente.append('Mujer')
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
            modcliente.append('; '.join(pagos))

            if var.ui.spinEnvio.value() == 0:
                modcliente.append(0)
            elif var.ui.spinEnvio.value() == 1:
                modcliente.append(1)
            elif var.ui.spinEnvio.value() == 2:
                modcliente.append(2)
            elif var.ui.spinEnvio.value() == 3:
                modcliente.append(3)

            conexion.Conexion.modifCli(modcliente)
            conexion.Conexion.cargaTabCli()
            events.Eventos.limpiaForm(self)

        except Exception as error:
            print('Error en modificación de cliente', error)

    def bajaCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargaTabCli()
            events.Eventos.limpiaForm(self)
        except Exception as error:
            print('Error en baja cliente', error)

    def cargarSpin(self):
        try:
            var.ui.spinEnvio.setMinimum(0)
            var.ui.spinEnvio.setMaximum(3)
            valor = var.ui.spinEnvio.value()
            if valor == 0:
                var.ui.lblEnvio.setText('Recogida cliente')
            elif valor == 1:
                var.ui.lblEnvio.setText('Envío express')
            elif valor == 2:
                var.ui.lblEnvio.setText('Envío normal')
            elif valor == 3:
                var.ui.lblEnvio.setText('Envío internacional')
        except Exception as error:
            print('Error en cargar spin', error)

    def buscarDni():
        try:
            dni = str(var.ui.txtDni.text())
            datos = conexion.Conexion.consultaDni(dni)
            var.ui.txtFechaAlta.setText(datos[0])
            var.ui.txtNome.setText(datos[1])
            var.ui.txtApel.setText(datos[2])
            var.ui.txtDir.setText(datos[3])

            var.ui.cmbProv.setCurrentText(str(datos[4]))
            var.ui.cmbMun.setCurrentText(str(datos[5]))

            if str(datos[6]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            if str(datos[6]) == 'Mujer':
                var.ui.rbtFem.setChecked(True)

            if 'Efectivo' in datos[7]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Transferencia' in datos[7]:
                var.ui.chkTransfer.setChecked(True)
            if 'Tarjeta' in datos[7]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Cargo cuenta' in datos[7]:
                var.ui.chkCargoCuenta.setChecked(True)



            if datos[8] == 0:
                var.ui.spinEnvio.setValue(0)
            elif datos[8] == 1:
                var.ui.spinEnvio.setValue(1)
            elif datos[8] == 2:
                var.ui.spinEnvio.setValue(2)
            elif datos[8] == 3:
                var.ui.spinEnvio.setValue(3)

        except Exception as error:
            print('Error en la busqueda del dni', error)

    # Módulos gestión base datos cliente