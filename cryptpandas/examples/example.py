import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1,2,3],
                   'B': ['one', 'one', 'four']})


crp.write_encrypted(df, path='file.crypt', password='mypassowrd123')

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')

print((df == decrypted_df).all().all())