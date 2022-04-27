"""
Desafío 2
• Dado el dataset con datos de video juegos del Apple store.
• Armar un menú con PySimpleGUi que permita:
1. listar los juegos gratuitos disponibles en idioma español.
2. los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count
"""

import csv
import os

# Nombre de la carpeta donde está el archivo
ruta_archivos = "archivos"

# creacion de la ruta "completa", agregando la variable con el nombre del archivo.
ruta_completa = os.path.join(os.getcwd(), ruta_archivos)

# Asignacion del nombre del archivo .csv a la variable con la ruta definida.
archivo_juegos = os.path.join(ruta_completa, "appstore_games.csv")

# Apertura del archivo "ruteado"
archivo = open(archivo_juegos, 'r', encoding='utf-8')

csv_reader = csv.reader(archivo, delimiter=',')
header, loggs = next(csv_reader), list(csv_reader)











