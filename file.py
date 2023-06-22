'''Se utiliza este módulo para cargar el catálogo y poder guardarlo como archivo.'''
import menu

def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre completo del archivo (Catalogo.txt): ")
    try:
        with open(nombre_archivo, "r") as archivo:
            menu.menu_productos = eval(archivo.read())
        print("El catálogo se ha cargado.")
    except FileNotFoundError:
        print("catalogo no existe.")
    except:
        print("Ocurrió un error.")

#Función para guardar catálogo.
def guardar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(str(menu.menu_productos))
        print("Se ha guardado correctamente.")
    except:
        print("Ocurrió un error.")