'''from translation import google, ConnectError

# 127.0.0.1:1080 is a vaild proxies
try:
    print(google('hello world!', dst = 'zh-CN', proxies = {'http': '127.0.0.1:1080'}))
except ConnectError:
    print('Invaild proxy')

#with open('check.py', mode='r') as myFile:
    #text = myFile.read()
    #print(text)'''

from translate import Translator

trans = Translator(to_lang ="hi")

with open('name.txt', mode='r') as myFile:
    text = myFile.read()
    tns = trans.translate(text)
    print(tns)
    with open('name.txt', mode='a') as myf:    
        myf.write(tns)