'''En este módulo se utilizan ciertas funciones para buscar productos dentro del catálogo.'''

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