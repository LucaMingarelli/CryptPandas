import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})


class TestReadWrite:
  def test_import(self):
    import cryptpandas as crp
    assert crp
  
  def test_read_write(self):
    crp.to_encrypted(df, password='mypassowrd123', path='file.crypt')
    decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')
    assert (df == decrypted_df).all().all()
  
  def test_with_salt(self):
    my_salt = crp.make_salt(32)
    from crp.SALT import SALT
    crp.to_encrypted(df, password='mypassword123', path='file.crypt', salt=my_salt)
    decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123', salt=my_salt)
    assert (df == decrypted_df).all().all()
  

