#!/usr/bin/env python2.7

#####################################################
# Socket bajo protocolo UDP
# Jose Fernando Gonzalez S.
# Giancarlo Marin H.
# Laura Rincon R.
#####################################################

#Biblioteca importadas
import socket	#Para configuracion de sockets
import sys		#Para manejo del sistema

## Constantes
HOST = '127.0.0.1'	# localhost
PUERTO = 8888	# Puerto arbitrario 


try:
	# Create the socket bajo protocolo UDP
	Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
	print ('Error al crear socket')
	sys.exit()


#Bandera adicional del estado de conexion
conexion = True
#loop inifito para tener el canal activo
while(conexion) :
	#Recibe desde consola el mensaje del cliente y guarda en mensaje
	mensaje = raw_input('Escriba mensaje a enviar o ENTER para salir:\n')
	
	#Envia el mensaje al servidor por medio de la direccion y puerto
	Socket.sendto(mensaje, (HOST, PUERTO))

	#Si no ingresaron mensaje, se finaliza la comunicacion
	if not mensaje:
	    conexion = False

	# De contrario, se recibe la respuesta del servidor
	else:
	    #repusta del servidor con una tamano maximo de 1024 bytes
	    respuesta, dir = Socket.recvfrom(1024)
	    print ('Respuesta del servidor : ' + respuesta)
	
#Finaliza comunicacion
Socket.close()