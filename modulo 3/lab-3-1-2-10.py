###################################################################
#                 Pazos Macarena Lab 3.1.2.10                     #
###################################################################

#LABORATORIO: La sentencia continue - El Feo Devorador de Vocales

userWord = input("Ingrese una palabra: ") #Indicar al usuario que ingrese una palabra
userWord = userWord.upper()	#paso la palabra ingresada a mayúsculas

for letra in userWord:		#hago un ciclo for para recorrer letra por letra
 if letra in 'AEIOU':		#si la letra es una vocal
  continue			#continua
 print(letra)			#imprimo letra por letra (las consonantes)
