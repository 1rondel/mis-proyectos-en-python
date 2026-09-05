import json
import os
def cargar_tarea():
    try:
        with open('tareas.json','r') as archivo:
            datos = json.load(archivo)
            return datos['tareas'], datos['estados']
    except FileNotFoundError:
            
    
        respuesta = input("Archivo inexistente, desea crear uno nuevo, s/n").lower()
        if respuesta == 's':
                print('Creando archivo de guardado...')
                with open('tareas.json', 'w') as archivo:
                    json.dump({'tareas':[],'estados':[]}, archivo, indent = 4)
                    print('Archivo creado exitosamente')
                return [], []
        else:
                print('Continuando sin guardado')
                return [], []
    return [], []

def guardar_tarea(tareas, estados):
 with open('tareas.json', 'w') as archivo:
    json.dump({'tareas':tareas, 'estados':estados}, archivo, indent = 4)
 print('Tareas guardadas exitosamente')



def mostrar_menu():
     print('Menu de opciones')
     print('1. Agregar tareas')
     print('2. Ver tareas con estados')
     print('3. Marcar tarea como completada')
     print('4. Eliminar tarea')
     print('5. Salir del programa')

def agregar_tareas(tareas, estados):
    #debes de crear una funcion para agregar tareas
    descripcion = input('Describa su tarea')
    tareas.append(descripcion)
    estados.append(False)
    guardar_tarea(tareas, estados)
    print("Tarea agregada exitosamente")

def ver_tareas_estados(tareas, estados):
    if not tareas:
        print('No hay tareas')
        return
    else:
     for i in range(len(tareas)):
      estado = '[X]' if estados[i] else '[ ]'
      print(f'{i+1}. {estado} {tareas[i]}')
      
    # para ver tareas junto con su estado
    
def marcar_completado(tareas, estados):
    #debes de hacer una funcion que marque como completado la tarea seleccionada
    if len(tareas) == 0:
            print('No hay Tareas')
            return
    else:
        for i in range(len(tareas)):
         estado = '[X]' if estados[i] else '[ ]'
         print(f'{i+1}. {estado} {tareas[i]}')
    try:
     numero = int(input('ingresa el numero de la tarea que haz completado'))
    
     indice = numero - 1
     if 0 <= indice < len(tareas):
               estados[indice] = True
               guardar_tarea(tareas, estados)
               print('Felicidades la tarea fue completada')
     else:
              print('numero invalido')
    except ValueError:
       print('Debes de ingresar un numero valido')

def eliminar_tarea(tareas, estados):
    if len(tareas) == 0:
        print('No hay Tareas')
        return
    else:
        for i in range(len(tareas)-1, -1, -1):
            estado = '[x]' if estados[i] else '[ ]'
            print(f'{i+1}. {estado} {tareas[i]}')
    try:
        numero = int(input('ingresa el numero de la tarea que deseas eliminar'))
        indice = numero -1
        if 0 <= indice < len(tareas):
            del tareas[indice]
            del estados[indice]
            guardar_tarea(tareas, estados)
            print('Tarea eliminada exitosamente')
    except ValueError:
        print('Debes de ingresar un numero valido')
       

#------administrador-------
tareas, estados = cargar_tarea()
while True:
    try:
     mostrar_menu()
     funcion = int(input('Marque el numero de opcion'))
     if funcion == 1:
        agregar_tareas(tareas, estados)
     elif funcion == 2:
        ver_tareas_estados(tareas, estados)
     elif funcion == 3:
        marcar_completado(tareas, estados)
        eliminar = input('desea eliminar alguna tarea completada? s/n').lower()
        if eliminar == 's':
            eliminar_tarea(tareas, estados)
        else:
            print('Continuando sin eliminar tarea')
     elif funcion == 4:
        eliminar_tarea(tareas, estados)
     elif funcion == 5:
        guardar_tarea(tareas, estados)
        print('Finalizando programa')
        break
     else:
         print('ingrese numero valido entre el 1 y 5') 
    except ValueError:
        print('Ingrese un numero valido')
        continue