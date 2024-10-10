# Programa para determinar si un número es positivo, negativo o cero

# Pedir al usuario que ingrese un número
try:
    numero = float(input("Ingresa un número: "))

    # Condicional para verificar si es positivo, negativo o cero
    if numero > 0:
        print(f"El número {numero} es positivo.")
    elif numero < 0:
        print(f"El número {numero} es negativo.")
    else:
        print("El número es cero.")

except ValueError:
    print("Por favor, ingresa un número válido.")
