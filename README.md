# CryptPandas ![](https://raw.githubusercontent.com/LucaMingarelli/cryptpandas/master/cryptpandas/res/encrypted.svg)


[![version](https://img.shields.io/badge/version-0.0.3-success.svg)](#)

## About

CryptPandas allows you to easily encrypt and decrypt pandas dataframe, regardless of their content.

# Installation
You can install with pip as:

`pip install cryptpandas`

## Example

Encrypting and decrypting your *pandas dataframe* is easy:
```python
import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1,2,3],
                   'B': ['one', 'one', 'four']})

crp.write_encrypted(df, path='file.crypt', password='mypassowrd123')

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')

print((df == decrypted_df).all().all())
```

By default CryptPandas uses PBKDF2 with a default salt. 
This allows anyone with your chosen password or passphrase to decrypt the content of your encrypted dataframe.

For an additional layer of security you can generate your own salt with `cryptpandas.make_salt`.
For example:
```python
import pandas as pd, cryptpandas as crp

df = pd.DataFrame({'A': [1,2,3],
                   'B': ['one', 'one', 'four']})

my_salt = crp.make_salt()
crp.write_encrypted(df, path='file.crypt', password='mypassowrd123', salt=my_salt)

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123', salt=my_salt)
```
Now it is possible to decrypt the encrypted dataframe only if in possession of both the salt and the password. 


### Requirements
- `pandas`
- `cryptography`
- `pyarrow`

# Author
Luca Mingarelli, 2020

[![Python](https://img.shields.io/static/v1?label=made%20with&message=Python&color=blue&style=for-the-badge&logo=Python&logoColor=white)](#)

