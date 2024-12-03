# Pedir los datos al usuario
nombre = input("Ingresa el nombre del aprendiz: ")
asignatura = input("Ingresa la asignatura: ")

# Pedir la calificación final
try:
    calificacion = float(input("Ingresa la calificación final (de 1 a 10): "))
    
    # Validar que la calificación esté dentro del rango permitido
    if calificacion < 1 or calificacion > 10:
        print("Error: La calificación debe estar entre 1 y 10.")
    else:
        # Mostrar el resultado dependiendo de la calificación
        if calificacion < 7:
            print(f"{nombre} ha reprobado la asignatura {asignatura}.")
            print("REPROBADO")
        else:
            print(f"{nombre} ha aprobado la asignatura {asignatura}.")
            print("APROBADO")
    
except ValueError:
    print("Error: Por favor, ingresa una calificación numérica válida.")
