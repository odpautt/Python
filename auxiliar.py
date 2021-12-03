# from openpyxl import load_workbook
# from openpyxl.drawing.image import Image
# from os import listdir
# import os
# # archivo= "./ejemplo.xlsx"
# # wb=load_workbook(archivo)
# # #hojas=wb.get_sheet_names()
# # ws=wb.active
# # celda_a= ws.cell(14,16)# se declara la celda inicial para pegar la imagen "A1"
# # print(celda_a)
# # a=str(celda_a)
# # b=a.find(".")
# # c=a.find(">")
# # d=a[b+1:c]
# # print(d)

# # celda_a=celda_a.offset(0,12)
# # print(celda_a)
# # a=str(celda_a)
# # b=a.find(".")
# # c=a.find(">")
# # d=a[b+1:c]
# imagen=r'C:\Users\OOP07199\Documents\O.Pautt\Evidencias\OE_4636\SmokeTest_LIbre destino_1.png'
# imagen2=r'C:\Users\OOP07199\Documents\O.Pautt\Evidencias\OE_4636\SmokeTest_LIbre destino_2.png'
# # Importamos la libreria canvas del paquete reportlab
# from reportlab.pdfgen import canvas
# # abrimos el pdf
# c = canvas.Canvas('mypdf.pdf')
# # Para titulos asignamos una fuente y el tamaño = 20
# c.setFont('Helvetica', 20)
# # Dibujamos texto: (X,Y,Texto)
# c.drawString(25,800,"Crear PDF con Reportlab en Python!")
# # Para parrafos normales cambiamos el tamaño a 12
# c.setFont('Helvetica', 12)
# # Dibujamos texto: (X,Y,Texto)
# c.drawString(25,780,"Este es un ejemplo de parrafo en un PDF con la libreria reportlab y python!")
# # Dibujamos una imagen (IMAGEN, X,Y, WIDTH, HEIGH)
# c.drawImage(imagen, 25, 480, 500, 290)
# c.drawImage(imagen2, 25, 0, 500, 290)
# # Guardar
# c.save()
import datetime
import os
import easygui as es
try:
    from PIL import ImageGrab
    import numpy as np
    import cv2
    from win32api import GetSystemMetrics
except:
    os.system('cmd /k "echo.&pause& pip install pillow numpy opencv-python pywin32"')
while True:
		if cv2.waitKey(10) == ord('q'):
			print ("Fuera")
		break