
from webbrowser import get

# Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
# la siguiente tabla de valores del juego Scrabble:


def calcular_valor_palabra(palabra):
    """
      Recibe una palabra y cuenta sus valores segun el caracter q la compone
    """

    total = 0
    if " " in palabra:
        return 'no es una palabra'
    else:
        for lett in palabra:
            for key, value in valores.items():
                if lett in value:
                    total = total + (key)
        return total


palabra = input('ingrese una palabra ...')

valores = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 2: ["D", "G"], 3: [
    "B", "C", "M", "P"], 4: ["F", "H", "V", "W", "Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q", "Z"]}


print(f'total valor palabra: >>{palabra}<< '.upper(),
      calcular_valor_palabra(palabra.upper()))
