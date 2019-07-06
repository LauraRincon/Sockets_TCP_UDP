import socket
import sys

# Crea el socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el puerto al servidor
server_address = ('localhost', 42500)
print >>sys.stderr, 'Iniciando el puerto %s en la direccion %s' % server_address
sock.bind(server_address)

# Escucha las conexiones que entran
sock.listen(1)

while True:
    # Espera una conexion
    print >>sys.stderr, 'Esperando conexion'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'Conexion desde ', client_address

        # Recibe los datos
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'Recibido "%s"' % data
            if data:
                print >>sys.stderr, 'Devolviendo al cliente '
                connection.sendall(data.upper())
            else:
                print >>sys.stderr, 'No hay mas datos desde ', client_address
                break
            break
    finally:
        # Termina la conexion
        connection.close()
