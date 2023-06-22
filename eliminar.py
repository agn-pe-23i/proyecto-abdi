"""Para este módulo se ocupa importar el menu para seleccionar "elminiar", y seguimos con la función
 '.remove' para quitarlo del catálogo"""

import menu

def eliminar_producto():
    titulo = input("Ingrese el título del producto que desea eliminar: ")

    for producto in menu.menu_productos:
        if producto["Título"] == titulo:
            menu.menu_productos.remove(producto)
            print("El producto fue eliminado.")
            return

    print("No se encontró producto.")