###################################################################
#                 Pazos Macarena Lab 3.1.1.11                     #
###################################################################

#Operadores de comparación y ejecución condicional

﻿n = input("palabra: ") #Le pido al usuario que ingrese una palabra

#Luego comparo esa palabra ingresa haciendo un analisis por casos y
#muestro un resultado por pantalla.

if n == 'Espatifilo':	
    print("Si, ¡Espatifilo es la mejor planta de todas!")
elif n == 'espatifilo':
    print("No, ¡quiero un gran Espatifilo!")
else:
    print('¡Espatifilo! ¡No %s!' %n)
