# Función para calcular el factorial de un número
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Solicitar al usuario que ingrese un número
try:
    numero = int(input("Introduce un número entero para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        # Llamamos a la función para calcular el factorial
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")

    