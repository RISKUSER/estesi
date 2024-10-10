# Programa para convertir temperaturas de Celsius a Fahrenheit

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

# Solicitar la temperatura en Celsius al usuario
try:
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C es igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, ingresa un número válido.")
