import os

if not os.path.exists("credenciales.xlsx"):
    print("El archivo credenciales.xlsx no se encuentra en la carpeta.")
    exit()

from openpyxl import load_workbook
# Load the workbook
wb = load_workbook("credenciales.xlsx")
sheet = wb.active

credenciales = {}
# 4. Recorrer las filas del Excel
for row in sheet.iter_rows(min_row=2, values_only=True):
    # row es una tupla que contiene los valores de una fila
    # row[0] es el primer valor de la fila (columna A: usuario)
    # row[1] es el segundo valor (columna B: contraseña)
    usuario = row[0]
    contrasena = row[1]
    credenciales[usuario] = contrasena

while True:

 usercode = input("Write your username").strip()
 if usercode == "exit":#se escribe exit para salir del programa
   print("Exiting the program")
   break
 if usercode == "":
    print("Username can't be empty, please write a valid username")
    continue#se vuelve a pedir el username
 if usercode in credenciales:
    print("Is a valid Username, can procced")
 else:
    print("This is not a valid username")
    continue#se vuelve a pedir el username

 password = input("Write your password").strip()
 if password == "exit":#se escribe exit para salir del programa
   print("Exiting the program")
   break#se sale del bucle y termina el programa
 if password == "":
    print("Password can't be empty, please write a valid password")
    continue#se vuelve a pedir el password
 if password == credenciales[usercode]:
    print("Valid password")
    print("Access granted, welcome")
    print("Program finished, thanks for using it")
    break  #no hay mas nada quee ejecutar, por lo que se sale del bucle
 else:
    print("Invalid password can't proceed")
    continue
 #programa finalizado
