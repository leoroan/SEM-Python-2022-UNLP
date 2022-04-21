# Fechas - DATE TIME
from calendar import month
import collections
import csv
import datetime
import os

x = datetime.datetime.now()

# • Como saber qué número de día de la semana es hoy
nro_dia = datetime.datetime.today().weekday()

# • Para obtener los días de la semana en castellano podemos utilizar una estructura auxiliar:
dias_semana = ['lunes', 'martes', 'miercoles',
               'jueves', 'viernes', 'sabado', 'domingo']

# • Consultar algún dato en particular, como la hora
print('Hora: ',x.hour,'Hs')

# • Para guardar los datos en archivos se debe guardar en string indicando el formato en que
#   queremos guardarla.
horario_juego = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S")
print('tipo de "horario_juego = datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S")" ',type(horario_juego))

# #############################
# Nombre del archivo nuevo
logs = 'BBB_nuevo.csv'

# ruta del archivo
path_file = "archivos_tp3"
path_arch = os.path.join(os.getcwd(), path_file)

# Abro y trabajo con el archivo
with open(os.path.join(path_arch, logs)) as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header, logs_recurso = next(data_logs), list(data_logs)

dias = []
for linea in logs_recurso:
    print(linea[0])
    formato = "%d/%m/%Y %H:%M"
    #print(datetime.datetime.strptime(linea[0], formato).weekday())
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    nro_dia = datetime.datetime.strptime(linea[0], formato).weekday()
    dias.append(nro_dia)
    #print(dias_semana[nro_dia])
    #print(datetime.datetime.strptime(linea[0], formato).weekday())

# Indique los días de la semana que más registros hubo:

tot = collections.Counter(dias)
dia = tot.most_common(1)

print('Día de la semana que más registros hubo: ',dias_semana[dia[0][0]])

# Calcule cuántos dias pasaron entre el primer registro y el último.

# Obtengo el dia del logg
ultimo_dia = logs_recurso[0][0]
primer_dia = logs_recurso[-1][0]
# Lo modifico al tipo de datetime
diaU = datetime.datetime.strptime(ultimo_dia, "%d/%m/%Y %H:%M")
diaP = datetime.datetime.strptime(primer_dia, "%d/%m/%Y %H:%M")
# Me quedo con los días
tdU = datetime.timedelta(days=diaU.day)
tdP = datetime.timedelta(days=diaP.day)

# Calculo el total
total_dias = abs((diaU - diaP).days)

print('Dias que pasaron entre el primer registro y el último: ',str(total_dias))



