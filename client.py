import socket

SERVER_ADDRESS = input("Informe o endereço IP do receptor: ")
SERVER_PORT = int(input("Informe a porta definida pelo receptor: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
print("Conexão estabelecida com sucesso!")

message = input("Digite a mensagem a ser enviada: ")
client_socket.sendall(message.encode("utf-8"))
client_socket.close()