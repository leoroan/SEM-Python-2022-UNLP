
import csv
import os

# Establecer nombre de la carpeta.
path_file = "archivos_tp3"
# Establecer el nombre del archivo y su extension.
archivo_net = "netflix_titles.csv"

# Hacer la ruta uniendola con path_file
path_arch = os.path.join(os.getcwd(), path_file)

# Abre el archivo usando la ruta path_arch y el nombre del archivo_net(de netflix.csv)
archivo = open(os.path.join(path_arch, archivo_net), "r", encoding='utf-8')
data_net = csv.reader(archivo, delimiter=',')

# Guarda en Header los datros cabecera y en datos la lista con lo que intregra al archivo (lector csv)
header, datos = next(data_net), list(data_net)

# print(header)

"""
  1. Encontrar qué tipo de shows tiene un país determinado.
    • Realizar una función que informe todos los países que existen.
    • Realizar una función que dado un país informe si es parte de la línea del show pasado como
      argumento. 
      Nota: utilice las funciones vistas de lambda(utilizando la función definida), map
      para informar los tipos de shows (valores únicos) en que participa un país.
  Analizar:
    • ¿En qué número de columna está el país?
    • Como en algunos casos hay varios países en un show debemos separarlos y quedarnos con
      valores únicos.
"""
