# Ingresar las notas

# Ingresar las notas
nota = int(input("Ingresá una nota (-1 para finalizar)"))
lista_de_notas = []
while nota != -1:
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar) \n"))

prom = sum(lista_de_notas)/len(lista_de_notas)
# Calcular el promedio
print('Promedio: ' + str(prom))
# o print('Promedio: '+ str(sum(lista_de_notas)/len(lista_de_notas)))

# Calcular cuántos tienen notas menores al promedio
total = 0
for n in lista_de_notas:
    if n < sum(lista_de_notas)/len(lista_de_notas):
        print('menor al prom: '+str(n))
        total += 1
print('cantidad de notas menores al prom: '+str(total))
