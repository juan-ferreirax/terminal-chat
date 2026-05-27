import socket

SERVER_ADDRESS = input("Informe o endereço IP do receptor: ")
SERVER_PORT = int(input("Informe a porta definida pelo receptor: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
print("Conexão estabelecida com sucesso!")


try:
    while True:
        message = input("Digite a mensagem a ser enviada: ")
        if message == "sair":
            break
        else:
            client_socket.sendall(message.encode("utf-8"))
except TimeoutError:
    print("Erro de timeout")
except Exception as e:
    print(e)
finally:
    client_socket.close()
    print("A conexão foi encerrada com o receptor!")