
palabras = input('ingrese cuatro palabras...\n')
##print(palabras.split())
##print(len(palabras.split()))
if len(palabras.split()) == 4:
  for  wd in palabras.split():
    if "r" in wd:
      print(wd)
else :
  print("No ingresó cuatro palabras")