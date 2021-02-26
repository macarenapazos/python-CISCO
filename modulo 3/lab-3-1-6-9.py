###################################################################
#                 Pazos Macarena Lab 3.1.6.9                      #
###################################################################

#LABORATORIO: Operando con listas - conceptos básicos

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]  #creo una lista con elementos
nuevaLista = []				  #creo una lista vacía

for element in miLista:			  #hago un for para recorrer la lista
 if element in nuevaLista:		  #si el elemento ya se encuentra en la nueva lista continuo
  continue
 else:					  #si el elemento no esta en la nueva lista
  nuevaLista.append(element)		  #lo agrego
miLista = nuevaLista			  

print("La lista solo con elementos únicos: ", miLista)	#muestro la lista con elementos sin repetir


