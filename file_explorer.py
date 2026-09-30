import os

carpeta_actual = os.getcwd()
print("Carpeta actual:  ", carpeta_actual)

ruta = input("Escriba una ruta de su computadora:  ")

if  os.path.exists(ruta):
    print("Ruta encontrada")
    print("Archivos de la ruta:  ", os.listdir(ruta))
else:
    print("ERROR")
    print("La ruta no fue encontrada")