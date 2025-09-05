#  Ejercicio 2: Identificador de vocales
#  Objetivo: Clasificar caracteres usando condicionales.
#  Instrucciones:
# 1. Solicita una letra al usuario.
# 2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra
# ingresada es una vocal".
# 3. En otro caso, imprime: "La letra ingresada no es una vocal".

letra_ingresada = input("Ingrese una letra:")

letra_final = letra_ingresada.lower()

if letra_final == "a,e,i,o,u":
    print("La letgra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")    

#  Ejercicio 3: Clasificador de números
#  Objetivo: Determinar el signo de un número.
#  Instrucciones:
# 1. Pide un número al usuario.
# 2. Si es positivo, imprime: "El número es positivo".
# 3. Si es negativo, imprime: "El número es negativo".
# 4. Si es c ero, imprime: "El número es cero".

numero = int(input("Ingrese un numero para determinar su valor"))

if numero > 0 :
    print("El número ingresado es positivo")
elif numero < 0 :
    print("El número ingresado es negativo")
elif numero == 0 :
    print("El número ingresado es 0")
    

#  Objetivo: Comparar dos números con condicionales.
#  Instrucciones:
# 1. Solicita dos números al usuario.
# 2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# 3. Si el primero es menor, imprime: "El primer número ingresado es menor".
# 4. Si son iguales, imprime: "Los números ingresados son iguales".

numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el segundo numero"))

if numero1 > numero2:
    print("El primer número ingresado es mayor")
elif numero1 < numero2 :
    print("El primer número ingresado es menor")
elif numero1 == numero2:
    print("Los números ingresados son iguales")
else:
    print("ERROR")
    
# Ejercicio 6: Detector de años bisiestos
#  Objetivo: Aplicar condiciones compuestas.
#  Instrucciones:
# 1. Pide un año al usuario.
# 2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se
# ingresó un año bisiesto".
# 3. En otro caso, imprime: "Se ingresó un año no bisiesto".

anio = int(input("Ingrese un año"))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) :
    print("Es un año bisiesto")
else: 
    print("No es una año bisiesto")
    
# Objetivo: Manipular strings con condicionales.
#  Instrucciones:
# 1. Pide una frase o palabra al usuario.
# 2. Si no termina en punto, añádelo al final.
# 3. Imprime el resultado.


frase = input("Ingrese una palabra o frase")

if not frase.endswith(".") :
    print(f"{frase}.")
else:
    print("Resultado:", frase)
    
#  Objetivo: Implementar múltiples condiciones.
#  Instrucciones:
# 1. Pide al usuario que cree una contrasenia.
# 2. Verifica que cumpla:
# o 8+ caracteres y ≤20 caracteres.
# o Al menos 1 mayúscula (usa .isupper()).
# o Al menos 1 número (usa .isdigit()).
# 3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contrasenia.".
# 4. Si no, imprime: "La contrasenia no es segura.".


contrasenia = input("Crea una contrasenia: ")


longitud_valida = 8 <= len(contrasenia) <= 20
tiene_mayuscula = any(caracter.isupper() for caracter in contrasenia)
tiene_numero = any(caracter.isdigit() for caracter in contrasenia)


if longitud_valida and tiene_mayuscula and tiene_numero:
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura.")

# 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# o Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al
# menos 8 caracteres.".
# o Si tiene >20 caracteres: "...no más de 20 caracteres.".
# o Si falta mayúscula: "...al menos una mayúscula.".
# o Si falta número: "...al menos un número.".

contrasenia = input("Crea una contraseña: ")

if len(contrasenia) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
elif len(contrasenia) > 20:
    print("La contraseña no es segura. No más de 20 caracteres.")
elif not any(c.isupper() for c in contrasenia):
    print("La contraseña no es segura. Debe tener al menos una mayúscula.")
elif not any(c.isdigit() for c in contrasenia):
    print("La contraseña no es segura. Debe tener al menos un número.")
else:
    print("¡Felicitaciones! Creaste tu contraseña.")

# 1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
# 2. Usa la tabla proporcionada para determinar el resultado (ganador o
# empate).
# 3. Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE"

jugador1 = input("Jugador 1, elige: piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige: piedra, papel o tijera: ").lower()

if jugador1 == "piedra":
    if jugador2 == "piedra":
        print("EMPATE")
    elif jugador2 == "papel":
        print("GANA JUGADOR 2")
    elif jugador2 == "tijera":
        print("GANA JUGADOR 1")
    else:
        print("Jugada inválida de Jugador 2")
elif jugador1 == "papel":
    if jugador2 == "piedra":
        print("GANA JUGADOR 1")
    elif jugador2 == "papel":
        print("EMPATE")
    elif jugador2 == "tijera":
        print("GANA JUGADOR 2")
    else:
        print("Jugada inválida de Jugador 2")
elif jugador1 == "tijera":
    if jugador2 == "piedra":
        print("GANA JUGADOR 2")
    elif jugador2 == "papel":
        print("GANA JUGADOR 1")
    elif jugador2 == "tijera":
        print("EMPATE")
    else:
        print("Jugada inválida de Jugador 2")
else:
    print("Jugada inválida de Jugador 1")
