from bs4 import BeautifulSoup
import requests
import lxml

parser = 'html.parser'
url = ('https://nypost.com/')

with requests.get(url) as response:
    soup = BeautifulSoup(response.text, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
