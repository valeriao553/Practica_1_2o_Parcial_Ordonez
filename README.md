# Practica_1_2o_Parcial_Ordonez
Practica 1 segundo parcial

Ejercicio 1.
# Lista de precios
print(" ")#Espacio
print("Ordonez Martinez Valeria 3W, Lista de precios") #Nombre
print(" ") #Espacio
thislist=[43, 57, 92, 20, 37, 5, 9] #Almacenar los prcios en una lista
print("precios:", thislist) #Imprimir la lista
print("El menor de los precios es:", thislist[5]) #Mostrar el menor precio de la lista
print("El mayor de los precios es:", thislist[2]) #Mostrar el mayor precio de la lista
print(" ") #Espacio

![image](https://github.com/user-attachments/assets/6bde1b8b-20ae-4423-b442-ebfea12380b3)
![image](https://github.com/user-attachments/assets/2ee54edb-4878-45c2-9ab8-6ad9c254b811)

Ejercicio 2, 3 y 4.
# Materias
print(" ")#Espacio
print("Ordonez Martinez Valeria 3W, Lista de Materias") #Nombre
print(" ") #Espacio
thislist=["Humaninades","Ingles","Ecosistemas","L. y Comunicacion","P.Matenatico",] #Defino la lista
print(" ")#Espacio
print("La materias son: ",thislist) #Imprimir las materias que tenemos
print(" ") #Espacio
print("Estoy cursando: ",thislist[0]) #Mostrar la materia que se encuentra en el lugar 0
print("Estoy cursando: ",thislist[1]) #Mostrar la materia que se encuentra en el lugar 0
print("Estoy cursando: ",thislist[2]) #Mostrar la materia que se encuentra en el lugar 0
print("Estoy cursando: ",thislist[3]) #Mostrar la materia que se encuentra en el lugar 0
print("Estoy cursando: ",thislist[4]) #Mostrar la materia que se encuentra en el lugar 0
print(" ") #Esoacio
hum=int(input("Ingrese su calificacion en humanidades: ")) #Solicitar la calificacion
ing=int(input("Ingrese su calificacion en ingles "))       #Solicitar la calificacion
ec=int(input("Ingrese su calificacion en ecosistemas: "))  #Solicitar la calificacion
lc=int(input("Ingrese su calificacion en L. y comunicacion: ")) #Solicitar la calificacion
pm=int(input("Ingrese su calificacion en pensamiento matematico: ")) #Solicitar la calificacion
print(" ")
print("En humanidades tienes una calificacion de: ", hum) #Mostrar la calificacion
print("En ingles tienes una calificacion de: ", ing)      #Mostrar la calificacion
print("En ecosistemas tienes una calificacion de: ", ec)  #Mostrar la calificacion
print("En lengua y comunicacion tienes una calificacion de: ", lc) #Mostrar la calificacion
print("En pensamiento matematico tienes una calificacion de: ", pm) #Mostrar la calificacion
print(" ")

![image](https://github.com/user-attachments/assets/e865c38b-0190-4062-975b-3b7c90f94d9c)
![image](https://github.com/user-attachments/assets/d3600604-a8c2-4ae5-9d5c-63669e126318)

Ejercicio 5.
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

![image](https://github.com/user-attachments/assets/1040b128-b310-4456-bffd-4a40095db274)
![image](https://github.com/user-attachments/assets/34287025-f165-4663-b81c-3bae62bb2a4a)







