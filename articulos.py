from PyQt5 import QtWidgets

import conexion
import events
import var

class Articulos():
    def guardaArt(self):
        try:
            newArt = [var.ui.txtNombreArt.text().title(), var.ui.txtPrecioArt.text()]
            conexion.Conexion.altaArt(newArt) # Graba el articulo en la bbdd
            conexion.Conexion.cargaTabArt(self) # Recarga la tabla
            events.Eventos.limpiaFormArt(self) # Limpia el formulario
        except Exception as error:
            print('Error en módulo guardar articulo', error)

    def cargaArticulo(self):
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
        try:
            codigo = var.ui.lblResulCodigo.text()
            conexion.Conexion.bajaArticulo(codigo)
            conexion.Conexion.cargaTabArt(self)
            events.Eventos.limpiaFormArt(self)
        except Exception as error:
            print('Error en baja articulo', error)

    def modifArt(self):
        try:
            articulo = [var.ui.lblResulCodigo.text(), var.ui.txtNombreArt.text(), var.ui.txtPrecioArt.text()]

            conexion.Conexion.modifArticulo(articulo)
            conexion.Conexion.cargaTabArt(self)
            events.Eventos.limpiaFormArt(self)

        except Exception as error:
            print('Error en modificación de articulo', error)

    def buscarArt(self):
        try:
            nombre = var.ui.txtNombreArt.text()
            var.ui.txtPrecioArt.setText('')
            var.ui.lblResulCodigo.setText('')

            conexion.Conexion.buscarArticulo(nombre)
        except Exception as error:
            print('Error buscando articulo', error)
