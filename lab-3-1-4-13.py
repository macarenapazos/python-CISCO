# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2:", beatles)

# paso 3
for miembro in range(2):
 nombre = input("Ingrese otro miembro de la banda: ")
 beatles.append(nombre)
 print("Paso 3:", beatles)

# etapa 4
del beatles[3:5]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
