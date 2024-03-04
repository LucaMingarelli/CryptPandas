"""
Created on Tue Dec 22 00:11:40 2020

@author: Luca Mingarelli
"""
__about__ = "A tool for encryption and decryption of pandas dataframes."
__version__= '1.0.1'
__author__ = 'Luca Mingarelli'
__email__ = "lucamingarelli@me.com"
__url__ = "https://github.com/LucaMingarelli/cryptpandas"


from cryptpandas.encrypt_decrypt import to_encrypted, read_encrypted, make_salt
