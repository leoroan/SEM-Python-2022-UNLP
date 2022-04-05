
import string
from typing import Counter


def get_file(nombre):
  ''' abrimos el archivo ubicado en la misma carpeta 
      del ejecutable
  '''
  return open(nombre,'r').read()  


## Puede ser un input(); 
nombreArchivo = 'readme.txt'  

## separo el archivo 
my_file = get_file(nombreArchivo).lower().split()

# 1. Imprima todas las líneas que contienen ‘http’ o ‘https'

# cad = 'http' or 'https'
for word in my_file:
  if ('http' or 'https') in word:
    print(word) 
    print( "-" * 25, '\n')    

# 2. Indique la palabra que aparece mayor 
# cantidad de veces en el texto del README.md de numpy

my_file_set = set(my_file)
#print(my_file_set)

c = Counter(my_file)
var = Counter(c).most_common(5)
new_list = []
for elem in var:
  #print(elem[0].split()[0][0])
  if elem[0][0] in string.ascii_letters:
    #print(elem[0])
    new_list.append(elem[0])

print('Palabra que aparece mas veces en el texto: ',new_list[0])