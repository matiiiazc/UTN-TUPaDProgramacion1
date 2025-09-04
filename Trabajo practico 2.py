# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_del_usuario = int(input ("Ingrese su edad"))

if edad_del_usuario >= 18:
    print ("Eres mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.


nota_obtenida = int(input("Ingrese la nota obtenida"))

if nota_obtenida >= 6 :
    print("Aprobado")
else:
    print("Desaprobado")
    
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese solo numeros pares"))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Porfavor ingrese un numero par")
    
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un niño")
elif edad >= 12 and edad < 18: 
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven")
else:
    print("Eres un adulto/a mayor")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contrasena = input("Ingrese una contraseña entre 8 y 14 caracteres")

long_contrasena = len(contrasena)

if long_contrasena <= 14:
    print("Usted a ingresado correctamente la contraseña")
else:
    print("Por favor ingrese una contraseña de 8 a 14 caracteres")
    
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

from statistics import list 
from statistics import mean, median, mode
import random

numeros_aleatorios = [random.randit(1,100) for i in range (50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(f"La media es:{media},La mediana es:{mediana} y la moda es:{moda}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase_ingresada = input("Ingrese una frase: ")


ultima_letra = frase_ingresada[-1].lower()

if ultima_letra in "aeiou":
    print(f"{frase_ingresada}!")
else:
    print(frase_ingresada)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    nombre_en_mayusculas = nombre.upper()
    print(nombre_en_mayusculas)
elif opcion == 2:
    nombre_en_minusculas = nombre.lower()
    print(nombre_en_minusculas)
elif opcion == 3:
    nombre_con_mayuscula_primer_letra = nombre.title()
    print(nombre_con_mayuscula_primer_letra)
else:
    print("ingrese un valor correcto")
    
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud"))

if magnitud > 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("leve")
elif magnitud >= 4 and magnitud < 5:
    print("moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
else:
    print("ERROR")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

if hemisferio == "N":
    print(f"Estás en el hemisferio norte. La estación es: {estacion_norte}")
elif hemisferio == "S":
    print(f"Estás en el hemisferio sur. La estación es: {estacion_sur}")
else:
    print("Hemisferio inválido. Debe ser 'N' o 'S'.")
