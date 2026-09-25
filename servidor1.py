import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost", 5000))

server.listen()

print("Servidor escuchando en puerto 5000...")

client_socket, address = server.accept()

data = client_socket.recv(1024)

print("Message got from client:", data.decode())

answer = f"Hello from server!, I received your message: {data.decode()}"

client_socket.send(answer.encode())

client_socket.close()
server.close()