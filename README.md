[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
UNIVERSIDAD AUTÓNOMA METROPOLITANA  "UNIDAD   CUAJIMALPA"
# Trabajo Final: Informe Proyecto
LICENCIATURA: INGENIERÍA EN COMPUTACIÓN 


UEA: *PROGRAMACIÓN ESTRUCTURADA*

*ALUMNAS:*


Daniela Nava Martínez     MATRÍCULA: 2223028762


Abigail Sánchez López     MATRÍCULA: 2223068506

*PROFESOR:* 


Abel García Nájera


# RESUMEN
El proyecto final de la UEA de *Programación Estructurada* consiste en la creación de un catálogo de streaming que aplicará los conocimientos adquiridos durante el curso. Este proyecto abarca una variedad de conceptos y técnicas, como estructuras de control, tipos de datos, secuencias de datos, funciones, módulos, registros y archivos.


El objetivo principal es desarrollar un catálogo de streaming que cumpla con ciertas condiciones específicas que serán definidas en etapas posteriores del proyecto. Para abordar este proyecto completo, se utilizará el enfoque de *diseño top-down*, que implica comenzar con una visión global del problema y luego descomponerlo en subproblemas más pequeños y manejables. Esto permite un enfoque más estructurado y facilita el desarrollo y mantenimiento del código.


La herramienta seleccionada para la implementación del código es PyCharm, una aplicación que ha sido utilizada a lo largo del trimestre en la UEA. *PyCharm* ofrece una amplia gama de características útiles, como resultados inteligentes del código, inspección del código en busca de posibles errores, detección de errores en tiempo real y sugerencias de correcciones rápidas. Estas características permiten una programación más eficiente y aseguran que el código esté completo y funcional.


Para mantener la organización del proyecto, se creará una carpeta principal que contendrá los archivos principales del catálogo de streaming. Además, se crearán módulos como agregar producto, buscar producto, eliminar producto, mostrar catálogo, cargar catálogo y guardar catálogo para almacenar los registros de películas, series, documentales y eventos deportivos, lo que facilitará la gestión y navegación dentro del proyecto.


En resumen, el proyecto final de la UEA de *Programación Estructurada* consiste en desarrollar un catálogo de streaming utilizando el enfoque de *diseño top-down* y la herramienta *PyCharm*. Se aplicarán los conocimientos adquiridos durante el curso para implementar las estructuras de control, tipos de datos, funciones, módulos, registros y archivos necesarios. El objetivo es crear un catálogo funcional que cumpla con las condiciones específicas establecidas.



# ANTECEDENTES
Un servicio de streaming busca actualizar su sistema de renta y venta de películas, series, documentales y eventos deportivos en vivo. El objetivo es tener un catálogo completo y actualizado de los productos disponibles para su transmisión. Para lograrlo, se necesita desarrollar un sistema que permita interactuar de manera eficiente con dicho catálogo.


El sistema deberá contar con una interfaz de usuario intuitiva y amigable que permita la manipulación correcta y completa del catálogo de productos. Para lograr esto, se implementará una serie de menús que facilitarán la navegación y manipulación de la información.
En primer lugar, el sistema proporcionará un menú principal que presentará las opciones disponibles, como *"Buscar", "Agregar", "Mostrar" y "Eliminar"*. Estas opciones permitirán al usuario realizar diferentes acciones sobre el catálogo de productos.


En resumen, el servicio de streaming necesita actualizar su sistema de renta y venta de productos. El nuevo sistema contará con un catálogo completo y actualizado, y permitirá interactuar con él a través de una serie de menús que facilitarán la manipulación correcta y completa de los productos. Estos menús incluirán opciones para buscar, agregar, editar y eliminar productos, entre otras funcionalidades relevantes para el correcto funcionamiento del servicio.


# PROBLEMA
*MENÚ PRINCIPAL*
1. Deberá de considerar las siguientes opciones:
2. Agregar un producto
3. Buscar producto
4. Eliminar un producto
5. Mostrar el catálogo
6. Cargar catálogo
7. Guardar catálogo
8. Salir

   
*AGREGAR UN PRODUCTO*
En cada opción, el sistema debe registrar y recibir la información correspondiente, validando los valores ingresados y resolviendo los posibles errores que se presenten.
Menú agregar producto
1. Película
2. Serie
3. Documental
4. Evento deportivo en vivo
5. Regresar

   
*BUSCAR PRODUCTO*
El sistema debe solicitar palabras clave del título del producto a buscar y desplegar todos los productos que coincidan con el criterio de búsqueda, mostrando también el tipo de producto.


*ELIMINAR UN PRODUCTO*
Es necesario que el usuario introduzca la información necesaria para identificar de forma única el producto que desea eliminar.


*MOSTRAR CATÁLOGO*
Desplegará el segundo menú, y mostrará la información de acuerdo a la elección del usuario.
Menú mostrar catálogo
1. Películas
2. Series
3. Documentales
4. Eventos deportivos
5. Todo
6. Regresar

   
*CARGAR CATÁLOGO*
 Solicitará el nombre del archivo en donde está almacenado el catálogo. Si el archivo existe y se puede leer, se cargará el contenido del mismo.

 
*GUARDAR CATÁLOGO*
El sistema solicitará el nombre del archivo en donde se guardará el catálogo. Si el archivo se puede abrir para escritura, se guardarán los datos de los productos.


*CATÁLOGO DE PRODUCTOS*
El catálogo deberá considerar la siguiente información para cada producto:
'Película:'
Título, actriz o actor principal, directora o director, año.
'Serie:'
Título, actriz o actor principal, directora o director, temporadas.
'Documental:' 
Título, director o directora, tema, año.
'Evento deportivo en vivo:'
Título, deporte, fecha, hora, lugar.
Además, las películas, las series y los documentales tienen un costo de renta o de venta o de ambos. Los eventos deportivos en vivo sólo tienen costo de venta.


# DOCUMENTACIÓN

 __1. MAIN:__
Este código implementa un programa principal que utiliza diferentes módulos para realizar operaciones en un catálogo de productos. A continuación, se explica el flujo del programa:


Se importan los módulos necesarios para que el programa pueda funcionar. Los módulos importados son *eliminar, mostrar, menu, buscar, agregar y file*. Estos módulos contienen las funciones y lógica necesaria para realizar operaciones específicas en el catálogo de productos.


Se define la función *menu_principal()* que muestra el menú principal del programa. El menú presenta varias opciones para seleccionar, como agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar el catálogo desde un archivo y guardar el catálogo en un archivo. Además, hay una opción para salir del programa. El usuario selecciona una opción ingresando el número correspondiente.


La función *ejecutar_opcion(opcion)* recibe la opción seleccionada por el usuario y ejecuta la operación correspondiente según la opción seleccionada. Cada opción invoca la función correspondiente del módulo respectivo. Por ejemplo, si la opción es "1", se llama a la función *agregar.menu_agregar()* del módulo *agregar* para agregar un producto al catálogo.


La función *main()* es el punto de entrada del programa. Se ejecuta en un bucle infinito hasta que el usuario seleccione la opción "7" para salir. Dentro del bucle, se muestra el menú principal, se obtiene la opción seleccionada y se ejecuta esa opción llamando a *ejecutar_opcion(opcion)*. Si la opción seleccionada es "7", se rompe el bucle y el programa finaliza.


La sentencia *if __name__ == "__main__"*: asegura que el código dentro de main() se ejecute solo si el módulo se ejecuta como programa principal. Esto evita que el código se ejecute si el módulo se importa en otro lugar.
En resumen, este código crea un programa principal que interactúa con el usuario a través de un menú y utiliza diferentes módulos para realizar operaciones en un catálogo de productos, como agregar, buscar, eliminar, mostrar y gestionar el catálogo en archivos.

__2. BUSCAR_ELIMINAR:__
Para la primera parte de este módulo tenemos que buscar:
Este código es una función que permite buscar productos en un catálogo utilizando una palabra clave. 


*-import menu*: Importa un módulo llamado *menu*. Este módulo contiene la definición de la variable *menu_productos*, que es donde se almacenan los productos del catálogo.


*-def buscar_producto()*: Define una función llamada *buscar_producto*. Esta función permite al usuario ingresar una palabra clave para buscar productos en el catálogo.


*-clave = input("Ingrese palabra clave: ")*: Solicita al usuario que ingrese una palabra clave para realizar la búsqueda. La palabra clave se guarda en la variable *clave*.


*-resultados = []*: Crea una lista vacía llamada *resultados* donde se almacenarán los productos que coincidan con la búsqueda.


*-for producto in menu.menu_productos*: Itera sobre cada producto en la lista *menu.menu_productos* (que contiene los productos del catálogo).


*-if clave.lower() in producto["Título"].lower()*: Verifica si la palabra clave (en minúsculas) está presente en el título de cada producto del catálogo. La comparación se realiza en minúsculas para hacerla insensible a mayúsculas y minúsculas.


*-resultados.append(producto)*: Si el título del producto coincide con la palabra clave, se agrega el producto a la lista *resultados*.


*-if len(resultados) > 0:*: Verifica si se encontraron resultados de la búsqueda (es decir, si la lista *resultados* no está vacía).


*-print(f" Se encontraron {len(resultados)} resultado(s) que coinciden con la búsqueda:")*: Muestra un mensaje indicando la cantidad de resultados encontrados.
Itera sobre cada producto en la lista *resultados* y muestra información relevante del producto, como el tipo y el título.


*-else:*: Si no se encontraron resultados de la búsqueda, es decir, la lista *resultados* está vacía.


*-print("No se encontraron productos con la búsqueda.")*: Muestra un mensaje indicando que no se encontraron productos que coincidan con la búsqueda.


En resumen, este código implementa una función que permite buscar productos en un catálogo utilizando una palabra clave. Itera sobre los productos del catálogo y compara la palabra clave con el título de cada producto. Los productos que coincidan se almacenan en una lista de resultados y se muestran al usuario. Si no se encuentran productos que coincidan, se muestra un mensaje indicando que no se encontraron resultados.


Para la segunda parte de este módulo tenemos que *eliminar*:
Este código es una función que permite eliminar un producto del catálogo. 


*-import menu*: Importa un módulo llamado *menu*. Este módulo contiene la definición de la variable *menu_productos*, que es donde se almacenan los productos del catálogo.


*-def eliminar_producto()*: Define una función llamada *eliminar_producto*. Esta función permite al usuario ingresar el título del producto que desea eliminar del catálogo.


*-titulo = input("Ingrese el título del producto que desea eliminar: ")*: Solicita al usuario que ingrese el título del producto que desea eliminar. El título se guarda en la variable titulo.


*-for producto in menu.menu_productos:*: Itera sobre cada producto en la lista menu.menu_productos (que contiene los productos del catálogo).


*-if producto["Título"] == titulo:*: Verifica si el título del producto actual coincide con el título ingresado por el usuario.


*menu.menu_productos.remove(producto)*: Si se encuentra un producto con el título ingresado, se elimina el producto de la lista menu.menu_productos utilizando el método remove().


*print("El producto fue eliminado.")*: Muestra un mensaje indicando que el producto ha sido eliminado.


*-return*: Retorna de la función después de eliminar el producto. Esto evita que se siga iterando sobre los productos restantes en el catálogo.


*-print("No se encontró producto.")*: Si no se encontró un producto con el título ingresado, se muestra un mensaje indicando que no se encontró el producto.


En resumen, este código implementa una función que permite eliminar un producto del catálogo. Itera sobre los productos del catálogo y compara el título de cada producto con el título ingresado por el usuario. Si se encuentra un producto con el título coincidente, se elimina de la lista de productos. Si no se encuentra un producto con el título ingresado, se muestra un mensaje indicando que no se encontró el producto.


 __3. FILE:__
Este código define dos funciones relacionadas con la carga y el guardado de un catálogo en un archivo. 


*-import menu*: Importa un módulo llamado *menu*. Este módulo contiene la definición de la variable *menu_productos*, que es donde se almacenan los productos del catálogo.


*-def cargar_catalogo()*: Define una función llamada *cargar_catalogo*. Esta función permite cargar un catálogo desde un archivo.


*-nombre_archivo = input("Ingrese el nombre del archivo: ")*: Solicita al usuario que ingrese el nombre del archivo desde el cual se desea cargar el catálogo. El nombre del archivo se guarda en la variable *nombre_archivo*.


*-try:*: Inicia un bloque try-except para manejar excepciones.


*-with open(nombre_archivo, "r") as archivo:*: Abre el archivo especificado por el nombre ingresado en modo de lectura ("r") utilizando el contexto with, lo que garantiza que el archivo se cierre correctamente al finalizar.


*-menu.menu_productos = eval(archivo.read())*: Lee el contenido del archivo y utiliza la función eval() para evaluarlo como una expresión de Python. Se asume que el contenido del archivo es una representación válida de la lista *menu.menu_productos*. El resultado de la evaluación se asigna a la variable *menu.menu_productos*, sobrescribiendo el contenido anterior del catálogo.


*-print("El catálogo se ha cargado.")*: Muestra un mensaje indicando que el catálogo se ha cargado correctamente. *. except FileNotFoundError:*: Captura la excepción *FileNotFoundError* que se produce cuando el archivo especificado no se encuentra.


*-print("catalogo no existe.")*: Muestra un mensaje indicando que el archivo del catálogo no existe.


*-except:*: Captura cualquier otra excepción que no sea *FileNotFoundError*.


*-print("Ocurrió un error.")*: Muestra un mensaje genérico indicando que ocurrió un error al cargar el catálogo.


*-def guardar_catalogo()*: Define una función llamada guardar_catalogo. Esta función permite guardar el catálogo en un archivo. 


*-nombre_archivo = input("Ingrese el nombre del archivo: ")*: Solicita al usuario que ingrese el nombre del archivo en el cual se desea guardar el catálogo. El nombre del archivo se guarda en la variable *nombre_archivo*.


*-try:*: Inicia un bloque try-except para manejar excepciones.


*-with open(nombre_archivo, "w") as archivo:*: Abre el archivo especificado por el nombre ingresado en modo de escritura ("w") utilizando el contexto *with*, lo que garantiza que el archivo se cierre correctamente al finalizar.


*-archivo.write(str(menu.menu_productos))*: Escribe una representación en forma de cadena (str) de la lista *menu.menu_productos* en el archivo.


*-print("Se ha guardado correctamente.")*: Muestra un mensaje indicando que el catálogo se ha guardado correctamente en el archivo.


*-except*:Captura cualquier excepción que se produzca durante el guardado del catálogo.


*-print("Ocurrió un error.")*: Muestra un mensaje genérico indicando que ocurrió un error al guardar el catálogo.


En resumen, este código define dos funciones: *cargar_catalogo()* para cargar un catálogo desde un archivo y sobrescribir el contenido anterior del catálogo, y *guardar_catalogo()* para guardar el catálogo actual en un archivo. Ambas funciones manejan excepciones para mostrar mensajes de error en caso de problemas durante la carga o el guardado del catálogo.


__4. MENU:__
Este código implementa un menú interactivo para agregar nuevos productos a una lista llamada *menu_productos*. Los productos pueden ser películas, series, documentales o eventos deportivos en vivo.


El código comienza definiendo una lista vacía llamada *menu_productos* que se utilizará para almacenar los productos ingresados por el usuario.
A continuación, se definen varias funciones para agregar diferentes tipos de productos:


La función *agregar_producto()* muestra un menú con opciones para seleccionar el tipo de producto a agregar. Dependiendo de la opción elegida, se invoca la función correspondiente para agregar ese tipo de producto.


La función *agregar_pelicula()* solicita al usuario ingresar los datos de una película, como el título, el actor principal, el director, el año, el costo de renta y el costo de venta. Luego, crea un diccionario con esos datos y lo agrega a la lista *menu_productos*.


La función *agregar_serie()* funciona de manera similar a *agregar_pelicula()*, pero solicita los datos específicos de una serie, como el número de temporadas.


La función *agregar_documental()* solicita al usuario ingresar los datos de un documental, como el título, el director, el tema, el año, el costo de renta y el costo de venta. Luego, agrega un diccionario con esos datos a la lista *menu_productos*.


La función *agregar_evento_deportivo()* solicita al usuario ingresar los datos de un evento deportivo en vivo, como el título, el deporte, la fecha, la hora, el lugar y el costo de venta. Luego, agrega un diccionario con esos datos a la lista *menu_productos*.


Cada función de agregar producto imprime un mensaje indicando que el producto ha sido agregado exitosamente.


En general, este código permite al usuario agregar productos a la lista *menu_productos* seleccionando el tipo de producto y proporcionando los detalles específicos de cada tipo de producto.


__5. MOSTRAR:__
Este código implementa un menú interactivo para mostrar el catálogo de productos. El catálogo es proporcionado por el módulo *menu* (que no se muestra en el código proporcionado, pero contiene una lista llamada *menu_productos* con los productos).
El código define varias funciones para mostrar diferentes categorías de productos:


La función *mostrar_menu()* muestra el menú de opciones y solicita al usuario que seleccione una opción. Dependiendo de la opción elegida, se invoca la función correspondiente para mostrar la categoría de productos correspondiente. Si se selecciona la opción *"5. Todo"*, se muestra el catálogo completo llamando a la función *mostrar_todo()*. Si se selecciona la opción *"6. Regresar"*, se sale de la función y regresa al punto desde donde se llamó.


Las funciones *mostrar_peliculas()*, *mostrar_series()*, *mostrar_documentales()* y *mostrar_eventos_deportivos()* recorren la lista de productos en *menu.menu_productos* y recopilan los productos que pertenecen a la categoría correspondiente. Luego, imprime los detalles de cada producto utilizando la función *print_producto()*.


La función *mostrar_todo()* simplemente recorre la lista *menu.menu_productos* y muestra los detalles de cada producto utilizando la función *print_producto()*.


La función *print_producto(producto)* imprime los detalles de un producto específico. Muestra el tipo de producto, el título y otros detalles relevantes dependiendo del tipo de producto. Por ejemplo, para películas y series, se muestra el actor principal y el director. Para series, también se muestra el número de temporadas. Para documentales, se muestra el tema. Para eventos deportivos en vivo, se muestra el deporte, la fecha, la hora y el lugar. Además, se muestra el costo de renta y el costo de venta de cada producto.


En resumen, este código permite al usuario seleccionar diferentes categorías de productos para mostrar en el catálogo, incluyendo la opción de mostrar todo el catálogo completo. Cada categoría se muestra con sus respectivos detalles y se indica si no hay productos en esta categoría.



 
# DIAGRAMA DE ESTRUCTURA
Este diagrama representa las principales funciones y estructuras de datos utilizadas en el código. Estas funciones son clave para el funcionamiento del programa y gestionan las diferentes acciones que se pueden realizar en el catálogo de productos. A continuación, se describen brevemente estas funciones:


La función *"cargar_catalogo"* se encarga de cargar los datos del catálogo desde un archivo. Abre el archivo utilizando la función "open" y luego lee cada línea, procesando los datos y añadiéndolos al catálogo.


La función *"agregar_producto"* permite al usuario agregar un nuevo producto al catálogo. Dependiendo de la opción seleccionada, solicita la información específica del tipo de producto y la añade al catálogo.


La función *"buscar_producto"* permite al usuario buscar productos en el catálogo utilizando una palabra clave en el título. Recorre el catálogo y compara el título de cada producto con la palabra clave.


La función *"eliminar_producto"* permite al usuario eliminar un producto del catálogo. Muestra una lista numerada de productos y solicita al usuario que seleccione un número. Luego, elimina el producto correspondiente del catálogo.


La función *"mostrar_catalogo"* muestra diferentes opciones de visualización del catálogo, como mostrar películas, series, documentales, eventos deportivos o todo el catálogo completo. Recorre el catálogo y muestra los detalles de cada producto según la opción seleccionada.


Las funciones *"cargar_catalogo"* y *"guardar_catalogo"* se encargan de cargar y guardar el catálogo en un archivo, respectivamente. Utilizan la función *"open"* para abrir o crear el archivo y escriben los datos del catálogo en el formato adecuado.


La función *"menu_principal"* es el punto de entrada del programa y muestra el menú principal al usuario. Permite seleccionar una opción y ejecutar la función correspondiente para realizar la acción deseada.


Estas funciones y estructuras de datos trabajan en conjunto para brindar la funcionalidad completa del programa y gestionar eficientemente el catálogo de productos.


*Salida:* Finaliza el programa y muestra un mensaje de despedida.


Cada función realiza las operaciones correspondientes y luego vuelve a menu_principal() para que el usuario pueda seleccionar otra opción o salir del programa.

![diagrama_completo](https://github.com/agn-pe-23i/proyecto-abdi/assets/125592302/06288ef5-3eb6-42d2-b6db-f5e1746ce369)


Después de que el programa a sido separado por los módulos *main, buscar eliminar, file, menu y mostrar*, el diagrama se aprecia de la siguiente manera: 
![diagrama_modulos](https://github.com/agn-pe-23i/proyecto-abdi/assets/125592302/50439f8e-bc14-441f-803b-8e3f48c264c2)


# COMENTARIO
Durante el desarrollo del proyecto final, nos enfrentamos a diversas dificultades. Inicialmente, al escribir los códigos, a pesar de estos desafíos, perseveramos y mejoramos nuestro código.


Decidimos estructurar el proyecto en diferentes módulos. El principal, que contiene todos los módulos, se encarga de gestionar el catálogo. Los módulos se dividen en agregar producto, buscar producto, eliminar producto y archivo para cargar y guardar el catálogo en un archivo.


El módulo "menu" nos permite seleccionar la opción de incluir películas, series, documentales o eventos deportivos que no estén en el catálogo. El módulo "buscar_elimiar" se divide en dos, la parte “buscar” nos permite encontrar elementos existentes en el catálogo mediante una palabra clave. La segunda parte "eliminar" se encarga de eliminar productos del catálogo. El módulo "file" nos ayuda con la carga y el guardado del catálogo en un archivo.


Además, el programa principal presenta un menú que nos permite agregar nuevos productos. El módulo, llamado "mostrar", se encarga de mostrar el catálogo.  Durante la integración de estos módulos en el programa principal, enfrentamos algunas adversidades, ya que en ocasiones no se reconocían correctamente y no obteníamos los resultados esperados. Sin embargo, finalmente logramos cumplir con nuestro objetivo.



# IMPLEMENTACIÓN
Dentro de este código se hizo uso de las siguientes funciones para que el código pudiera funcionar: 


La función *def* en Python: La función *def* se utiliza para definir una función en Python. Una función es un bloque de líneas de código o un conjunto de instrucciones que realiza una tarea específica y puede ser reutilizada para repetir esa tarea. Al definir una función, se le da un nombre y se pueden especificar parámetros que se utilizan para recibir valores de entrada. Las funciones ayudan a que el código sea más legible y comprensible, y permiten crear soluciones más modulares.


La cláusula *with*: La cláusula *with* se utiliza para establecer un contexto local en un bloque de código. Permite definir un conjunto de acciones a realizar antes y después de la ejecución del bloque de código. Esta cláusula es comúnmente utilizada para trabajar con recursos que deben ser cerrados o liberados de manera adecuada, como archivos o conexiones a bases de datos. Al utilizar la cláusula *with*, nos aseguramos de que los recursos se manejen de manera correcta y se liberen automáticamente al finalizar el bloque de código.


El bucle *for*: El bucle *for* se utiliza para recorrer los elementos de un objeto iterable, como una lista, tupla, conjunto o diccionario, y ejecutar un bloque de código para cada elemento. En cada iteración, el bucle *for* toma un único elemento del objeto iterable y se pueden realizar diversas operaciones con él. Este tipo de bucle es útil cuando se necesita realizar una acción para cada elemento de una colección de datos.


*for-in*: A veces, el elemento actual del iterable que se está recorriendo puede ser irrelevante. En estos casos, se puede utilizar la variable *in* para indicar esta situación. Al utilizar *for item in iterable*, el bucle *for* ejecutará el bloque de código para cada elemento del iterable, pero no utilizará explícitamente el valor de *item* en el bloque. Esta construcción es útil cuando solo se necesita iterar una determinada cantidad de veces y no se requiere el valor del elemento en sí.


*elif*: La palabra clave *elif* en Python (abreviatura de "else if") se utiliza para evaluar múltiples condiciones en una escalera lógica condicional. En una estructura *if-elif-else*, cada bloque *elif* representa una condición adicional que se verifica si las condiciones anteriores no se cumplen. Solo se ejecutará el bloque *elif* cuya expresión booleana correspondiente se evalúe como verdadera. Esto permite crear una serie de comprobaciones condicionales y ejecutar el bloque de código correspondiente al primer caso que sea verdadero.


El bloque *try-except-else-finally*: El bloque *try* se utiliza para probar un bloque de código en busca de errores. Dentro del bloque *try*, se coloca el código que se desea ejecutar y que podría generar una excepción. Si se produce una excepción dentro del bloque *try*, se captura y se maneja en el bloque *except*, donde se pueden tomar acciones específicas para lidiar con el error. El bloque *else* se ejecuta cuando no se produce ninguna excepción dentro del bloque *try*. El bloque *finally* se ejecuta siempre, independientemente de si se produjo una excepción o no. Se utiliza para ejecutar código de limpieza o acciones finales, como cerrar archivos o liberar recursos, asegurándose de que se realicen incluso en caso de error.


La instrucción *return*: La instrucción *return* se utiliza para finalizar la ejecución de una función y "devolver" un resultado al llamador de la función. Al utilizar *return*, se puede especificar un valor o una expresión que se desea devolver como resultado de la función. Después de la instrucción *return*, no se ejecutarán más líneas de código dentro de la función. Si no se proporciona ninguna expresión después de *return*, se devuelve el valor especial *None*. La instrucción *return* es comúnmente utilizada para obtener resultados de una función y permitir que se realicen acciones basadas en esos resultados en el código que llamó a la función.

