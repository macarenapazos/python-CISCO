miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

nuevaLista = []

for element in miLista:
 if element in nuevaLista:
  continue
 else:
  nuevaLista.append(element)
miLista = nuevaLista

print("La lista solo con elementos únicos:")
print(miLista)

