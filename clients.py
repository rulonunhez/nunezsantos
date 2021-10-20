from window import *
import var, dnivalido

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

        except Exception as error:
            print('Error en módulo validarDni')

    def selSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Marcaste sexo femenino')
            if var.ui.rbtHom.isChecked():
                print('Marcaste sexo masculino')
        except Exception as error:
            print('Error en módulo selSexo')

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Has seleccionado efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Has seleccionado tarjeta')
            if var.ui.chkCargoCuenta.isChecked():
                print('Has seleccionado cargo en cuenta')
            if var.ui.chkTransfer.isChecked():
                print('Has seleccionado transferencia bancaria')
        except Exception as error:
            print('Error en módulo selPago')

    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Eror en módulo cargaProv, ', error)

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de', prov)
            return prov
        except Exception as error:
            print('Error en módulo selProv, ', error)

    def cargaMun(self):
        try:
            var.ui.cmbMun.clear()
            mun = ['', 'A', 'B', 'C', 'D']
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
            data = ('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
            var.dlgcalendar.hide()

        except Exception as error:
            print('Error en módulo cargarFecha ',error)

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
            newCli = [] # para la base de datos
            tabCli = [] # para tablewidget
            client = [var.ui.txtDni, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAlta] # para la TableView
            for i in client:
                tabCli.append(i.text())

            pagos = []
            if var.ui.chkCargoCuenta.isChecked:
                pagos.append('Cargo cuenta')
            if var.ui.chkEfectivo.isChecked:
                pagos.append('Efectivo')
            if var.ui.chkTransfer.isChecked:
                pagos.append('Transferencia')
            if var.ui.chkTarjeta.isChecked:
                pagos.append('Tarjeta')

            pagos = set(pagos)
            tabCli.append('; '.join(pagos))

            # Cargamos en la tabla
            if dnivalido:
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)

                for campo in tabCli:
                    cell = QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row, column, cell)
                    column += 1

        except Exception as error:
            print('Error en módulo guardar clientes ', error)
