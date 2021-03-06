import locale

from PyQt5 import QtWidgets, QtCore

import conexion
import events
import var

locale.setlocale( locale.LC_ALL, '' )


class Facturas():
    def buscaCli(self):
        """

        Módulo que busca los datos de un cliente por su DNI y los imprime en la sección superior de la pestaña Facturación

        """
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
        """

        Módulo que recoge los datos de una factura y llama a un método del ficher conexion.py para darla de alta

        """
        try:
            registro = [var.ui.txtDniFac.text(), var.ui.txtFechaFac.text()]
            conexion.Conexion.facturar(registro)
            conexion.Conexion.cargaTabFacturas(self)
            codfac = conexion.Conexion.buscaCodFac(self)
            var.ui.txtCodFac.setText(str(codfac))
        except Exception as error:
            print('Error en facturar', error)

    def cargaFac(self):
        """

        Módulo que imprime los datos de una factura al seleccionarla en la tabla

        """
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
        """

        Módulo que carga en la tabla de ventas la línea para introducir una venta nueva

        :param index: Indíce de la fila de la tabla
        :type index: Int

        """
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(100,25)
            conexion.Conexion.cargarCmbproducto()
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(70,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)
            var.ui.tabVentas.setRowCount(int(index) + 1)
            var.ui.tabVentas.setCellWidget(int(index), 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(int(index), 3, var.txtCantidad)
            var.cmbProducto.currentIndexChanged.connect(Facturas.procesoVenta)
            var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta)

        except Exception as error:
            print('Error en cargar linea venta', error)

    def procesoVenta(self):
        """

        Módulo que recoge el nombre y el precio de un articulo para la carga de una línea de venta

        """
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            # precio = dato[1]
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(dato[1]))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)

        except Exception as error:
            print('Error en proceso venta ', error)

    def totalLineaVenta(self = None):
        """

        Módulo que calcula el total de la línea de venta y recoge todos los datos de esa venta para llamar a un método
        del fichero conexion.py que dará de alta esa venta

        """
        try:
            venta = []
            producto = var.cmbProducto.currentText()
            row = var.ui.tabVentas.currentRow()
            precio = var.ui.tabVentas.item(row, 2).text().replace(',', '.').replace('€', '')
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            total = round(float(precio) * cantidad, 2)
            total = locale.currency(float(total))
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total)))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            codfac = var.ui.txtCodFac.text()
            datosProducto = conexion.Conexion.obtenerCodPrecio(producto)
            codpro = datosProducto[0]
            venta.append(int(codfac))
            venta.append(int(codpro))
            venta.append(float(cantidad))
            venta.append(float(precio))
            conexion.Conexion.cargarVenta(venta)

        except Exception as error:
            print ('Error en el cálculo del total de venta', error)

