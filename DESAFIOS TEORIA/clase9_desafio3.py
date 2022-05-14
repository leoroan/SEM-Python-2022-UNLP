import os
import pandas as pd


url = "https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol"
df = pd.read_html(url)

#El df[4] es el que quiero para trabajar...
goleadores = df[4]

# Elimino la primera columna que repetía el indice
goleadores = goleadores.drop(goleadores.columns[0],axis=1)

# Quiero saber qué goleadores hicieron más de "x" goles 
masde = goleadores [goleadores["Goles"] > 11 ]

# corroboro los datos
print(masde)

# los salvo
masde.to_csv(os.path.join(os.getcwd(),'resultadoGoleadores.csv'))
