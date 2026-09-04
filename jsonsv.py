import json
#diccionario de ejemplo
data = {'name': 'Daniel',
        'age': 16,
        'city': 'Santo domingo'}


#Guardar en un archivo json
with open('data.json', 'w') as file:
    json.dump(data, file, indent = 4)  # indent para formatear el JSON con sangría
print("Archivo JSON guardado exitosamente.")


with open('data.json', 'r') as file:
    data_loaded = json.load(file)
print("Datos cargados desde el archivo JSON:",data_loaded)

