import socket
import sys

# Crea el socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket al puerto que esta escuchando del servidor
server_address = ('localhost', 42500)
print >>sys.stderr, 'Conectando al puerto %s a la direccion %s' % server_address
sock.connect(server_address)

try:
    
    # Envia los datos recibidos desde la consola del cliente
    message = str(raw_input())
    print >>sys.stderr, 'Enviado "%s"' % message
    sock.sendall(message)

    # Espera la respuesta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'Recibido "%s"' % data

finally:
    print >>sys.stderr, 'Terminando conexion'
    sock.close()