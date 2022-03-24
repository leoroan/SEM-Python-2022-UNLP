• Analizar:
– Tipos de datos trabajados:
	Puedo observar el uso de la estructura "diccionario" (words) y
	listas.

– Funciones definidas:
	*get_Random_Word()
	*display_Board()
	*hint()
	*get_Guess()
	*play_Again()

– ¿Cómo define los niveles?:
	-Los distintos niveles de dificultad los define por medio de la cantidad de "aciertos"
	que podemos tener en el juego.
	si es el modo facil, tenemos "X" cantidad de aciertos para ganar, y a medida q lo aumenta (MEDIO Y  DIFICIL) le 	va restando oportunidades.

– ¿Se respeta la PEP 8?:
	no, tube que realizarle modificaciones al documento, como en el nombre de las funciones, algunos ajustes de  	lineas y espacios y corregirle los comentarios dentro de los modulos.

• ¿Se animan a modificarlo?
– Agregar pistas sobre el tipo de la palabra a adivinar

	agrego: el juego asi con el codigo compartido YA posee una ayuda sobre el tipo de palabra a adivinar:
		" The secret word is in the set: XXXXX "

	por esto me tome la libertad de agregar otra funcion de ayuda: hint()
		simplemente lo que hace es devolvernos algun caracter aleatorio, de la palabra secreta.

	codigo:

-+--------------------------------------+-
 |  def hint():				|
 |   	help = secretWord.split()	|
 |   	lista = list(map(list,help))	|
 |   	for letra in correctLetters:	|
 |      if letra in lista[0]:		|
 |        lista[0].remove(letra)        |   
 |  return random.choice(lista[0])	|
-+--------------------------------------+-