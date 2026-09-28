import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost", 5000))

server.listen()

cliente_socket, direccion = server.accept()

while True:
    data = cliente_socket.recv(1024)
    mensaje = data.decode()
    print("Cliente: ",mensaje)
    
    if mensaje.lower() == "salir":
        print("El cliente se ha desconectado")
        break
    
    respuesta = input("Tu:  ")
    cliente_socket.send(respuesta.encode())
    