import os
from datetime import datetime

from PyQt5 import QtSql

import var, conexion

from reportlab.pdfgen import canvas

class Informes:
    def listadoClientes(self):
        """

        Módulo que crea el informe con los datos de los clientes

        """
        try:
            var.cv = canvas.Canvas('informes/listadoClientes.pdf')
            Informes.cabecera(self)
            # var.cv.setFont('Helvetica-Bold', 16)
            # cv.drawString(30, 750, 'Listado Clientes')
            # cv.line(30, 500, 450, 500)
            # cv.circle(150, 500, 40, stroke=1, fill=1)
            # text = 'Este es un ejemplo de párrafo en el informe que estoy creando'
            # cv.setFont('Courier-Oblique', 10)
            # cv.drawString(30, 200, text)
            rootPath = '.\\informes'
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Rulas')
            textoTitulo = 'LISTADO CLIENTES'
            Informes.pie(textoTitulo)
            var.cv.setFont('Helvetica-Bold', 9)
            var.cv.drawString(250, 690, textoTitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['DNI', 'Nombre', 'Formas de pago']
            var.cv.drawString(65, 675,items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(370, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            var.cv.setFont('Helvetica', 8)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pago from clientes order by apellidos, nombre')
            if query.exec_():
                i = 50
                j = 660
                while query.next():
                    if j <= 40:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        var.cv.setFont('Helvetica-Bold', 9)
                        var.cv.drawString(250, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        var.cv.setFont('Helvetica', 8)
                        Informes.pie(textoTitulo)
                        i = 50
                        j = 660
                    var.cv.setFont('Helvetica', 8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i + 130, j, str(query.value(1) + ', ' + query.value(2)))
                    var.cv.drawString(i + 300, j, str(query.value(3)))
                    j -= 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoClientes.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont += 1

        except Exception as error:
            print('Error en informe clientes', error)

    def cabecera(self):
        """

        Módulo que establece la cabecera de las páginas

        """
        try:
            logo = '.\\img\\logoEmpresa.jpg'
            var.cv.line(40, 800, 530, 800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50, 785, 'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50, 770, 'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia, 101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'micorreo@mail.com')
            var.cv.drawImage(logo, 375, 696)
            var.cv.line(40, 710, 530, 710)
        except Exception as error:
            print('Error en la cabecera', error)

    def pie(texto):
        """

        Módulo que establece el pié de pagina con el texto recibido

        :param texto: Datos para mostrar en el pié de página
        :type texto: String

        """
        try:
            var.cv.line(50, 50, 530, 50)
            fecha = datetime.today().strftime('%d/%m/%Y %H.%M.%S')
            var.cv.setFont('Helvetica', 6)
            var.cv.drawString(70, 40, str(fecha))
            var.cv.drawString(255, 40, str(texto))
            var.cv.drawString(500, 40, str('Página %s ' %var.cv.getPageNumber()))

        except Exception as error:
            print('Error en el pie del informe clientes', error)

    def listadoArticulos(self):
        """

        Módulo que crea el informe con los datos de los productos

        """
        try:
            var.cv = canvas.Canvas('informes/listadoArticulos.pdf')
            Informes.cabecera(self)
            rootPath = '.\\informes'
            var.cv.setTitle('Listado Articulos')
            var.cv.setAuthor('Rulas')
            textoTitulo = 'LISTADO ARTICULOS'
            Informes.pie(textoTitulo)
            var.cv.setFont('Helvetica-Bold', 9)
            var.cv.drawString(250, 690, textoTitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['Codigo', 'Nombre', 'Precio']
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(400, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            var.cv.setFont('Helvetica', 8)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos')
            if query.exec_():
                i = 80
                j = 660
                while query.next():
                    if j <= 40:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        var.cv.setFont('Helvetica-Bold', 9)
                        var.cv.drawString(250, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['Codigo', 'Nombre', 'Precio']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(400, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        var.cv.setFont('Helvetica', 8)
                        Informes.pie(textoTitulo)
                        i = 80
                        j = 660
                    var.cv.setFont('Helvetica', 8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i + 120, j, str(query.value(1)))
                    var.cv.drawString(i + 300, j, str(round(query.value(2), 2)))
                    j -= 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoArticulos.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont += 1

        except Exception as error:
            print('Error en listado de articulos para informe', error)

    def listadoFacturas(self):
        """

        Módulo que crea el informe con los datos de las facturas

        """
        try:
            var.cv = canvas.Canvas('informes/listadoFacturas.pdf')
            var.cv.setTitle('Factura')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=12)
            textotitulo = 'FACTURA'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            codfac = var.ui.txtCodFac.text()
            var.cv.setFont('Helvetica-Bold', size=12)
            var.cv.drawString(255, 695, textotitulo + ': ' + str(codfac))
            var.cv.line(40, 685, 530, 685)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select direccion, provincia, municipio from clientes where dni = :dni')
            query1.bindValue(':dni', str(var.ui.txtDniFac.text()))
            if query1.exec_():
                dir = []
                while query1.next():
                    dir.append(query1.value(0))
                    dir.append(query1.value(1))
                    dir.append(query1.value(2))
            var.cv.setFont('Helvetica-Bold', size=9)
            var.cv.drawString(250, 785, 'DATOS CLIENTE')
            var.cv.setFont('Helvetica', size=9)
            var.cv.drawString(230, 770, 'CIF: ' + var.ui.txtDniFac.text())
            var.cv.drawString(230, 755, 'Cliente: ' + var.ui.txtClienteFac.text())
            var.cv.drawString(230, 740, 'Direccion: ' + str(dir[0]))
            print(str(dir[2]))
            if (str(dir[2])) == '':
                var.cv.drawString(230, 725, str(dir[1]))
            else:
                var.cv.drawString(230, 725, str(dir[1]) + ' (' + str(dir[2]) + ')')
            items = ['Venta', 'Artículo', 'Precio', 'Cantidad', 'Total']
            var.cv.drawString(60, 675, items[0])
            var.cv.drawString(150, 675, items[1])
            var.cv.drawString(290, 675, items[2])
            var.cv.drawString(390, 675, items[3])
            var.cv.drawString(495, 675, items[4])
            var.cv.line(40, 670, 530, 670)
            suma = 0.0
            query = QtSql.QSqlQuery()
            query.prepare('select codven, precio, cantidad, codarticulo from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    codventa = query.value(0)
                    precio = str('{:.2f}'.format(round(query.value(1), 2))) + ' €'
                    cantidad = str('{:.2f}'.format(round(query.value(2), 2)))
                    articulo = conexion.Conexion.consultarArticulo(str(query.value(3)))
                    suma = suma + (round(query.value(1), 2) * round(query.value(2), 2))
                    total = str('{:.2f}'.format(round(query.value(1) * query.value(2), 2))).replace(',', '.') + ' €'
                    var.cv.drawCentredString(i + 20, j, str(codventa))
                    var.cv.drawString(i + 100, j, str(articulo))
                    var.cv.drawString(i + 230, j, str(precio) + ' €/kg')
                    var.cv.drawString(i + 350, j, str(cantidad))
                    var.cv.drawString(i + 440, j, str(total))
                    j = j - 20
                var.cv.setFont('Helvetica', size=8)
                subTotal = var.ui.lblSubtotal.text()
                iva = var.ui.lblIva.text()
                final = var.ui.lblTotal.text()
                var.cv.drawString(i + 410, j - 20, "Sub Total: " + subTotal)
                var.cv.drawString(i + 410, j - 40, "IVA: " + iva)
                var.cv.drawString(i + 410, j - 60, "Total: " + final)

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoFacturas.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error en informes productos, ', error)
