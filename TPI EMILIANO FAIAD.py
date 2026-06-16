#Emiliano Faiad
#DNI: 46054757
#TRABAJO PRACTICO INTEGRADOR

import csv

ARCHIVO = "C:/Users/Emiliano/Documents/UNT/programacion/Paises.csv"


def cargar_paises():
    paises = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })

    except FileNotFoundError:
        print("Archivo no encontrado.")

    return paises


def guardar_paises(paises):

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


def agregar_pais(paises):

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("No puede estar vacío.")
        return

    poblacion = int(input("Población: "))
    superficie = int(input("Superficie: "))
    continente = input("Continente: ")

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    print("País agregado.")


def actualizar_pais(paises):

    nombre = input("País a actualizar: ").lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            pais["poblacion"] = int(input("Nueva población: "))
            pais["superficie"] = int(input("Nueva superficie: "))

            print("Datos actualizados.")
            return

    print("País no encontrado.")


def buscar_pais(paises):

    texto = input("Buscar: ").lower()

    encontrados = []

    for pais in paises:

        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if encontrados:

        for pais in encontrados:
            print(pais)

    else:
        print("Sin resultados.")


def filtrar_continente(paises):

    continente = input("Continente: ").lower()

    for pais in paises:

        if pais["continente"].lower() == continente:
            print(pais)


def filtrar_poblacion(paises):

    minimo = int(input("Mínimo: "))
    maximo = int(input("Máximo: "))

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:
            print(pais)


def filtrar_superficie(paises):

    minimo = int(input("Mínimo: "))
    maximo = int(input("Máximo: "))

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:
            print(pais)


def ordenar_nombre(paises):

    ordenados = sorted(paises, key=lambda x: x["nombre"])

    for pais in ordenados:
        print(pais)


def ordenar_poblacion(paises):

    ordenados = sorted(paises,
                       key=lambda x: x["poblacion"])

    for pais in ordenados:
        print(pais)


def ordenar_superficie(paises):

    opcion = input("Ascendente(A) o Descendente(D): ").upper()

    if opcion == "A":
        ordenados = sorted(
            paises,
            key=lambda x: x["superficie"]
        )
    elif opcion == "D":
        ordenados = sorted(
            paises,
            key=lambda x: x["superficie"],
            reverse=True
        )
    else:
        print("opcion invalida")
        
    for pais in ordenados:
        print(pais)


def mostrar_estadisticas(paises):

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    promedio_poblacion = sum(
        p["poblacion"] for p in paises
    ) / len(paises)

    promedio_superficie = sum(
        p["superficie"] for p in paises
    ) / len(paises)

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nESTADÍSTICAS")
    print("Mayor población:", mayor["nombre"])
    print("Menor población:", menor["nombre"])
    print("Promedio población:", promedio_poblacion)
    print("Promedio superficie:", promedio_superficie)

    print("\nPaíses por continente")

    for cont, cantidad in continentes.items():
        print(cont, ":", cantidad)


def menu():

    paises = cargar_paises()

    while True:

        print("\n===== MENÚ =====")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar por nombre")
        print("8. Ordenar por población")
        print("9. Ordenar por superficie")
        print("10. Estadísticas")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_continente(paises)

        elif opcion == "5":
            filtrar_poblacion(paises)

        elif opcion == "6":
            filtrar_superficie(paises)

        elif opcion == "7":
            ordenar_nombre(paises)

        elif opcion == "8":
            ordenar_poblacion(paises)

        elif opcion == "9":
            ordenar_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            guardar_paises(paises)
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()