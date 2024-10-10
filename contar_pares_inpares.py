# Programa para contar números pares e impares

try:
    limite = int(input("Ingresa un número: "))
    pares = 0
    impares = 0

    # Bucle for para iterar sobre los números desde 1 hasta el límite
    for i in range(1, limite + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Hay {pares} números pares y {impares} números impares entre 1 y {limite}.")

except ValueError:
    print("Por favor, ingresa un número válido.")
