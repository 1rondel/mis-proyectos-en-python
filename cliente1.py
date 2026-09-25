import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5000))

message = "Hello server, this is client"

client.send(message.encode())

server_reply = client.recv(1024)
print("Message got from server:", server_reply.decode())

client.close()

