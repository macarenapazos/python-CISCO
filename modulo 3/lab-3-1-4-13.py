###################################################################
#                 Pazos Macarena Lab 3.1.4.13                     #
###################################################################

#LABORATORIO: Lo básico de las listas - The Beatles

# paso 1
beatles = []			#creo una lista vacía
print("Paso 1:", beatles)	#imprimo el paso 1

# paso 2
beatles.append('John Lennon')	#agrego un miembro a la lista
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2:", beatles)	#imprimo el paso2

# paso 3
for miembro in range(2):	#Hago un for para pedirle al usuario que ingrese dos miembros
 nombre = input("Ingrese otro miembro de la banda: ")
 beatles.append(nombre)
 print("Paso 3:", beatles)	#imprimo el paso 3

# etapa 4
del beatles[3:5]		#borro los elementos en la posicion que se indica
print("Paso 4:", beatles)	#muestro el paso 4

# paso 5
beatles.insert(0, "Ringo Starr")	#Agrego Ringo Starr en la posición 0
print("Paso 5:", beatles)		#muestro el paso 5


# probando la longitud de la lista
print("Los Fab", len(beatles))		#muestro el largo de la lista
