def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Programa principal
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    mayor = mayor_de_tres(num1, num2, num3)
    print(f"El mayor de los tres números es: {mayor}")

except ValueError:
    print("Por favor, ingresa un número válido.")
