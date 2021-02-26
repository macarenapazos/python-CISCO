###################################################################
#                 Pazos Macarena Lab 3.1.2.3                      #
###################################################################

#LABORATORIO: Lo esencial del ciclo while - Adivina el número secreto

numeroSecreto = 777 #guardo en una variable el número a adivinar

print( #imprimo el mensaje por pantalla
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

n = int(input("numero secreto: ")) #le pido al usuario que ingrese un numero y lo guardo en una variable como int para poder compararlo

while n !=numeroSecreto:	#realizo un ciclo while, asi mientras que el usuario no ingrese el numero correcto no podra salir
 print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
 n = int(input("numero secreto: "))
print("¡Bien hecho, muggle! Eres libre ahora") #muestro este mensaje si logra adivinar el numero
