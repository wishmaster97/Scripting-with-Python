import requests
import hashlib

# we have the pwned_api_check() func' -> we need to direct the password to the below given API(URL)

#sending the password to API
def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching : {res.status_code}, check the api and try again')

    return res
'''
#function for catching all the responses from the given API
#the  fucntion will return all the hashes will match the begining (head) of the password
def read_res(response):
    print(response.text)
'''

#Modifying the above function "read_res()"to check the complete password pawned and count

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    with open('listOfRes.txt', 'w') as listOfResponse:
        for h, count in hashes:
            hash_string = h+" "+count+'\n'
            listOfResponse.write(hash_string)
        


#we will split password that we are sending to the API in 2
# 1 - first 5 chars
# 2 - rest of the chars

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1password[:5], sha1password[5:]
    #print(head, "    ", tail)
   

    #calling the req_api_data func', param = head(first 5 chars ) and storing the response
    response = req_api_data(head)
    str_res = response.text
    with open('responseObj.txt', 'w') as resObj:
        resObj.write(str_res)

    #retrun the value and assign it to the function this will read all the passowrd pawned list
    return get_password_leaks_count(response, tail)


pwned_api_check('pass123')