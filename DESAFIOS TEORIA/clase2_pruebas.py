from turtle import clear


varios = ["hola", 2]
varios[0] = [3, 'perro']
varios.append({})
print(varios)
print(len(varios))

vocales = ["a", "e", "i", "o", "u"]
print(vocales[1:-1])

lista = [[1, 2], 8, 9]
lista2 = lista.copy()
print(id(lista), id(lista2))

tupla = 1, 2
tupla1 = (1, 2)
tupla2 = (1, )  # OJO con esto
tupla3 = ()
print(type(tupla2))

tupla = (1, 2, 3, "hola")
print(tupla[1:4])
nueva_tupla = ("nueva",) + tupla[1:3]
print(nueva_tupla)

nueva_tupla = ("nueva", ) + tupla[1:3]

musica = {"rock": ["Riff", "La Renga", "La Torre"],
          "blues": ["La Mississippi", "Memphis", "violeta"]}

claves = musica.keys()
valores = musica.values()
items = musica.items()

print(claves)
print(valores)
print(items)

print("rock" in musica)

musica["pop"] = ["nsync"]

print(claves)
print(valores)
print(musica)

musica.update({"pop": "asdfa"})
print(musica)
del(musica["pop"])
print(musica)

for elem in musica:
    print(elem)
    print(musica[elem])


dicc = dict([("enero", 31), ("febrero", 28), ("marzo", 31)])


def ingreso_notas():
    """sadsadd"""
    nombre = input("Ingresa un nombre (<FIN> para finalizar) \n")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre} \n"))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar) \n")
    return dicci


notas_de_estudiantes = ingreso_notas()

print(notas_de_estudiantes)
