import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
#print(res)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)

#To check whether i manage to create HTML file and run it on browser
'''
with open('check.html', 'w') as htmlFile:
    htmlFile.write(str(soup))
'''
#to print all the  body contents in the list format
'''print(soup.body.contents)'''

#if we want to find all the div's / linkin this soup object, in a list form 
print(soup.find_all('div'))
print(soup.find_all('a'))

#if we want to find the first anchor tag
print(soup.a)
#or
print(soup.find('a'))

#find for specific Search ID
print(soup.find(id="<id>"))