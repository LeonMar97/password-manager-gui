# import hashlib
from cryptography.fernet import Fernet
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# you can change the salt here for more security, but use the same one each time to retrieve the data
SALT = b"some_random_salt"


def generate_kdf(password):
    """gerate kdf 32byts key matiriall for generatin encryption key later-on from users main password,
    using sha256 algo
    Parameter:
    password= my pass paswords for gui

    Returns:
    key token to insert to fernet later
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=SALT,
        length=32,  # Length of the key (32 bytes for Fernet)
        backend=default_backend(),
    )
    key = kdf.derive(password.encode("utf-8"))
    return key


def get_key(main_pass):
    """genrate Fernet encryption key from user mypass password

    Parameters:
    main_pass= myPass password

    Returns:
    Fernets ecryption key
    """

    encryption_key = generate_kdf(main_pass)
    return Fernet(base64.urlsafe_b64encode(encryption_key))


def get_data():
    """get encrypted data in byts"""
    with open(file="passwords/encrypted-passwords.txt", mode="rb") as data:
        d = data.read()
        if not d:
            return None
        else:
            return d


def set_data(enrypted_data):
    """write encrypted data in bytes

    Parameters:
    encrypted data in bytes"""
    with open(file="passwords/encrypted-passwords.txt", mode="wb") as file:
        file.write(enrypted_data)


def encrypt_data(main_usr, main_pass, website, new_password):
    """encrypt website and new password as json encrypted bytes"""
    key = get_key(main_usr + main_pass)
    decrypted_d = decrypt_data(key=main_usr + main_pass)
    if not decrypted_d:
        return False
    data = json.loads((decrypted_d.replace("'", '"')))

    data[website] = new_password
    data_to_encrypt = str(data).encode("utf-8")
    encrypted_data = key.encrypt(data_to_encrypt)

    try:
        set_data(encrypted_data)
    except:  # noqa: E722
        return False
    return True


def decrypt_data(key):
    """decrypts data

    Parameters:
    key=myPass password (gui's password)

    Returns:
    json in str format
    """
    data = get_data()
    if not data:
        data = "{}"
    else:
        try:
            data = get_key(key).decrypt(data).decode("utf-8")
        except:  # noqa: E722
            return None

    return data
