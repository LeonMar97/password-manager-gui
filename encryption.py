import hashlib
from cryptography.fernet import Fernet
import json
SALT = b'some_random_salt'
def generate_key(password=None):
    while not password:
        password=input("Enter password\n")
    key=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),SALT,100000)
    return key
def get_key():
    encryption_key = generate_key()
    return Fernet(encryption_key)

def get_data():
    with open (file="passwords/encrypted-passwords.txt",mode='r') as data:
        d=data.read()
        if not d:
            None
        else:
            return d

def set_data(enrypted_data):
    with open(file="passwords/encrypted-passwords.txt",mode='w') as file:
        file.write(enrypted_data)

def encrypt_data(user_name,new_password):
    key=get_key()
    data=decrypt_data()
    data[user_name]=new_password
    data_to_encrypt = data.encode("utf-8")  
    encrypted_data = key.encrypt(data_to_encrypt)
    set_data(encrypted_data)

def decrypt_data():
    data=get_data()
    key=get_key()
    if not data:
        data='{}'
    else:
        data=key.decrypt(data).decode("utf-8")
    return data
    


