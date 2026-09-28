import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 5000))

while True:
    print("si quiere desconectarse escriba: salir")
    mensaje = input("Escriba su mensaje:")
    cliente.send(mensaje.encode())
    if mensaje.lower().strip() == "salir":
        print("Se ha desconectado exitosamente")
        cliente.close()
        break
    respuesta = cliente.recv(1024)
    print("Servidor:", respuesta.decode())