###################################################################
#                 Pazos Macarena Lab 3.1.1.13                     #
###################################################################

#LABORATORIO: Lo fundamental de la sentencia if-elif-else

#Le pido al usuario que intrduzca un año y lo guardo en una variable
﻿año = int(input("Introduzca un año:"))

#Realizo un analisis por caso para ver si pertenece al calendario gregoriano
if año < 1582:
 print("No está dentro del período del calendario gregoriano")
else:
#en caso de que pertenezca hago otro ciclo if para ver cual es año bisiesto
 if año%4 !=0:
  print("Año común")
 else:
  if año%100 !=0:
   print("Año bisiesto")
  elif año%400 !=0:
   print("Año común")
  else:
   print("Año bisiesto")
   
