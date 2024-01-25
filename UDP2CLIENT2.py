import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_server_ip():
    # Pedimos la dirección IP al usuario
    ip = input("Introduce la dirección IP del servidor: ")
    return ip

def get_server_port():
    # Pedimos el puerto al usuario
    port = int(input("Introduce el puerto del servidor: "))
    return port

def send_message(message):
    client_socket.sendto(message.encode(), (server_ip, server_port))

def receive_messages():
    while True:
        data, _ = client_socket.recvfrom(1024)
        print(f'Mensaje recibido: {data.decode()}')

if __name__ == '__main__':
    # Obtenemos la dirección IP y el número de puerto del servidor
    server_ip = get_server_ip()
    server_port = get_server_port()

    # Imprimimos un mensaje en la consola indicando que nos estamos conectando al servidor
    print(f'Conectando al servidor en {server_ip}:{server_port}')

    # Creamos un hilo separado para recibir mensajes del servidor mientras escribimos mensajes para enviar
    threading.Thread(target=receive_messages, daemon=True).start()

    # Bucle que se ejecuta continuamente mientras el cliente esté en funcionamiento
    while True:
        # Pedimos al usuario que escriba un mensaje
        message = input('Escribe tu mensaje: ')

        # Enviamos el mensaje al servidor
        send_message(message)

