from openpyxl import load_workbook, Workbook
import os
def cargar_tareas():
  # Vamos a verificar si el archivo de excel existe
 if os.path.exists('tareas.xlsx'):
  wb = load_workbook('tareas.xlsx')
  hoja = wb.active
  tareas = []
  estados = []
  #Leer filas(empeando desde la fila 1 asumiendo que tiene datos)
  for fila in hoja.iter_rows(values_only=True):
    min_row=2
    descripcion = fila[0]
    estado_texto = fila[1]
  if descripcion is not None: #evitar filas vacias
      tareas.append(descripcion)
      estados.append(estado_texto == 'completado') #convertir a booleano True-False
  return tareas, estados
 else:
   #preguntar si desea crear el archivo de excel
   respuesta = input('El archivo tareas.xlsx no existe. deseas crearlo? (s/n)')
   if respuesta.lower() == "s":
     wb = Workbook()
     hoja = wb.active
     hoja.append(['Descripcion', 'Estado']) #Encabezados
     wb.save('tareas.xlsx')
     print('Archivo creado.')
     return [], []
   else:
     print('continuando sin guardado.')
     return [], []
def guardar_tareas(tareas, estados):
  #esta funcion sirve para guardar las tareas en una hoja de excel
  wb = Workbook()
  hoja = wb.active
  hoja.append(['Descripcion', 'Estado'])
  for tarea, estado in zip(tareas, estados):
    estado_texto = 'Completada' if estado else 'pendiente'
    hoja.append([tarea, estado_texto])
  wb.save('tareas.xlsx')

#-----administrador de tareas -------
tareas, estados = cargar_tareas()

while True:
  print('Opciones')
  print('1. Agregar tarea')
  print('2. Ver tareas')
  print('3. Marcar tarea como completada')
  print('4. Salir')
  try:
    opcion = int(input('Elige una opcion: '))
  except ValueError:
    print('Opcion no valida.')
    continue

  if opcion == 1:
    #Agregar Tareas
    descripcion = input('Agrega descripcion de la tarea: ')
    tareas.append(descripcion)
    estados.append(False)
    guardar_tareas(tareas, estados)
    print('Tarea agregada')
  elif opcion == 2:
    #Ver las tareas
    if not tareas:
      print('no hay tareas')
    else:
      for i in range(len(tareas)):
        estado = '[X]' if estados[i] else '[ ]'
        print(f'{i+1}.{estado} {tareas[i]}') 
  elif opcion == 3:
    #Marcar las tareas como completadas
    if len(tareas) == 0:
      print('No hay tareas')
    else:
      for i in range(len(tareas)):
        estado = '[X]' if estados[i] else '[ ]'
        print(f'{i+1}. {estado} {tareas[i]}')
        numero = input('Que tarea completaste (la numero):')
        try:
          numero = int(numero)
          indice = numero - 1
          if 0 <= indice < len(tareas):
            estados[indice] = True
            guardar_tareas(tareas, estados)
            print('Tarea completada!')
          else:
            print('Numero invalido')
        except ValueError:
          print('Debes ingresar un numero valido.')
  elif opcion == 4:
  #Salir del programa 
   guardar_tareas
  print('saliendo del programa')
  break
#---Siempre se van a guardar las tareas siempre que se modifique la lista y se use la funcion guardar_tareas---