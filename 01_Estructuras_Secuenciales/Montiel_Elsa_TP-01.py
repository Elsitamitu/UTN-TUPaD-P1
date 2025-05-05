#Ejercicio1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo")

print("///////////////////////////////////////////////////////////////////////////")

#Ejercicio2
## Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla. 
nombre = input("Ingrese su nombre: ")
print(f"Hola",nombre,"!")


print("//////////////////////////////////////////////////////////////////")

#Ejercicio3
## Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
residencia=input("Ingrese su lugar de residencia:")
print(f"Soy",nombre,apellido,",tengo",edad,"años y vivo en ",residencia)


print("//////////////////////////////////////////////////////////////////////")

#Ejercicio4
## Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.
pi=3.14159
radio=float(input("Ingrese el radio del círculo :"))
perímetro=float(2*pi*radio)
área=float(pi*radio**2)
print("El área del circulo es:",área,"y su perímetro es:",perímetro)


print("////////////////////////////////////////////////////////////////////////")

#Ejercicio5
##Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.
segundo=int(input("Ingrese la cantidad de segundos que desea transformar a horas :"))
hora=segundo/3600
print("La equivalencia de:",segundo,"segundos a horas es de:",hora)


print("//////////////////////////////////////////////////////////////")

#Ejercicio6
## Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 
tabla=int(input("Ingrese un número del que quiera saber su tabla de multiplicar:"))
print("La tabla del",tabla,"es:")
print(f"{tabla}x1={tabla*1}")
print(f"{tabla}x2={tabla*2}")
print(f"{tabla}x3={tabla*3}")
print(f"{tabla}x4={tabla*4}")
print(f"{tabla}x5={tabla*5}")
print(f"{tabla}x6={tabla*6}")
print(f"{tabla}x7={tabla*7}")
print(f"{tabla}x8={tabla*8}")
print(f"{tabla}x9={tabla*9}")
print(f"{tabla}x10={tabla*10}")

print("//////////////////////////////////////////////////////////////////////////")

#Ejercicio7
## Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1=int(input("Ingrese un primer número distinto de cero:"))
numero2=int(input("Ingrese un segundo número distinto de cero:"))
suma=numero1+numero2
resta=numero1-numero2
producto=numero1*numero2
division=numero1/numero2
print("El resultado de la suma es:",suma)
print("El resultado de la resta es:",resta)
print("El resultado de la multiplicación es :",producto)
print("El resultado de la división es :",division)


print("///////////////////////////////////////////////////////////////////////")

#Ejercicio8
## Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.
peso=float(input("Ingrese su peso en kilogramos:"))
altura=float(input("Ingrese su altura en metros:"))
indice_de_masa_corporal=peso/altura**2
print("El índice de masa corporal es:",indice_de_masa_corporal)


print("///////////////////////////////////////////////////////////////////")

#Ejercicio9
## Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. 
temperatura_celsius=float(input("Ingrese la temperatura en Celsius que desea convertir a Fahrenheit:"))
temperatura_fahrenheit=(9/5)*temperatura_celsius+32
print("El resultado de la conversión es:",temperatura_fahrenheit)


print("/////////////////////////////////////////////////////////////////")

#Ejercicio10
## Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
print("Ingresa los tres numeros que deseas para calcular su promedio")
numero1=float(input("Ingresa el primer número:"))
numero2=float(input("Ingresa el segundo número:"))
numero3=float(input("Ingresa el tercer número:"))
promedio=(numero1+numero2+numero3)/3
print("El promedio de los tres números es:",promedio)



print("///////////////////////////////////////////////////////////")
