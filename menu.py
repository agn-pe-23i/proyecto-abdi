'''Menu para poder ingresar los nuevos productos.
Aquí importamos el catálogo y damos un menu en el que pueden seleccionar la opción que desean ejecutar'''
menu_productos = []


import menu


def obten_num(msj):
    while True:
        valor = input(msj)
        try:
            num = float(valor)
            return num
        except ValueError:
            print("Error: Debe ingresar un numero valido")

def agregar_producto():
    print("Menú agregar producto")
    print("1. Película")
    print("2. Serie")
    print("3. Documental")
    print("4. Evento deportivo en vivo")
    print("5. Regresar")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_pelicula()
    elif opcion == 2:
        agregar_serie()
    elif opcion == 3:
        agregar_documental()
    elif opcion == 4:
        agregar_evento_deportivo()

    # Agregar datos en peliculas.

def agregar_pelicula():
    titulo = input("Ingrese el título de la película: ")
    actor_principal = input("Ingrese el actor: ")
    director = input("Ingrese el director: ")
    año = input("Ingrese el año de la película: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    menu_productos.append({"Tipo": "Película", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Año": año, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La película ha sido agregada")

#agregar datos en series.
def agregar_serie():
    titulo = input("Ingrese el título de la serie: ")
    actor_principal = input("Ingrese el actor: ")
    director = input("Ingrese el director: ")
    temporadas = input("Ingrese la cantidad de temporadas: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    menu_productos.append({"Tipo": "Serie", "Título": titulo, "Actor principal": actor_principal, "Director": director, "Temporadas": temporadas, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("La serie ha sido agregada.")

#agregar datos en documentales.
def agregar_documental():
    titulo = input("Ingrese el título del documental: ")
    director = input("Ingrese el director: ")
    tema = input("Ingrese el tema del documental: ")
    anio = input("Ingrese el año del documental: ")
    costo_renta = float(input("Ingrese el costo de renta: "))
    costo_venta = float(input("Ingrese el costo de venta: "))
    menu_productos.append({"Tipo": "Documental", "Título": titulo, "Director": director, "Tema": tema, "Año": anio, "Costo de renta": costo_renta, "Costo de venta": costo_venta})
    print("El documental ha sido agregado.")

def agregar_evento_deportivo():
    titulo = input("Ingrese el título del evento deportivo: ")
    deporte = input("Ingrese el deporte del evento: ")
    fecha = input("Ingrese la fecha del evento: ")
    hora = input("Ingrese la hora del evento: ")
    lugar = input("Ingrese el lugar del evento: ")
    costo_venta = float(input("Ingrese el costo de venta: "))
    menu_productos.append({"Tipo": "Evento deportivo en vivo", "Título": titulo, "Deporte": deporte, "Fecha": fecha, "Hora": hora, "Lugar": lugar, "Costo de venta": costo_venta})
    print("El evento deportivo ha sido agregado.")
