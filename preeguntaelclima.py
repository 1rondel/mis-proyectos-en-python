import requests

clima = input("¿Cuál es la ciudad de la que quieres saber el clima? ").lower()

texto = clima.replace(" ", "+")

url = f"https://wttr.in/{texto}?format=3"

respuesta = requests.get(url)

print("Este es el clima de tu ciudad:", respuesta.text)