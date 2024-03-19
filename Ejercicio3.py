class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nave: {self.nombre}, Longitud: {self.longitud}, Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}"


def ordenar_naves(lista_naves):
    """
    Ordena la lista de naves por nombre de forma ascendente y longitud de forma descendente.
    """
    lista_naves.sort(key=lambda x: (x.nombre, -x.longitud))


def mostrar_info_naves_especificas(lista_naves):
    """
    Muestra la información de las naves "Cometa Veloz" y "Titán del Cosmos".
    """
    print("Información de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in lista_naves:
        if nave.nombre == "Cometa Veloz" or nave.nombre == "Titán del Cosmos":
            print(nave)


def naves_con_mas_pasajeros(lista_naves):
    """
    Devuelve las cinco naves con mayor cantidad de pasajeros.
    """
    lista_naves.sort(key=lambda x: x.pasajeros, reverse=True)
    return lista_naves[:5]


def nave_con_mas_tripulacion(lista_naves):
    """
    Devuelve la nave que requiere la mayor cantidad de tripulación.
    """
    lista_naves.sort(key=lambda x: x.tripulantes, reverse=True)
    return lista_naves[0]


def mostrar_naves_con_prefijo(lista_naves, prefijo):
    """
    Muestra todas las naves cuyo nombre comienza con el prefijo dado.
    """
    print(f"Naves cuyo nombre comienza con '{prefijo}':")
    for nave in lista_naves:
        if nave.nombre.startswith(prefijo):
            print(nave)


def naves_con_suficientes_pasajeros(lista_naves, cantidad_pasajeros):
    """
    Devuelve una lista de todas las naves que pueden llevar la cantidad de pasajeros especificada o más.
    """
    naves_suficientes = [nave for nave in lista_naves if nave.pasajeros >= cantidad_pasajeros]
    return naves_suficientes


def mostrar_nave_extremos(lista_naves):
    """
    Muestra la información de la nave más pequeña y la más grande.
    """
    lista_naves.sort(key=lambda x: x.longitud)
    print("Información de la nave más pequeña:")
    print(lista_naves[0])
    print("Información de la nave más grande:")
    print(lista_naves[-1])


if __name__ == "__main__":
    nave1 = NaveEspacial("Cometa Veloz", 100, 10, 50)
    nave2 = NaveEspacial("Titán del Cosmos", 200, 20, 100)
    nave3 = NaveEspacial("GX-5000", 150, 15, 80)
    nave4 = NaveEspacial("Estrella Fugaz", 180, 18, 90)
    nave5 = NaveEspacial("Galaxia Explorer", 120, 12, 70)
    lista_naves = [nave1, nave2, nave3, nave4, nave5]

    # Ordenar la lista de naves
    ordenar_naves(lista_naves)

    # Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
    mostrar_info_naves_especificas(lista_naves)

    # Determinar las cinco naves con mayor cantidad de pasajeros
    cinco_naves_mas_pasajeros = naves_con_mas_pasajeros(lista_naves)
    print("\nLas cinco naves con mayor cantidad de pasajeros son:")
    for nave in cinco_naves_mas_pasajeros:
        print(nave)

    # Indicar la nave que requiere la mayor cantidad de tripulación
    nave_mayor_tripulacion = nave_con_mas_tripulacion(lista_naves)
    print("\nLa nave que requiere la mayor cantidad de tripulación es:")
    print(nave_mayor_tripulacion)

    # Mostrar todas las naves cuyo nombre comienza con "GX"
    mostrar_naves_con_prefijo(lista_naves, "GX")

    # Listar todas las naves que pueden llevar seis o más pasajeros
    print("\nNaves que pueden llevar seis o más pasajeros:")
    naves_seis_o_mas_pasajeros = naves_con_suficientes_pasajeros(lista_naves, 6)
    for nave in naves_seis_o_mas_pasajeros:
        print(nave)

    # Mostrar la información de la nave más pequeña y la más grande
    mostrar_nave_extremos(lista_naves)
