from PyQt5 import QtSql, QtWidgets

import clients
import var


class Conexion():
    def db_connect(filename):
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


    def altaCli(newCli):
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
        try:
            query = QtSql.QSqlQuery()
            query.prepare('SELECT alta, nombre, apellidos, direccion, provincia, municipio, sexo, pago, envio'
                          ' FROM clientes where dni = :dni')
            datos = []
            query.bindValue(':dni', dni)
            if query.exec_():
                for i in range(9):
                    datos.append(str(query.value(i)))
            return datos

        except Exception as error:
            print('Error en la consulta a la base de datos', error)

    def altaArt(newArt):
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
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codigo, nombre, precio FROM articulos')
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
            print('Error en módulo cargar tabla articulos', error)

    def bajaArticulo(codigo):
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
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre = :nombre, precio = :precio where codigo = :codigo')
            query.bindValue(':codigo', str(articulo[0]))
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

    def cargaTabFacturas(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, fechafac from facturas order by fechafac desc')
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    fechafac = str(query.value(1))
                    var.ui.tabFacturas.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    index += 1

        except Exception as error:
            print('Error en cargar la tabla de facturas', error)

    def cargaFactura(codigo):
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



