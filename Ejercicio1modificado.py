# Función para calcular el factorial y la suma de los números involucrados
def calcular_factorial_y_suma(n):
    if n == 0:
        return 1, 0  # El factorial de 0 es 1, pero no hay números involucrados en la suma
    else:
        factorial = 1
        suma = 0
        for i in range(1, n + 1):
            factorial *= i
            suma += i
        return factorial, suma

# Solicitar al usuario que ingrese un número
try:
    numero = int(input("Introduce un número entero para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        # Llamamos a la función para calcular el factorial y la suma
        resultado_factorial, suma_numeros = calcular_factorial_y_suma(numero)
        promedio = suma_numeros / numero if numero > 0 else 0
        
        print(f"El factorial de {numero} es: {resultado_factorial}")
        print(f"La suma de los números involucrados en el factorial es: {suma_numeros}")
        print(f"El promedio de los números involucrados es: {promedio}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
