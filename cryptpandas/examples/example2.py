import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1,2,3],
                   'B': ['one', 'one', 'four']})

my_salt = crp.make_salt(32)
crp.write_encrypted(df, path='file.crypt', password='mypassowrd123', salt=my_salt)

decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123', salt=my_salt)

print((df == decrypted_df).all().all())