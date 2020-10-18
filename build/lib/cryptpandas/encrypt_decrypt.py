import pandas as pd
import io, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptpandas.SALT import SALT

def _get_key(password):
    """Generates secret key associated with provided password."""
    enpassword = password.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=SALT,
                     iterations=100000,
                     backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(enpassword))   # You can use kfd only once
    return key


def write_encrypted(df, password, path):
    """ Writes padas.DataFrame to password encrypted file.
    Args:
       df (pandas.DataFrame): The DataFrame to be encrypted.
       password (str):        Unique password.
       path (str):            Path where to write encrypted file.
    """
    key = _get_key(password)
    fernet = Fernet(key)
    f = io.BytesIO()
    df.to_parquet(f)
    f.seek(0)
    encrypted_df = fernet.encrypt(f.read())
    
    with open(path, 'wb') as f:
        f.write(encrypted_df)


def read_encrypted(path, password):
    """Reads a previously encrypted file into a pandas.DataFrame.
    Args:
       path (str):     Path from which to read the encrypted file.
       password (str): Unique password used to encrypt the file.
    """
    with open(path, 'rb') as f:
        encrypted_df = f.read()
    
    key = _get_key(password)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_df)
    
    return pd.read_parquet(io.BytesIO(decrypted))

    





