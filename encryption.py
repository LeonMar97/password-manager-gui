import hashlib
from cryptography.fernet import Fernet
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
#you can change the salt here for more security, but use the same one each time to retrieve the data
SALT = b'some_random_salt'
def generate_key(password):
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    iterations=100000,
    salt=SALT,
    length=32,  # Length of the key (32 bytes for Fernet)
    backend=default_backend()
)
    key = kdf.derive(password.encode('utf-8'))
    return key
def get_key(main_pass):
    encryption_key = generate_key(main_pass)
    return Fernet(base64.urlsafe_b64encode(encryption_key))

def get_data():
    with open (file="passwords/encrypted-passwords.txt",mode='rb') as data:
        d=data.read()
        if not d:
            None
        else:
            return d

def set_data(enrypted_data):
    with open(file="passwords/encrypted-passwords.txt",mode='wb') as file:
        file.write(enrypted_data)

def encrypt_data(main_pass,website,new_password):
    key=get_key(main_pass)
    data=json.loads((decrypt_data(key=main_pass).replace("'","\"")))
    data[website]=new_password
    data_to_encrypt = str(data).encode("utf-8")  
    encrypted_data = key.encrypt(data_to_encrypt)
    try:
        set_data(encrypted_data)
    except:
        return False
    return True

def decrypt_data(key):
    data=get_data()
    if not data:
        data='{}'
    else:
        try:
            data=get_key(key).decrypt(data).decode("utf-8")
        except:
            return None
    return data
    


