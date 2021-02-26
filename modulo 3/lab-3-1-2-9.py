###################################################################
#                 Pazos Macarena Lab 3.1.2.9                      #
###################################################################

#LABORATORIO: La declaración break - Atascado en un ciclo

﻿while True: #Hago un bucle infinito
 n=input('Ingrese una palabra: ') #le pido al usuario que ingrese una palabra
 if n!='chupacabras':	#si la palabra ingresada no es igual a 'chupacabras'
  n			#le vuelvo a pedir que ingrese una palabra
 else:			#si la palabra ingresada coincide con 'chupacabras'
  print("¡Has dejado el ciclo con éxito")		#muestro este mensaje
  break							#salgo del ciclo
