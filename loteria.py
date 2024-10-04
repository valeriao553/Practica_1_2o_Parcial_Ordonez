# Loteria
print(" ")  # Espacio
print("Ordonez Martinez Valeria 3W, Loteria")  # Nombre
print(" ")  # Espacio
#Solicitar al usuario numeros ganadores y declarar las variables
g1 = int(input("Ingrese el primer numero triunfador: "))
g2 = int(input("Ingrese el segundo numero triunfador: "))
g3 = int(input("Ingrese el tercer numero triunfador: "))
#Imprimir los numeros ganadores
thislist = [g1, g2, g3]
#Usar sort para ordenarlos de menor a mayor
thislist.sort() 
#Hacer loop para ponerlos en una lista vertical
print(thislist)
for x in thislist:
  print(x) 
