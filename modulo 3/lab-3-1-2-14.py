###################################################################
#                 Pazos Macarena Lab 3.1.2.14                     #
###################################################################

#LABORATORIO: Lo fundamental del ciclo while

bloques = int(input("Ingrese el número de bloques:"))  #le pido al usuario que ingrese el numero de bloques
altura = 0					       #inicializo la variable altura

while bloques > altura:				       #Hago un ciclo while con la condicion, si la cumple entra al ciclo
 altura = altura + 1
 bloques = bloques - altura
 
print("La altura de la pirámide:", altura)	       #imprimo por pantalla la altura de la pirámide 
