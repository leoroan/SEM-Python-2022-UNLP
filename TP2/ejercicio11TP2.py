
# 11. Con la información de los archivos de texto que se encuentran disponibles en el curso:
# • nombres_1
# • nombres_2
# • Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
# • Genere tres variables con la lista de notas y nombres que se incluyen en los archivos: nombres_1, eval1.txt y eval2.txt e imprima con formato los nombres de los estudiantes con las
#   correspondientes nota y la suma de ambas como se ve en la imagen


def formatear_Lista(lista):

    aux = []
    for x in lista:
        x = x.replace("\n", "").replace(",", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
        aux.append(x)
    return aux

# Abro los archivos y los combierto a una lista para facilitar su lectura
nombres1 = list(open("nombres_1.txt", encoding='utf-8'))
nombres2 = list(open("nombres_2.txt", encoding='utf-8'))

# formateo la lista recibida eliminando caracteres innecesarios
lista1 = formatear_Lista(nombres1)
lista2 = formatear_Lista(nombres2)

# Indico los nombre que se encuentran en ambas listas usando "list comprehension"
# -> List Comprehension - Syntax: newlist = [expression for item in iterable if condition == True]
aux = [x for x in lista1 if x in lista2]
print("nombres que se encuentran en ambos listados: ",aux)

notas1 = list(open("eval1.txt", encoding='utf-8'))
notas2 = list(open("eval2.txt", encoding='utf-8'))

lista3 = formatear_Lista(notas1)
lista4 = formatear_Lista(notas2)

# imprima con formato los nombres de los estudiantes con las
# correspondientes nota y la suma de ambas como se ve en la imagen
print("estudiante  nota1  nota2  suma_notas")
for x in range(len(lista1)):
    print(x,  lista1[x],"  ",lista3[x],"  ",lista4[x],"  ",int(lista3[x])+int(lista4[x]))


