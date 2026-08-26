Administrador de Tareas v2
Descripcion
Este es un programa de linea de comandos desarrollado en Python que permite gestionar una lista de tareas. Las tareas se guardan automaticamente en un archivo Excel (tareas.xlsx) para que no se pierdan al cerrar el programa.

Funcionalidades
Agregar nuevas tareas.

Ver todas las tareas con su estado (pendiente o completada).

Marcar tareas como completadas.

Guardado automatico en Excel.

Carga automatica de tareas al iniciar el programa.

Manejo de errores para entradas invalidas del usuario.

Tecnologias utilizadas
Python 3

openpyxl (para manejo de archivos Excel)

os (para verificar existencia de archivos)

Como usar
Clona este repositorio.

Asegurate de tener Python 3 instalado.

Instala la libreria openpyxl con: pip install openpyxl

Ejecuta el programa con: python administrador_de_tareas_v2.py

Sigue las instrucciones en pantalla.

Estructura del codigo
cargar_tarea(): Lee las tareas desde el archivo Excel.

guardar_tarea(): Guarda las tareas en el archivo Excel.

mostrar_menu(): Muestra las opciones del programa.

agregar_tareas(): Permite agregar una nueva tarea.

ver_tareas_estados(): Muestra todas las tareas con su estado.

marcar_completado(): Permite marcar una tarea como completada.

Notas del desarrollo
Este proyecto fue desarrollado como parte de un plan de aprendizaje de Python, enfocado en:

Uso de funciones para organizar el codigo.

Manejo de errores y excepciones.

Persistencia de datos con archivos externos.

Refactorizacion y mejora de codigo existente.

Mejoras futuras
Añadir fechas de vencimiento a las tareas.

Permitir eliminar tareas.

Usar JSON en lugar de Excel.

Interfaz grafica simple.

Autor
[1rondel-Danielh.]