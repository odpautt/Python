from easygui import *
import os
from os import listdir
path='C:/Users/OOP07199/Documents/O.Pautt/Evidencias/Acuerdos Comerciales'
listado=[f for f in listdir(path) if f.endswith('.JPG',) or f.endswith('.png')]
print(len(listado))
#permite eliminar el .png de los nombres para poder filtarlos y dejar solo los casos de prueba
for i in range(len(listado)):
	a= listado[i].find("_")
	b= listado[i]
	listado[i]=b[0:a]
	print(listado[i])
listado=sorted(list(set(listado)))#elimina los duplicados de una lista y los ordena 
print(len(listado))
print(listado)


# message to be displayed
text = "Selected any one item"
  
# window title
title = "Window Title GfG"
   
# creating a button box
output = choicebox(text, title, listado)
  
# title for the message box
title = "Message Box"
  
# message 
message = "You selected : " + str(output)
  
# creating a message box 
msg = msgbox(message, title)








# for i in range(len(lista2)):
# 		a=lista2[i]
# 		lista2[i]=a[0:len(b)]
# 		lista2=[a for a in lista2]
# lista2=sorted(list(set(lista2)))
# print(lista2)


# lista=["CPP0001.1","CPP0002.1","CPP0001.2"]
# lista2=[f for f in lista if f.find("CPP0001")==0]
# a="CPP0001.1"
# b="CPP0001"
# listaaux=[]
# for i in range(len(lista2)):
# 		a=lista2[i]
# 		lista2[i]=a[0:len(b)]
# 		lista2=[a for a in lista2]
# lista2=sorted(list(set(lista2)))
# print(lista2)


# myList = ["a","a","b","b","c","d"] 
# print(myList)
# myList = sorted(list(set(myList)))
# print(myList)