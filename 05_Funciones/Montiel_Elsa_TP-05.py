#LISTAS
#Ejercicio1
#  Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range.

multiplos_de_cuatro=list(range(4,101,4))  #crea y almacena la lista que contiene los multiplos de 4
print(multiplos_de_cuatro)    #imprime en pantalla


print("////////////////////////////////////////////////////////////////////")

#Ejercicio2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos!

lista_de_5_elementos=["Elsa","escuchar","&",9,5]  #crea y almacena la lista de 5 elementos
penultimo_elemento=lista_de_5_elementos[3]    #selecciona el penultimo elemento
print(penultimo_elemento)    #lo imprime por pantalla


#CON INDEXING    # lo mismo pero usando indexing con numeros negativos
mi_penultimo_elemento=lista_de_5_elementos[-2]
print(mi_penultimo_elemento)



print("////////////////////////////////////////////////////////////////")

#Ejercicio3
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: 
#lista_vacia = [] 

lista_vacia=[]   #crea una lista vacia
print(lista_vacia) #muestra la lista vacia
lista_vacia.append("Elsa")  #agrega primer elemento
print(f"La lista con el primer elemento es: {lista_vacia}")  #muestra el resultado
lista_vacia.append("Juan")    #agrega el segundo elemento
print(f"La lista con el segundo elemento es: {lista_vacia}")  #muestra el resultado
lista_vacia.append("Luis")    #agrega el tercer elemento
print(f"La lista con el tercer elemento es :{lista_vacia}")   #muestra el resultado


print("//////////////////////////////////////////////////////////////")

#Ejercicio4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"]

lista_animales=["perro","gato","conejo","pez"]   #se crea lista de animales
print(lista_animales)
lista_animales[1]="loro"  #en lista de animales se reemplaza el segundo elemento por "loro"
print(lista_animales)
lista_animales[-1]="oso"  #en lista de animales se reemplaza el ultimo elemento por "oso"
print(lista_animales)     #imprime la lista con todas las modificaciones


print("//////////////////////////////////////////////////////////////")


#Ejercicio5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#numeros=[8,15,3,22,7]
#numeros.remove(max(numeros))
#print(numeros)

#RESPUESTA: elimina de la lista "numeros"el maximo valor y luego lo imprime


print("///////////////////////////////////////////////////////////////")


#Ejercicio6
#  Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros.

lista_de_numeros=list(range(10,31,5)) #crea y almacena una lista desde 10 al 30 con escala 5
primeros_dos=lista_de_numeros[0:2]     #crea y almacena los dos primeros numeros de la lista
print(f"los dos primeros numeros de la lista son : {primeros_dos}")  #imprime los dos primeros numeros de la lista


print("//////////////////////////////////////////////////////////////////////")


#Ejercicio7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 

autos=["sedan","polo","suran","gol"]  #lista original
autos[1]="ford"   #se reemplaza del indice 1 por "ford"
autos[2]="coupe"   #se reemplaza del indice 2 por "coupe"
print(autos)       #se imprime la nueva lista


print("////////////////////////////////////////////////////////")


#Ejercicio8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla.

dobles=[]    #crea lista vacia
dobles.append(5*2)  #se le agrega el doble de 5
dobles.append(10*2)    #se agrega el doble de 10
dobles.append(15*2)   #se agrega el doble de 15
print(dobles)    #se imprime la lista resultante


print("///////////////////////////////////////////////////////")

#Ejercicio9
#Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
#compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 


#Agregando jugo a la lista del tercer cliente
compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]   #se crea la lista compras
posicion_dos=compras[2]  # se la almacena el contenido de la subcadena
posicion_dos.append("jugo")   #para agregarle otro elemento

#Reemplazando fideos por tallarines al segundo cliente
posicion_uno=compras[1]   #se almacena el contenido de la subcadena
posicion_uno[1]="tallarines"   #cambia de la posicion uno fideos por tallarines

#Elimina pan de la lista del primer cliente
posicion_cero=compras[0]  #se almacena el contenido de la subcadena
posicion_cero.remove("pan")  #elimina de la lista el elemento pan


#Imprime la lista resultante por pantalla
print(f"la lista modificada es : {compras}")



print("///////////////////////////////////////////////////////////////")

#Ejercicio10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.

lista_anidada=[15,True,[25.5,57.9,30.6],False]  #se crea la lista con los elementos que pide la consigna
print(f"La lista es : {lista_anidada}")   #se imprime por pantalla la lista resultante
















