# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 866)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(360, -10, 271, 51))
        self.lblClientes.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lblClientes.setPalette(palette)
        self.lblClientes.setStyleSheet("font: 22pt \"Palatino Linotype\";\n"
"color: rgb(170, 0, 0);\n"
"")
        self.lblClientes.setObjectName("lblClientes")
        self.tabPrograma = QtWidgets.QTabWidget(self.centralwidget)
        self.tabPrograma.setGeometry(QtCore.QRect(10, 20, 1001, 801))
        self.tabPrograma.setObjectName("tabPrograma")
        self.tabClientes_2 = QtWidgets.QWidget()
        self.tabClientes_2.setObjectName("tabClientes_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tabClientes_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(100, 150, 741, 21))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblFormaPago = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lblFormaPago.setObjectName("lblFormaPago")
        self.horizontalLayout_5.addWidget(self.lblFormaPago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.setExclusive(False)
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_5.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_5.addWidget(self.chkTarjeta)
        self.chkCargoCuenta = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.chkCargoCuenta.setObjectName("chkCargoCuenta")
        self.chkGroupPago.addButton(self.chkCargoCuenta)
        self.horizontalLayout_5.addWidget(self.chkCargoCuenta)
        self.chkTransfer = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.chkTransfer.setObjectName("chkTransfer")
        self.chkGroupPago.addButton(self.chkTransfer)
        self.horizontalLayout_5.addWidget(self.chkTransfer)
        self.btnGrabaCli = QtWidgets.QPushButton(self.tabClientes_2)
        self.btnGrabaCli.setGeometry(QtCore.QRect(300, 190, 81, 23))
        self.btnGrabaCli.setObjectName("btnGrabaCli")
        self.btnCalendar = QtWidgets.QPushButton(self.tabClientes_2)
        self.btnCalendar.setGeometry(QtCore.QRect(760, 30, 81, 23))
        self.btnCalendar.setText("")
        self.btnCalendar.setAutoDefault(False)
        self.btnCalendar.setDefault(False)
        self.btnCalendar.setFlat(False)
        self.btnCalendar.setObjectName("btnCalendar")
        self.pushButton = QtWidgets.QPushButton(self.tabClientes_2)
        self.pushButton.setGeometry(QtCore.QRect(550, 190, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tabClientes_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 90, 751, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblDir = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lblDir.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_3.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.txtDir.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDir.sizePolicy().hasHeightForWidth())
        self.txtDir.setSizePolicy(sizePolicy)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_3.addWidget(self.txtDir)
        spacerItem = QtWidgets.QSpacerItem(60, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblProv = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProv.sizePolicy().hasHeightForWidth())
        self.lblProv.setSizePolicy(sizePolicy)
        self.lblProv.setObjectName("lblProv")
        self.horizontalLayout_3.addWidget(self.lblProv)
        self.cmbProv = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_3.addWidget(self.cmbProv)
        self.lblMun = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.lblMun.setObjectName("lblMun")
        self.horizontalLayout_3.addWidget(self.lblMun)
        self.cmbMun = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_3.addWidget(self.cmbMun)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tabClientes_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 59, 751, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblApel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_2.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_2.addWidget(self.txtApel)
        spacerItem1 = QtWidgets.QSpacerItem(60, 15, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lblNome = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lblNome.setObjectName("lblNome")
        self.horizontalLayout_2.addWidget(self.lblNome)
        self.txtNome = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_2.addWidget(self.txtNome)
        self.lblRestablecer = QtWidgets.QLabel(self.tabClientes_2)
        self.lblRestablecer.setGeometry(QtCore.QRect(690, 730, 141, 41))
        self.lblRestablecer.setObjectName("lblRestablecer")
        self.tabClientes = QtWidgets.QTableWidget(self.tabClientes_2)
        self.tabClientes.setGeometry(QtCore.QRect(80, 220, 800, 500))
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(5)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        self.tabClientes.verticalHeader().setDefaultSectionSize(40)
        self.btnRestablecer = QtWidgets.QPushButton(self.tabClientes_2)
        self.btnRestablecer.setGeometry(QtCore.QRect(830, 730, 51, 41))
        self.btnRestablecer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/img/Recarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestablecer.setIcon(icon)
        self.btnRestablecer.setObjectName("btnRestablecer")
        self.line = QtWidgets.QFrame(self.tabClientes_2)
        self.line.setGeometry(QtCore.QRect(100, 170, 761, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtFechaAlta = QtWidgets.QLineEdit(self.tabClientes_2)
        self.txtFechaAlta.setGeometry(QtCore.QRect(600, 30, 151, 20))
        self.txtFechaAlta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtFechaAlta.setObjectName("txtFechaAlta")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tabClientes_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 30, 261, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDNI = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblDNI.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"")
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout.addWidget(self.lblDNI)
        self.txtDni = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout.addWidget(self.txtDni)
        self.lblValidoDNI = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.horizontalLayout.addWidget(self.lblValidoDNI)
        self.lblFechaAlta = QtWidgets.QLabel(self.tabClientes_2)
        self.lblFechaAlta.setGeometry(QtCore.QRect(520, 30, 81, 16))
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tabClientes_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(100, 120, 211, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblSexo = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lblSexo.setObjectName("lblSexo")
        self.horizontalLayout_4.addWidget(self.lblSexo)
        self.rbtFem = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout_4.addWidget(self.rbtFem)
        self.rbtHom = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.rbtHom.setObjectName("rbtHom")
        self.rbtGroupSex.addButton(self.rbtHom)
        self.horizontalLayout_4.addWidget(self.rbtHom)
        self.btnModifCli = QtWidgets.QPushButton(self.tabClientes_2)
        self.btnModifCli.setGeometry(QtCore.QRect(390, 190, 75, 23))
        self.btnModifCli.setObjectName("btnModifCli")
        self.btnBajaCli = QtWidgets.QPushButton(self.tabClientes_2)
        self.btnBajaCli.setGeometry(QtCore.QRect(470, 190, 75, 23))
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.lblFecha = QtWidgets.QLabel(self.tabClientes_2)
        self.lblFecha.setGeometry(QtCore.QRect(10, 760, 111, 16))
        self.lblFecha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFecha.setObjectName("lblFecha")
        self.tabPrograma.addTab(self.tabClientes_2, "")
        self.tabFacturacion = QtWidgets.QWidget()
        self.tabFacturacion.setObjectName("tabFacturacion")
        self.label = QtWidgets.QLabel(self.tabFacturacion)
        self.label.setGeometry(QtCore.QRect(316, 232, 261, 81))
        self.label.setObjectName("label")
        self.tabPrograma.addTab(self.tabFacturacion, "")
        self.tabArticulos = QtWidgets.QWidget()
        self.tabArticulos.setObjectName("tabArticulos")
        self.label_2 = QtWidgets.QLabel(self.tabArticulos)
        self.label_2.setGeometry(QtCore.QRect(360, 340, 251, 111))
        self.label_2.setObjectName("label_2")
        self.tabPrograma.addTab(self.tabArticulos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuadar = QtWidgets.QAction(MainWindow)
        self.actionGuadar.setObjectName("actionGuadar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionFichero = QtWidgets.QAction(MainWindow)
        self.actionFichero.setObjectName("actionFichero")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionCrear_Backup = QtWidgets.QAction(MainWindow)
        self.actionCrear_Backup.setObjectName("actionCrear_Backup")
        self.actionRecuperar_Backup = QtWidgets.QAction(MainWindow)
        self.actionRecuperar_Backup.setObjectName("actionRecuperar_Backup")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuadar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRecuperar_Backup)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPrograma.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMPORT - EXPORT TEIS"))
        self.lblClientes.setText(_translate("MainWindow", "XESTIÓN CLIENTES"))
        self.lblFormaPago.setText(_translate("MainWindow", "Forma de pago:"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkCargoCuenta.setText(_translate("MainWindow", "Cargo en cuenta"))
        self.chkTransfer.setText(_translate("MainWindow", "Transferencia"))
        self.btnGrabaCli.setText(_translate("MainWindow", "Grabar"))
        self.pushButton.setText(_translate("MainWindow", "Salir"))
        self.lblDir.setText(_translate("MainWindow", "Dirección:        "))
        self.lblProv.setText(_translate("MainWindow", "Provincia:"))
        self.lblMun.setText(_translate("MainWindow", "Municipio:"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.lblRestablecer.setText(_translate("MainWindow", "Restablecer datos:"))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha alta"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Formas de pago"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:                "))
        self.lblFechaAlta.setText(_translate("MainWindow", "Fecha alta:"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.rbtFem.setText(_translate("MainWindow", "Mujer"))
        self.rbtHom.setText(_translate("MainWindow", "Hombre"))
        self.btnModifCli.setText(_translate("MainWindow", "Modificar"))
        self.btnBajaCli.setText(_translate("MainWindow", "Eliminar"))
        self.lblFecha.setText(_translate("MainWindow", "TextLabel"))
        self.tabPrograma.setTabText(self.tabPrograma.indexOf(self.tabClientes_2), _translate("MainWindow", "Clientes"))
        self.label.setText(_translate("MainWindow", "EN CONSTRUCCIÓN"))
        self.tabPrograma.setTabText(self.tabPrograma.indexOf(self.tabFacturacion), _translate("MainWindow", "Facturación"))
        self.label_2.setText(_translate("MainWindow", "ARTICULOS"))
        self.tabPrograma.setTabText(self.tabPrograma.indexOf(self.tabArticulos), _translate("MainWindow", "Articulos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.actionGuadar.setText(_translate("MainWindow", "Guadar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionFichero.setText(_translate("MainWindow", "Fichero"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionCrear_Backup.setText(_translate("MainWindow", "Crear Backup"))
        self.actionRecuperar_Backup.setText(_translate("MainWindow", "Recuperar Backup"))
