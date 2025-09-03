from Crypto.Cipher import AES
import os

def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_name, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(file_name + ".enc", 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)

if __name__ == "__main__":
    key = os.urandom(16)  # AES key
    file_name = input("Enter the file name to encrypt: ")
    encrypt_file(file_name, key)
    print(f"File encrypted and saved as {file_name}.enc")
