import requests
import hashlib

def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching : {res.status_code}, check the api and try again')


def pwned_api_check(password):
   sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
   return sha1password


print(pwned_api_check('pass123'))