import pandas as pd
import cryptpandas as crp

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['one', 'one', 'four']})


def test_import():
  import cryptpandas as crp
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
  assert (df == decrypted_df).all().all()

def test_with_salt():
  my_salt = crp.make_salt(32)

  crp.to_encrypted(df, password='mypassword123', path='file.crypt', salt=my_salt)
  decrypted_df = crp.read_encrypted(path='file.crypt', password='mypassword123', salt=my_salt)
  assert (df == decrypted_df).all().all()


