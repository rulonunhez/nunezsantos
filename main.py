# This is a sample Python script.
import clients
import events
from window import *
from windowaviso import *
import sys, var, events
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):

        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accept)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)

class Main (QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        # Eventos de botones
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        var.ui.pushButton.clicked.connect(events.Eventos.Salir)
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)

        # Eventos barra de menú
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        # Eventos caja de texto
        var.ui.txtDni.editingFinished.connect(clients.Clientes.validarDni)

        # Eventos de Combo Box
        clients.Clientes.cargaProv(self)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        clients.Clientes.cargaMun(self)

        # Events de Calendar
        var.ui.calendarFechaAlta.selectedDate(clients.Clientes.selFechaAlta())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    window.show()
    sys.exit(app.exec())
