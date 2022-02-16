from PyQt5 import QtSql, QtWidgets, QtGui, QtCore

import clients
import events
import facturas
import var
import sqlite3, shutil, os, csv
import locale
locale.setlocale( locale.LC_ALL, '' )

class Conexion():
    def create_db(filename):
        """

        Recibe el nombre de la base de datos.
        Módulo que se ejecuta al principio del programa.
        Crea las tablas y carga municipios y provincias.
        Crea los directorios necesarios.

        :type: String
        :param: Nombre de la bbdd
        :rtype: Object

        """
        try:
            con = sqlite3.connect(database = filename)
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS clientes (dni	TEXT NOT NULL, alta	TEXT, apellidos	TEXT NOT NULL, nombre	TEXT NOT NULL, '
                        'direccion	TEXT NOT NULL, provincia	TEXT NOT NULL, municipio	TEXT, sexo	TEXT NOT NULL, pago	TEXT, envio	INTEGER,'
                        'PRIMARY KEY(dni))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS articulos (codigo	INTEGER NOT NULL, nombre TEXT, precio	REAL, '
                        'PRIMARY KEY(codigo AUTOINCREMENT))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS facturas (codfac	INTEGER NOT NULL, fechafac	TEXT NOT NULL, dni	TEXT NOT NULL, '
                        'PRIMARY KEY(codfac AUTOINCREMENT), FOREIGN KEY(dni) REFERENCES clientes(dni))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS municipios (provincia_id	INTEGER NOT NULL, municipio	TEXT NOT NULL, '
                        'id	INTEGER NOT NULL, PRIMARY KEY(id))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS provincias (id	INTEGER NOT NULL, provincia	TEXT NOT NULL, '
                        'PRIMARY KEY(id))')
            con.commit()
            cur.execute('CREATE TABLE IF NOT EXISTS ventas (codven	INTEGER NOT NULL, codfac	INTEGER NOT NULL, '
                        'codarticulo	INTEGER NOT NULL, cantidad	REAL NOT NULL, precio	REAL NOT NULL, '
                        'PRIMARY KEY(codven AUTOINCREMENT), FOREIGN KEY(codarticulo) REFERENCES articulos(codigo), '
                        'FOREIGN KEY(codfac) REFERENCES facturas(codfac) on delete cascade)')
            con.commit()
            cur.execute('select count() from provincias')
            numero = cur.fetchone()[0]
            con.commit()
            if int(numero) == 0:
                with open ('provincias.csv', 'r', encoding="utf-8") as fin:
                    dr = csv.DictReader(fin)
                    to_db = [(i['id'], i['provincia']) for i in dr]
                cur.executemany('insert into provincias (id, provincia) VALUES (?,?);', to_db)
                con.commit()
            con.close()

            '''creación de directorios'''
            if not os.path.exists('.\\informes'):
                os.mkdir('.\\informes')
            if not os.path.exists('.\\img'):
                os.mkdir('.\\img')
                # shutil.move('logo')
            if not os.path.exists('C:\\copias'):
                os.mkdir('C:\\copias')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(str(error))
            msg.exec()

    def db_connect(filename):
        """

        Realiza la conexión con la base de datos

        :param: Nombre de la bbdd
        :type: String
        :return: True si se conecta correctamente, False en caso contrario
        :rtype: Boolean

        """
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos.\nHaz clic para continuar',
                                               QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('Conexión establecida')
                return True
        except Exception as error:
            print('Problemas en conexión ',error)

    # def existeDni (?, no está xd)
    # Módulo que busca DNI en la bbdd
    # :return: True si el DNI no se encuentra ya en la bbdd, False en caso de que sí se encuentre
    # :rtype: Boolean

    def altaCli(newCli):
        """

        Módulo que recibe datos de un cliente y los carga en la bbdd

        :param: Datos de un cliente
        :type: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio) values (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)')
            query.bindValue(':dni', str(newCli[0]))
            query.bindValue(':alta', str(newCli[1]))
            query.bindValue(':apellidos', str(newCli[2]))
            query.bindValue(':nombre', str(newCli[3]))
            query.bindValue(':direccion', str(newCli[4]))
            query.bindValue(':provincia', str(newCli[5]))
            query.bindValue(':municipio', str(newCli[6]))
            query.bindValue(':sexo', str(newCli[7]))
            query.bindValue(':pago', str(newCli[8]))
            query.bindValue(':envio', newCli[9])
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de alta')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()


        except Exception as error:
            print('Error en módulo alta cliente', error)

    def cargaTabCli():
        """

        Módulo que carga la tabla del panel de Clientes

        """
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT dni, apellidos, nombre, alta, pago FROM clientes ORDER BY apellidos, nombre')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tabClientes.setRowCount(index+1) #creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1
        except Exception as error:
            print('Error en módulo cargar tabla clientes', error)

    def cargaCli2(dni):
        """

        Módulo que selecciona un cliente por su DNI y devuelve algunos de sus campos a la función cargaCli
        del fichero clients.py

        :param: DNI del cliente
        :type: String
        :return: Lista con los datos del cliente (direccion, provincia, municipio, sexo y envio)
        :rtype: Lista

        """
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT direccion, provincia, municipio, sexo, envio  FROM clientes WHERE dni = :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(5):
                        record.append(query.value(i))
            return record

        except Exception as error:
            print('Error en módulo cargar cliente dos ', error)

    def bajaCli(dni):
        """

        Módulo que recibe el DNI del cliente y elimina a ese cliente de la bbdd

        :param: DNI de un cliente
        :type: String

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM clientes WHERE dni = :dni')
            query.bindValue(':dni', str(dni))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error baja ciente en conexion', error)

    def cargarProv(self):
        """

        Módulo que carga las provincias en el comboBox de la interfaz gráfica del panel de Clientes

        :return: Diccionario con clave Id de provincia y valor nombre de la provincia
        :rtype: Diccionario

        """
        try:
            provinciaId = []
            provinciaNombre = []
            provincias = {}

            query = QtSql.QSqlQuery()
            query.prepare('SELECT id, provincia FROM provincias')
            if query.exec_():
                while query.next():
                    provinciaId.append(query.value(0))
                    provinciaNombre.append(query.value(1))

            provincias = dict(zip(provinciaId, provinciaNombre))

            return provincias

        except Exception as error:
            print('Error cargar provincias en conexion', error)

    def cargarMun(self):
        """

        Módulo que carga los municipios según la provincia seleccionada en el comboBox de la interfaz gráfica del panel
         de Clientes

        :return: Lista con los nombres de los municipios
        :rtype: Lista

        """
        try:
            provincias = Conexion.cargarProv(self)
            prov = var.ui.cmbProv.currentText()
            municipios = []
            id = ""

            for dato in provincias:
                if (provincias.get(dato) == prov):
                    id = dato

            query = QtSql.QSqlQuery()
            query.prepare('SELECT municipio FROM municipios where provincia_id = :id')
            query.bindValue(':id', id)
            if query.exec_():
                while query.next():
                    municipios.append(query.value(0))

            return municipios

        except Exception as error:
            print('Error cargar municipios en conexion', error)

    def modifCli(modcliente):
        """

        Módulo que recibe los datos del cliente para modificarlo y lo actualiza en la bbdd

        :param: Datos de los campos de un cliente
        :type: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'update clientes set alta = :alta, apellidos = :apellidos, nombre = :nombre, direccion = :direccion, '
                'provincia = :provincia, municipio = :municipio, sexo = :sexo, pago = :pago, envio = :envio where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pago', str(modcliente[8]))
            query.bindValue(':envio', modcliente[9])

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente modificado')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en modificar cliente en conexión', error)

    def consultaDni(dni):
        """

        Módulo que dado el DNI busca los datos del cliente para cargarlas en el panel de gestión de clientes

        :param: DNI de un cliente
        :type: String
        :return: Datos de un cliente
        :rtype: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            print(dni)
            query.prepare('SELECT alta, nombre, apellidos, direccion, provincia, municipio, sexo, pago, envio FROM clientes where dni = :dni')
            datos = []
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    for i in range(9):
                        print(query.value(i))
                        datos.append(str(query.value(i)))
            return datos

        except Exception as error:
            print('Error en la consulta a la base de datos', error)

    def altaArt(newArt):
        """

        Módulo que recibe los datos de un producto y lo almacena en la bbdd

        :param: Valores de los campos de un producto (nombre y precio)
        :type: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into articulos (nombre, precio) values (:nombre, :precio)')
            query.bindValue(':nombre', str(newArt[0]))
            query.bindValue(':precio', str(newArt[1]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Articulo dado de alta')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en módulo alta articulos', error)

    def cargaTabArt(self):
        """

        Módulo que carga la tabla de productos, se recarga siempre que se haga una operación sobre la bbdd

        """
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codigo, nombre, precio FROM articulos order by nombre')
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    nombre = str(query.value(1))
                    precio = round(float(query.value(2)), 2)
                    var.ui.tabArts.setRowCount(index+1) #creamos la fila y luego cargamos datos
                    var.ui.tabArts.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabArts.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArts.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio) + ' €'))
                    var.ui.tabArts.item(index, 2).setTextAlignment(QtCore.Qt.AlignRight)
                    var.ui.tabArts.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print('Error en módulo cargar tabla articulos', error)

    def bajaArticulo(codigo):
        """

        Módulo que da de baja un producto en la bbdd según el codigo del producto recibido

        :param: Código de un producto
        :type: String

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM articulos WHERE codigo = :codigo')
            query.bindValue(':codigo', str(codigo))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Artículo dado de baja')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error baja articulo en conexion', error)

    def modifArticulo(articulo):
        """

        Módulo que recibe datos de un producto para modificar y lo actualiza en la bbdd

        :param: Datos de los campos de un producto
        :type: Lista

        """
        try:
            articulo[2] = articulo[2].replace('€', '')
            print(articulo[2])
            articulo[2] = articulo[2].replace(',', '.')
            print(articulo[2])
            articulo[2] = locale.currency(float(articulo[2]))
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre = :nombre, precio = :precio where codigo = :codigo')
            query.bindValue(':codigo', articulo[0])
            query.bindValue(':nombre', str(articulo[1]))
            query.bindValue(':precio', str(articulo[2]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente modificado')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error en modificar articulo en conexión', error)

    def buscarArticulo(articulo):
        """

        Módulo que recoge los datos de un producto según su nombre

        :param: Nombre del producto
        :type: String

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos where nombre = :nombre')
            query.bindValue(':nombre', str(articulo))
            index = 0
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    nombre = str(query.value(1))
                    precio = str(round(query.value(2), 2))
                    var.ui.tabArts.setRowCount(index+1) #creamos la fila y luego cargamos datos
                    var.ui.tabArts.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabArts.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArts.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    index += 1

        except Exception as error:
            print('Error en bucar articulo en conexion', error)

    # Métodos facturación

    def buscaCliFac(dni):
        """

        Módulo que busca los datos de un cliente sobre el que se va a hacer una factura según el DNI recibido

        :param: DNI del cliente
        :type: String
        :return: Datos del cliente
        :rtype: Lista

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select nombre, apellidos from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                while query.next():
                    registro.append(query.value(0))
                    registro.append(query.value(1))

            return registro
        except Exception as error:
            print('Error en buscar cliente en conexion', error)

    def facturar(registro):
        """

        Módulo que recibe los datos de una factura y la almacena en la bbdd

        :param: Datos de la factura
        :type: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (dni, fechafac) values (:dni, :fechafac)')
            query.bindValue(':dni', str(registro[0]))
            query.bindValue(':fechafac', str(registro[1]))
            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de alta')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('Error en facturar en conexion', error)

    # def cargaTabFacturas(self):
    #     try:
    #         index = 0
    #         query = QtSql.QSqlQuery()
    #         query.prepare('select codfac, fechafac from facturas order by fechafac desc')
    #         if query.exec_():
    #             while query.next():
    #                 codigo = str(query.value(0))
    #                 fechafac = str(query.value(1))
    #                 var.ui.tabFacturas.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
    #                 var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
    #                 var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
    #                 index += 1
    #
    #     except Exception as error:
    #         print('Error en cargar la tabla de facturas', error)

    def cargaFactura(codigo):
        """

        Módulo que recoge los datos del cliente referenciado en una factura según el código de la factura recibido

        :param: Código de la factura
        :type: String
        :return: Datos del cliente
        :rtype: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select dni from facturas where codfac = :codfac')
            query.bindValue(':codfac', codigo)
            if query.exec_():
                while query.next():
                    dni = str(query.value(0))
            query2 = QtSql.QSqlQuery()
            query2.prepare('select nombre, apellidos from clientes where dni = :dni')
            query2.bindValue(':dni', dni)
            if query2.exec_():
                while query2.next():
                    nombre = str(query2.value(0))
                    apellidos = str(query2.value(1))
            registro = [dni, nombre, apellidos]
            return registro

        except Exception as error:
            print('Error en cargar factura', error)

    def cargaTabFacturas(self):
        """

        Módulo que carga los datos de las facturas de la bbdd en la tabla de la pestaña Facturación

        """
        try:
            var.ui.tabFacturas.clear()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, fechafac from facturas')
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    icopapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(24, 24)
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))
                    var.ui.tabFacturas.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tabFacturas.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index = index + 1


        except Exception as error:
            print('Error en carga listado facturas ', error)

    def bajaFac(self):
        """

        Módulo que elimina una factura de la bbdd

        """
        try:
            query = QtSql.QSqlQuery()
            codigo = var.ui.txtCodFac.text()
            Conexion.borrarVentasFac(codigo)
            query.prepare('DELETE FROM facturas WHERE codfac = :codigo')
            query.bindValue(':codigo', str(codigo))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de baja')
                msg.exec()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()

            Conexion.cargaTabFacturas(self)

        except Exception as error:
            print('Error baja factura en conexion', error)

    def cargarCmbproducto():
        """

        Módulo que carga el comboBox de productos de la tabla de Facturación desde la bbdd

        """
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')
            query.prepare('select nombre from articulos order by nombre')
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))

        except Exception as error:
            print ('Error en cargar cmbproducto', error)

    def obtenerCodPrecio(articulo):
        """

        Módulo que recibe el nombre de un producto y busca en la bbdd su código y su precio

        :param: Nombre del producto
        :type: String
        :return: Datos de código y precio del producto
        :rtype: Lista

        """
        try:
            dato = []
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, precio from articulos where nombre = :nombre')
            query.bindValue(':nombre', str(articulo))
            if query.exec_():
                while query.next():
                    dato.append(int(query.value(0)))
                    dato.append(query.value(1))
            return dato
        except Exception as error:
            print ('Error en obtener codigo y precio de un articulo', error)

    def cargarVenta(venta):
        """

        Módulo que recibe los datos de una venta y la almacena en la bbdd

        :param: Datos de una venta
        :type: Lista

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into ventas (codfac, codarticulo, precio, cantidad) values (:codfac, :codarticulo, :precio, :cantidad)')
            query.bindValue(':codfac', int(venta[0]))
            query.bindValue(':codarticulo', int(venta[1]))
            query.bindValue(':precio', float(venta[3]))
            query.bindValue(':cantidad', float(venta[2]))
            query.exec()

            Conexion.cargarLineasVenta(int(venta[0]))

        except Exception as error:
            print('Error en cargar venta', error)

    def buscaCodFac(self):
        """

        Módulo que busca el código de factura más alto en la bbdd

        :return: Código de factura
        :rtype: String

        """
        try:
            dato = 0
            query = QtSql.QSqlQuery()
            query.prepare(
                'select codfac from facturas order by codfac desc limit 1')
            if query.exec_():
                while query.next():
                    dato = query.value(0)
            return dato
        except Exception as error:
            print('Error en busca codigo de factura', error)

    def cargarLineasVenta(codfac):
        """

        Módulo que recibe el código de una factura y carga todas las ventas con ese código referenciado

        :param: Código de una factura
        :type: String

        """
        try:
            suma = 0
            var.ui.tabVentas.clearContents()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codven, codarticulo, precio, cantidad from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))

            if query.exec_():
                while query.next():
                    codventa = query.value(0)
                    precio = query.value(2)
                    cantidad = query.value(3)
                    codArticulo = query.value(1)
                    total = round(cantidad * precio, 2)
                    suma += total
                    articulo = Conexion.consultarArticulo(codArticulo)
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index,0, QtWidgets.QTableWidgetItem(str(codventa)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio)))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(articulo)))
                    var.ui.tabVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(total)))
                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    index = index + 1

            iva = suma * 0.21
            total = suma + iva
            var.ui.lblSubtotal.setText(str(round(suma, 2)) + '€')
            var.ui.lblTotal.setText(str(round(total, 2)) + '€')
            var.ui.lblIva.setText(str(round(iva, 2)) + '€')
            facturas.Facturas.cargarLineaVenta(int(index))
            var.ui.tabVentas.scrollToBottom()

        except Exception as error:
            print('error cargar las lineas de factura', error)

    def consultarArticulo(articulo):
        """

        Módulo que recibe el codigo de un producto y busca su nombre en la bbdd

        :param: Código de un producto
        :type: String
        :return: Nombre del artículo
        :rtype: String

        """
        try:
            nombre = ''
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from articulos where codigo = :codart')
            query.bindValue(':codart', int(articulo))
            if query.exec_():
                while query.next():
                    nombre = query.value(0)
            return nombre
        except Exception as error:
            print('Error en busqueda del nombre del articulo', error)

    def borraVenta(self):
        """

        Módulo que borra una venta en la bbdd

        """
        try:
            row = var.ui.tabVentas.currentRow()
            codventa = var.ui.tabVentas.item(row, 0).text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codven = :codven')
            query.bindValue(':codven', int(codventa))
            if query.exec_():
                msg1 = QtWidgets.QMessageBox()
                msg1.setWindowTitle('Aviso')
                msg1.setIcon(QtWidgets.QMessageBox.Information)
                msg1.setText('Venta eliminada')
                msg1.exec()
                codfac = var.ui.txtCodFac.text()
                Conexion.cargarLineasVenta(codfac)
        except Exception as error:
            print('Error en dar de baja una venta', error)

    def borrarVentasFac(codfac):
        """

        Módulo que recibe el código de una factura que se va a eliminar y borra todas sus ventas asociadas

        :param: Código de una factura
        :type: String

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            query.exec()
            events.Eventos.limpiaFormFac()

        except Exception as error:
            print('Error en dar de baja las ventas', error)





