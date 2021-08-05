import socket
import time

TAMANO_DE_PAQUETE = 32

def codificar(msg):
    if ( len(msg) <= TAMANO_DE_PAQUETE ):
        msg = msg + " " * ( TAMANO_DE_PAQUETE - len(msg) )
        msg = str.encode(msg)
    else:
        print("ERROR: Mensaje muy grande.")
    return msg

UDP_IP = "127.0.0.1"
UDP_PORT = 8082

print("Puerto: %s" % UDP_PORT)

# Especificando UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Mensaje a enviar: ")
    msg = codificar(msg)
    sock.sendto(msg, (UDP_IP, UDP_PORT))
    print("Mensaje enviado: %s" % msg)
