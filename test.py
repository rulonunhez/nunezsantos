import unittest
import clients, conexion, var
from PyQt5 import QtSql

class MyTestCase(unittest.TestCase):
    def test_conexion(self):
        value = conexion.Conexion.db_connect(var.filedb)
        msg = 'Conexión no válida'
        self.assertTrue(value, msg)

    def test_dni(self):
        dni = '00000000T'
        value = clients.Clientes.validarDni(dni)
        msg = 'Proba erronea'
        self.assertTrue(value, msg)  # add assertion here

    def test_fact(self):
        valor = 486.71
        codfac = 15
        try:
            msg = 'Cálculos incorrectos'
            var.subfac = 0.00
            query = QtSql.QSqlQuery()
            query1 = QtSql.QSqlQuery()
            query.prepare('select codven, codarticulo, cantidad from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codarticulo = query.value(1)
                    cantidad =  query.value(2)
                    query1.prepare('select nombre, precio from articulos where codigo = :codarticulo')
                    query1.bindValue(':codarticulo', int(codarticulo))
                    if query1.exec_():
                        while query1.next():
                            precio = query1.value(1)
                            subtotal = round(float(cantidad) * float(precio), 2)
                    var.subfac = round(float(subtotal) + float(var.subfac), 2)
            var.iva = round(float(var.subfac) * 0.21, 2)
            var.fac = round(float(var.iva) + float(var.subfac), 2)
        except Exception as error:
            print('Error listado de la tabla de ventas: %s ' % str(error))
        self.assertEqual(round(float(valor), 2), round(float(var.fac), 2), msg)




if __name__ == '__main__':
    unittest.main()
