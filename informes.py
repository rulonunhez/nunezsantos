import os
import var

from reportlab.pdfgen import canvas

class Informes:
    def listadoClientes(self):
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
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Rulas')
            var.cv.save()
            rootPath = '.\\informes'
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont += 1

        except Exception as error:
            print('Error en informe clientes', error)

    def cabecera(self):
        try:
            logo = '.\\img\\logoEmpresa.jpg'
            var.cv.line(40, 800, 560, 800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50, 785, 'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50, 770, 'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia, 101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'micorreo@mail.com')
            var.cv.drawImage(logo, 400, 696)
            var.cv.line(40, 710, 560, 710)
        except Exception as error:
            print('Error en la cabecera', error)