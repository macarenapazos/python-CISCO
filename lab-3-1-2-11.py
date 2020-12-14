palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
 if letra in 'AEIOU':
  continue
 palabraSinVocal = palabraSinVocal + letra
# Imprimir la palabra asignada a palabraSinVocal.
print(palabraSinVocal)