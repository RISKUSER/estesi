# Programa para verificar si una persona es mayor de edad y si puede consumir alcohol

# Pedir al usuario que ingrese su edad
try:
    edad = int(input("Ingresa tu edad: "))

    # Verificar si es mayor de edad
    if edad >= 18:
        print("Eres mayor de edad.")
        # Verificar si puede consumir alcohol (mayores de 21 en algunos países)
        if edad >= 21:
            print("Puedes consumir alcohol en países como EE.UU.")
        else:
            print("No puedes consumir alcohol en países como EE.UU.")
    else:
        print("Eres menor de edad.")

except ValueError:
    print("Por favor, ingresa una edad válida.")
