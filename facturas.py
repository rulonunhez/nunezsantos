from PyQt5 import QtWidgets

import conexion
import events
import var


class Facturas():
    def buscaCli(self):
        try:
            var.ui.txtCodFac.setText('')
            var.ui.txtFechaFac.setText('')
            dni = var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro = conexion.Conexion.buscaCliFac(dni)
            mensaje = str(registro[1]) + ', ' + str(registro[0])
            var.ui.txtClienteFac.setText(mensaje)

        except Exception as error:
            if dni:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('No existe ningun cliente con ese DNI asociado')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Debe escribir un DNI previamente para buscar')
                msg.exec()

    def altaFac(self):
        try:
            registro = [var.ui.txtDniFac.text(), var.ui.txtFechaFac.text()]
            conexion.Conexion.facturar(registro)
            conexion.Conexion.cargaTabFacturas(self)
        except Exception as error:
            print('Error en facturar', error)

    def cargaFac(self):
        try:
            # events.Eventos.limpiaFormArt(self)
            fila = var.ui.tabFacturas.selectedItems()

            if fila:
                row = [dato.text() for dato in fila]

            var.ui.txtCodFac.setText(row[0])
            var.ui.txtFechaFac.setText(row[1])
            registro = conexion.Conexion.cargaFactura(row[0])
            var.ui.txtDniFac.setText(registro[0])
            var.ui.txtClienteFac.setText(registro[2] + ', ' + registro[1])

        except Exception as error:
            print('Error en módulo cargar factura', error)