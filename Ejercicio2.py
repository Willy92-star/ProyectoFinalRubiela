# Función para obtener los números impares en un rango
def obtener_impares(inicio, fin):
    # Verificamos que el rango sea válido
    if inicio > fin:
        return "El inicio del rango debe ser menor o igual al final."

    # Lista para almacenar los números impares
    impares = []

    # Iteramos desde el inicio hasta el fin
    for num in range(inicio, fin + 1):
        # Comprobamos si el número es impar
        if num % 2 != 0:
            impares.append(num)

    # Verificamos si la lista de impares está vacía
    if not impares:
        return "No existen números impares en el rango indicado"
    else:
        # Retornamos la lista de números impares
        return impares

# Bloque principal
try:
    # Solicitar al usuario los valores de inicio y fin
    inicio = int(input("Introduce el inicio del rango: "))
    fin = int(input("Introduce el final del rango: "))

    # Llamamos a la función para obtener los números impares
    resultado = obtener_impares(inicio, fin)

    # Verificamos si el resultado es una lista de impares o un mensaje de error
    if isinstance(resultado, list):
        print(f"Números impares entre {inicio} y {fin}: {', '.join(map(str, resultado))}")
    else:
        # Si no es una lista, mostramos el mensaje de error o mensaje sin impares
        print(resultado)

except ValueError:
    print("Por favor, ingresa números enteros válidos.")