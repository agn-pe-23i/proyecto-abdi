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


Para mantener la organización del proyecto, se creará una carpeta principal que contendrá los archivos principales del catálogo de streaming. Además, se crearán subcarpetas específicas para almacenar los registros de películas, series, documentales y eventos deportivos, lo que facilitará la gestión y navegación dentro del proyecto.


En resumen, el proyecto final de la UEA de *Programación Estructurada* consiste en desarrollar un catálogo de streaming utilizando el enfoque de *diseño top-down* y la herramienta *PyCharm*. Se aplicarán los conocimientos adquiridos durante el curso para implementar las estructuras de control, tipos de datos, funciones, módulos, registros y archivos necesarios. El objetivo es crear un catálogo funcional que cumpla con las condiciones específicas establecidas.



# ANTECEDENTES
Un servicio de streaming busca actualizar su sistema de renta y venta de películas, series, documentales y eventos deportivos en vivo. El objetivo es tener un catálogo completo y actualizado de los productos disponibles para su transmisión. Para lograrlo, se necesita desarrollar un sistema que permita interactuar de manera eficiente con dicho catálogo.


El sistema deberá contar con una interfaz de usuario intuitiva y amigable que permita la manipulación correcta y completa del catálogo de productos. Para lograr esto, se implementará una serie de menús que facilitarán la navegación y manipulación de la información.
En primer lugar, el sistema proporcionará un menú principal que presentará las opciones disponibles, como *"Buscar", "Agregar", "Editar" y "Eliminar"*. Estas opciones permitirán al usuario realizar diferentes acciones sobre el catálogo de productos.


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

                             +------------------+
                             |  cargar_catalog| 
                             +------------------+
                                       |
                                      V
                                   +--try--+
                                    |        |
                                   V        |
                             +-----------+  |
                             |                |  |
                             |  catalog  |  |
                             |                |  |
                             +-----+-----+  |
                                    |         |
                                   V        |
                             +-----+-----+  |
                             |                |  |
                             |   input     |  |
                             |                |  |
                             +-----+-----+  |
                                   |          |
                                   V        |
                             +-----+-----+  |
                             |                |  |
                             |   open     |  |
                             |                |  |
                             +-----+-----+  |
                                   |          |
                                   V         |
                    +------------+--------+------+
                    |             |               |
                    V             V               V
               +----+----+  +-----+-----+  +------+------+
               | Película |  |   Serie   |  | Documental |   ... (diferentes tipos)
               +----+----+  +-----+-----+  +------+------+
                    |             |               |
                    V             V               V
             +------+-----+  +------+------+ +------+-----+
             |  tipo          |  | título          |  | ...          |   ... (atributos específicos)
             |  título        |  | actor_prin  |  |              |
             |  actor_…  |  | director      |  |              |
             |  ...             |  | ...               |  |              |
             +-----------+  +-------------+  +--------------+



En el siguiente diagrama también se muestra los diferentes módulos:

+-------------------+
|  menu_principal() |
+-------------------+
        |
        |   +------------------+
        +-->| agregar_producto()|
        |   +------------------+
        |
        |   +-----------------+
        +-->| buscar_producto()|
        |   +-----------------+
        |
        |   +------------------+
        +-->| eliminar_producto()|
        |   +------------------+
        |
        |   +-----------------+
        +-->| mostrar_catalogo()|
        |   +-----------------+
        |
        |   +----------------+
        +-->| cargar_catalogo()|
        |   +----------------+
        |
        |   +----------------+
        +-->| guardar_catalogo()|
        |   +----------------+
        |
        |
        +---[Salida]


        Para que el diagrama se vea de forma completa, favor de abrir como si se fuera a editar.
        
El diagrama muestra la función menu_principal() como el punto de entrada y la función principal que controla el flujo del programa. Desde menu_principal(), se puede acceder a varias opciones, cada una de las cuales corresponde a una función específica que realiza una operación particular.
Las opciones disponibles son:


*agregar_producto():* Permite al usuario agregar un nuevo producto al catálogo.


*buscar_producto():* Permite al usuario buscar un producto en el catálogo según palabras clave.



*eliminar_producto():* Permite al usuario eliminar un producto específico del catálogo.


*mostrar_catalogo():* Muestra al usuario diferentes opciones para ver el catálogo, incluyendo películas, series, documentales, eventos deportivos y el catálogo completo.


*cargar_catalogo():* Permite al usuario cargar un catálogo existente desde un archivo.


*guardar_catalogo():* Permite al usuario guardar el catálogo actual en un archivo.


*Salida:* Finaliza el programa y muestra un mensaje de despedida.


Cada función realiza las operaciones correspondientes y luego vuelve a menu_principal() para que el usuario pueda seleccionar otra opción o salir del programa.

![diagrama_1](https://github.com/agn-pe-23i/proyecto-abdi/assets/125592302/061692a6-07de-4f03-b343-6e1e745b8acb)

# COMENTARIO
Durante el desarrollo del proyecto final, encontramos que el primer código, considerado como el código principal, resultó relativamente sencillo. En esta sección, se presentan opciones como buscar, eliminar, mostrar, cargar y guardar productos en el catálogo. Al ejecutar este código, los usuarios tenían la oportunidad de interactuar con el catálogo de productos.


Sin embargo, enfrentamos mayores dificultades al trabajar en el segundo código, el cual no se reflejaba directamente en el primero. Esta etapa se convirtió en nuestro mayor desafío, ya que no sabíamos cómo abordar su implementación.


Inicialmente, teníamos poca claridad sobre cómo desarrollar el segundo catálogo. Nos surgieron preguntas sobre la cantidad de ejemplos de cada producto a incluir y cómo traducirlos adecuadamente al código.


Para superar estos obstáculos, realizamos una exhaustiva investigación y recopilamos información adicional. A medida que adquirimos más conocimientos, pudimos determinar la estructura del segundo catálogo y encontrar la forma adecuada de representarlo en código.


Aunque enfrentamos dificultades iniciales y tuvimos dudas sobre cómo abordar ciertos aspectos del proyecto, logramos superar los obstáculos y encontrar soluciones adecuadas gracias a nuestra perseverancia y dedicación. A medida que avanzamos en nuestro aprendizaje, adquirimos confianza y nos sentimos más cómodas al implementar el segundo código.


# IMPLEMENTACIÓN
Dentro de este código se hizo uso de las siguientes funciones para que el código pudiera funcionar: 


La función *def* en Python: La función *def* se utiliza para definir una función en Python. Una función es un bloque de líneas de código o un conjunto de instrucciones que realiza una tarea específica y puede ser reutilizada para repetir esa tarea. Al definir una función, se le da un nombre y se pueden especificar parámetros que se utilizan para recibir valores de entrada. Las funciones ayudan a que el código sea más legible y comprensible, y permiten crear soluciones más modulares.


La cláusula *with*: La cláusula *with* se utiliza para establecer un contexto local en un bloque de código. Permite definir un conjunto de acciones a realizar antes y después de la ejecución del bloque de código. Esta cláusula es comúnmente utilizada para trabajar con recursos que deben ser cerrados o liberados de manera adecuada, como archivos o conexiones a bases de datos. Al utilizar la cláusula *with*, nos aseguramos de que los recursos se manejen de manera correcta y se liberen automáticamente al finalizar el bloque de código.


El bucle *for*: El bucle *for* se utiliza para recorrer los elementos de un objeto iterable, como una lista, tupla, conjunto o diccionario, y ejecutar un bloque de código para cada elemento. En cada iteración, el bucle *for* toma un único elemento del objeto iterable y se pueden realizar diversas operaciones con él. Este tipo de bucle es útil cuando se necesita realizar una acción para cada elemento de una colección de datos.


*for-in*: A veces, el elemento actual del iterable que se está recorriendo puede ser irrelevante. En estos casos, se puede utilizar la variable *in* para indicar esta situación. Al utilizar *for item in iterable*, el bucle *for* ejecutará el bloque de código para cada elemento del iterable, pero no utilizará explícitamente el valor de *item* en el bloque. Esta construcción es útil cuando solo se necesita iterar una determinada cantidad de veces y no se requiere el valor del elemento en sí.


*elif*: La palabra clave *elif* en Python (abreviatura de "else if") se utiliza para evaluar múltiples condiciones en una escalera lógica condicional. En una estructura *if-elif-else*, cada bloque *elif* representa una condición adicional que se verifica si las condiciones anteriores no se cumplen. Solo se ejecutará el bloque *elif* cuya expresión booleana correspondiente se evalúe como verdadera. Esto permite crear una serie de comprobaciones condicionales y ejecutar el bloque de código correspondiente al primer caso que sea verdadero.


El bloque *try-except-else-finally*: El bloque *try* se utiliza para probar un bloque de código en busca de errores. Dentro del bloque *try*, se coloca el código que se desea ejecutar y que podría generar una excepción. Si se produce una excepción dentro del bloque *try*, se captura y se maneja en el bloque *except*, donde se pueden tomar acciones específicas para lidiar con el error. El bloque *else* se ejecuta cuando no se produce ninguna excepción dentro del bloque *try*. El bloque *finally* se ejecuta siempre, independientemente de si se produjo una excepción o no. Se utiliza para ejecutar código de limpieza o acciones finales, como cerrar archivos o liberar recursos, asegurándose de que se realicen incluso en caso de error.


La instrucción *return*: La instrucción *return* se utiliza para finalizar la ejecución de una función y "devolver" un resultado al llamador de la función. Al utilizar *return*, se puede especificar un valor o una expresión que se desea devolver como resultado de la función. Después de la instrucción *return*, no se ejecutarán más líneas de código dentro de la función. Si no se proporciona ninguna expresión después de *return*, se devuelve el valor especial *None*. La instrucción *return* es comúnmente utilizada para obtener resultados de una función y permitir que se realicen acciones basadas en esos resultados en el código que llamó a la función.
