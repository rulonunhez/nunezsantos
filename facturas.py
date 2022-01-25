from PyQt5 import QtWidgets, QtCore

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
            if registro:
                mensaje = str(registro[1]) + ', ' + str(registro[0])
                var.ui.txtClienteFac.setText(mensaje)
            else:
                if dni:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText('No existe ningún cliente con ese DNI asociado')
                    msg.exec()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText('Debe escribir un DNI previamente para buscar un cliente')
                    msg.exec()

        except Exception as error:
            print('Error en buscar cliente en facturas')

    def altaFac(self):
        try:
            registro = [var.ui.txtDniFac.text(), var.ui.txtFechaFac.text()]
            conexion.Conexion.facturar(registro)
            conexion.Conexion.cargaTabFacturas(self)
            codfac = conexion.Conexion.buscaCodFac(self)
            var.ui.txtCodFac.setText(str(codfac))
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

            datos = [var.ui.txtCodFac.text(), var.ui.txtFechaFac.text()]
            conexion.Conexion.cargarLineasVenta(str(var.ui.txtCodFac.text()))
            # Facturas.cargarLineaVenta(self)

        except Exception as error:
            print('Error en módulo cargar factura', error)

    def cargarLineaVenta(index):
        try:
            # index = var.ui.tabVentas.currentRow() + 1
            # index = 3
            print(index)
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(100,25)
            conexion.Conexion.cargarCmbproducto()
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(70,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(int(index), 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(int(index), 3, var.txtCantidad)
            var.cmbProducto.currentIndexChanged.connect(Facturas.procesoVenta)
            if var.txtCantidad.text() != "" and var.txtCantidad.text() is not None:
                print('a')
            # var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta(var.cmbProducto.currentText()))
            # else:
                Facturas.totalLineaVenta(var.cmbProducto.currentText())
        except Exception as error:
            print('Error en cargar linea venta', error)

    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            # codigo = dato[0]
            precio = round(dato[1], 2)
            # var.ui.tabVentas.setItem(row, 0, QtWidgets.QTableWidgetItem(str(codigo)))
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(precio)))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)

        except Exception as error:
            print ('Error en proceso venta ', error)

    def totalLineaVenta(producto):
        try:
            venta = []
            row = var.ui.tabVentas.currentRow()
            precio = var.ui.tabVentas.item(row, 2).text()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total = round(float(precio) * cantidad, 2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total)))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            codfac = var.ui.txtCodFac.text()
            # NoneType
            # codpro = var.ui.tabVentas.item(row, 0).text()
            # LLamar a método de obtener cod y precio de articulo según el nombre del combo box y recuperar el codigo para añadir una venta
            datosProducto = conexion.Conexion.obtenerCodPrecio(producto)
            codpro = datosProducto[0]
            print(codpro)
            venta.append(int(codfac))
            venta.append(int(codpro))
            venta.append(float(cantidad))
            venta.append(float(precio))
            print(venta)
            conexion.Conexion.cargarVenta(venta)

        except Exception as error:
            print ('Error en el cálculo del total de venta', error)

