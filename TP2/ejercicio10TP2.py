
# 10. Trabajando con los contenidos de los archivos que pueden acceder en el curso:
# • nombres
# • eval1
# • eval2
# Manipule estos archivos para realizar lo siguiente:
# • Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
# • Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
# promedio

def formatear_Lista(lista):

    aux = []
    for x in lista:
        x = x.replace("\n", "").replace(",", "").replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
        aux.append(x)
    return aux

def str_to_num(lista1):

  lista2 = []
  for x in lista1:
    lista2.append(int(x))
  return lista2   

def informar_alumnos_por_debajo_del_promedio(nombres,nota1,nota2,promedio):

  for x in range(len(nombres)):
    if (int(nota1[x])+int(nota2[x])) < promedio:
      print("el alumno: ",nombres[x]," está por debajo del promedio (",promedio,")" )
      

# Abro los archivos y los convierto a una lista para facilitar su lectura
nombres1 = list(open("nombres_1.txt", encoding='utf-8'))
notas1 = list(open("eval1.txt", encoding='utf-8'))
notas2 = list(open("eval2.txt", encoding='utf-8'))

# formateo la lista recibida eliminando caracteres innecesarios
lista1 = formatear_Lista(nombres1)
lista3 = formatear_Lista(notas1)
lista4 = formatear_Lista(notas2)

# imprime los nombres de los estudiantes con la correspondientes nota total
for x in range(len(lista1)):
    print(x,  lista1[x]," Total_: ",int(lista3[x])+int(lista4[x]))

listaAux = str_to_num(lista3)
promedio_notas = round(sum(listaAux)/len(lista3), 2)


print("El promedio de las notas es: ", promedio_notas)
informar_alumnos_por_debajo_del_promedio(lista1,lista3,lista4,promedio_notas)
