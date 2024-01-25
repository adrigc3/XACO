import socket

# Creamos un objeto socket del tipo AF_INET (IPv4) y SOCK_DGRAM (UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazamos el socket a una dirección IP y un número de puerto específico en el servidor
server_socket.bind(('10.192.226.79', 12345))

# Creamos un conjunto para almacenar las direcciones de los clientes que se conectan al servidor
clients = set()

# Imprimimos un mensaje en la consola indicando que el servidor se ha iniciado
print('Servidor iniciado')

# Bucle que se ejecutará continuamente mientras el servidor esté en funcionamiento
while True:
    # Esperamos recibir datos del socket mediante la función recvfrom
    data, addr = server_socket.recvfrom(1024)

    # Agregamos la dirección del cliente que envió el mensaje al conjunto de clientes
    clients.add(addr)

    # Decodificamos el mensaje a partir de los datos recibidos mediante la función decode y lo almacenamos en la variable "message"
    message = data.decode()

    # Si el mensaje es "GET_IP", enviamos la dirección IP del servidor al cliente que envió el mensaje
    if message == 'GET_IP':
        # Obtenemos la dirección IP del servidor mediante la función gethostbyname
        ip_address = socket.gethostbyname(socket.gethostname())
        # Enviamos la dirección IP al cliente que envió el mensaje mediante la función sendto
        server_socket.sendto(ip_address.encode(), addr)

    # Si el mensaje es "GET_PORT", enviamos el número de puerto en el que está escuchando el socket
    elif message == 'GET_PORT':
        # Obtenemos el número de puerto mediante la función getsockname
        port_number = str(server_socket.getsockname()[1])
        # Enviamos el número de puerto al cliente que envió el mensaje mediante la función sendto
        server_socket.sendto(port_number.encode(), addr)

    # Si el mensaje no es "GET_IP" o "GET_PORT", enviamos el mensaje recibido a todos los clientes en el conjunto de clientes
    else:
        # Imprimimos un mensaje en la consola indicando que se ha recibido un mensaje del cliente con la dirección IP y el número de puerto correspondientes
        print(f'Mensaje recibido de {addr[0]}:{addr[1]}: {message}')

        # Enviamos el mensaje a cada dirección de cliente en el conjunto, excepto al que lo envió originalmente
        for client_addr in clients:
            if client_addr != addr:
                server_socket.sendto(message.encode(), client_addr)

