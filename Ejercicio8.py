# Programa que indica si una persona puede jubilarse según su edad y sexo

# Solicitar la edad y el sexo al usuario
edad = int(input("Por favor, ingresa tu edad: "))
sexo = input("¿Cuál es tu sexo? (Hombre/Mujer): ").strip().lower()

# Verificar si la persona puede jubilarse
if sexo == "hombre":
    if edad >= 63:
        print("¡Ya puedes jubilarte!")
    else:
        print("Aún no puedes jubilarte.")
elif sexo == "mujer":
    if edad > 54:
        print("¡Ya puedes jubilarte!")
    else:
        print("Aún no puedes jubilarte.")
else:
    print("Sexo inválido. Por favor ingresa 'Hombre' o 'Mujer'.")
