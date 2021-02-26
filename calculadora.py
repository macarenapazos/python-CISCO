#################################################################
# Pazos Macarena - Actividad libre de python, programación 1.   #
#################################################################



#defino la funcion menu que mostrara las opciones para que el usuario pueda interactuar.
def menu():
	print(
		"******************************************"
		"\n* Elija la operación que desea realizar: *"
		"\n*                                        *"
		"\n* A. Sumar dos números.                  *"
		"\n* B. Restar dos números.                 *"
		"\n* C. Dividir dos números.                *"
		"\n* D. Multiplicar dos números.            *"
		"\n****************************************** "
		)
	operacion = input("Elija la operación que desea realizar:") #le pido al usuario que seleccione que desea realizar
	operacion = operacion.upper()				  # paso su opción a mayus.	
	return operacion

#defino las funciones que tendra esta mini calculadora, en todas las funciones tomaran dos numeros para hacer los calculos indicados.

def sumar(a, b):
	return a+b

def restar(a,b):
	return a-b

def multiplicar(a,b):
	return a*b

def dividir(a,b):
	if(b == 0):
		print("No se puede dividir por cero")
		menu()   #cuando no se puede realizar la división volvera al menu.
	return a/b

#invocar a la funcion que realiza la operacion que el usuario desea realizar
def resultado(operacion):
	a = int(input("Ingrese el primer número: "))
	b= int(input("Ingrese el segundo número: "))
	if operacion == 'A':
		result = sumar(a,b)
	elif operacion == 'B':
		result =restar(a,b)
	elif operacion == 'D':
		result =multiplicar(a,b)
	elif operacion == 'C':
		result =dividir(a,b)
	return result

#programa principal: aqui se ejecutaran las funcion y se dará inicio al programa.
continua = True   #controlara el bucle
while(continua):
	operacion = menu()		#se guarda la opcion seleccionada por el usuario
	result = resultado(operacion)	#se le pasa a la funcion resultado donde seleccionara la funcion
	print(result)
	print("¿Desea hacer otra operación? (s/n)") 
	if(input() == 's' or input() == 'S'):
		continua = True
	elif(input() == 'n' or input() == 'N'):
		continua = False	#se le cambia el valor a la variable y el programa finaliza saliendo del bucle.
	else:
		print("Opción incorrecta")
		continua = True

