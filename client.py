import socket, sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 8080))

(clientsocket, address) = clientsocket.accept()
user_text = ("Server started at ", address)
client_socket.send(user_text.encode())
answer = client_socket.recv(1024)
client_socket.close()
