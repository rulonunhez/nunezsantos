# This is a sample Python script.
import events
from window import *
from windowaviso import *
import sys, var, events
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):

        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)

class Main (QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        # var.ui.btnAceptar.clicked.connect(events.Eventos.Salir)
        var.ui.pushButton.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    window.show()
    sys.exit(app.exec())
