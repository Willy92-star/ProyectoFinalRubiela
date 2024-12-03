# Función para calcular el capital final con interés compuesto
def calcular_inversion(capital_inicial, tasa_interes, tiempo):
    # Fórmula de interés compuesto
    capital_final = capital_inicial * (1 + tasa_interes)**tiempo
    return capital_final

# Bloque principal
try:
    # Solicitar al usuario los datos de la inversión
    monto_invertir = float(input("Ingresa la cantidad de dinero a invertir: "))
    interes_anual = float(input("Ingresa el interés anual (en porcentaje): ")) / 100  # Convertir porcentaje a decimal
    tiempo_inversion = float(input("Ingresa el tiempo de la inversión en años: "))

    # Calcular el capital final
    capital_obtenido = calcular_inversion(monto_invertir, interes_anual, tiempo_inversion)

    # Mostrar el resultado
    print(f"El capital obtenido después de {tiempo_inversion} años es: ${capital_obtenido:.2f}")

except ValueError:
    print("Por favor, ingresa valores válidos para la inversión, interés y tiempo.")
