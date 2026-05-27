import socket

IP_ADDRESS = input("Informe o endereço IP do servidor: ")
PORT = int(input("Informe uma porta(1024 a 65535): "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen()
print(f"Servidor ouvindo na porta {PORT}...")

connection, address = server_socket.accept()
print("Conexão estabelecida com sucesso! Aguardando mensagem...")

data = connection.recv(1024).decode("utf-8")
print(data)

server_socket.close()

