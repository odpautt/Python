import os
from os import listdir

listado=[]
path='C:/Users/OOP07199/Documents/O.Pautt/Evidencias/Evidencias Sprint 2/Bloque Debida Diligencia Portal'


listado=[f for f in listdir(path) if f.endswith('.JPG',) or f.endswith('.png')]
listado.sort()

print(listado)


contador=1
for i in listado:
    file=path+"/"+i
    newname=path+"/BloqueoDebidaDiligencia_PortalPN_CE_"+ str(contador)+".png"
    os.rename(file, newname)
    contador=contador+1


