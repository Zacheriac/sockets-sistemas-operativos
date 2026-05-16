import socket
import threading
import os

HOST = ''
PORT = 8000
clientes = []

RUTA_BASE = os.path.dirname(os.path.abspath(__file__))

def atender_cliente(cliente, nombre):
    while True:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break

            mensaje_decodificado = mensaje.decode().strip()

            if mensaje_decodificado.upper() == "SALIR":
                print(f"{nombre} salió del servidor.")
                cliente.send("Desconectado del servidor.".encode())
                clientes.remove(cliente)
                cliente.close()
                broadcast(f"{nombre} ha salido del chat.", cliente)
                break

            elif mensaje_decodificado.startswith("GET:"):
                nombre_archivo = mensaje_decodificado[4:].strip()
                ruta_archivo = os.path.join(RUTA_BASE, nombre_archivo)

                if os.path.isfile(ruta_archivo):
                    try:
                        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                            contenido = archivo.read()
                        cliente.send(f"CONTENIDO:{nombre_archivo}\n{contenido}".encode())
                    except Exception as e:
                        cliente.send(f"ERROR 500: No se pudo leer el archivo\n{str(e)}".encode())
                else:
                    cliente.send("ERROR 404: Archivo no encontrado".encode())

            else:
                print(f"{nombre}: {mensaje_decodificado}")
                broadcast(f"{nombre}: {mensaje_decodificado}", cliente)

        except (ConnectionResetError, ConnectionAbortedError):
            print(f"{nombre} se ha desconectado.")
            if cliente in clientes:
                clientes.remove(cliente)
            cliente.close()
            break

def broadcast(mensaje, emisor):
    for cliente in clientes:
        if cliente != emisor:
            try:
                cliente.send(mensaje.encode())
            except:
                clientes.remove(cliente)
                cliente.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("El servidor está esperando conexiones ...")

while True:
    try:
        cliente, direccion = servidor.accept()
        print(f"Un cliente se conectó desde la IP {direccion}")

        nombre = cliente.recv(1024).decode().strip() or "Desconocido"

        clientes.append(cliente)
        broadcast(f"{nombre} se acaba de unir al servidor.", cliente)
        cliente.send("¡Bienvenido al servidor del grupo 15! Usa el menú para interactuar.".encode())

        hilo_cliente = threading.Thread(target=atender_cliente, args=(cliente, nombre))
        hilo_cliente.start()
    except Exception as e:
        print(f"Error en el servidor: {str(e)}")
