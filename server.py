import socket

IP_ADDRESS = input("Informe o endereço IP do servidor: ")
PORT = int(input("Informe uma porta(1024 a 65535): "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen()
print(f"Servidor ouvindo na porta {PORT}...")

while True:
    connection, address = server_socket.accept()
    client_ip, client_port = address
    print(f"""Conexão estabelecida com sucesso!
Endereço IP do emissor: {client_ip}
Porta do emissor: {client_port}
Aguardando mensagens...\n"""
    )
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            print(data.decode("utf-8"))
    except Exception as e:
        print(e)
    finally:
        connection.close()
        print(f"O emissor com o socket {client_ip}:{client_port} encerrou a conexão!")
        print(f"Aguardando por uma nova conexão na porta {PORT}...\n")

