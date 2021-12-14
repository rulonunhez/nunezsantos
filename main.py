# This is a sample Python script.
import articulos
import clients
import conexion
import events
import facturas
import informes
from window import *
from windowaviso import *
from windowcal import *
import sys, var, events, locale
from datetime import *
locale.setlocale(locale.LC_ALL, 'es-ES')

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()

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

        # Base de datos
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargaTabCli()
        conexion.Conexion.cargaTabArt(self)
        conexion.Conexion.cargaTabFacturas(self)

        # var.ui.tabPrograma.currentIndex().connect(events.Eventos.cambiaGestion)

        # Eventos de Combo Box
        clients.Clientes.cargaProv(self)
        clients.Clientes.cargaMun(self)
        var.ui.cmbProv.currentTextChanged[str].connect(clients.Clientes.cargaMun)

        # Eventos de botones sobre clientes
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSexo)
        # var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnRestablecer.clicked.connect(events.Eventos.limpiaForm)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnPDFCli.clicked.connect(informes.Informes.listadoClientes)

        # Eventos de botones sobre articulos
        var.ui.btnGrabaArticulo.clicked.connect(articulos.Articulos.guardaArt)
        var.ui.btnBajaArticulo.clicked.connect(articulos.Articulos.bajaArt)
        var.ui.btnModifArticulo.clicked.connect(articulos.Articulos.modifArt)
        var.ui.btnRestablecer_2.clicked.connect(events.Eventos.limpiaFormArt)
        var.ui.btnRestablecer_2.clicked.connect(conexion.Conexion.cargaTabArt)
        var.ui.btnBuscarArt.clicked.connect(articulos.Articulos.buscarArt)
        var.ui.btnPDFArts.clicked.connect(informes.Informes.listadoArticulos)

        # Eventos de botones sobre facturación
        var.ui.btnBuscaCliFac.clicked.connect(facturas.Facturas.buscaCli)
        var.ui.btnFechaFac.clicked.connect(events.Eventos.abrircal)
        var.ui.btnFacturar.clicked.connect(facturas.Facturas.altaFac)

        # Eventos barra de menú y herramientas
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.Abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRecuperar_Backup.triggered.connect(events.Eventos.recuperarBackup)
        var.ui.actionImprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.actionImportar_Datos.triggered.connect(events.Eventos.cargarExcel)
        var.ui.actionExportar_Datos.triggered.connect(events.Eventos.exportExcel)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)

        # Eventos caja de texto en clientes
        var.ui.txtDni.editingFinished.connect(clients.Clientes.validarDni)
        var.ui.txtDni.editingFinished.connect(clients.Clientes.buscarDni)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.cambiarAMayuscula)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.cambiarAMayuscula)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.cambiarAMayuscula)

        # Eventos caja de texto en articulos
        # var.ui.txtNombreArt.editingFinished.connect(articulos.Articulos.cambiarAMayus)

        # Eventos QTableWidget
        events.Eventos.resizeTablaCli(self)
        events.Eventos.resizeTabArts(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabArts.clicked.connect(articulos.Articulos.cargaArticulo)
        var.ui.tabArts.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFacturas.clicked.connect(facturas.Facturas.cargaFac)
        var.ui.tabFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        day = datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d de %B de %Y'))

        # Eventos menú de herramientas
        var.ui.actionbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionbarAbrirDirectorio.triggered.connect(events.Eventos.Abrir)
        var.ui.actionbarCrearBackup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionbarRestaurarBackup.triggered.connect(events.Eventos.recuperarBackup)
        var.ui.actionbarImpresora.triggered.connect(events.Eventos.imprimir)

        # Control del spinBox
        var.ui.spinEnvio.textChanged[str].connect(clients.Clientes.cargarSpin)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
