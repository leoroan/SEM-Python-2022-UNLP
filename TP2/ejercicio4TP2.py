
from dataclasses import replace
import string
from typing import Counter


def evaluar_Titulo(cadena):
    """
      Recibe una cadena en oracion, y devuelve la cantidad de palabras.
    """
    # me quedo con la primer oracion hasta el "."
    c = Counter(cadena[0].lower().split())
    # borro si existe la palabra "titulo" para los acentos y demas caracteres:
    # outputString = unidecode.unidecode(string)
    del c['título:']
    return c.total()


def evaluate(cadena):
    """
        defina si cumple las especificaciones del título y
         cuántas oraciones tiene de cada categoría
    """

    easy = 0
    med = 0
    hard = 0
    hardd = 0

    cadena = evaluar.split('.')
    i = 1
    for i in range(len(cadena)-1):
        # print(cadena[i].lower().split())
        c = Counter(cadena[i].lower().split())
        # print(c.total())
        if (c.total() <= 12):
            easy += 1
        elif (c.total() >= 13) & (c.total() <= 17):
            med += 1
        elif (c.total() >= 18) & (c.total() <= 25):
            hard += 1
        elif (c.total() > 25):
            hardd += 1
    print('Cantidad de oraciones FACILES de leer: ', easy, ' ACEPTABLES: ',
          med, ' DIFICILES: ', hard, ' MUY DIFICILES: ', hardd)


evaluar = """
          título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python.
          resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the 
          promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge 
          required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our 
          experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. 
          We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), 
          to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
          and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging 
          computing architectures.
          """

# Vamos a evaluar la cantidad de palabras del titulo

print('Cantidad de palabras en el titulo: ',
      evaluar_Titulo(evaluar.split('.')))

# evaluamos cada oracion del texto
# cada oración del resumen:
# – hasta 12 palabras: fácil de leer
# – entre 13-17 palabras: aceptable para leer
# – entre 18-25 palabras: difícil de leer
# – mas de 25 palabras: muy difícil

evaluate(evaluar)
