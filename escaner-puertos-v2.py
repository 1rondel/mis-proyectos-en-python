import socket
import threading

puertos_abiertos = []

def escanear_puerto(ip, puerto):
    sock_ob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_ob.settimeout(2)
    resultado = sock_ob.connect_ex((ip, puerto))
    sock_ob.close()
    
    if resultado == 0:
        print(f"puerto {puerto}:  ABIERTO")
        puertos_abiertos.append(puerto)


#---solicitar datos al usuario---#

ip = input("Escriba su ip(ej: localhost o 127.*.*.*):   ")

puertoI = int(input("Ingrese el puerto inicial:   "))
puertoF = int(input("Ingrese el puerto final:   "))

hilos = []

#---bucle para crear un hilo por puerto---#

for puerto in range(puertoI, puertoF + 1):
    hilo = threading.Thread(target=escanear_puerto, args=(ip, puerto))
    hilos.append(hilo)
    hilo.start()
    
#---bucle para esperar a que todos los hilos terminen---#

for hilo in hilos:
    hilo.join()
    
    
#---mostrar resultados---#
print(f"puertos abiertos: {puertos_abiertos}")