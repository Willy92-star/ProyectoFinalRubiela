# Programa para calcular la calificación final de un aprendiz

# Solicitar los datos al usuario
nombre = input("Ingrese su nombre: ")
asignatura = input("Ingrese la asignatura: ")
nota1 = float(input("Ingrese la nota del primer examen (0 a 5): "))
nota2 = float(input("Ingrese la nota del segundo examen (0 a 5): "))
nota3 = float(input("Ingrese la nota del último examen (0 a 5): "))

# Calcular la calificación final con los porcentajes especificados
calificacion_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

# Mostrar el resultado
print("\n---- Resultados ----")
print(f"Nombre del aprendiz: {nombre}")
print(f"Asignatura: {asignatura}")
print(f"Calificación final: {calificacion_final:.2f}")

# Determinar si aprueba o no
if calificacion_final >= 4.0:
    print("¡Felicidades! Has aprobado.")
else:
    print("Lo siento, no has aprobado.")
