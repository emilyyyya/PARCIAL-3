def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 0:
        return
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

# Driver code
def main():
    while True:
        try:
            n = int(input("Por favor, ingresa el número de discos (entre 0 y 5): "))
            if 0 <= n <= 5:
                break
            else:
                print("El número de discos debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if n > 0:
        TowerOfHanoi(n, 'A', 'B', 'C')
    else:
        print("No hay discos para mover.")

if __name__ == "__main__":
    main()








