from window import *
import var

class Clientes():
    def validarDni():
        try:
            dni = var.ui.txtDni.text()
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
                else:
                    var.ui.lblValidoDni.setStyleSheet('QLabel {color: red;}')
                    var.ui.lblValidoDni.setText('F')
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidoDNI.setText('F')

        except Exception as error:
            print('Error en módulo validarDni')