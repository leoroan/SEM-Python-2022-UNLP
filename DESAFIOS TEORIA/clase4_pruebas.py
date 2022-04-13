"""
import json
archivo = open("bandas.txt", "w")
datos = [
    {"nombre": "William Campbell", "ciudad": "La Plata",
        "ref": "www.instagram.com/williamcampbellok"},
    {"nombre": "Buendia", "ciudad": "La Plata",
        "ref": "https: // buendia.bandcamp.com /"},
    {"nombre": "Lúmine", "ciudad": "La Plata",
        "ref": "https: // www.instagram.com/luminelp /"}
        ]
json.dump(datos, archivo)
archivo.close()

archivo = open("bandas.txt", "r")
datos = json.load(archivo)
print(type(datos))
print(datos[2])
datos_a_mostrar = json.dumps(datos, indent=4)
print(type(datos_a_mostrar))

archivo.close()
"""
# with csv
import csv
import json

archivo = open("bandas.txt")
archivo_csv = open("bandas.csv", "w")

bandas = json.load(archivo)
writer = csv.writer(archivo_csv, )

for banda in bandas:
  writer.writerow(["Nombre", "Ciudad de procedencia", "Refencias"])
  writer.writerow([banda["nombre"], banda["ciudad"], banda["ref"]])
archivo.close()
archivo_csv.close()
print(type(writer))


archivo_cvs = open("bandas.csv", "r")
csvreader = csv.reader(archivo_cvs, delimiter=',')
for linea in csvreader:
  if linea != []:
    print(linea)

archivo_csv.close()

archivo_cvs = open("bandas.csv", "r")
csvreader = csv.DictReader(archivo_cvs, delimiter=',')
for linea in csvreader:
  print(linea["Nombre"])
archivo_csv.close()
