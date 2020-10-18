# CryptPandas ![](cryptpandas/res/encrypted.svg)


[![version](https://img.shields.io/badge/version-0.0.1-success.svg)](#)

## About


# Installation


## Example

Performing specific queries and returning the results into *pandas dataframes* is easy:
```python
import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1,2,3],
                   'B': ['one', 'one', 'four']})

crp.write_encrypted(df, path='file.crypt', password='mypassowrd123')

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')

print((df == decrypted_df).all().all())
```



### Requirements
- `pandas`
- `cryptography`

# Author
Luca Mingarelli, 2020

[![Python](https://img.shields.io/static/v1?label=made%20with&message=Python&color=blue&style=for-the-badge&logo=Python&logoColor=white)](#)

