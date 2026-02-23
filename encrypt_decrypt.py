from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    encrypted_file = file_path + '.encrypted'
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted)
    print(f"Encrypted file saved as: {encrypted_file}")

def decrypt_file(file_path, key):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)
        decrypted_file = file_path + '.decrypted'
        with open(decrypted_file, 'wb') as f:
            f.write(decrypted)
        print(f"Decrypted file saved as: {decrypted_file}")
    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    file_path = input("Enter file path: ").strip()
    if mode == 'encrypt':
        key = generate_key()
        print("Generated key:", key.decode())
        encrypt_file(file_path, key)
    elif mode == 'decrypt':
        key_str = input("Enter key: ").strip()
        try:
            key = key_str.encode()
            decrypt_file(file_path, key)
        except Exception as e:
            print(f"Invalid key: {e}")
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")