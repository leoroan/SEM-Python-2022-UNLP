# Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
# veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas.


def wd_finder(frase,cadena):
    """
      Contamos la cantidad de veces q se repite una palabra
    """
    frase = frase.split()
    cant = 0
    for wd in frase:
        if wd == cadena:
            cant += 1
    return cant


frase = input('Ingrese una frase...').lower()
cadena = input('Ingrese una palabra...').lower()

print('cantidad de veces la palabra ',cadena,' en la frase: ',wd_finder(frase,cadena))
