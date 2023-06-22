'''Aquí damos el comando para que, si se selecciona la opción mostrar catálogo, salga todo el contenido.'''

import menu


def mostrar_menu():
    while True:
        print("Menú mostrar catálogo")
        print("1. Películas")
        print("2. Series")
        print("3. Documentales")
        print("4. Eventos deportivos")
        print("5. Todo")
        print("6. Regresar")

        opcion = input("Por favor, haga una selección: ")

        if opcion == "1":
            mostrar_peliculas()
        elif opcion == "2":
            mostrar_series()
        elif opcion == "3":
            mostrar_documentales()
        elif opcion == "4":
            mostrar_eventos_deportivos()
        elif opcion == "5":
            mostrar_todo()
        elif opcion == "6":
            return
        else:
            print("Seleccione una opción válida.")


def mostrar_peliculas():
    peliculas = []
    for producto in menu.menu_productos:
        if producto["Tipo"] == "Película":
            peliculas.append(producto)

    if peliculas:
        print("Películas:")
        for pelicula in peliculas:
            print_producto(pelicula)
    else:
        print("No hay películas en el catálogo.")


def mostrar_series():
    series = []
    for producto in menu.menu_productos:
        if producto["Tipo"] == "Serie":
            series.append(producto)

    if series:
        print("Series:")
        for serie in series:
            print_producto(serie)
    else:
        print("No hay series en el catálogo.")


def mostrar_documentales():
    documentales = []
    for producto in menu.menu_productos:
        if producto["Tipo"] == "Documental":
            documentales.append(producto)

    if documentales:
        print("Documentales:")
        for documental in documentales:
            print_producto(documental)
    else:
        print("No hay documentales en el catálogo.")


def mostrar_eventos_deportivos():
    eventos = []
    for producto in menu.menu_productos:
        if producto["Tipo"] == "Evento deportivo en vivo":
            eventos.append(producto)

    if eventos:
        print("Eventos deportivos en vivo:")
        for evento in eventos:
            print_producto(evento)
    else:
        print("No hay eventos deportivos en vivo en el catálogo.")


def mostrar_todo():
    if menu.menu_productos:
        print("Catálogo completo:")
        for producto in menu.menu_productos:
            print_producto(producto)
    else:
        print("El catálogo está vacío.")


def print_producto(producto):
    print(f"Tipo: {producto['Tipo']}")
    print(f"Título: {producto['Título']}")
    tipo = producto['Tipo']

    if producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie':
        print(f"Actor principal: {producto.get('Actor principal', 'No hay actor principal')}")

    elif producto['Tipo'] == 'Película' or producto['Tipo'] == 'Serie' or producto['Tipo'] == 'Documental':
        print(f"Director: {producto.get('Director', 'No hay director')}")

    elif producto['Tipo'] == 'Serie':
        print(f"Temporadas: {producto.get('Temporadas', 'No hay temporadas disponibles')}")

    elif producto['Tipo'] == 'Documental':
        print(f"Tema: {producto.get('Tema', 'No hay tema disponible')}")

    elif producto['Tipo'] == 'Película' or producto['Tipo'] == 'Documental':
        print(f"Año: {producto.get('Año', 'No hay año disponible')}")

    else:
        producto['Tipo'] == 'Evento deportivo en vivo'
        print(f"Deporte: {producto.get('Deporte', 'No existe deporte o no se puso el deporte')}")
        print(f"Fecha: {producto.get('Fecha', 'No hay fecha')}")
        print(f"Hora: {producto.get('Hora', 'No hay hora')}")
        print(f"Lugar: {producto.get('Lugar', 'No hay lugar')}")

    print(f"Costo de renta: {producto.get('Costo de renta', 'No esta en renta')}")
    print(f"Costo de venta: {producto.get('Costo de venta', 'No esta en venta')}")