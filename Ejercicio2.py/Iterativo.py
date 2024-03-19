def determinante_iterativo(matriz):
    det = 0
    n = len(matriz)
    
    # Si la matriz es de 2x2, calculamos el determinante directamente
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    # Aplicamos la regla de Sarrus
    for i in range(n):
        producto = 1
        for j in range(n):
            producto *= matriz[j][(i + j) % n]
        det += producto
    
    for i in range(n):
        producto = 1
        for j in range(n):
            producto *= matriz[j][(n - 1 - i + j) % n]
        det -= producto

    return det

# Función para solicitar al usuario los números de la matriz
def ingresar_matriz():
    matriz = []
    for _ in range(3):
        fila = []
        print("Ingresa una fila de números de derecha a izquierda:")
        for _ in range(3):
            num = int(input("Ingresa un número: "))
            fila.insert(0, num)  # Insertamos el número al inicio de la fila
        matriz.insert(0, fila)  # Insertamos la fila al inicio de la matriz
    return matriz

# Ejemplo de uso:
print("Ingresa los números de la matriz por filas de 3 en 3 de derecha a izquierda:")
matriz = ingresar_matriz()
determinante = determinante_iterativo(matriz)
print("El determinante de la matriz es:", determinante)

