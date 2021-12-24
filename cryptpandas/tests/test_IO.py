import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})


class TestReadWrite:
  def test_read_write(self):
    crp.to_encrypted(df, password='mypassowrd123', path='file.crypt')
    decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')
    assert (df == decrypted_df).all().all()

