###################################################################
#                 Pazos Macarena Lab 3.1.1.12                     #
###################################################################

#LABORATORIO: Lo fundamental de la instrucción if-else

#Le pido al usuario que ingrese un número y lo paso a float

ingreso=float(input("Ingrese el ingreso anual:")) 

#Hago una analisis por casos para calcular el impuesto

if ingreso <= 85528:
    impuesto= (ingreso*18)/100 - 556.02
    if impuesto<0:
        impuesto=0
else:
    impuesto= 14839.02 + ((ingreso-85528)*32)/100

#Redondeo el impuesto y luego lo muestro por pantalla
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
