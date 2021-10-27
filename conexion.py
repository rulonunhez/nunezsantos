from PyQt5 import QtSql, QtWidgets

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
            query.prepare('INSERT INTO clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago) VALUES (:dni, :alta, :apellidos, :nombre, :direccion'
                          ', :provincia, :municipio, :sexo, :pago)')
            query.bindValue(':dni', str(newCli[0]))
            query.bindValue(':alta', str(newCli[1]))
            query.bindValue(':apellidos', str(newCli[2]))
            query.bindValue(':nombre', str(newCli[3]))
            query.bindValue(':direccion', str(newCli[4]))
            query.bindValue(':provincia,', str(newCli[5]))
            query.bindValue(':municipio', str(newCli[6]))
            query.bindValue(':sexo', str(newCli[7]))
            query.bindValue(':pago', str(newCli[8]))
            print(newCli)
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
                msg.setText('Error dando de alta el cliente')
                msg.exec()


        except Exception as error:
            print('Error en módulo alta cliente', error)
