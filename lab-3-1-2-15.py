c0 = int(input("Ingrese un numero: "))

if c0 < 1:
 print("Use un número positivo distinto de 0")
 exit
else:
 pasos = 0

 while c0 != 1:
  if c0 % 2 == 0:
   c0 = c0/2
  else:
   c0 = 3*c0+1
  print(int(c0))
  pasos += 1
 print("Número total de pasos: ", pasos)
