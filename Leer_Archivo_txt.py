f = open (r'C:\Users\OOP07199\Documents\O.Pautt\Archivo.txt','r')

print ("+++ 1 ++++")
datos = []
with open(r'C:\Users\OOP07199\Documents\O.Pautt\Archivo.txt') as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
a=datos[1].split("-")

print (datos)
print (a)

print ("*** 2 ***")

datos2 = []
with open(r'C:\Users\OOP07199\Documents\O.Pautt\Archivo.txt') as fname:
	for lineas in fname:
		datos2.extend(lineas.split("-"))
		print (datos2)
print (datos2)
print ("***")