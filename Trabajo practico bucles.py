# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

num = 0 

for num in range(0,101,1):
    print(f"{num}")
    
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Ingresa el primer numero: "))
fin = int(input("Ingresa el segundo numero: "))

if inicio > fin:
    inicio,fin = fin,inicio

suma = 0

for numero in range (inicio + 1, fin):
    suma += numero

print (f"la suma de los números entre {inicio} y {fin} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0

while True:
    numero = int(input("Ingrese un numero entero, para finalizar ingrese 0 "))

    if numero == 0:
        break
    
    suma += numero

print(f"El total de la suma de todos los numeros ingresados es de: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 

numero_aleatorio = random.randint(1,9)

intentos = 0

while True:
   numero_ingresado = int(input("Adivina el número entre 0 y 9: "))
   intentos += 1
   
   if numero_ingresado == numero_aleatorio:
       print("GANASTE!!!!")
       break
   else:
       print("No es el numero correcto")
       

print(f"Lograste adivinar en: {intentos} intentos")
    
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range (100,0,-2):
    print(numero)
    
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_ingresado_7 = int(input("Ingrese un numero entero:   "))
suma_total = 0

for i in range(0, numero_ingresado_7 + 1):
    suma_total += i


print(f"La suma de todos los valores entre 0 y {numero_ingresado_7} es: {suma_total}")
    
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

cantidad = 10  

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1


print(f"\nLa cantidad de pares es: {pares}")
print(f"La cantidad de impares es: {impares}")
print(f"La cantidad de positivos es: {positivos}")
print(f"La cantidad de negativos es: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 10 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad = 10  
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / cantidad

print(f"\nLa media de los {cantidad} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_ingresado10 = int(input("Ingrese un numero entero: "))

numero_invertido = int(str(numero_ingresado10)[::-1])

print(f"El número invertido es: {numero_invertido}")