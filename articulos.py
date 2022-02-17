from PyQt5 import QtWidgets

import conexion
import events
import var
import locale
locale.setlocale( locale.LC_ALL, '' )

class Articulos():
    def guardaArt(self):
        """

        Módulo que recoge los datos de un producto y se los envía al fichero conexion.py para darlos de alta en la bbdd

        """
        try:
            precio = var.ui.txtPrecioArt.text().replace(',', '.')
            precio = locale.currency(float(precio))
            newArt = [var.ui.txtNombreArt.text().title(), precio]
            conexion.Conexion.altaArt(newArt) # Graba el articulo en la bbdd
            conexion.Conexion.cargaTabArt(self) # Recarga la tabla
            events.Eventos.limpiaFormArt(self) # Limpia el formulario
        except Exception as error:
            print('Error en módulo guardar articulo', error)

    def cargaArticulo(self):
        """

        Módulo que carga los productos en la tabla

        """
        try:
            events.Eventos.limpiaFormArt(self)
            fila = var.ui.tabArts.selectedItems()

            if fila:
                row = [dato.text() for dato in fila]

            var.ui.lblResulCodigo.setText(row[0])
            var.ui.txtNombreArt.setText(row[1])
            var.ui.txtPrecioArt.setText(row[2])

        except Exception as error:
            print('Error en módulo cargar articulo', error)

    def bajaArt(self):
        """

        Módulo que recoge el código de un producto y llama a un método del fichero conexion.py para darlo de baja
        en la bbdd

        """
        try:
            codigo = var.ui.lblResulCodigo.text()
            conexion.Conexion.bajaArticulo(codigo)
            conexion.Conexion.cargaTabArt(self)
            events.Eventos.limpiaFormArt(self)
        except Exception as error:
            print('Error en baja articulo', error)

    def modifArt(self):
        """

        Módulo que recoge los datos de un producto a modificar y llama a un método del fichero conexion.py para
        actualizarlo en la bbdd

        """
        try:
            articulo = [var.ui.lblResulCodigo.text(), var.ui.txtNombreArt.text(), var.ui.txtPrecioArt.text()]

            conexion.Conexion.modifArticulo(articulo)
            conexion.Conexion.cargaTabArt(self)
            events.Eventos.limpiaFormArt(self)

        except Exception as error:
            print('Error en modificación de articulo', error)

    def buscarArt(self):
        """

        Módulo que busca un producto por su nombre e imprime los datos en la tabla

        """
        try:
            nombre = var.ui.txtNombreArt.text()
            var.ui.txtPrecioArt.setText('')
            var.ui.lblResulCodigo.setText('')

            conexion.Conexion.buscarArticulo(nombre)
        except Exception as error:
            print('Error buscando articulo', error)
