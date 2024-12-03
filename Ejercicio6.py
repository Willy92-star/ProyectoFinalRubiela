# Función para convertir dólares a pesos
def convertir_dolares_a_pesos(dolares):
    tasa_de_cambio = 3934  # Definir la tasa de cambio primero
    return dolares * tasa_de_cambio  # Usar la tasa de cambio después de haberla definido

# Función que realiza la conversión y permite al usuario seguir haciendo conversiones
while True:
    # Solicitar al usuario que ingrese la cantidad de dólares
    try:
        dolares = float(input("Ingresa la cantidad de dólares a convertir: "))
        
        # Convertir dólares a pesos
        pesos = convertir_dolares_a_pesos(dolares)
        
        # Mostrar el resultado de la conversión
        print(f"{dolares} dólares equivalen a {pesos} pesos.")

    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")
    
    # Preguntar si desea seguir realizando conversiones
    respuesta = input("¿Deseas realizar otra conversión? (sí/no): ").strip().lower()
    
    # Verificar la respuesta y continuar o salir
    if respuesta == "sí":
        continue  # Si la respuesta es "sí", el ciclo continúa
    elif respuesta == "no":
        print("Gracias por utilizar el convertidor. ¡Hasta luego!")
        break  # Si la respuesta es "no", se termina el ciclo
    else:
        print("Respuesta no válida. Por favor, ingresa 'sí' o 'no'.")