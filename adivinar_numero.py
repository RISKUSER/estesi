import random

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intento = None

print("Adivina el número secreto entre 1 y 100.")

# Bucle while para continuar hasta que el usuario adivine correctamente
while intento != numero_secreto:
    try:
        intento = int(input("Ingresa tu intento: "))
        
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto: {numero_secreto}.")
    
    except ValueError:
        print("Por favor, ingresa un número válido.")
