"""
name: script_with_options.py
description: A script for encripting and decripting data
author: hdaojin
version: 1.0.0
creation date: 2022-10-27
last modified: 2022-10-27
usage: python3 script_with_options.py 
"""

"""
Python modules for encripting and decripting:
- base64                  # For simple encription.
- hashlib                 # For single-way encription.
- hmac                    # For single-way encription with a key.
- cryptography.fernet     # For AES symmetric encription.
- cryptography.hazmat     # For RSA asymmetric encription.
- rsa                     # For RSA asymmetric encription.
- secrets                 # For generating cryptographically strong random numbers.
"""

from cryptography.fernet import Fernet
import rsa

def fernet_encrypt():
    """Encrypt data with fernet."""
    # Generate a key.
    key = Fernet.generate_key()

    # Encrypt data with a key.
    f = Fernet(key)
    encrypted_data = f.encrypt(message.encode())
    print(encrypted_data)

    # Decrypt data with a key.
    decrypted_data = f.decrypt(encrypted_data)
    print(decrypted_data.decode())

def rsa_encrypt():
    """Encrypt data with rsa."""
    # Generate a public and private key.
    public_key, private_key = rsa.newkeys(2048, poolsize=8)

    # Encrypt data with a public key.
    data = message.encode('utf-8')
    encrypted_data = rsa.encrypt(data, public_key)
    print(encrypted_data)

    # Decrypt data with a private key.
    decrypted_data = rsa.decrypt(encrypted_data, private_key)
    print(decrypted_data.decode('utf8'))


if __name__ == "__main__":
    message = "Hello World!"
    fernet_encrypt()
    print("--------------------")
    rsa_encrypt()