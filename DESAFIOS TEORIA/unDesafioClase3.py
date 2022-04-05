# Usando expresiones lambda escribir una función
# que permita codificar una frase según el siguiente algoritmo:
""" ((Cifrado CESAR))
    encripto("a") --> "b"
    encripto("ABC") --> "BCD"
    encripto("Rock2021") --> "Spdl3132"
"""


from dataclasses import replace
from operator import index


def encriptar_Cifrado_Cesar(word, len):
    """
      La funciion recibe una palabra o frase y un valor para el cifrado
    """
    new_word = []
    may = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    min = list("abcdefghijklmnñopqrstuvwxyz")
    num = list("01234567890")
    for letra in word:
        if letra in may:
            letter = may[(may.index(letra)+len) % 27]
            new_word.append(letter)
        elif letra in min:
            letter = min[(min.index(letra)+len) % 27]
            new_word.append(letter)
        else:
            letter = num[(num.index(letra)+len) % 27]
            new_word.append(letter)

    return "".join(new_word)



palabra = input('Ingrese palabra o frase...')

# print(f'Palabra "{palabra}" encriptada, es :',encriptar_Cifrado_Cesar(palabra, 1))

abecedario = list("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
abecedario.sort(key=str.lower)

#print("".join(list(map(lambda ch: abecedario[(abecedario.index(ch)+1) % 27], palabra))))
print("".join(list(map(lambda ch: abecedario[(abecedario.index(ch)+1)], palabra))))

