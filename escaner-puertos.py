import socket

ip =  input("Escriba su IP aqui porfavor(puede ser localhost o 127.*.*.*)")

print("se le va a pedir un rango de puertos")

puerto_inicial = int(input('ingrese el numero del puerto con el que quiere iniciar'))

puerto_final = int(input("ingrese el puerto con el que va a finalizar"))

print(f"Escaneando {ip}.....")

abiertos = 0

for puerto in range(puerto_inicial, puerto_final + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, puerto))
    s.close()
    
    if resultado == 0:
        print(f"Puerto{puerto}: Abierto")
        
        abiertos += 1
        
if abiertos == 0:
    print("no se encontraron puertos abiertos")

else:
    print(f"Se encontraron {abiertos} puertos abiertos")