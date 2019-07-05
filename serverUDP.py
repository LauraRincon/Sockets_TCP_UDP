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


try :
	# Create the socket bajo protocolo UDP
	Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print('Socket creado')
	# Asocia el socket a la direccion IP y puerto dado
	Socket.bind((HOST, PUERTO))
except:
	#Mensaje de fallo en caso de error
	print('Error al crear y asociar socket')
	sys.exit()

#Bandera adicional del estado de conexion
conexion = True
#loop inifito para tener el canal activo
while conexion:
	# Recibe datos proveniente del cliente (dato + dir)
	dato, dir = Socket.recvfrom(1024)
	# Datagrama de tamano maximo de 1024 bytes que se puede recibir
	
	# Si no se recibe un mensaje, se finaliza la conexion
	if not dato: 
		conexion = False
		
	# De contrario, se procesa para convertirlo en mayusculas
	else:
		#Mensaje para identificar procedencia del dato
		print ('Mensaje[' + dir[0] + ':' + str(dir[1]) + '] - ' + dato.strip())
		#Convierte el dato en mayusculo
		respuesta= dato.upper()
		#Envia la respuesta del servidor a direccion recibida
		Socket.sendto(respuesta , dir)
	
#Finaliza comunicacion
print('Comunicacion finalizada')
Socket.close()



