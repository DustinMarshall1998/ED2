from cryptography.fernet import Fernet

# Generate a key and save it for later use
key = Fernet.generate_key()
with open('encryption_key.key', 'wb') as key_file:
    key_file.write(key)

# Load the key
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Encrypt a file
with open('example.txt', 'rb') as file:
    file_data = file.read()

encrypted_data = cipher.encrypt(file_data)

# Save the encrypted file
with open('example.txt.encrypted', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")
