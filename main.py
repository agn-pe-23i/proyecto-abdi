'''Importamos todos los modulos para que el programa principal pueda funcionar.
Se despliega el menu para que se muestren las opciones que se pueden seleccionar.'''

import mostrar
import menu
import buscar_eliminar

import file


def menu_principal():
    print("Menú principal")
    print("1. Agregar un producto")
    print("2. Buscar producto")
    print("3. Eliminar un producto")
    print("4. Mostrar el catálogo")
    print("5. Cargar catálogo")
    print("6. Guardar catálogo")
    print("7. Salir")

    opcion = input("Porfavor seleccione un número: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "1":
        menu.agregar_producto()
    elif opcion == "2":
        buscar_eliminar.buscar_producto()
    elif opcion == "3":
        buscar_eliminar.eliminar_producto()
    elif opcion == "4":
        mostrar.mostrar_menu()
    elif opcion == "5":
        file.cargar_catalogo()
    elif opcion == "6":
        file.guardar_catalogo()
    elif opcion == "7":
        print("Adios")
    else:
        print("Seleccione una opcion valida.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "7":
            break
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()