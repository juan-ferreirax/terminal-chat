import socket
import sys

SERVER_ADDRESS = input("Informe o endereço IP do receptor: ")
SERVER_PORT = int(input("Informe a porta definida pelo receptor: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
print(f"""Conexão estabelecida com sucesso!
Endereço do receptor: {SERVER_ADDRESS}
Porta: {SERVER_PORT}""")

try:
    while True:
        message = input("Mensagem: ")
        if message.strip().lower() == "q":
            break
        elif message:
            client_socket.sendall(message.encode("utf-8"))
            sys.stdout.write(f"\033[F\033[K{message} ✅️\n")
            sys.stdout.flush()
except socket.timeout:
    print("Erro de timeout")
except Exception as e:
    print(e)
finally:
    client_socket.close()
    print("A conexão foi encerrada com o receptor!")