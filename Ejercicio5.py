# Función para calcular el promedio de las notas y determinar si aprueba
def calcular_promedio_y_aprobar():
    # Pedimos al profesor que ingrese cuántas notas se van a introducir
    try:
        cantidad_notas = int(input("Ingresa la cantidad de notas: "))
        
        # Inicializamos las variables
        suma_notas = 0
        contador = 0
        
        # Usamos el ciclo while para ingresar las notas una por una
        while contador < cantidad_notas:
            # Pedimos al usuario que ingrese una nota
            nota = float(input(f"Ingresa la nota {contador + 1}: "))
            
            # Verificamos si la nota está en el rango válido
            if 0 <= nota <= 5:
                suma_notas += nota
                contador += 1
            else:
                print("Nota inválida. Debe estar en el rango de 0 a 5.")
        
        # Calculamos el promedio
        promedio = suma_notas / cantidad_notas
        
        # Mostramos el promedio
        print(f"El promedio es: {promedio:.2f}")
        
        # Determinamos si el estudiante aprueba o no
        if promedio >= 4.5:
            print("¡El estudiante aprueba la asignatura!")
        else:
            print("El estudiante no aprueba la asignatura.")
    
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamamos a la función
calcular_promedio_y_aprobar()
