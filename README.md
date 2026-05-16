#  Proyecto Sockets — Sistemas Operativos | Grupo 15

##  Descripción
Sistema de comunicación Cliente-Servidor implementado con Sockets 
en Python. Permite que múltiples clientes se conecten al servidor 
simultáneamente, intercambien mensajes en tiempo real y soliciten 
archivos remotamente.

##  Funcionalidades
-  **Chat en tiempo real** entre múltiples clientes conectados
-  **Solicitud de archivos** remotos desde el servidor
-  **Exploración de archivos** mediante index.txt
-  **Multicliente** — maneja varias conexiones simultáneas con hilos
-  **Conexión flexible** — por localhost o IP personalizada

##  Estructura del proyecto
sockets-sistemas-operativos/
├── Servidor/
│   ├── servidor.py      ← lógica del servidor
│   ├── index.txt        ← lista de archivos disponibles
│   ├── datos1.txt
│   ├── datos2.txt
│   ├── datos3.txt
│   └── datos4.txt
└── Cliente/
└── cliente.py       ← interfaz del cliente

##  Cómo ejecutar

###  IMPORTANTE: Ejecutar el Servidor ANTES que el Cliente

###  Terminal 1 — Iniciar el Servidor
```bash
cd Servidor
python servidor.py
```
Verás: `El servidor está esperando conexiones ...`

###  Terminal 2 — Conectar el Cliente
```bash
cd Cliente
python cliente.py
```

##  Uso del Cliente
Al conectarte el cliente mostrará un menú:
Opciones:

Solicitar archivos (se mostrará index.txt)
Escribir un mensaje
Salir

- **Opción 1** → muestra el index.txt con los archivos disponibles,
  luego puedes pedir cualquier archivo por nombre
- **Opción 2** → envía un mensaje a todos los clientes conectados
- **Opción 3** → desconecta el cliente del servidor

##  Tecnologías y módulos
| Módulo | Uso |
|--------|-----|
| `socket` | Comunicación TCP Cliente-Servidor |
| `threading` | Manejo de múltiples clientes simultáneos |
| `queue` | Cola de mensajes para sincronización |
| `os` | Manejo de rutas y archivos del servidor |

##  Requisitos
- Python 3.x
- No requiere librerías externas — solo módulos nativos de Python

##  Configuración
- **Puerto:** 8000
- **Protocolo:** TCP (SOCK_STREAM)
- **Codificación:** UTF-8
- **Buffer:** 4096 bytes (cliente) / 1024 bytes (servidor)
