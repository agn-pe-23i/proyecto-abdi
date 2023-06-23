'''En este módulo se utilizan ciertas funciones para buscar productos dentro del catálogo; así como poder eliminarlo del mismo.'''

import menu

def buscar_producto():
    clave = input("Ingrese palabra clave: ")
    resultados = []

#Se busca el producto.
    for producto in menu.menu_productos:
        if clave.lower() in producto["Título"].lower():
            resultados.append(producto)

    if len(resultados) > 0:
        print(f"Se encontraron {len(resultados)} resultado(s) que coinciden con la búsqueda:")
        for producto in resultados:
            print(f"Tipo: {producto['Tipo']}")
            print(f"Título: {producto['Título']}")
    else:
        print("No se encontraron productos con la búsqueda.")


'''Iniciamos el programa para que, de desearlo se elimine un producto del catálogo. 
Ocupa importar el menu para seleccionar "eliminar", y seguimos con la función '.remove' para quitarlo del catálogo'''

def eliminar_producto():
    titulo = input("Ingrese el título del producto que desea eliminar: ")

    for producto in menu.menu_productos:
        if producto["Título"] == titulo:
            menu.menu_productos.remove(producto)
            print("El producto fue eliminado.")
            return

    print("No se encontró producto.")