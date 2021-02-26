###################################################################
#                 Pazos Macarena Lab 3.1.2.11                     #
###################################################################

#LABORATORIO: La declaración continue - El Bonito Devorador de Vocales

﻿palabraSinVocal = ""   #creo una variable str

userWord = input("Ingrese una palabra: ") #le pido al usuario que ingrese una palabra
userWord = userWord.upper()		  #la paso a mayúscula

for letra in userWord: 	#en el ciclo for recorro letra por letra
 if letra in 'AEIOU':	#me fijo si la letra es una vocal, y lo es
  continue		#continuo
 palabraSinVocal = palabraSinVocal + letra	#concateno la letra no vocal al str 
print(palabraSinVocal) 		#imprimo la palabra asignada a palabraSinVocal.
