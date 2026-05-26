from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

# Create cipher object
cipher = Fernet(key)

# Encrypt function
def encrypt_message(message):
    return cipher.encrypt(message.encode())

# Decrypt function
def decrypt_message(message):
    return cipher.decrypt(message).decode()