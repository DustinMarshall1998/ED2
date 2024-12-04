from cryptography.fernet import Fernet

# Load the key
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Decrypt the file
with open('example.txt.encrypted', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted file
with open('example.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")
