def determinante_recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(len(matriz)):
            signo = (-1) ** i
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            det += signo * matriz[0][i] * determinante_recursivo(submatriz)
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
determinante = determinante_recursivo(matriz)
print("El determinante de la matriz es:", determinante)

