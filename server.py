import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server started...")

# Send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

# Accept clients
while True:
    client, address = server.accept()
    print(f"Connected with {address}")

    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()