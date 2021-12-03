# hace la lectura del archivo plano y almacena su información en la variable content
# si el archivo plano no queda dentro de la misma carpeta, se debe definir nom_archivo = "ruta del archivo" para que lo pueda leer de lo contrario genera error
def leer(nom_archivo):
    with open(nom_archivo) as reader:
        content = reader.readlines()
    # se crea la lista text vacia donde se almacenara la informacion de content separado por (;)
    text = []
    for i in content:
        sp = i.split(";")
        text.append(sp)
    # imprime la lista de listas es decir la matriz de listas
    return text
