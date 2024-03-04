# CryptPandas ![](https://raw.githubusercontent.com/LucaMingarelli/CryptPandas/master/cryptpandas/res/encrypted.svg)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/LucaMingarelli/CryptPandas/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/LucaMingarelli/CryptPandas/tree/master)
[![Build and test GitHub](https://github.com/lucamingarelli/CryptPandas/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/LucaMingarelli/CryptPandas/actions)
[![version](https://img.shields.io/badge/version-1.0.0-success.svg)](#)
[![PyPI Latest Release](https://img.shields.io/pypi/v/CryptPandas.svg)](https://pypi.org/project/CryptPandas/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/153275ef99d84ec89045afedf639ad35)](https://app.codacy.com/gh/LucaMingarelli/CryptPandas?utm_source=github.com&utm_medium=referral&utm_content=LucaMingarelli/CryptPandas&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge Coverage](https://app.codacy.com/project/badge/Coverage/6e3fd357feba4659be21858c6c7f39f2)](https://www.codacy.com/gh/LucaMingarelli/CryptPandas/dashboard?utm_source=github.com&utm_medium=referral&utm_content=LucaMingarelli/CryptPandas&utm_campaign=Badge_Coverage)
[![Snyk Security Score](https://snyk-widget.herokuapp.com/badge/pip/cryptpandas/1.0.0/badge.svg)](https://snyk.io/vuln/pip:CryptPandas)
[![Codacy Security Scan](https://github.com/LucaMingarelli/CryptPandas/actions/workflows/codacy-analysis.yml/badge.svg)](https://github.com/LucaMingarelli/CryptPandas/actions/workflows/codacy-analysis.yml)
[![License](https://img.shields.io/pypi/l/CryptPandas.svg)](https://github.com/LucaMingarelli/CryptPandas/blob/master/LICENSE.txt)
[![Downloads](https://static.pepy.tech/personalized-badge/cryptpandas?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/cryptpandas)
[![Run on Repl.it](https://repl.it/badge/github/lucamingarelli/cryptpandas)](https://replit.com/@lucamingarelli/Try-out-CryptPandas#main.py)

## About

CryptPandas allows you to easily encrypt and decrypt pandas dataframe, regardless of their content.

## Installation
You can install with pip as:

`pip install cryptpandas`

### Example

Encrypting and decrypting your *pandas dataframe* is easy:

```python
import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})

crp.to_encrypted(df, password='mypassword123', path='file.crypt')

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123')

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
crp.to_encrypted(df, password='mypassword123', path='file.crypt', salt=my_salt)

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123', salt=my_salt)
```
Now it is possible to decrypt the encrypted dataframe only if in possession of both the salt and the password. 

### Requirements

-   `pandas`
-   `cryptography`
-   `pyarrow`

## Author

Luca Mingarelli, 2020

[![Python](https://img.shields.io/static/v1?label=made%20with&message=Python&color=blue&style=for-the-badge&logo=Python&logoColor=white)](#)
