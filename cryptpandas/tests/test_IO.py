import pandas as pd
import cryptpandas as crp
import io

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})

def test_import():
  from cryptpandas.SALT import SALT
  assert crp
  assert SALT

def test_get_key():
  from cryptpandas.SALT import SALT
  key = crp.encrypt_decrypt._get_key(password='ApassWord', salt=SALT)
  key_val = b'mn68JONFMiJhvbi5mcQ1pzwWYA7mysfDg2w_IaXjwBo='
  assert key == key_val

def test_make_salt():
  from cryptpandas import make_salt
  assert len(make_salt(__size=124)) == 124

def test_read_write():
  crp.to_encrypted(df, password='mypassowrd123', path='file.crypt')
  decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassowrd123')
  assert df.equals(decrypted_df)

def test_with_salt():
  my_salt = crp.make_salt(32)

  crp.to_encrypted(df, password='mypassword123', path='file.crypt', salt=my_salt)
  decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123', salt=my_salt)
  assert df.equals(decrypted_df)

def test_read_write_with_buffer():
  PASSWORD = 'mypassword123'
  path = io.BytesIO()
  crp.to_encrypted(df, password=PASSWORD, 
                   path=path)

  path.seek(0)

  decrypted_df = crp.read_encrypted(path=path, 
                                    password=PASSWORD)
  assert df.equals(decrypted_df)


