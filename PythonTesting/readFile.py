# hace la lectura del archivo plano y almacena su información en la variable content
with open("test.txt") as reader:
    content = reader.readlines()
# se crea la lista text vacia donde se almacenara la informacion de content separado por ;
text = []
for i in content:
    sp = i.split(";")
    text.append(sp)
# imprime la lista de listas es decir la matriz de listas
print(text)
