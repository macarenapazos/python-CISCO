año = int(input("Introduzca un año:"))

if año < 1582:
 print("No está dentro del período del calendario gregoriano")
else:
 if año%4 !=0:
  print("Año común")
 else:
  if año%100 !=0:
   print("Año bisiesto")
  elif año%400 !=0:
   print("Año común")
  else:
   print("Año bisiesto")
   