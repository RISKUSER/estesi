# Definición de funciones para las operaciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

# Programa principal
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    print(f"Suma: {sumar(num1, num2)}")
    print(f"Resta: {restar(num1, num2)}")
    print(f"Multiplicación: {multiplicar(num1, num2)}")
    print(f"División: {dividir(num1, num2)}")

except ValueError:
    print("Por favor, ingresa un número válido.")
