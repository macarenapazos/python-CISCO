###################################################################
#                 Pazos Macarena Lab 3.1.2.15                     #
###################################################################

#LABORATORIO: Hipótesis de Collatz

﻿c0 = int(input("Ingrese un numero: "))	#le pido al usuario que ingrese un numero y lo guardo en una variable

if c0 < 1:				#si el numero es negativo
 print("Use un número positivo distinto de 0")	#imprimo este mensaje
 exit					#y salgo del if
else:					# si el número es positivo
 pasos = 0				#creo una variable que contara el numero total de pasos

 while c0 != 1:				#hago un bucle que se va a usar siempre que c0 sea distinto que 1
  if c0 % 2 == 0:			#si c0 es par se divide en 2
   c0 = c0/2
  else:					#si c0 es impar se multiplica por 3 y se suma 1
   c0 = 3*c0+1
  print(int(c0))			#imprimo el valor que va tomando c0
  pasos += 1				#voy contandolos pasos
 print("Número total de pasos: ", pasos)#imprimo el numero total de pasos
