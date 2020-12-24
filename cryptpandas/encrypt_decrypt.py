import pandas as pd
import io, base64, os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptpandas.SALT import SALT

def make_salt(__size=16):
    """Makes a new salt.
    Args:
        __size (int): desired size of salt

    Returns: salt of size `__size`.
    """
    return os.urandom(__size)

def _get_key(password, salt=None):
    """Generates secret key associated with provided password.
    Args:
        password (str): Your password or passphrase.
        salt:           The salt; if `None` (default) uses a default salt.
        """
    enpassword = password.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt or SALT,
                     iterations=100000,
                     backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(enpassword))   # You can use kfd only once
    return key


def write_encrypted(df, password, path, salt=None):
    """ Writes pandas.DataFrame to password encrypted file.
    Args:
       df (pandas.DataFrame): The DataFrame to be encrypted.
       password (str):        Unique password or passphrase.
       path (str):            Path where to write encrypted file.
       salt:                  Salt for data encryption; if `None` (default) uses a default salt.
    """
    key = _get_key(password, salt=salt)
    fernet = Fernet(key)
    f = io.BytesIO()
    df.columns = df.columns.astype(str)
    df.to_parquet(f)
    f.seek(0)
    encrypted_df = fernet.encrypt(f.read())
    
    with open(path, 'wb') as f:
        f.write(encrypted_df)


def read_encrypted(path, password, salt=None):
    """Reads a previously encrypted file into a pandas.DataFrame.
    Args:
       path (str):     Path from which to read the encrypted file.
       password (str): Unique password used to encrypt the file.
       salt:           Salt for data encryption; if `None` (default) uses a default salt.
    """
    with open(path, 'rb') as f:
        encrypted_df = f.read()
    
    key = _get_key(password, salt=salt)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_df)
    
    return pd.read_parquet(io.BytesIO(decrypted))

    





