
"""
7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
"""


import string
from typing import Counter


def verificar_heterograma(word):
  
    palabra = ''.join(char for char in word if char.isalnum())
    print(palabra)
    if len(set(palabra)) == len(palabra):
        return 'es heterograma'
    else:
        return 'NO es heterograma'



palabra = ['cruzamiento', 'centrifugados', 'portón',
           'casa', 'día de sol', 'con diez uñas', 'no-se-duplica']

#palabra = input('ingrese una frase o palabra para ver si es un "heterograma"...')


for cad in palabra:
    print(cad, ' - ', verificar_heterograma(cad))
