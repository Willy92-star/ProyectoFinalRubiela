# Recorrer los números del 1 al 30
for i in range(1, 31):
    # Imprimir el número, sin salto de línea al final (por eso usamos 'end=" "')
    print(i, end=" ")

    # Cada vez que se imprimen 7 números, imprimimos un salto de línea
    if i % 7 == 0:
        print()  # Esto genera un salto de línea

