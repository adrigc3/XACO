import socket
import threading

# Función que recibe mensajes del socket y los imprime en la consola
def recibir_mensajes(sock):
    while True:
        data = sock.recv(1024)
        if not data:  # Si no hay datos recibidos, se sale del bucle
            break
        print(data.decode('utf-8'))  # Imprime los datos decodificados en la consola

# Función que envía mensajes ingresados por el usuario a través del socket
def enviar_mensajes(sock):
    while True:
        mensaje = input("Enter message: ")
        sock.sendall(mensaje.encode('utf-8'))  # Codifica el mensaje y lo envía a través del socket

# Función principal que determina si el usuario desea ejecutar como host o cliente
def iniciar_chat():
    modo = input('¿Deseas ejecutar como host (h) o como cliente (c)? ')
    if modo == 'h':
        iniciar_chat_como_host()
    else:
        iniciar_chat_como_cliente()

# Función que inicializa el chat como host (servidor)
def iniciar_chat_como_host():
    host = input('Ingresa la dirección IP del host: ')
    port = int(input('Ingresa el puerto: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket utilizando IPv4 y TCP
    sock.bind((host, port))  # Asigna la dirección IP y el puerto al socket
    sock.listen(1)  # Establece el socket en modo escucha, permitiendo una conexión entrante a la vez
    conn, addr = sock.accept()  # Acepta la conexión entrante

    # Crea dos hilos: uno para recibir mensajes y otro para enviar mensajes a través del socket
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(conn,))
    hilo_recibir.start()

    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(conn,))
    hilo_enviar.start()

# Función que inicializa el chat como cliente
def iniciar_chat_como_cliente():
    host = input('Ingresa la dirección IP del host: ')
    port = int(input('Ingresa el puerto: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket utilizando IPv4 y TCP
    sock.connect((host, port))  # Conecta el socket a la dirección IP y el puerto especificados

    # Crea dos hilos: uno para recibir mensajes y otro para enviar mensajes a través del socket
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(sock,))
    hilo_recibir.start()

    hilo_enviar = threading.Thread(target=enviar_mensajes, args=(sock,))
    hilo_enviar.start()

if __name__ == '__main__':
    iniciar_chat()  # Llama a la función principal para iniciar el chat.

