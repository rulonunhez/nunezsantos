import conexion
import events
import var


class Facturas():
    def buscaCli(self):
        try:
            dni = var.ui.txtDniFac.text().upper()
            var.ui.txtDniFac.setText(dni)
            registro = conexion.Conexion.buscaCliFac(dni)
            mensaje = str(registro[1]) + ', ' + str(registro[0])
            var.ui.txtClienteFac.setText(mensaje)
        except Exception as error:
            print('Error buscar cliente en facturas', error)

    def altaFac(self):
        try:
            registro = [var.ui.txtDniFac.text(), var.ui.txtFechaFac.text()]
            conexion.Conexion.facturar(registro)
        except Exception as error:
            print('Error en facturar', error)