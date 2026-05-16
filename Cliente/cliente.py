import socket
import threading
import queue

cola_mensajes = queue.Queue()

def recibir():
    while True:
        try:
            mensaje = cliente.recv(4096).decode()
            if not mensaje:
                break
            cola_mensajes.put(mensaje)
        except:
            break

def esperar_respuesta():
    try:
        return cola_mensajes.get(timeout=5)
    except queue.Empty:
        return "No hubo respuesta del servidor."

print("¿Cómo deseas conectarte al servidor?")
print("1. Usar localhost")
print("2. Ingresar una IP")

opcion = input("Selecciona una opción (1 o 2): ")
if opcion == '1':
    HOST = 'localhost'
elif opcion == '2':
    HOST = input("Ingresa la IP del servidor: ")
else:
    print("Opción inválida.")
    exit()

PORT = 8000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((HOST, PORT))
except Exception as e:
    print("No se pudo conectar:", e)
    exit()

nombre = input("¿Cuál es tu nombre? ")
cliente.send(nombre.encode())

# Iniciar hilo receptor
hilo = threading.Thread(target=recibir, daemon=True)
hilo.start()

# Esperar mensaje de bienvenida
print(">>", esperar_respuesta())

while True:
    print("\nOpciones:")
    print("1. Solicitar archivos (se mostrará index.txt)")
    print("2. Escribir un mensaje")
    print("3. Salir")
    eleccion = input("Selecciona una opción: ")

    if eleccion == '1':
        cliente.send("GET:index.txt".encode())
        respuesta = esperar_respuesta()
        print(">>", respuesta) 
        
        nombre_archivo = input("\n¿Qué archivo deseas abrir? (Escribe su nombre y extensión): ")
        cliente.send(f"GET:{nombre_archivo}".encode())
        print(">>", esperar_respuesta())
        
    elif eleccion == '2':
        mensaje = input("Escribe tu mensaje: ")
        cliente.send(mensaje.encode())
    elif eleccion == '3':
        cliente.send("SALIR".encode())
        print("Saliendo del servidor...")
        cliente.close()
        break
    else:
        print("Opción inválida.")
