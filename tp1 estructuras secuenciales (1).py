#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Como es tu nombre? ")
apellido = input("Como es tu apellido? ")
edad = int(input("Que edad tienes? "))
residencia = input("Cual es tu lugar de residencia? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
#Área = π * radio² y Perímetro = 2 * π * radio,

import math 

radio = float(input("Ingrese su radio: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El perimetro es: {perimetro} y el area es: {area}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

segundos = int(input("Ingrese la cantidad de segundos: "))
minutos = segundos / 60
horas = minutos / 60

print("Equivale a", horas, "horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un número: "))

numero_por_1 = numero * 1
numero_por_2 = numero * 2 
numero_por_3 = numero * 3
numero_por_4 = numero * 4
numero_por_5 = numero * 5
numero_por_6 = numero * 6
numero_por_7 = numero * 7
numero_por_8 = numero * 8
numero_por_9 = numero * 9
numero_por_10 = numero * 10

print(f"""
{numero} x 1  = {numero_por_1}
{numero} x 2  = {numero_por_2}
{numero} x 3  = {numero_por_3}
{numero} x 4  = {numero_por_4}
{numero} x 5  = {numero_por_5}
{numero} x 6  = {numero_por_6}
{numero} x 7  = {numero_por_7}
{numero} x 8  = {numero_por_8}
{numero} x 9  = {numero_por_9}
{numero} x 10 = {numero_por_10}
""")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingrese el primer número (distinto de 0): "))
numero_2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicación es {multiplicacion}")
print(f"La división es {division}")

#8)
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura = float(input("Ingrese su altura en metros (ej: 1.75): "))
peso = float(input("Ingrese su peso en kilogramos: "))

indice_de_masa_corporal = peso / (altura ** 2)

print(f"Su índice de masa corporal es {indice_de_masa_corporal:.2f}")

#9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

grados_fahrenheit = (9/5) * grados_celsius + 32 

print(f"La conversion de Celsius a Fahrenheit es: {grados_fahrenheit:.2f} °F")

#10
# ) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

suma_total = numero1 + numero2 + numero3

promedio = suma_total / 3

print(f"El promedio de los numeros {numero1}, {numero2}, {numero3} es {promedio}")
