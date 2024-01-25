import socket
import threading

# Función para enviar mensajes a través del socket
def send_msg(sock, msg, addr):
    # Codifica el mensaje y lo envía a la dirección especificada
    sock.sendto(msg.encode('utf-8'), addr)

# Función para recibir mensajes en el socket
def recv_msg(sock):
    while True:
        # Recibe un mensaje y la dirección del remitente
        data, addr = sock.recvfrom(1024)
        # Imprime el mensaje recibido
        print(f"Received message: {data.decode('utf-8')}")

# Función para crear un socket y enlazarlo a una dirección IP y un número de puerto
def create_socket(ip, port):
    # Crea un objeto de socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Enlaza el socket a la dirección IP y el puerto especificados
    sock.bind((ip, port))
    return sock

def main():
    # Solicita al usuario que ingrese la dirección IP y el puerto local, así como la dirección IP y el puerto remotos
    local_ip = input("Enter your IP: ")
    local_port = int(input("Enter your port: "))
    remote_ip = input("Enter your friend's IP: ")
    remote_port = int(input("Enter your friend's port: "))

    # Crea el socket y lo enlaza a la dirección IP y el puerto local especificados
    sock = create_socket(local_ip, local_port)

    # Crea un hilo para recibir mensajes entrantes en el socket
    recv_thread = threading.Thread(target=recv_msg, args=(sock,))
    recv_thread.start()

    while True:
        # Solicita al usuario que ingrese un mensaje
        msg = input("Enter message: ")

        # Envía el mensaje a través del socket a la dirección IP y el puerto remotos especificados
        send_msg(sock, msg, (remote_ip, remote_port))

if __name__ == "__main__":
    main()

