# CryptPandas ![](https://raw.githubusercontent.com/LucaMingarelli/CryptPandas/master/cryptpandas/res/encrypted.svg)


[![version](https://img.shields.io/badge/version-0.1.1-success.svg)](#)
[![PyPI Latest Release](https://img.shields.io/pypi/v/CryptPandas.svg)](https://pypi.org/project/CryptPandas/)
[![License](https://img.shields.io/pypi/l/CryptPandas.svg)](https://github.com/LucaMingarelli/CryptPandas/blob/master/LICENSE.txt)
[![Downloads](https://static.pepy.tech/personalized-badge/cryptpandas?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/cryptpandas)


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

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})

crp.to_encrypted(df, password='mypassowrd123', path='file.crypt')

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')

print((df == decrypted_df).all().all())
```

By default CryptPandas uses PBKDF2 with a default salt. 
This allows anyone with your chosen password or passphrase to decrypt the content of your encrypted dataframe.

For an additional layer of security you can generate your own salt with `cryptpandas.make_salt`.
For example:

```python
import pandas as pd, cryptpandas as crp

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})

my_salt = crp.make_salt()
crp.to_encrypted(df, password='mypassowrd123', path='file.crypt', salt=my_salt)

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

