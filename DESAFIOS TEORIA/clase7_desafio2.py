"""
Desafío 2
• Dado el dataset con datos de video juegos del Apple store.
• Armar un menú con PySimpleGUi que permita:
1. listar los juegos gratuitos disponibles en idioma español.
2. los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count
"""

import csv
import os

# ESTABLECEMOS LA RUTA DEL ARCHIVO
# Nombre de la carpeta donde está el archivo
ruta_archivos = "archivos"
# creacion de la ruta "completa", agregando la variable con el nombre del archivo.
ruta_completa = os.path.join(os.getcwd(), ruta_archivos)
# Asignacion del nombre del archivo .csv a la variable con la ruta definida.
archivo_juegos = os.path.join(ruta_completa, "appstore_games.csv")


# Apertura del archivo "ruteado"
archivo = open(archivo_juegos, 'r', encoding='utf-8')
# Usamos un lector CSV para "leer" el archivo
csv_reader = csv.reader(archivo, delimiter=',')
header, loggs = next(csv_reader), list(csv_reader)


# Listado de juegos gratuitos disponibles en español
# for x in range(len(loggs)):
#   if (("ES" in loggs[x][12])and(loggs[x][7] == "0")):
#     print(loggs[x][2])

# manera de pasar a diccionario el header para "saber" mejor las pos de las columnas.
new_dict = {}
for x in range(len(header)):
  new_dict[x] = header[x]
#print(new_dict)

import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Juegos gratuitos en idioma Español: ')],
            [sg.Text('Presione OK para mostrar: ')],
            [sg.Output(size=(100 ,40))],
            [sg.OK(), sg.Cancel()]]
                      
# Create the Window
window = sg.Window('MiWIn_dou', layout )

# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif sg.OK:
      for x in range(len(loggs)):
          if (("ES" in loggs[x][12])and(loggs[x][7] == "0")):
              print('Name: ',loggs[x][2],'URL: ', loggs[x][0])
    #elif event in (sg.OK, 'OK'):
    #  print("great",values[0])  

window.close()









