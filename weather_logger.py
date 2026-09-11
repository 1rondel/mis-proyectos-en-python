import requests
import json
from datetime import datetime
import os

def obtener_clima(ciudad):
   try: 
    ciudad = ciudad.replace(" ", "+")
    url = f"https://wttr.in/{ciudad}?format=3"
    
    respuesta = requests.get(url)
    
    return respuesta.text

   except requests.exceptions.RequestException as e:
        print("Error al obtener el clima:", e)



def guardar_consulta(ciudad, clima):
    if os.path.exists("consultasdelclima.json"):
        with open("consultasdelclima.json", "r") as archivo:
            consultas = json.load(archivo)
    else:
        consultas = []
    
    consulta = {
        "ciudad": ciudad,
        "clima": clima,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    consultas.append(consulta)
    
    with open("consultasdelclima.json", "w") as archivo:
        json.dump(consultas, archivo, indent=4)

def ver_historial():
    if not os.path.exists("consultasdelclima.json"):
        print("No hay historial de consultas.")
        return
    else:
     with open("consultasdelclima.json", "r") as archivo:
        consultas = json.load(archivo)
        return consultas

while True:
    print("1. Consultar clima")
    print("2. Ver historial de consultas")
    print("3. Salir")
    try:
     opcion = int(input("seleccione una opcion:"))
    except ValueError:
     print("Por favor, ingrese un número válido.")
     continue
    if opcion == 1:
         ciudad = input("ingrese el nombre de la ciudad").lower()
         clima = obtener_clima(ciudad)
         print(f"El clima en {ciudad} es: {clima}")
         if clima:
          guardar_consulta(ciudad, clima)
         else:
          print("No se pudo obtener el clima para la ciudad ingresada.")
    elif opcion == 2:
        historial = ver_historial()
        if historial:
            for consulta in historial:
                print(f"{consulta['fecha']}: {consulta['ciudad']} - {consulta['clima']}")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida 1 2 3.")