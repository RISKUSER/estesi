# Programa para realizar operaciones aritméticas básicas

# Solicitar dos números al usuario
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Realizar las operaciones
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 if numero2 != 0 else "No se puede dividir por cero"

    # Mostrar los resultados
    print(f"La suma de {numero1} y {numero2} es: {suma}")
    print(f"La resta de {numero1} y {numero2} es: {resta}")
    print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
    print(f"La división de {numero1} entre {numero2} es: {division}")

except ValueError:
    print("Por favor, ingresa un número válido.")
