import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive messages
def receive():
    while True:
        try:
            message = client.recv(1024)

            print("\nEncrypted Message:")
            print(message)

            print("Decrypted Message:")
            print(decrypt_message(message))

        except:
            print("Error!")
            client.close()
            break

# Send messages
def write():
    while True:
        msg = input("")
        encrypted = encrypt_message(msg)
        client.send(encrypted)

# Threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()